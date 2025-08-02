from pydantic import BaseModel
from typing import List,Dict

class CodeRequest(BaseModel):
    code: str

class CodeResponse(BaseModel):
    refactored_code : str
    issues: List[str]
    score: int
    score_breakdown: Dict[str,int]
    tips:List[str]