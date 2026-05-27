from pathlib import Path
import os

directory_path = os.path.dirname(os.getcwd())
file_path = os.path.join(directory_path+"/prompts/job_description.txt")

def load_job_description() -> str:
    path = Path(file_path)

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
- matching Experience score 
- matching Summary score
- matching Projects score
- matching Education score
"""