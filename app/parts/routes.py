from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import SessionLocal


router = APIRouter(
    prefix="/parts",
    tags=["Parts"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", response_model=schemas.PartResponse)
def create_part(part: schemas.PartCreate, db: Session = Depends(get_db)):
    existing_part = db.query(models.Part).filter(
        models.Part.part_number == part.part_number
    ).first()

    if existing_part:
        raise HTTPException(
            status_code=400,
            detail="Part number already exists"
        )

    new_part = models.Part(**part.model_dump())
    db.add(new_part)
    db.commit()
    db.refresh(new_part)
    return new_part


@router.get("", response_model=list[schemas.PartResponse])
def get_parts(db: Session = Depends(get_db)):
    return db.query(models.Part).all()


@router.get("/{part_number}", response_model=schemas.PartResponse)
def get_part(part_number: str, db: Session = Depends(get_db)):
    part = db.query(models.Part).filter(
        models.Part.part_number == part_number
    ).first()

    if not part:
        raise HTTPException(
            status_code=404,
            detail="Part not found"
        )

    return part