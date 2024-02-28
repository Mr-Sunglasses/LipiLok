from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from spello.model import SpellCorrectionModel

from ..models import Recommendation
from ..database import get_db
from ..schemas import CorrectionRequest, CorrectionResponse, RecommendationRequest

router = APIRouter()

sp = SpellCorrectionModel(language="en")


@router.post(
    "/fix-spelling/", status_code=status.HTTP_200_OK, response_model=CorrectionResponse
)
def fix_spelling(data: CorrectionRequest):
    fixed_text = sp.spell_correct(data.orginal_text)["spell_corrected_text"]
    print(fixed_text)
    return CorrectionResponse(original_text=data.orginal_text, fixed_text=fixed_text)


@router.post("/recommend/")
def recommend(
    recommendation_request: RecommendationRequest, db: Session = Depends(get_db)
):
    sp.train([recommendation_request.fixed_text])
    recommendation = Recommendation(
        original_text=recommendation_request.original_text,
        fixed_text=recommendation_request.fixed_text,
        train=True,
    )
    db.add(recommendation)
    db.commit()
    return {"message": "Recommendation received and model Trained"}


@router.get("/healthz", status_code=status.HTTP_200_OK)
async def healthz() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/readyz", status_code=status.HTTP_200_OK)
async def readyz() -> dict[str, str]:
    return {"status": "ok"}
