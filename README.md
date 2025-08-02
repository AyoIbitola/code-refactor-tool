# 🔧 AI Code Refactor & Analyzer

A sleek web app that uses **Google Gemini AI** to refactor code, detect issues, and score your code's quality — all with stylish visualizations. Built with **FastAPI** (backend) and **Streamlit** (frontend).

---

## 🚀 Features

- 🧠 **AI-Powered Analysis** using Google Gemini  
- 🔍 Refactors your code for best practices and efficiency  
- 🧾 Lists detected code issues  
- 📊 Scores code quality out of 100 (readability, efficiency, best practices)  
- 💡 Gives tips for improvement  
- 🔁 Shows original and refactored code side-by-side  
- 🍰 Beautiful pie chart breakdown of the scores  
- 🎨 Gradient UI with smooth, bouncy transitions (Streamlit frontend)

---

## 🛠 Tech Stack

| Layer     | Tech              |
|-----------|-------------------|
| Backend   | FastAPI (Python)   |
| Frontend  | Streamlit          |
| AI Model  | Google Gemini API  |
| Optional  | PostgreSQL (for history) |
| Future    | GitHub Integration |

---

## 📦 Installation & Setup

1. **Clone the repo**  
   ```bash
   git clone https://github.com/YOUR_USERNAME/refactor-app.git
   cd refactor-app
   ```

2. **Create a Python virtual environment**  
   ```bash
   python -m venv .venv
   # Windows
   source .venv/Scripts/activate
   # Mac/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file in the root folder** and add your Gemini API key:  
   ```env
   GEMINI_KEY=your_google_gemini_api_key
   ```

---

## 🧪 Running the App

### Backend (FastAPI)  
```bash
uvicorn app.main:app --reload
```

API docs available at:  
`http://127.0.0.1:8000/docs`

### Frontend (Streamlit)  
```bash
streamlit run streamlit_app.py
```

Open frontend at:  
`http://localhost:8501`

---

## 📂 Project Structure

```plaintext
refactor-app/
│
├── app/
│   ├── main.py             # FastAPI app entry point
│   ├── analyze.py          # Gemini AI code analysis logic
│
├── streamlit/              # Streamlit folder
│     ├── app.py                  # Streamlit frontend app
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (gitignored)
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

---

## 🧠 Sample Gemini JSON Response

```json
{
  "refactored_code": "...",
  "issues": ["...", "..."],
  "score": 87,
  "score_breakdown": {
    "readability": 90,
    "efficiency": 85,
    "best_practices": 80
  },
  "tips": ["...", "..."]
}
```





---

## 🧑‍💻 Author

Built with ❤️ by [Emmanuel Ibitola](https://github.com/AyoIbitola)

---

## 📄 License

MIT License — Feel free to use, modify, and share!
