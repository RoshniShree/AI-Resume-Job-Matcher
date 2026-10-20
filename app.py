import streamlit as st

from src.workflow import analyze_resume_text


st.set_page_config(page_title="AI Resume Matcher", page_icon="📄", layout="wide")
st.title("AI-Powered Resume and Job Description Matching Assistant")
st.write(
    "Upload a text-based PDF resume and paste a job description to review "
    "candidate skills, potential gaps, and recommendations."
)

uploaded_file = st.file_uploader("Upload resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste job description", height=220)

if st.button("Analyze", type="primary"):
    if uploaded_file is None:
        st.warning("Please upload a PDF resume.")
    elif not job_description.strip():
        st.warning("Please paste a job description.")
    else:
        try:
            from pypdf import PdfReader
            import io

            reader = PdfReader(io.BytesIO(uploaded_file.getvalue()))
            resume_text = "\n".join(page.extract_text() or "" for page in reader.pages)
            if not resume_text.strip():
                st.error("No selectable text was found. Try a text-based PDF.")
            else:
                with st.spinner("Analyzing resume..."):
                    result = analyze_resume_text(resume_text, job_description)
                st.subheader("Analysis report")
                st.write("**Resume skills**")
                st.write(", ".join(result["resume_skills"]) or "No matching skills identified.")
                st.write("**Job-required skills**")
                st.write(", ".join(result["required_skills"]) or "No matching skills identified.")
                st.write("**Potential skill gaps**")
                st.write(", ".join(result["skill_gaps"]) or "No gaps found in the starter skill list.")
                st.write("**Recommendations**")
                for item in result["recommendations"]:
                    st.write(f"- {item}")
                st.caption(
                    "Starter implementation: uses keyword matching, not an LLM. "
                    "Connect your LangChain/LangGraph workflow to enable LLM-based analysis."
                )
        except Exception as exc:
            st.error(f"Could not analyze this file: {exc}")
