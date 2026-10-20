import re

# Starter keyword list. Extend this based on your domain and evaluation data.
KNOWN_SKILLS = {
    "python", "java", "sql", "machine learning", "deep learning",
    "data analysis", "pandas", "numpy", "langchain", "langgraph",
    "streamlit", "git", "docker", "aws", "communication",
    "problem solving", "natural language processing", "nlp",
}


def extract_known_skills(text: str) -> list[str]:
    """Find known skill keywords in text (case-insensitive baseline)."""
    normalized = re.sub(r"\s+", " ", text.lower())
    found = []
    for skill in sorted(KNOWN_SKILLS):
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"
        if re.search(pattern, normalized):
            found.append(skill)
    return found


def compare_skills(resume_text: str, job_description: str) -> dict:
    resume_skills = extract_known_skills(resume_text)
    required_skills = extract_known_skills(job_description)
    resume_set = set(resume_skills)
    gaps = [skill for skill in required_skills if skill not in resume_set]
    return {
        "resume_skills": resume_skills,
        "required_skills": required_skills,
        "skill_gaps": gaps,
    }
