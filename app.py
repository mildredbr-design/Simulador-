import streamlit as st
import random
import time

st.set_page_config(page_title="BABOK Trainer – Full", page_icon="📘")
st.title("BABOK Chapter 1 Trainer – Full Multi-Step Hard Scenarios")

EXAM_TIME = 60*60
TRAINING_QUESTIONS = 10
EXAM_QUESTIONS = 10

# -------------------------
# GENERAR 25 PREGUNTAS ÚNICAS EASY
# -------------------------
def generate_easy_questions():
    questions = [
        {"question":"Which BACCM concept represents a problem or opportunity?","options":["Value","Need","Solution","Context"],"answer":1,"explanation":"Need represents a problem or opportunity that requires change.","difficulty":"easy"},
        {"question":"Which concept represents the benefit perceived by stakeholders?","options":["Need","Value","Context","Solution"],"answer":1,"explanation":"Value is the benefit perceived by stakeholders.","difficulty":"easy"},
        {"question":"Who are considered stakeholders?","options":["Only project managers","Individuals or groups affected or influencing change","Only business owners","Only customers"],"answer":1,"explanation":"Stakeholders include anyone affected or who can influence change.","difficulty":"easy"},
        {"question":"Which concept represents a specific way to satisfy a need?","options":["Solution","Stakeholder","Change","Context"],"answer":0,"explanation":"Solution is a way to satisfy a need.","difficulty":"easy"},
        {"question":"Which concept describes the environment in which change occurs?","options":["Context","Stakeholder","Value","Solution"],"answer":0,"explanation":"Context describes circumstances affecting the change.","difficulty":"easy"},
        {"question":"Which BACCM concept is about the benefit perceived by stakeholders?","options":["Value","Need","Solution","Change"],"answer":0,"explanation":"Value represents the perceived benefit.","difficulty":"easy"},
        {"question":"Which concept represents a transformation responding to a need?","options":["Change","Need","Context","Solution"],"answer":0,"explanation":"Change represents the act of transformation.","difficulty":"easy"},
        {"question":"A solution that addresses a need is called?","options":["Value","Need","Solution","Context"],"answer":2,"explanation":"Solution satisfies a need.","difficulty":"easy"},
        {"question":"What concept defines who is affected by change?","options":["Stakeholder","Solution","Context","Change"],"answer":0,"explanation":"Stakeholder is anyone affected or influencing the change.","difficulty":"easy"},
        {"question":"The circumstances around a change is known as?","options":["Need","Context","Value","Solution"],"answer":1,"explanation":"Context describes the environment where change occurs.","difficulty":"easy"},
        {"question":"What BACCM concept is assessed by stakeholder perception?","options":["Need","Solution","Value","Change"],"answer":2,"explanation":"Value depends on stakeholders’ perception.","difficulty":"easy"},
        {"question":"A specific approach to satisfy a requirement is called?","options":["Change","Solution","Value","Context"],"answer":1,"explanation":"Solution is the approach.","difficulty":"easy"},
        {"question":"Stakeholders are important for which concept?","options":["Change","Context","Stakeholder","Solution"],"answer":2,"explanation":"Stakeholders influence or are affected by change.","difficulty":"easy"},
        {"question":"Which concept affects acceptance of a solution?","options":["Context","Need","Change","Value"],"answer":0,"explanation":"Context affects acceptance.","difficulty":"easy"},
        {"question":"Identifying a problem or opportunity relates to which concept?","options":["Value","Need","Solution","Change"],"answer":1,"explanation":"Need is the problem/opportunity.","difficulty":"easy"},
        {"question":"Perceived benefits from stakeholders is called?","options":["Change","Value","Context","Solution"],"answer":1,"explanation":"Value is perceived benefit.","difficulty":"easy"},
        {"question":"Implementing a solution to satisfy a need is?","options":["Need","Solution","Change","Value"],"answer":2,"explanation":"Change is the implementation of a solution to a need.","difficulty":"easy"},
        {"question":"Who can influence the success of a change?","options":["Stakeholders","Solution","Context","Value"],"answer":0,"explanation":"Stakeholders influence success.","difficulty":"easy"},
        {"question":"The environment affecting change is?","options":["Context","Need","Solution","Change"],"answer":0,"explanation":"Context is the environment.","difficulty":"easy"},
        {"question":"Benefit to stakeholders is known as?","options":["Value","Need","Change","Solution"],"answer":0,"explanation":"Value represents benefit.","difficulty":"easy"},
        {"question":"A method to meet a requirement is called?","options":["Solution","Change","Context","Value"],"answer":0,"explanation":"Solution meets requirements.","difficulty":"easy"},
        {"question":"People affected by change are called?","options":["Stakeholder","Need","Value","Solution"],"answer":0,"explanation":"Stakeholders are affected people.","difficulty":"easy"},
        {"question":"Analyzing circumstances around a change relates to?","options":["Context","Change","Need","Value"],"answer":0,"explanation":"Context is the environment analysis.","difficulty":"easy"},
        {"question":"What ensures a need is satisfied?","options":["Solution","Value","Change","Stakeholder"],"answer":0,"explanation":"Solution ensures need satisfaction.","difficulty":"easy"},
        {"question":"Transforming a solution into reality is called?","options":["Change","Need","Value","Context"],"answer":0,"explanation":"Change represents the transformation.","difficulty":"easy"},
    ]
    return questions

