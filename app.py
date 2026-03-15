import streamlit as st
import random
import time
import pandas as pd
import os

st.set_page_config(page_title="BABOK Exam Platform", page_icon="📘", layout="wide")

st.title("BABOK Certification Training Platform")

EXAM_TIME = 60 * 60
QUESTION_COUNT = 10

# -----------------------------
# QUESTION BANK
# -----------------------------

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

# -----------------------------
# SIDEBAR CONTROLS
# -----------------------------

mode = st.sidebar.selectbox(
"Mode",
["Study Mode","Exam Simulation"]
)

selected_chapter = st.sidebar.selectbox(
"Chapter",
["All","1"]
)

if selected_chapter != "All":
    filtered_questions = [q for q in question_bank if q["chapter"] == selected_chapter]
else:
    filtered_questions = question_bank

# -----------------------------
# SESSION STATE
# -----------------------------

if "questions" not in st.session_state:

    st.session_state.questions = random.sample(filtered_questions, min(QUESTION_COUNT,len(filtered_questions)))
    st.session_state.answers = {}
    st.session_state.start_time = time.time()
    st.session_state.finished = False
    st.session_state.score = 0

# -----------------------------
# TIMER
# -----------------------------

if mode == "Exam Simulation":

    remaining = EXAM_TIME - (time.time() - st.session_state.start_time)

    minutes = int(remaining//60)
    seconds = int(remaining%60)

    st.sidebar.write(f"Time Remaining: {minutes:02}:{seconds:02}")

    if remaining <= 0:
        st.session_state.finished = True

# -----------------------------
# PROGRESS BAR
# -----------------------------

progress = len(st.session_state.answers)/len(st.session_state.questions)
st.progress(progress)

# -----------------------------
# QUESTIONS
# -----------------------------

for i,q in enumerate(st.session_state.questions):

    st.subheader(f"Question {i+1}")

    ans = st.radio(
        q["question"],
        q["options"],
        key=f"q{i}"
    )

    st.session_state.answers[i] = q["options"].index(ans)

    if mode == "Study Mode":

        if st.session_state.answers[i] == q["answer"]:
            st.success("Correct")
        else:
            st.error("Incorrect")
            st.write("Correct answer:",q["options"][q["answer"]])

        st.write("Explanation:",q["explanation"])

# -----------------------------
# SUBMIT
# -----------------------------

if st.button("Submit Exam"):

    st.session_state.finished = True

# -----------------------------
# RESULTS
# -----------------------------

if st.session_state.finished:

    score = 0

    st.header("Results")

    for i,q in enumerate(st.session_state.questions):

        correct = q["answer"]
        user = st.session_state.answers.get(i)

        if user == correct:
            score +=1
            st.success(f"Question {i+1}: Correct")
        else:
            st.error(f"Question {i+1}: Incorrect")
            st.write("Correct:",q["options"][correct])

        st.write("Explanation:",q["explanation"])
        st.write("---")

    st.subheader(f"Final Score: {score}/{len(st.session_state.questions)}")

    # SAVE RESULTS

    result = pd.DataFrame({
        "score":[score],
        "total":[len(st.session_state.questions)],
        "date":[pd.Timestamp.now()]
    })

    if os.path.exists("results.csv"):
        result.to_csv("results.csv",mode="a",header=False,index=False)
    else:
        result.to_csv("results.csv",index=False)

    # DASHBOARD

    if os.path.exists("results.csv"):

        st.subheader("Progress Dashboard")

        df = pd.read_csv("results.csv")

        col1,col2 = st.columns(2)

        col1.metric("Average Score", round(df["score"].mean(),2))
        col2.metric("Attempts", len(df))

        st.line_chart(df["score"])

# -----------------------------
# NEW EXAM
# -----------------------------

if st.button("Start New Exam"):

    st.session_state.questions = random.sample(filtered_questions,min(QUESTION_COUNT,len(filtered_questions)))
    st.session_state.answers = {}
    st.session_state.start_time = time.time()
    st.session_state.finished = False
    st.rerun()
