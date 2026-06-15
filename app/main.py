from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import engine, SessionLocal
from app import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Dealership ERP")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Dealership ERP running"}


@app.post("/parts", response_model=schemas.PartResponse)
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


@app.get("/parts", response_model=list[schemas.PartResponse])
def get_parts(db: Session = Depends(get_db)):
    return db.query(models.Part).all()


@app.get("/parts/{part_number}", response_model=schemas.PartResponse)
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