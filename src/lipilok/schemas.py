from pydantic import BaseModel


class CorrectionRequest(BaseModel):
    orginal_text: str


class CorrectionResponse(BaseModel):
    original_text: str
    fixed_text: str


class RecommendationRequest(BaseModel):
    original_text: str
    fixed_text: str
