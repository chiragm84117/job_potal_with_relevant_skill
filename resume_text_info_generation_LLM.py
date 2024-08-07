from resume_data_fetch import input_pdf_text as resume
import google.generativeai as genai
import os

def get_gemini_result(input):
    genai.configure(api_key="AIzaSyDmwZiI6Ob9VA-CsfzWRGE0Bo-LE07eS0g")
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response=model.generate_content(input)
    return response.text

text1 = resume('newest_resume_chirag_makwana.pdf')

prompt_keywords = f"""
Analyze the provided resume and extract a list of important keywords that are relevant across all sections of the resume, including the summary, skills section, work experience, projects, certifications, and education. Keywords should capture the core competencies, technologies, skills, and significant terms. Provide the keywords in a list format:

{{
  "ImportantKeywords": ["keyword1", "keyword2", ...]
}}
{text1}
"""

prompt_experience = f"""
Analyze the provided experience section in resume and determine the individual's experience level. Specifically, identify if the person is a fresher or experienced. If experienced, please estimate the number of years of experience they have. Provide the response in the following format:

{{
  "ExperienceLevel": "Fresher" or "Experienced",
  "YearsOfExperience": "number_of_years" (if experienced) or (if fresher then 0) it should only be a number
}}
{text1}
"""



resp_keywords = get_gemini_result(prompt_keywords)
resp_exprience = get_gemini_result(prompt_experience)

print(resp_keywords)
print(resp_exprience)



