import streamlit as st
import random
import time
import pandas as pd
import os

st.set_page_config(page_title="BABOK Training App", page_icon="📘")

st.title("BABOK Certification Trainer")

# -----------------------
# CONFIG
# -----------------------

EXAM_TIME = 60 * 60
PRACTICE_QUESTIONS = 5
EXAM_QUESTIONS = 10

# -----------------------
# QUESTION BANK
# -----------------------

question_bank = [

{
"chapter":"1",
"question":"According to BABOK, what is Business Analysis?",
"options":[
"Managing IT infrastructure",
"Enabling change by defining needs and recommending solutions that deliver value",
"Developing software applications",
"Testing enterprise systems"
],
"answer":1,
"explanation":"Business analysis enables change by defining needs and recommending solutions that deliver value."
},

{
"chapter":"1",
"question":"Which of the following is NOT part of BACCM?",
"options":[
"Change",
"Stakeholder",
"Budget",
"Value"
],
"answer":2,
"explanation":"BACCM concepts are Change, Need, Solution, Stakeholder, Value, Context."
},

{
"chapter":"1",
"question":"What does Need represent?",
"options":[
"A project plan",
"A problem or opportunity",
"A technical design",
"A budget"
],
"answer":1,
"explanation":"Need represents a problem or opportunity."
},

{
"chapter":"1",
"question":"Which concept represents the environment of change?",
"options":[
"Value",
"Context",
"Solution",
"Need"
],
"answer":1,
"explanation":"Context describes circumstances surrounding the change."
},

{
"chapter":"1",
"question":"What is Value?",
"options":[
"Money only",
"Worth to stakeholders",
"Budget amount",
"Project cost"
],
"answer":1,
"explanation":"Value represents importance or usefulness to stakeholders."
},

{
"chapter":"1",
"question":"Stakeholders are:",
"options":[
"Managers only",
"People affected by change",
"Developers",
"Investors"
],
"answer":1,
"explanation":"Stakeholders are anyone impacted by the change."
},

{
"chapter":"1",
"question":"Solutions represent:",
"options":[
"Budget allocation",
"A way to satisfy needs",
"Risk mitigation",
"Marketing strategy"
],
"answer":1,
"explanation":"Solutions satisfy identified needs."
},

{
"chapter":"1",
"question":"Change means:",
"options":[
"Financial revision",
"Transformation responding to a need",
"Project cancellation",
"Budget reduction"
],
"answer":1,
"explanation":"Change represents transformation."
}

]

# -----------------------
# MODE SELECTION
# -----------------------

mode = st.sidebar.radio(
"Select Mode",
["Practice Mode","Real Exam Mode"]
)

question_count = PRACTICE_QUESTIONS if mode == "Practice Mode" else EXAM_QUESTIONS

# -----------------------
# SESSION STATE
# -----------------------

if "questions" not in st.session_state:

    st.session_state.questions = random.sample(question_bank, min(question_count,len(question_bank)))
    st.session_state.answers = {}
    st.session_state.start_time = time.time()
    st.session_state.finished = False

# -----------------------
# TIMER (only exam)
# -----------------------

if mode == "Real Exam Mode":

    remaining = EXAM_TIME - (time.time() - st.session_state.start_time)

    minutes = int(remaining // 60)
    seconds = int(remaining % 60)

    st.sidebar.write(f"Time remaining: {minutes:02}:{seconds:02}")

    if remaining <= 0:
        st.session_state.finished = True

# -----------------------
# QUESTIONS
# -----------------------

for i,q in enumerate(st.session_state.questions):

    st.subheader(f"Question {i+1}")

    answer = st.radio(
        q["question"],
        q["options"],
        key=f"q{i}"
    )

    st.session_state.answers[i] = q["options"].index(answer)

    # Practice mode feedback
    if mode == "Practice Mode":

        if st.session_state.answers[i] == q["answer"]:
            st.success("Correct")
        else:
            st.error("Incorrect")
            st.write("Correct answer:", q["options"][q["answer"]])

        st.write("Explanation:", q["explanation"])

# -----------------------
# SUBMIT
# -----------------------

if st.button("Submit"):

    st.session_state.finished = True

# -----------------------
# RESULTS
# -----------------------

if st.session_state.finished:

    score = 0

    st.header("Results")

    for i,q in enumerate(st.session_state.questions):

        correct = q["answer"]
        user = st.session_state.answers.get(i)

        if user == correct:
            score += 1
            st.success(f"Question {i+1}: Correct")
        else:
            st.error(f"Question {i+1}: Incorrect")
            st.write("Correct answer:", q["options"][correct])

        if mode == "Real Exam Mode":
            st.write("Explanation:", q["explanation"])

        st.write("---")

    st.subheader(f"Score: {score}/{len(st.session_state.questions)}")

# -----------------------
# RESET
# -----------------------

if st.button("New Attempt"):

    st.session_state.questions = random.sample(question_bank, min(question_count,len(question_bank)))
    st.session_state.answers = {}
    st.session_state.start_time = time.time()
    st.session_state.finished = False

    st.rerun()
