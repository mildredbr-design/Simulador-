import streamlit as st
import random
import time

st.set_page_config(page_title="BABOK Trainer – Full", page_icon="📘")
st.title("BABOK Chapter 1 Trainer – Full Multi-Step Hard Scenarios")

EXAM_TIME = 60*60
TRAINING_QUESTIONS = 10
EXAM_QUESTIONS = 10

# -------------------------
# PREGUNTAS ÚNICAS EASY
# -------------------------
def generate_easy_questions():
    questions = [
        # Section 1: Core Definitions
        {"question":"What is the primary purpose of business analysis according to BABOK v3?",
        "options":["To develop software solutions","To manage project timelines and budgets","To enable change by defining needs and recommending solutions that deliver value","To document technical specifications"],
        "answer":2,
        "explanation":"BABOK defines business analysis as enabling change by defining needs and recommending solutions that deliver value to stakeholders.",
        "difficulty":"easy"},
        {"question":"Business analysis is primarily concerned with:",
        "options":["Only IT-related changes","Any kind of change within an enterprise","Financial analysis and reporting","Marketing strategy development"],
        "answer":1,
        "explanation":"Business analysis applies to all types of enterprise change, not only IT.",
        "difficulty":"easy"},
        {"question":"The role of a business analyst is best described as:",
        "options":["A technical developer","A project manager","A change facilitator","A quality assurance tester"],
        "answer":2,
        "explanation":"Business analysts facilitate change by identifying needs and recommending solutions.",
        "difficulty":"easy"},
        {"question":"Which statement BEST reflects the business analyst's value proposition?",
        "options":["Reducing development costs by 20%","Ensuring projects finish on time","Delivering solutions that meet business needs and provide value","Writing perfect requirement documents"],
        "answer":2,
        "explanation":"The core value of business analysis is ensuring solutions deliver value and meet business needs.",
        "difficulty":"easy"},
        # Section 4: Key Terminology
        {"question":"A person or group with an interest in the change or solution is called a:",
        "options":["Developer","Stakeholder","Sponsor","User"],
        "answer":1,
        "explanation":"A stakeholder is any individual or group with an interest in or affected by the change.",
        "difficulty":"easy"},
        {"question":"The value delivered by a solution is measured by:",
        "options":["The number of features implemented","How well it meets stakeholder needs","The complexity of the technical architecture","The size of the requirement document"],
        "answer":1,
        "explanation":"Value is determined by how effectively the solution satisfies stakeholder needs.",
        "difficulty":"easy"},
        {"question":"A usable representation of a need is called a:",
        "options":["Requirement","Specification","Design","Blueprint"],
        "answer":0,
        "explanation":"BABOK defines a requirement as a usable representation of a need.",
        "difficulty":"easy"},
        {"question":"The set of activities a business analyst performs is organized in BABOK as:",
        "options":["Processes and procedures","Tasks and techniques","Phases and milestones","Sprints and iterations"],
        "answer":1,
        "explanation":"BABOK structures business analysis work using tasks and techniques.",
        "difficulty":"easy"},
        {"question":"The business analysis approach is typically defined during:",
        "options":["Solution Evaluation","Requirements Analysis and Design Definition","Business Analysis Planning and Monitoring","Strategy Analysis"],
        "answer":2,
        "explanation":"The business analysis approach is defined in Business Analysis Planning and Monitoring.",
        "difficulty":"easy"},
    ]
    return questions

