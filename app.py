import streamlit as st
import random
import time

st.set_page_config(page_title="BABOK Chapter 1 Trainer", page_icon="📘")
st.title("BABOK Chapter 1 Trainer – BACCM & Introduction")

EXAM_TIME = 60*60
TRAINING_QUESTIONS = 20
EXAM_QUESTIONS = 40

# -------------------------
# QUESTION BANK GENERADO DINÁMICAMENTE
# -------------------------
question_bank = []

# -------------------------
# EASY 1–100
# -------------------------
easy_questions = []
for i in range(1, 101):
    easy_questions.append({
        "question": f"Easy Question {i}: Which BACCM concept does this example illustrate?",
        "options": ["Option A", "Option B", "Option C", "Option D"],
        "answer": random.randint(0, 3),
        "explanation": f"Explanation for Easy Question {i}.",
        "difficulty": "easy"
    })

# -------------------------
# MEDIUM 101–200
# -------------------------
medium_questions = []
for i in range(101, 201):
    medium_questions.append({
        "question": f"Medium Question {i}: Situational BACCM question example?",
        "options": ["Option A", "Option B", "Option C", "Option D"],
        "answer": random.randint(0, 3),
        "explanation": f"Explanation for Medium Question {i}.",
        "difficulty": "medium"
    })

# -------------------------
# HARD 201–300
# -------------------------
hard_questions = []
for i in range(201, 301):
    hard_questions.append({
        "question": f"Hard Question {i}: Complex scenario-based BACCM question?",
        "options": ["Option A", "Option B", "Option C", "Option D"],
        "answer": random.randint(0, 3),
        "explanation": f"Explanation for Hard Question {i}.",
        "difficulty": "hard"
    })

# -------------------------
# UNIR TODO EL BANCO
# -------------------------
question_bank.extend(easy_questions)
question_bank.extend(medium_questions)
question_bank.extend(hard_questions)

# -------------------------
# MODO
# -------------------------
mode = st.sidebar.radio("Select Mode", ["Training Mode","Exam Mode"])
question_count = TRAINING_QUESTIONS if mode == "Training Mode" else EXAM_QUESTIONS

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
    score = 0
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
# NUEVO INTENTO
# -------------------------
if st.button("New Attempt"):
    st.session_state.questions = random.sample(question_bank, question_count)
    st.session_state.answers = {}
    st.session_state.start_time = time.time()
    st.session_state.finished = False
    st.rerun()
