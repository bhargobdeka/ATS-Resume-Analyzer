import streamlit as st
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part
vertexai.init(project='ats-gemini-project')

# clear cache
st.cache_data.clear()

from pypdf import PdfReader
def readpdf(filename):
    pdf_pages = PdfReader(filename)
    pages = pdf_pages.pages[0]
    return pages
# print(first_page.extract_text())

model = GenerativeModel("gemini-pro")

## Prompts
input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """ 
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

input_prompt3 = """
You are a mentor for candidate's searching for jobs as a data scientist/ML engineer/AI engineer. suggest me two project ideas that can highlight the candidate's missing skills with full end-to-end description including where and how to collect data, which ML model to build, and which tools to use for deploying the model for production. Do not include projects that are already mentioned in the resume.
"""

input_prompt4 = """
Suggest ways to improve the structure of the resume. Give examples on how the candidate can improve the resume.
"""

## Streamlit App
st.set_page_config(page_title="ATS Resume EXpert", page_icon='random',layout="wide")
st.header("Resume Analyzer")
st.write("This is a Resume Analyzer that can help you to analyze your resume against the job description and give you suggestions on how to improve your resume.")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume (PDF)",type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Tell Me About the Resume")

submit2 = st.button("Percentage match")

submit3 = st.button("Project Ideas")

submit4 = st.button("Resume Re-Structure Suggestions")

if submit1:
    if uploaded_file is not None:
        page_content = readpdf(uploaded_file)
        response = model.generate_content(f"{input_prompt1}\n{input_text}\n{page_content.extract_text()}", stream=False)
        st.subheader("The Response is")
        new_response = response.candidates[0].content.parts[0].text
        st.markdown(new_response)
    else:
        st.write("Please Upload a PDF file")
elif submit2:
    if uploaded_file is not None:
        page_content = readpdf(uploaded_file)
        response = model.generate_content(f"{input_prompt2}\n{input_text}\n{page_content.extract_text()}", stream=False)
        st.subheader("The Response is")
        new_response = response.candidates[0].content.parts[0].text
        st.markdown(new_response)
    else:
        st.write("Please Upload a PDF file")

elif submit3:
    if uploaded_file is not None:
        page_content = readpdf(uploaded_file)
        response = model.generate_content(f"{input_prompt3}\n{input_text}\n{page_content.extract_text()}", stream=False)
        st.subheader("The Response is")
        new_response = response.candidates[0].content.parts[0].text
        st.markdown(new_response)
    else:
        st.write("Please Upload a PDF file")

elif submit4:
    if uploaded_file is not None:
        page_content = readpdf(uploaded_file)
        response = model.generate_content(f"{input_prompt4}\n{input_text}\n{page_content.extract_text()}", stream=False)
        st.subheader("The Response is")
        new_response = response.candidates[0].content.parts[0].text
        st.markdown(new_response)
    else:
        st.write("Please Upload a PDF file")