# -------------------------
# PREGUNTAS ÚNICAS MEDIUM
# -------------------------
def generate_medium_questions():
    questions = [
        # Section 2: Knowledge Areas
        {"question":"How many Knowledge Areas does BABOK v3 define?",
        "options":["5","6","7","8"],
        "answer":1,
        "explanation":"BABOK v3 defines six Knowledge Areas.",
        "difficulty":"medium"},
        {"question":"Which Knowledge Area focuses on how business analysis work will be approached?",
        "options":["Requirements Life Cycle Management","Business Analysis Planning and Monitoring","Strategy Analysis","Elicitation and Collaboration"],
        "answer":1,
        "explanation":"Business Analysis Planning and Monitoring defines how BA activities will be approached.",
        "difficulty":"medium"},
        {"question":"Which Knowledge Area deals with understanding business needs and recommending solutions?",
        "options":["Solution Evaluation","Requirements Analysis and Design Definition","Strategy Analysis","Elicitation and Collaboration"],
        "answer":2,
        "explanation":"Strategy Analysis focuses on current state, future state, and change strategy.",
        "difficulty":"medium"},
        {"question":"Which Knowledge Area manages requirements from inception to retirement?",
        "options":["Business Analysis Planning and Monitoring","Requirements Life Cycle Management","Requirements Analysis and Design Definition","Solution Evaluation"],
        "answer":1,
        "explanation":"Requirements Life Cycle Management manages requirements throughout their lifecycle.",
        "difficulty":"medium"},
        {"question":"Producing usable requirements and designs for implementation occurs in which Knowledge Area?",
        "options":["Strategy Analysis","Requirements Analysis and Design Definition","Elicitation and Collaboration","Solution Evaluation"],
        "answer":1,
        "explanation":"Requirements Analysis and Design Definition structures and specifies requirements and designs.",
        "difficulty":"medium"},
        {"question":"Validating that a solution delivers expected value happens in which Knowledge Area?",
        "options":["Solution Evaluation","Strategy Analysis","Business Analysis Planning and Monitoring","Requirements Life Cycle Management"],
        "answer":0,
        "explanation":"Solution Evaluation measures performance and determines if the solution delivers value.",
        "difficulty":"medium"},
        {"question":"Which Knowledge Area involves preparing for and conducting elicitation?",
        "options":["Elicitation and Collaboration","Requirements Analysis and Design Definition","Business Analysis Planning and Monitoring","Strategy Analysis"],
        "answer":0,
        "explanation":"Elicitation and Collaboration focuses on eliciting and communicating with stakeholders.",
        "difficulty":"medium"},
        {"question":"The bridge between enterprise strategy and initiative execution is provided by:",
        "options":["Solution Evaluation","Strategy Analysis","Requirements Life Cycle Management","Business Analysis Planning and Monitoring"],
        "answer":1,
        "explanation":"Strategy Analysis links enterprise strategy with initiatives and solutions.",
        "difficulty":"medium"},
        # Section 3: Requirements Classification
        {"question":"Increase market share by 15% in two years is an example of what type of requirement?",
        "options":["Stakeholder Requirement","Business Requirement","Solution Requirement","Transition Requirement"],
        "answer":1,
        "explanation":"Business requirements describe goals and objectives of the organization.",
        "difficulty":"medium"},
        {"question":"A need expressed by a specific stakeholder group bridging business and solution requirements is called:",
        "options":["Business Requirement","Stakeholder Requirement","Functional Requirement","Transition Requirement"],
        "answer":1,
        "explanation":"Stakeholder requirements describe the needs of a stakeholder group.",
        "difficulty":"medium"},
        {"question":"The system must allow users to reset their passwords is an example of:",
        "options":["Business Requirement","Stakeholder Requirement","Functional Requirement","Transition Requirement"],
        "answer":2,
        "explanation":"Functional requirements describe behaviors or capabilities of a solution.",
        "difficulty":"medium"},
        {"question":"The application must support 10,000 concurrent users is what type of requirement?",
        "options":["Non-functional Requirement","Functional Requirement","Business Requirement","Stakeholder Requirement"],
        "answer":0,
        "explanation":"Performance constraints are non-functional requirements.",
        "difficulty":"medium"},
        {"question":"Temporary capabilities needed to transition from current to future state are called:",
        "options":["Solution Requirements","Transition Requirements","Business Requirements","Stakeholder Requirements"],
        "answer":1,
        "explanation":"Transition requirements enable the move from current state to future state.",
        "difficulty":"medium"},
        {"question":"Which requirement type focuses on what the solution must do?",
        "options":["Business Requirements","Stakeholder Requirements","Functional Requirements","Transition Requirements"],
        "answer":2,
        "explanation":"Functional requirements define what the system must do.",
        "difficulty":"medium"},
        {"question":"All managers must be trained on the new reporting system is an example of:",
        "options":["Transition Requirement","Business Requirement","Functional Requirement","Stakeholder Requirement"],
        "answer":0,
        "explanation":"Training during implementation is a transition requirement.",
        "difficulty":"medium"},
        {"question":"Solution requirements are composed of:",
        "options":["Business and stakeholder requirements","Functional and non-functional requirements","Transition and business requirements","Stakeholder and transition requirements"],
        "answer":1,
        "explanation":"Solution requirements include functional and non-functional requirements.",
        "difficulty":"medium"},
        # Sections 5–8 (Perspectives, Competencies, Tasks & Techniques, Scenario Questions)
        {"question":"Business analysis perspectives help business analysts to:",
        "options":["Limit their focus to specific industries","Apply business analysis practices in specific contexts","Avoid working on technical projects","Specialize in only one Knowledge Area"],
        "answer":1,
        "explanation":"Perspectives adapt BA practices to specific contexts such as Agile or Business Intelligence.",
        "difficulty":"medium"},
        {"question":"Which of these is NOT typically considered a business analysis perspective?",
        "options":["Agile","Business Intelligence","Programming","Information Technology"],
        "answer":2,
        "explanation":"Programming is not a BABOK perspective.",
        "difficulty":"medium"},
        {"question":"Skills such as communication, analytical thinking, and leadership are categorized as:",
        "options":["Techniques","Underlying Competencies","Knowledge Areas","Tasks"],
        "answer":1,
        "explanation":"BABOK classifies these skills as Underlying Competencies.",
        "difficulty":"medium"},
        {"question":"Which competency involves understanding how people think and learn?",
        "options":["Communication Skills","Analytical Thinking and Problem Solving","Learning","Interaction Skills"],
        "answer":2,
        "explanation":"Learning competency relates to understanding how individuals absorb and process information.",
        "difficulty":"medium"},
        {"question":"The ability to influence stakeholders and help them reach agreement relies on:",
        "options":["Technical writing skills","Interaction skills","Business knowledge","Tools and technology knowledge"],
        "answer":1,
        "explanation":"Interaction skills help BAs influence and collaborate with stakeholders.",
        "difficulty":"medium"},
        {"question":"How many tasks are defined across the six Knowledge Areas in BABOK v3?",
        "options":["30","50","75","100"],
        "answer":0,
        "explanation":"BABOK v3 defines 30 business analysis tasks across six Knowledge Areas.",
        "difficulty":"medium"},
        {"question":"A structured process for eliciting information is called a:",
        "options":["Task","Technique","Methodology","Framework"],
        "answer":1,
        "explanation":"Techniques are methods used to perform business analysis tasks.",
        "difficulty":"medium"},
        {"question":"Which of the following is an example of a business analysis technique?",
        "options":["Plan Business Analysis Approach","Conduct Elicitation","Interviews","Manage Requirements Traceability"],
        "answer":2,
        "explanation":"Interviews are a common elicitation technique.",
        "difficulty":"medium"},
        {"question":"Tasks are performed to:",
        "options":["Apply techniques effectively","Define business analysis methodology","Fulfill the purpose of each Knowledge Area","Create documentation templates"],
        "answer":2,
        "explanation":"Tasks define the work performed in each Knowledge Area.",
        "difficulty":"medium"},
        {"question":"A BA creates a plan identifying stakeholders, communication methods, and requirement management processes. Which Knowledge Area is this?",
        "options":["Business Analysis Planning and Monitoring","Requirements Life Cycle Management","Elicitation and Collaboration","Strategy Analysis"],
        "answer":0,
        "explanation":"Planning BA activities belongs to Business Analysis Planning and Monitoring.",
        "difficulty":"medium"},
        {"question":"Business needs change significantly during a project. Which Knowledge Area manages these changes?",
        "options":["Requirements Life Cycle Management","Solution Evaluation","Business Analysis Planning and Monitoring","Requirements Analysis and Design Definition"],
        "answer":0,
        "explanation":"Requirements Life Cycle Management governs requirement changes.",
        "difficulty":"medium"},
        {"question":"A BA analyzes root causes of a problem and defines the future state. Which Knowledge Area applies?",
        "options":["Strategy Analysis","Elicitation and Collaboration","Requirements Analysis and Design Definition","Solution Evaluation"],
        "answer":0,
        "explanation":"Strategy Analysis focuses on current state, future state, and change strategy.",
        "difficulty":"medium"},
        {"question":"After implementation, a BA evaluates solution performance and limitations. This belongs to:",
        "options":["Solution Evaluation","Strategy Analysis","Requirements Life Cycle Management","Business Analysis Planning and Monitoring"],
        "answer":0,
        "explanation":"Solution Evaluation measures solution performance and identifies improvements.",
        "difficulty":"medium"},
        {"question":"A BA conducts workshops and interviews with stakeholders. Which Knowledge Area applies?",
        "options":["Elicitation and Collaboration","Requirements Analysis and Design Definition","Business Analysis Planning and Monitoring","Strategy Analysis"],
        "answer":0,
        "explanation":"Workshops and interviews are part of Elicitation and Collaboration.",
        "difficulty":"medium"},
        {"question":"A BA organizes requirements into models and specifications. Which Knowledge Area is this?",
        "options":["Requirements Analysis and Design Definition","Requirements Life Cycle Management","Elicitation and Collaboration","Business Analysis Planning and Monitoring"],
        "answer":0,
        "explanation":"Requirements Analysis and Design Definition structures and specifies requirements.",
        "difficulty":"medium"},
    ]
    return questions

