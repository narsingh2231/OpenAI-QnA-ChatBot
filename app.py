from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()    # take environment variable from .env


## Function to load openAI model and get response
def get_openai_response(question):
    llm = OpenAI(openai_api_key = os.getenv('OPEN_API_KEY'), model_name = "text-davinci-003", temperature = 0.6)
    response = llm(question)
    return response


st.set_page_config(page_title = "QnA_Project Using OpenAI")
st.header("Langchain Application using OpenAI")

input = st.text_input("Input: ", key = "input")
response = get_openai_response(input)

submit = st.button("Ask the Question")

# if ask button is clicked
if submit:
    st.subheader("The response is ")
    st.write(response)