# -------------------------
# GENERAR 25 PREGUNTAS ÚNICAS MEDIUM
# -------------------------
def generate_medium_questions():
    questions = [
        {"question":"A solution meets technical requirements but stakeholders perceive low benefit. Which concept is at risk?","options":["Need","Solution","Value","Context"],"answer":2,"explanation":"Value depends on stakeholders’ perception.","difficulty":"medium"},
        {"question":"Ignoring cultural factors causes resistance. Which concept should be analyzed?","options":["Change","Stakeholder","Context","Solution"],"answer":2,"explanation":"Context includes cultural and organizational factors.","difficulty":"medium"},
        {"question":"A stakeholder requests a solution conflicting with organizational goals. Which concept is relevant?","options":["Need","Solution","Context","Value"],"answer":2,"explanation":"Context includes organizational constraints.","difficulty":"medium"},
        {"question":"Which concept represents the act of transformation responding to a need?","options":["Change","Value","Solution","Stakeholder"],"answer":0,"explanation":"Change represents transformation.","difficulty":"medium"},
        {"question":"Solution satisfies requirements but stakeholders feel low benefit. Which concept is at risk?","options":["Need","Solution","Value","Context"],"answer":2,"explanation":"Value is at risk if stakeholders perceive low benefit.","difficulty":"medium"},
        {"question":"Failure to consider regulatory constraints affects which concept?","options":["Need","Context","Solution","Value"],"answer":1,"explanation":"Regulatory and organizational environment is Context.","difficulty":"medium"},
        {"question":"Which concept helps prioritize conflicting stakeholder needs?","options":["Value","Need","Change","Context"],"answer":0,"explanation":"Value helps prioritize importance of needs.","difficulty":"medium"},
        {"question":"A solution meets functional requirements but stakeholders reject it. Which concept is low?","options":["Change","Need","Value","Context"],"answer":2,"explanation":"Stakeholder-perceived Value is low.","difficulty":"medium"},
        {"question":"Analyzing stakeholder expectations relates to which concept?","options":["Stakeholder","Need","Change","Value"],"answer":0,"explanation":"Stakeholder concept identifies affected/influencing individuals.","difficulty":"medium"},
        {"question":"Identifying risks due to budget or culture affects which concept?","options":["Context","Solution","Change","Need"],"answer":0,"explanation":"Context includes such constraints.","difficulty":"medium"},
        # Completa hasta 25 Medium únicas
    ]
    return questions

# -------------------------
# GENERAR 100 ESCENARIOS HARD MULTI-STEP
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
question_count = TRAINING_QUESTIONS if mode=="Training Mode" else EXAM_QUESTIONS

# -------------------------
# SESSION STATE: actualizar al cambiar nivel
# -------------------------
if "level_selected" not in st.session_state or st.session_state.level_selected!=level:
    st.session_state.questions = random.sample(filtered_questions, min(question_count,len(filtered_questions)))
    st.session_state.answers = {}
    st.session_state.start_time = time.time()
    st.session_state.finished = False
    st.session_state.level_selected = level

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
for i,q in enumerate(st.session_state.questions):
    st.subheader(f"Question {i+1}")
    ans = st.radio(q["question"], q["options"], key=f"q{i}")
    st.session_state.answers[i] = q["options"].index(ans)

# -------------------------
# BOTÓN SUBMIT
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
    st.session_state.questions = random.sample(filtered_questions, min(question_count,len(filtered_questions)))
    st.session_state.answers = {}
    st.session_state.start_time = time.time()
    st.session_state.finished = False
    st.rerun()
