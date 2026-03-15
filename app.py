import streamlit as st
import random
import time

st.set_page_config(page_title="BABOK Chapter 1 Trainer", page_icon="📘")
st.title("BABOK Chapter 1 Trainer – BACCM & Introduction")

EXAM_TIME = 60*60
TRAINING_QUESTIONS = 10
EXAM_QUESTIONS = 10

# -------------------------
# BANCO DE PREGUNTAS REALISTAS
# -------------------------
question_bank = [
    # EASY
    {
        "question": "Which BACCM concept represents a problem or opportunity to be addressed?",
        "options": ["Value","Need","Solution","Context"],
        "answer":1,
        "explanation":"Need represents a problem or opportunity that requires change.",
        "difficulty":"easy"
    },
    {
        "question":"Which concept describes the environment in which change occurs?",
        "options":["Context","Stakeholder","Value","Solution"],
        "answer":0,
        "explanation":"Context describes the circumstances affecting the change.",
        "difficulty":"easy"
    },
    {
        "question":"Who are stakeholders according to BABOK?",
        "options":["Only project managers","Individuals or groups affected or influencing change","Only business owners","Only customers"],
        "answer":1,
        "explanation":"Stakeholders are anyone affected by or who can influence the change.",
        "difficulty":"easy"
    },
    {
        "question":"Which concept represents the benefit perceived by stakeholders?",
        "options":["Need","Value","Context","Solution"],
        "answer":1,
        "explanation":"Value is the benefit or importance to stakeholders.",
        "difficulty":"easy"
    },
    {
        "question":"Which BACCM concept represents a specific way to satisfy a need?",
        "options":["Solution","Stakeholder","Change","Context"],
        "answer":0,
        "explanation":"Solution is a way to satisfy a need.",
        "difficulty":"easy"
    },

    # MEDIUM
    {
        "question":"A stakeholder requests a solution conflicting with organizational goals. Which BACCM concept is relevant?",
        "options":["Need","Solution","Context","Value"],
        "answer":2,
        "explanation":"Context includes environmental and organizational factors affecting change.",
        "difficulty":"medium"
    },
    {
        "question":"Which scenario best describes 'Value' in BACCM?",
        "options":["Money spent","Benefit perceived by stakeholders","Project timeline","Technical specification"],
        "answer":1,
        "explanation":"Value is the benefit perceived by stakeholders.",
        "difficulty":"medium"
    },
    {
        "question":"A solution satisfies technical requirements but stakeholders feel it has low benefit. Which concept is at risk?",
        "options":["Need","Solution","Value","Context"],
        "answer":2,
        "explanation":"Stakeholders’ perception determines value; low benefit risks value.",
        "difficulty":"medium"
    },
    {
        "question":"A solution is delivered without considering cultural factors, causing resistance. Which concept should have been analyzed?",
        "options":["Change","Stakeholder","Context","Solution"],
        "answer":2,
        "explanation":"Context includes cultural and organizational environment.",
        "difficulty":"medium"
    },
    {
        "question":"Which concept represents the act of transformation responding to a need?",
        "options":["Change","Value","Solution","Stakeholder"],
        "answer":0,
        "explanation":"Change represents transformation in response to a need.",
        "difficulty":"medium"
    },

    # HARD
    {
        "question":"A technically correct solution is rejected by stakeholders due to low perceived impact. Which concept explains this?",
        "options":["Solution","Value","Need","Change"],
        "answer":1,
        "explanation":"Even correct solutions may have low value if stakeholders perceive little benefit.",
        "difficulty":"hard"
    },
    {
        "question":"During analysis, conflicting stakeholder needs arise. Which BACCM concept helps prioritize?",
        "options":["Context","Need","Stakeholder","Value"],
        "answer":3,
        "explanation":"Value helps assess importance of different needs for prioritization.",
        "difficulty":"hard"
    },
    {
        "question":"A solution meets initial requirements but fails long-term objectives. Which concept could prevent this?",
        "options":["Change","Solution","Context","Value"],
        "answer":2,
        "explanation":"Context includes circumstances surrounding change to anticipate future impacts.",
        "difficulty":"hard"
    },
    {
        "question":"Which concept ensures that a need is properly addressed by a solution?",
        "options":["Need","Solution","Stakeholder","Value"],
        "answer":1,
        "explanation":"Solutions are designed to satisfy identified needs.",
        "difficulty":"hard"
    },
    {
        "question":"Stakeholders feel a solution creates unnecessary disruption. Which concept is relevant?",
        "options":["Change","Context","Value","Need"],
        "answer":1,
        "explanation":"Context considers conditions that affect acceptance of a solution.",
        "difficulty":"hard"
    }
]

# -------------------------
# MODO
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
    if remaining <= 0:
        st.session_state.finished = True

# -------------------------
# PREGUNTAS
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
# RESULTADOS
# -------------------------
if st.session_state.finished:
    score=0
    st.header("Results")
    for i,q in enumerate(st.session_state.questions):
        user = st.session_state.answers.get(i)
        correct = q["answer"]
        if user==correct:
            score += 1
            st.success(f"Question {i+1}: Correct")
        else:
            st.error(f"Question {i+1}: Incorrect")
            st.write("Correct answer:", q["options"][correct])
        st.write("Explanation:", q["explanation"])
        st.write("---")
    st.subheader(f"Score: {score}/{len(st.session_state.questions)}")

# -------------------------
# NUEVO INTENTO
# -------------------------
if st.button("New Attempt"):
    st.session_state.questions = random.sample(question_bank, question_count)
    st.session_state.answers = {}
    st.session_state.start_time = time.time()
    st.session_state.finished = False
    st.rerun()
