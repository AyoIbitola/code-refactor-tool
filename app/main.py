from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from gemini_ref import analyze_code
from schemas import CodeRequest,CodeResponse

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post("/analyze",response_model=CodeResponse)
def analyze(request: CodeRequest):
    result = analyze_code(request.code)
    return result