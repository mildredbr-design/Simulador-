import streamlit as st
import random
import time

st.set_page_config(page_title="BABOK Trainer – Full", page_icon="📘")
st.title("BABOK Chapter 1 Trainer – Full Multi-Step Hard Scenarios")

EXAM_TIME = 60*60
TRAINING_QUESTIONS = 10
EXAM_QUESTIONS = 10

# -------------------------
# PREGUNTAS BABOK CHAPTER 1 (FULL 60)
# -------------------------
def generate_babok_ch1_questions():
    questions = [
        {"question":"What is the primary purpose of the BABOK® Guide?",
         "options":["To serve as a strict methodology for software development.",
                    "To define the practices of business analysis and set a standard for the profession.",
                    "To replace project management frameworks like PMBOK.",
                    "To provide a detailed guide for technical writing."],
         "answer":1,
         "explanation":"The BABOK Guide defines practices and standards for the business analysis profession.",
         "difficulty":"medium"},
        {"question":"According to the BABOK, business analysis is the practice of enabling change in an enterprise by defining needs and recommending solutions that deliver value to whom?",
         "options":["Stakeholders","The Project Manager","The IT Department","Shareholders"],
         "answer":0,
         "explanation":"Value is delivered to stakeholders.",
         "difficulty":"medium"},
        {"question":"The Business Analysis Core Concept Model (BACCM) is a conceptual framework that ensures all concepts within it are what?",
         "options":["Documented in a requirements specification",
                    "Mutually dependent and comprehensive",
                    "Approved by the project sponsor",
                    "Technically feasible"],
         "answer":1,
         "explanation":"The BACCM ensures concepts are interrelated and comprehensive.",
         "difficulty":"medium"},
        {"question":"Which of the following is NOT one of the six Knowledge Areas in the BABOK?",
         "options":["Business Analysis Planning and Monitoring",
                    "Requirements Life Cycle Management",
                    "Solution Evaluation",
                    "Project Financial Management"],
         "answer":3,
         "explanation":"Project Financial Management is not a BABOK Knowledge Area.",
         "difficulty":"medium"},
        {"question":"A 'Need' in the BACCM is best defined as:",
         "options":["The solution chosen by the stakeholders.",
                    "A problem or opportunity to be addressed.",
                    "The budget allocated for the project.",
                    "The project plan."],
         "answer":1,
         "explanation":"A need is a problem or opportunity that requires a solution.",
         "difficulty":"medium"},
        {"question":"Which Knowledge Area is responsible for ensuring that the solution meets the business needs and delivers value?",
         "options":["Strategy Analysis","Requirements Analysis and Design Definition","Solution Evaluation","Elicitation and Collaboration"],
         "answer":2,
         "explanation":"Solution Evaluation measures performance and ensures business value.",
         "difficulty":"medium"},
        {"question":"The circumstances that influence, are influenced by, and provide understanding of the change is the BACCM definition for:",
         "options":["Context","Stakeholder","Value","Need"],
         "answer":0,
         "explanation":"Context represents conditions and constraints surrounding a change.",
         "difficulty":"medium"},
        {"question":"The act of transformation in response to a need is the BACCM definition for:",
         "options":["Solution","Change","Value","Context"],
         "answer":1,
         "explanation":"Change is the transformation performed to meet a need.",
         "difficulty":"medium"},
        {"question":"Which of the following best describes a 'Requirement' according to the BABOK?",
         "options":["A condition or capability needed by a stakeholder to solve a problem or achieve an objective.",
                    "A detailed specification for a software component.",
                    "A project milestone.",
                    "A stakeholder's wish list."],
         "answer":0,
         "explanation":"Requirements describe stakeholder needs and conditions to achieve objectives.",
         "difficulty":"medium"},
        {"question":"The Knowledge Area that describes the tasks to perform in order to organize and coordinate the business analysis efforts is:",
         "options":["Elicitation and Collaboration","Business Analysis Planning and Monitoring","Strategy Analysis","Requirements Life Cycle Management"],
         "answer":1,
         "explanation":"Planning and Monitoring organizes and coordinates BA efforts.",
         "difficulty":"medium"},
        {"question":"A specific way of satisfying one or more needs in a context is the BACCM definition for:",
         "options":["Change","Solution","Value","Requirement"],
         "answer":1,
         "explanation":"A solution is a way to meet one or more needs.",
         "difficulty":"medium"},
        {"question":"Which Knowledge Area focuses on understanding the business needs and defining the solution scope?",
         "options":["Solution Evaluation","Requirements Analysis and Design Definition","Strategy Analysis","Elicitation and Collaboration"],
         "answer":2,
         "explanation":"Strategy Analysis focuses on business needs and solution scope.",
         "difficulty":"medium"},
        {"question":"The worth, importance, or usefulness of something to a stakeholder within a context is the BACCM definition for:",
         "options":["Need","Value","Solution","Change"],
         "answer":1,
         "explanation":"Value is the worth or usefulness of a solution to stakeholders.",
         "difficulty":"medium"},
        {"question":"The BABOK Guide is primarily intended for:",
         "options":["Only senior business analysts with over 10 years of experience.",
                    "Anyone who performs business analysis activities, regardless of their job title.",
                    "Only consultants working in agile environments.",
                    "Project managers who also handle requirements."],
         "answer":1,
         "explanation":"The BABOK Guide is for anyone performing BA activities.",
         "difficulty":"medium"},
        {"question":"Which Knowledge Area involves tasks such as preparing for elicitation, conducting elicitation, and confirming elicitation results?",
         "options":["Requirements Life Cycle Management","Elicitation and Collaboration","Business Analysis Planning and Monitoring","Solution Evaluation"],
         "answer":1,
         "explanation":"Elicitation and Collaboration includes preparing and conducting elicitation.",
         "difficulty":"medium"},
        {"question":"A group or individual with a relationship to the change, the need, or the solution is the BACCM definition for:",
         "options":["Stakeholder","Sponsor","Context","Developer"],
         "answer":0,
         "explanation":"Stakeholders have a relationship with the change, need, or solution.",
         "difficulty":"medium"},
        {"question":"The Knowledge Area that describes how to manage and maintain requirements and design information from inception to retirement is:",
         "options":["Requirements Analysis and Design Definition","Business Analysis Planning and Monitoring","Requirements Life Cycle Management","Strategy Analysis"],
         "answer":2,
         "explanation":"Requirements Life Cycle Management maintains requirements throughout their lifecycle.",
         "difficulty":"medium"},
        # ... Aquí siguen todas las demás preguntas hasta completar las 60
    ]
    return questions

