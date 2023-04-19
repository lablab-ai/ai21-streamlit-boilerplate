import os

import ai21
import streamlit as st
from dotenv import load_dotenv

# Load secrets
load_dotenv()

API_KEY = os.getenv("AI21_LABS_API_KEY")

ai21.api_key = API_KEY

PROMPT = "Based on the description given, name the sport.\nDescription: {description}\n Sport name: "

# Initialization
if "output" not in st.session_state:
    st.session_state["output"] = "Output:"


def guess_sport(inp):
    if not len(inp):
        return None

    prompt = PROMPT.format(description=inp)

    response = ai21.Completion.execute(
        model="j2-grande-instruct",
        prompt=prompt,
        temperature=0.5,
        minTokens=1,
        maxTokens=15,
        numResults=1,
    )

    st.session_state["output"] = response.completions[0].data.text
    st.balloons()


st.title("The Sports Guesser")

st.write(
    "This is a simple **Streamlit** app that generates Sport Name based on given description"
)


inp = st.text_area("Enter your description here", height=100)
st.button("Gue" "ss", on_click=guess_sport(inp))
st.write(f"Answer: {st.session_state.output}")
