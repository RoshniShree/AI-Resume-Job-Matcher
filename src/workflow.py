from .job_matcher import compare_skills


def analyze_resume_text(resume_text: str, job_description: str) -> dict:
    """Starter workflow. Replace or extend with your LangChain/LangGraph graph."""
    comparison = compare_skills(resume_text, job_description)
    gaps = comparison["skill_gaps"]
    recommendations = [
        f"Add evidence of '{skill}' to your resume if you have this skill."
        for skill in gaps
    ]
    if not recommendations:
        recommendations = [
            "Review each job requirement and ensure your resume includes concrete evidence.",
            "Tailor project descriptions to show relevant impact and outcomes.",
        ]
    comparison["recommendations"] = recommendations
    return comparison
