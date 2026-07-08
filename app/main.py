from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import engine, SessionLocal
from app import models, schemas
from app.parts.routes import router as parts_router


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="NuggiesOS Dealership ERP")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "NuggiesOS Dealership ERP running"}


@app.post("/parties", response_model=schemas.PartyResponse)
def create_party(party: schemas.PartyCreate, db: Session = Depends(get_db)):
    new_party = models.Party(**party.model_dump())

    db.add(new_party)
    db.commit()
    db.refresh(new_party)

    return new_party


@app.get("/parties", response_model=list[schemas.PartyResponse])
def get_parties(db: Session = Depends(get_db)):
    return db.query(models.Party).all()


app.include_router(parts_router)