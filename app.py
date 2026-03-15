import streamlit as st
import random
import time

st.set_page_config(page_title="BABOK Chapter 1 Trainer – Full Multi-Step Hard", page_icon="📘")
st.title("BABOK Chapter 1 Trainer – Full Multi-Step Hard Scenarios")

EXAM_TIME = 60*60
TRAINING_QUESTIONS = 10
EXAM_QUESTIONS = 10

# -------------------------
# FUNCIONES PARA GENERAR PREGUNTAS
# -------------------------

def generate_easy_questions():
    questions = []
    for i in range(50):
        questions.append({
            "question": f"[Easy] Q{i+1}: Which BACCM concept represents a problem or opportunity?",
            "options":["Value","Need","Solution","Context"],
            "answer":1,
            "explanation":"Need represents a problem or opportunity that requires change.",
            "difficulty":"easy"
        })
        questions.append({
            "question": f"[Easy] Q{i+1}: Which concept represents the benefit perceived by stakeholders?",
            "options":["Need","Value","Context","Solution"],
            "answer":1,
            "explanation":"Value is the benefit or importance to stakeholders.",
            "difficulty":"easy"
        })
    return questions

def generate_medium_questions():
    questions = []
    for i in range(50):
        questions.append({
            "question": f"[Medium] Q{i+1}: A solution meets technical requirements but stakeholders perceive low benefit. Which concept is at risk?",
            "options":["Need","Solution","Value","Context"],
            "answer":2,
            "explanation":"Stakeholders’ perception determines value; low benefit risks value.",
            "difficulty":"medium"
        })
        questions.append({
            "question": f"[Medium] Q{i+1}: Which concept represents the transformation responding to a need?",
            "options":["Change","Value","Solution","Stakeholder"],
            "answer":0,
            "explanation":"Change represents transformation in response to a need.",
            "difficulty":"medium"
        })
    return questions

def generate_hard_questions():
    questions = []
    stakeholders = ["project manager","business owner","end-user","regulatory body","executive sponsor"]
    contexts = ["tight budget","cultural differences","remote teams","regulatory constraints","high-risk environment"]
    needs = ["improve efficiency","reduce cost","increase customer satisfaction","ensure compliance","enhance quality"]
    solutions = ["new software implementation","process reengineering","training program","organizational restructure","automation tool"]

    # 100 escenarios multi-step
    for i in range(100):
        stakeholder1, stakeholder2 = random.sample(stakeholders, 2)
        context = random.choice(contexts)
        need1, need2 = random.sample(needs, 2)
        solution = random.choice(solutions)

        # Pregunta 1: Value y Prioridad
        questions.append({
            "question": f"[Hard Q{i*3+1}] Scenario: {solution} is proposed to {need1} and {need2}. {stakeholder1} sees high benefit; {stakeholder2} sees risk due to {context}. Which concept helps prioritize needs?",
            "options":["Need","Value","Context","Change"],
            "answer":1,
            "explanation":"Value helps prioritize needs when stakeholders have conflicting views.",
            "difficulty":"hard"
        })

        # Pregunta 2: Change y gestión de stakeholders
        questions.append({
            "question": f"[Hard Q{i*3+2}] Based on the previous scenario, which BACCM concept is key to manage stakeholder resistance and implement the solution effectively?",
            "options":["Change","Solution","Stakeholder","Context"],
            "answer":0,
            "explanation":"Change represents the transformation and managing stakeholder responses.",
            "difficulty":"hard"
        })

        # Pregunta 3: Context y riesgos
        questions.append({
            "question": f"[Hard Q{i*3+3}] Considering the same scenario, which concept helps identify environmental and organizational constraints that may affect solution success?",
            "options":["Context","Need","Value","Solution"],
            "answer":0,
            "explanation":"Context includes conditions and constraints affecting solution acceptance.",
            "difficulty":"hard"
        })
    return questions

# -------------------------
# GENERAR BANCO COMPLETO
# -------------------------
question_bank = []
question_bank.extend(generate_easy_questions())    # 50 Easy
question_bank.extend(generate_medium_questions())  # 50 Medium
question_bank.extend(generate_hard_questions())    # 300 Hard

# -------------------------
# SELECCIÓN DE NIVEL Y MODO
# -------------------------
level = st.sidebar.selectbox("Select Difficulty Level", ["Easy", "Medium", "Hard"])
mode = st.sidebar.radio("Select Mode", ["Training Mode","Exam Mode"])

# Filtrar preguntas según nivel
filtered_questions = [q for q in question_bank if q["difficulty"] == level.lower()]

question_count = TRAINING_QUESTIONS if mode=="Training Mode" else EXAM_QUESTIONS

# -------------------------
# SESSION STATE
# -------------------------
if "questions" not in st.session_state or st.session_state.get("level_selected") != level:
    st.session_state.questions = random.sample(filtered_questions, question_count)
    st.session_state.answers = {}
    st.session_state.start_time = time.time()
    st.session_state.finished = False
    st.session_state.level_selected = level

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
    st.session_state.questions = random.sample(filtered_questions, question_count)
    st.session_state.answers = {}
    st.session_state.start_time = time.time()
    st.session_state.finished = False
    st.rerun()
