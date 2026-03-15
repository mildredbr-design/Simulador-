import streamlit as st
import random
import time

st.set_page_config(page_title="BABOK Chapter 1 Trainer", page_icon="📘")
st.title("BABOK Chapter 1 Trainer – BACCM & Introduction")

EXAM_TIME = 60*60
TRAINING_QUESTIONS = 20
EXAM_QUESTIONS = 40

# -------------------------
# QUESTION BANK (300 preguntas por patrón)
# -------------------------
question_bank = []

# -------------------------
# EASY QUESTIONS (1-100)
# -------------------------
easy_questions = [
{"question":"According to BABOK, what is business analysis?","options":["Manage IT infrastructure","Enable change by defining needs and recommending solutions","Develop software","Test systems"],"answer":1,"explanation":"Business analysis enables change by defining needs and recommending solutions that deliver value.","difficulty":"easy"},
{"question":"Which BACCM concept describes the environment for change?","options":["Value","Context","Solution","Need"],"answer":1,"explanation":"Context describes the circumstances surrounding the change.","difficulty":"easy"},
{"question":"Which concept represents a problem or opportunity to be addressed?","options":["Need","Solution","Stakeholder","Value"],"answer":0,"explanation":"Need represents a problem or opportunity.","difficulty":"easy"},
{"question":"Which concept represents the parties impacted by change?","options":["Solution","Stakeholder","Value","Context"],"answer":1,"explanation":"Stakeholders are anyone affected by or who can influence the change.","difficulty":"easy"},
{"question":"Which BACCM concept represents the benefit perceived by stakeholders?","options":["Need","Change","Value","Solution"],"answer":2,"explanation":"Value represents the importance or usefulness of something to stakeholders.","difficulty":"easy"},
# ... continuar hasta 100 variando conceptos y redacción
]

question_bank.extend(easy_questions)

# -------------------------
# MEDIUM QUESTIONS (101-200)
# -------------------------
medium_questions = [
{"question":"A stakeholder requests a solution conflicting with organizational goals. Which BACCM concept is relevant?","options":["Need","Solution","Context","Value"],"answer":2,"explanation":"Context includes the circumstances, constraints, and environment surrounding the change.","difficulty":"medium"},
{"question":"Which scenario best describes 'Value' in BACCM?","options":["Money spent","Benefit perceived by stakeholders","Project timeline","Technical specification"],"answer":1,"explanation":"Value represents the benefit or importance to stakeholders.","difficulty":"medium"},
{"question":"During analysis, a solution satisfies technical requirements but stakeholders feel it has low benefit. Which BACCM concept is primarily at risk?","options":["Need","Solution","Value","Context"],"answer":2,"explanation":"Value depends on stakeholder perception; even a technically correct solution can have low value.","difficulty":"medium"},
{"question":"A solution is delivered without considering cultural factors, causing resistance. Which BACCM concept should have been analyzed?","options":["Change","Stakeholder","Context","Solution"],"answer":2,"explanation":"Context includes environmental factors, including culture.","difficulty":"medium"},
{"question":"Which BACCM concept represents the act of transformation responding to a need?","options":["Change","Value","Solution","Stakeholder"],"answer":0,"explanation":"Change represents transformation in response to a need.","difficulty":"medium"},
# ... continuar hasta 100 variando escenarios y redacción
]

question_bank.extend(medium_questions)

# -------------------------
# HARD QUESTIONS (201-300)
# -------------------------
hard_questions = [
{"question":"A technically correct solution is rejected by stakeholders due to perceived low impact. Which BACCM concept explains this?","options":["Solution","Value","Need","Change"],"answer":1,"explanation":"Stakeholders determine value; even correct solutions may have low perceived value.","difficulty":"hard"},
{"question":"During analysis, conflicting stakeholder needs arise. Which BACCM concept helps to prioritize?","options":["Context","Need","Stakeholder","Value"],"answer":3,"explanation":"Value is used to assess the importance of different needs for prioritization.","difficulty":"hard"},
{"question":"A solution meets initial requirements but fails long-term objectives. Which BACCM concept could have prevented this?","options":["Change","Solution","Context","Value"],"answer":2,"explanation":"Context includes the circumstances surrounding the change and helps anticipate future impacts.","difficulty":"hard"},
{"question":"Which BACCM concept ensures that a need is properly addressed by a solution?","options":["Need","Solution","Stakeholder","Value"],"answer":1,"explanation":"Solutions are designed to satisfy identified needs.","difficulty":"hard"},
{"question":"Stakeholders feel a solution creates unnecessary disruption. Which BACCM concept is relevant?","options":["Change","Context","Value","Need"],"answer":1,"explanation":"Context includes conditions and circumstances that affect the acceptance of a solution.","difficulty":"hard"},
# ... continuar hasta 100 variando escenarios complejos
]

question_bank.extend(hard_questions)

# -------------------------
# MODE SELECTION
# -------------------------
mode = st.sidebar.radio("Select Mode", ["Training Mode","Exam Mode"])
question_count = TRAINING_QUESTIONS if mode=="Training Mode" else EXAM_QUESTIONS

# -------------------------
# SESSION STATE
# -------------------------
if "questions" not in st.session_state:
    st.session_state.questions = random.sample(question_bank, question_count)
    st.session_state.answers = {}
    st.session_state.start_time = time.time()
    st.session_state.finished = False

# -------------------------
# TIMER (Exam Mode)
# -------------------------
if mode=="Exam Mode":
    remaining = EXAM_TIME - (time.time() - st.session_state.start_time)
    minutes = int(remaining//60)
    seconds = int(remaining%60)
    st.sidebar.write(f"Time Remaining: {minutes:02}:{seconds:02}")
    if remaining<=0:
        st.session_state.finished=True

# -------------------------
# QUESTIONS
# -------------------------
for i,q in enumerate(st.session_state.questions):
    st.subheader(f"Question {i+1}")
    ans = st.radio(q["question"], q["options"], key=f"q{i}")
    st.session_state.answers[i] = q["options"].index(ans)

# -------------------------
# SUBMIT
# -------------------------
if st.button("Submit"):
    st.session_state.finished = True

# -------------------------
# RESULTS
# -------------------------
if st.session_state.finished:
    score=0
    st.header("Results")
    for i,q in enumerate(st.session_state.questions):
        user = st.session_state.answers.get(i)
        correct = q["answer"]
        if user==correct:
            score+=1
            st.success(f"Question {i+1}: Correct")
        else:
            st.error(f"Question {i+1}: Incorrect")
            st.write("Correct answer:", q["options"][correct])
        st.write("Explanation:", q["explanation"])
        st.write("---")
    st.subheader(f"Score: {score}/{len(st.session_state.questions)}")

# -------------------------
# NEW ATTEMPT
# -------------------------
if st.button("New Attempt"):
    st.session_state.questions = random.sample(question_bank, question_count)
    st.session_state.answers = {}
    st.session_state.start_time = time.time()
    st.session_state.finished = False
    st.rerun()
