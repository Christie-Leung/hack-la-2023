import openai

import streamlit as st
import pdfplumber

openai.api_key = "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"

# generate quiz
def generate_quiz(text):
    # print(prompt)
    prompt = f"""Create quiz questions based on the document provided.
    Just print questions and answers, not other instructions.
    Don't use information outside provided text. 
    Please generate 3 to 4 multiple-choice questions (MCQs) per page with 4 options and a corresponding answer letter using text:\n{text}. 
    Use template as follows for each question
    
    Question: question here \n
    A: choice here \n
    B: choice here \n
    C: choice here \n
    D: choice here \n
    Answer: A or B or C or D \n
    """

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1700,  
        n=1,  
    )
    print(response)

    return response.choices[0].text.strip()

if __name__ == "__main__":
    uploaded_file = st.file_uploader("Upload a file", type=["pdf"])

    if uploaded_file is not None:
        with pdfplumber.open(uploaded_file) as pdf:
            text_content = ""
            for page in pdf.pages:
                text_content += page.extract_text()
        quiz_question = generate_quiz(text_content)
        st.write("**Generated quiz questions:** \n")
        st.write(quiz_question)

    
