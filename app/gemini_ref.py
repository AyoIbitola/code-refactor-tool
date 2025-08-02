import os,json
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash-latest")

def analyze_code(code: str) :
    prompt = f"""
    You are an expert software engineer.

    1. Refactor the code.

    2. List issues in bullet points.
    3. Score the code out of 100 for readability, efficiency, best practices.
    4. Give improvement tips.
    5. Return only JSON like:
    
    {{
    
    "refactored_code": "...",
    "issues": ["...", "..."],
    "score": 78,
    "score_breakdown": {{
    "readability": 25,
    "efficiency": 30,
    "best_practices": 23
     }},
    "tips": ["...", "..."]
    }}

    Code:
    ```
    {code}

    """
     
    response = model.generate_content(prompt)
    text = response.text

    try:
        start = text.find("{")
        end = text.rfind("}")+1
        json_part = text[start:end]
        return json.loads(json_part)
    except Exception :
        raise ValueError("Failed to parse Gemini's JSON response")
