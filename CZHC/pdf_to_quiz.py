import openai

import streamlit as st
import pdfplumber

openai.api_key = ""

# generate quiz
def generate_quiz(text, num_questions):
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
        n=num_questions,  
    )
    # print(response)
    allquiz = []
    for choice in response.choices:
        choice_text = choice.text.strip()
        choice_question = choice_text.split("Question:")
        if (len(choice_question) >= 2):
            choice_question = choice_question[1].split("A:")[0]
            temp_choices = choice_text.split(": ")
            if (len(temp_choices) >= 2):
                for i in range(2, len(temp_choices)-1):
                    temp_choices[i] = temp_choices[i].split("\n")[0]
                print("temp choices ", temp_choices[2: len(temp_choices)-1])
                allquiz += st.radio(choice_question, temp_choices[2: len(temp_choices)-1], index=None)
    

if __name__ == "__main__":
    uploaded_file = st.file_uploader("Upload a file", type=["pdf"])
    num_questions = st.number_input("Max Number of Questions", min_value=1, max_value=50)

    if uploaded_file is not None:
        with pdfplumber.open(uploaded_file) as pdf:
            text_content = ""
            for page in pdf.pages:
                text_content += page.extract_text()
            st.write("**Generated quiz questions:** \n")
            print("text", text_content, "num", num_questions)
            quiz_question = generate_quiz(text_content, num_questions)
            
            # st.write(quiz_question)

    
