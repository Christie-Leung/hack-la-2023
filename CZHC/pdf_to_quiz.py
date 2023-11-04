import openai
import PyPDF2
import streamlit as st

openai.api_key = ""

page_count = 0

# get text input from the pdf file
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        page_count = len(pdf_reader.pages)
        for page_num in range(page_count):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

# generate quiz
def generate_quiz(text):
    prompt =  f"Create quiz questions. Do not print anything else than the question and the answer. Please generate a multiple-choice questions (MCQs) with 4 options and a corresponding answer letter using text:\n{text}"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1700,  
        n=1,  
    )
    print(response)

    return response.choices[0].text.strip()

if __name__ == "__main__":
    file_path = './data/Copy of Lecture 11.pdf'
    pdf_text = extract_text_from_pdf(file_path)
    quiz_question = generate_quiz(pdf_text)
    # st.write("**Generated quiz questions:** \n")
    # st.write(quiz_question)
    # uploaded_file = st.file_uploader("Upload a file", type=["pdf"])

    # if uploaded_file is not None:        
        # Get the file path of the uploaded PDF
        