# -------------------------
# BANCO COMPLETO
# -------------------------
question_bank = generate_babok_ch1_questions()

# -------------------------
# SELECCIÓN NIVEL Y MODO
# -------------------------
level = st.sidebar.selectbox("Select Difficulty Level", ["Medium"])
mode = st.sidebar.radio("Select Mode", ["Training Mode","Exam Mode"])

filtered_questions = [q for q in question_bank if q["difficulty"]==level.lower()]

# -------------------------
# SESIÓN STATE PARA EVITAR REPETICIONES
# -------------------------
if "level_selected" not in st.session_state or st.session_state.level_selected!=level:
    st.session_state.remaining_questions = filtered_questions.copy()
    random.shuffle(st.session_state.remaining_questions)
    st.session_state.current_index = 0
    st.session_state.answers = {}
    st.session_state.start_time = time.time()
    st.session_state.finished = False
    st.session_state.level_selected = level

# -------------------------
# TOMAR PREGUNTAS DEL MAZO
# -------------------------
question_count = TRAINING_QUESTIONS if mode=="Training Mode" else EXAM_QUESTIONS
start = st.session_state.current_index
end = start + question_count
current_questions = st.session_state.remaining_questions[start:end]

# -------------------------
# TIMER
# -------------------------
if mode=="Exam Mode":
    remaining = EXAM_TIME - (time.time() - st.session_state.start_time)
    minutes = int(remaining//60)
    seconds = int(remaining%60)
    st.sidebar.write(f"Time Remaining: {minutes:02}:{seconds:02}")
    if remaining <=0:
        st.session_state.finished = True

# -------------------------
# MOSTRAR PREGUNTAS
# -------------------------
for i,q in enumerate(current_questions):
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
    for i,q in enumerate(current_questions):
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
    st.subheader(f"Score: {score}/{len(current_questions)}")

# -------------------------
# NUEVO INTENTO / SIGUIENTE BLOQUE
# -------------------------
if st.button("Next/Repeat"):
    st.session_state.current_index += question_count
    if st.session_state.current_index >= len(st.session_state.remaining_questions):
        st.session_state.current_index = 0
        random.shuffle(st.session_state.remaining_questions)
    st.session_state.answers = {}
