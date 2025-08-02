import streamlit as st
import requests
import plotly.express as px

API_URL = "http://localhost:8000/analyze"  


st.set_page_config(
    page_title="AI Code Refactor & Analysis",
    layout="wide",
    page_icon="🤖"
)


st.markdown("""
    <style>
        html, body, [class*="css"] {
            background-color: #f8fbff;
            color: #202124;
            font-family: 'Segoe UI', sans-serif;
        }

        .stButton > button {
            background-color: #1f77b4;
            color: white;
            border-radius: 30px;
            padding: 0.6rem 2rem;
            font-weight: bold;
            border: none;
        }

        .stButton > button:hover {
            background-color: #166ba2;
        }

        .big-font {
            font-size: 2.5rem !important;
            font-weight: 700;
            text-align: center;
            color: #1f77b4;
            margin-bottom: 1rem;
        }

        .subtitle {
            text-align: center;
            color: #555;
            font-size: 1.2rem;
            margin-bottom: 2rem;
        }

        .section-title {
            font-size: 1.4rem;
            font-weight: 600;
            color: #1f77b4;
            margin: 1.2rem 0 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)


st.markdown('<p class="big-font">🤖 AI Code Refactor and Analysis</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Transform your code with AI-powered insights</p>', unsafe_allow_html=True)


code_input = st.text_area("📥 Paste your code here:", height=300, placeholder="e.g. def hello():\n    print('Hello')")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    analyze_button = st.button("🚀 Analyze Code", use_container_width=True)


if analyze_button:
    if not code_input.strip():
        st.warning("⚠️ Please enter some code to analyze.")
    else:
        with st.spinner("Analyzing your code..."):
            try:
                response = requests.post(API_URL, json={"code": code_input})
                if response.status_code != 200:
                    st.error(f"API Error: {response.json().get('detail', response.text)}")
                else:
                    result = response.json()

                    if "syntax_error" in result:
                        st.error(f"🛑 Syntax Error: {result['syntax_error']}")
                    else:
                       
                        st.markdown('<div class="section-title">🔍 Code Analysis</div>', unsafe_allow_html=True)

                        score_col1, score_col2 = st.columns([1, 2])
                        with score_col1:
                            st.metric("🎯 Quality Score", f"{result['score']}/100")
                        with score_col2:
                            fig = px.pie(
                                names=list(result["score_breakdown"].keys()),
                                values=list(result["score_breakdown"].values()),
                                title="Score Breakdown",
                                color_discrete_sequence=px.colors.sequential.Blues
                            )
                            st.plotly_chart(fig, use_container_width=True)

                        
                        issue_col, tip_col = st.columns(2)

                        with issue_col:
                            st.markdown("#### 🚨 Detected Issues")
                            if result["issues"]:
                                for issue in result["issues"]:
                                    st.error(f"• {issue}")
                            else:
                                st.success("🎉 No issues detected!")

                        with tip_col:
                            st.markdown("#### 💡 Optimization Tips")
                            if result["tips"]:
                                for tip in result["tips"]:
                                    st.info(f"• {tip}")
                            else:
                                st.info("✅ No tips available.")

                        
                        code_col1, code_col2 = st.columns(2)
                        with code_col1:
                            st.markdown('<div class="section-title">📄 Original Code</div>', unsafe_allow_html=True)
                            st.code(code_input, language="python")

                        with code_col2:
                            st.markdown('<div class="section-title">✨ Refactored Code</div>', unsafe_allow_html=True)
                            st.code(result["refactored_code"], language="python")

            except requests.exceptions.RequestException as e:
                st.error(f"Request failed: {e}")
            except Exception as e:
                st.error(f"Unexpected error: {e}")
