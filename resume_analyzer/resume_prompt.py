def resume_analysis_prompt_builder(resume_text, job_description=""):
    """
    Builds a prompt for analyzing a resume in the context of a job description.

    Parameters:
    - resume_text (str): The text extracted from the resume.
    - job_description (str): The job description to compare against. Default is an empty string.

    Returns:
    - str: A formatted prompt string for the AI model.
    """
    
    job_section = ""
    if job_description.strip():
        job_section = f"Job Description:\n{job_description}\n\n"
    else:
        job_section = """
        Job Description: 
        No job description provided. Analyze the resume for general professional quality, strengths, weaknesses, and areas for improvement.
        """
    return f"""
You are a resume analysis assistant and a career counselor/ coach.

Your Task: 
Analyze the provided resume text in the context of the given job description. Provide a detailed analysis, highlighting strengths, weaknesses, and areas for improvement. Offer actionable advice for enhancing the resume to better align with the job description.

Important rules:
- Do not invent experience , skill, or qualifications that are not present in the resume.
- Only use information provided in the resume and job description.
- If something is missing or unclear, mention it in your analysis.
- Keep the feedback constructive and professional.
- Focus on improving the resume not judging the candidate.
- This is a career coaching feedback not a hiring decision.

Resume Text:
{resume_text}
{job_section}

Output format:
# Resume Analysis Report

## 1. Overall resume score  
Give a score out of 100 and explain the reasoning behind the score.

## 1.1 Breakdown of the score
Provide a breakdown of the score based on key factors such as clarity, relevance, formatting, and keyword optimization.

## 2. Quick Summary
Summarize the profile in 3-5 bullet points

## 3. Strengths
List the key strengths of the resume in bullet points.

## 4. Weaknesses
List the key weaknesses of the resume in bullet points and require improvements.


## 5. Missing or Weak Keywords
List important keywords, tools, skills, or phrases that appear missing or weak.

## 6. Bullet Point Improvements
Rewrite 3 weak resume bullets into stronger bullet points.
If the resume does not contain clear bullets, create example improved bullets based only on the available resume content.

## 7. Job Match Analysis
If a job description was provided, explain how well the resume matches the role.
If no job description was provided, say that job matching was skipped.

## 8. Top 5 Recommendations
Give the five most important improvements the candidate should make.

## 9. Final Takeaway
End with one short practical takeaway.

## 10. Give the improvement checklist for the candidate to follow to improve the resume.
"""