# -------------------------
# PREGUNTAS HARD MULTI-STEP
# -------------------------
def generate_hard_questions():
    questions = []
    stakeholders = ["project manager","business owner","end-user","regulatory body","executive sponsor"]
    contexts = ["tight budget","cultural differences","remote teams","regulatory constraints","high-risk environment"]
    needs = ["improve efficiency","reduce cost","increase customer satisfaction","ensure compliance","enhance quality"]
    solutions = ["new software implementation","process reengineering","training program","organizational restructure","automation tool"]

    for i in range(100):
        stakeholder1, stakeholder2 = random.sample(stakeholders,2)
        context = random.choice(contexts)
        need1, need2 = random.sample(needs,2)
        solution = random.choice(solutions)

        # Pregunta 1
        questions.append({
            "question": f"[Hard Q{i*3+1}] Scenario: {solution} addresses {need1} and {need2}. {stakeholder1} sees high benefit; {stakeholder2} sees risk due to {context}. Which concept helps prioritize needs?",
            "options":["Need","Value","Context","Change"],
            "answer":1,
            "explanation":"Value helps prioritize needs with conflicting stakeholders.",
            "difficulty":"hard"
        })
        # Pregunta 2
        questions.append({
            "question": f"[Hard Q{i*3+2}] Based on previous scenario, which concept manages stakeholder resistance effectively?",
            "options":["Change","Solution","Stakeholder","Context"],
            "answer":0,
            "explanation":"Change represents transformation and stakeholder management.",
            "difficulty":"hard"
        })
        # Pregunta 3
        questions.append({
            "question": f"[Hard Q{i*3+3}] Considering the same scenario, which concept identifies constraints affecting success?",
            "options":["Context","Need","Value","Solution"],
            "answer":0,
            "explanation":"Context includes conditions and constraints affecting acceptance.",
            "difficulty":"hard"
        })
    return questions

# -------------------------
# BANCO COMPLETO
# -------------------------
question_bank = []
question_bank.extend(generate_easy_questions())
question_bank.extend(generate_medium_questions())
question_bank.extend(generate_hard_questions())

# -------------------------
# SELECCIÓN NIVEL Y MODO
# -------------------------
level = st.sidebar.selectbox("Select Difficulty Level", ["Easy","Medium","Hard"])
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
    st.session_state
