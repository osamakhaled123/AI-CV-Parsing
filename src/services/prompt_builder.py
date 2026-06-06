from pathlib import Path
import os

directory_path = os.path.dirname(os.path.dirname(__file__))
job_description_path = os.path.join(directory_path, "prompts")
job_description_path = os.path.join(job_description_path, "job_description.txt")


def load_job_description() -> str:
    path = Path(job_description_path)

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def build_prompt(cv_text: str, job_description: str) -> str:
    return f"""
You are an AI Engineer AI assistant.

Your task is:
1. Parse the candidate CV
2. Compare it against the job description
3. Return structured JSON

Job Description:
{job_description}

Candidate CV:
{cv_text}

Return STRICT JSON with:
- matching Experience score, called "Experience"
- matching Summary score, called "Summary"
- matching Projects score, called "Projects"
- matching Education score, called "Education"

Prepare your response to ber strictly as described above in every response, so not to change whenever requested.
"""