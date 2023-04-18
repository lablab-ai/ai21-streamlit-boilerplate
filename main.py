import os

import ai21
import streamlit as st
from dotenv import load_dotenv

# Load secrets
load_dotenv()

API_KEY = os.getenv('AI21_LABS_API_KEY')
ai21.api_key = API_KEY

# Initialization
if 'output' not in st.session_state:
    st.session_state['output'] = 'Output:'

def generate_hashtags(inp):
    if len(inp) == 0:
        return None
        
    response = ai21.Completion.execute( 
        model='j1-large', 
        prompt=f'Given a post, this program will generate relevant hashtags.\n\nPost: Why are there no country songs about software engineering\nHashtag: #softwareengineering #code \n--\nPost: Your soulmate is in the WeWork you decided not to go to\nHashtag: #wework #work \n--\nPost: If shes talking to you once a day im sorry bro thats not flirting that standup\nHashtag: #standup #funny \n--\nPost: {inp}\nHashtags:', 
        temperature=0.5, 
        max_tokens=20, 
        minTokens=4,
        maxTokens=32,
        numResults=1
    ) 

    st.session_state['output'] = response.completions[0].data.text
    st.balloons()


st.title('Hashtag Generator')
st.subheader('Boilerplate for AI21, Streamlit, Streamlit Cloud')
st.write('''This is a simple **Streamlit** app that generates hashtags from a small Post title caption.''')

inp = st.text_area('Enter your post title caption here', height=100)
st.button('Generate Hashtags', on_click = generate_hashtags(inp))
st.write(st.session_state.output)