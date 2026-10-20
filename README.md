# AI-Powered Resume and Job Description Matching Assistant

## Project Overview
A Python-based LLM application that analyzes resumes against job descriptions, extracts candidate skills, identifies potential skill gaps, and generates personalized recommendations. LangChain and LangGraph support the AI workflow, while Streamlit provides the user interface.

> This repository is a starter template. Replace placeholder modules with your implementation and verify all features before presenting it as a completed project.

## Objectives
- Extract relevant skills from a resume.
- Compare candidate skills with job requirements.
- Identify potential skill gaps.
- Generate personalized recommendations.
- Evaluate output quality with test cases and manual review.

## Technologies
- Python
- LangChain
- LangGraph
- Streamlit
- LLM provider integration (configure the provider used by your implementation)

## Suggested Workflow
1. Upload a resume and provide a job description.
2. Extract resume text and candidate skills.
3. Identify required skills in the job description.
4. Compare the two skill sets.
5. Generate recommendations.
6. Display a structured report in Streamlit.

## Project Structure
```text
AI-Resume-Job-Matcher/
├── app.py
├── requirements.txt
├── .gitignore
├── .env.example
├── README.md
├── src/
│   ├── __init__.py
│   ├── resume_parser.py
│   ├── job_matcher.py
│   └── workflow.py
├── tests/
│   └── test_resume_matching.py
└── sample_data/
    └── sample_job_description.txt
```

## Setup
Recommended: use a Python version supported by all packages in `requirements.txt`.

### 1. Create and activate a virtual environment
Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:
```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure the LLM provider
Copy `.env.example` to `.env` and add the API key for the provider you configure. Never commit `.env` or API keys to GitHub.

### 4. Run the app
```bash
streamlit run app.py
```

## Testing
Run:
```bash
python -m unittest discover -s tests
```

The included starter test checks simple skill-set comparison behavior. Add tests for your actual resume parser, LangGraph workflow, and LLM responses. Record measured results only after running the tests.

## Privacy
Resumes can contain personal data. Use synthetic or anonymized samples in demonstrations. Explain how uploads and any third-party LLM requests are handled.

## Future Improvements
- Support additional resume formats.
- Add explainable match scoring.
- Compare a resume with multiple job descriptions.
- Add automated evaluation metrics.
- Deploy the app to a hosting platform.

## Author
Roshni Shree- https://www.linkedin.com/in/roshni-shree-s-1abb2a22a

## License
Choose a license before distributing this project. Add a `LICENSE` file if you decide to use one.
