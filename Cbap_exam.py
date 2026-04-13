import streamlit as st
import random
import time

# ─────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="CBAP Exam Simulator",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
#  CUSTOM CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Source+Sans+3:wght@400;600&display=swap');

:root {
    --navy:   #0a1628;
    --blue:   #1a3a6b;
    --gold:   #c9a84c;
    --gold2:  #f0d080;
    --light:  #f4f1eb;
    --white:  #ffffff;
    --green:  #1e7c4a;
    --red:    #9b2335;
    --mid:    #6b7a99;
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--navy) !important;
    color: var(--light) !important;
}

[data-testid="stAppViewContainer"] > .main {
    background-color: var(--navy) !important;
}

/* Header */
.exam-header {
    background: linear-gradient(135deg, var(--blue) 0%, var(--navy) 100%);
    border: 1px solid var(--gold);
    border-radius: 12px;
    padding: 2rem 2.5rem;
    margin-bottom: 2rem;
    text-align: center;
}
.exam-header h1 {
    font-family: 'Playfair Display', serif;
    color: var(--gold);
    font-size: 2.4rem;
    margin: 0 0 .4rem 0;
    letter-spacing: 1px;
}
.exam-header p {
    font-family: 'Source Sans 3', sans-serif;
    color: var(--mid);
    margin: 0;
    font-size: 1rem;
}

/* Progress bar */
.progress-container {
    background: rgba(255,255,255,0.08);
    border-radius: 8px;
    height: 10px;
    margin: 1rem 0 1.5rem;
    overflow: hidden;
}
.progress-bar {
    background: linear-gradient(90deg, var(--gold), var(--gold2));
    height: 100%;
    border-radius: 8px;
    transition: width .5s ease;
}

/* Question card */
.q-card {
    background: linear-gradient(160deg, #112244 0%, #0d1e3a 100%);
    border: 1px solid rgba(201,168,76,0.3);
    border-radius: 12px;
    padding: 1.8rem 2rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 24px rgba(0,0,0,0.4);
}
.q-number {
    font-family: 'Source Sans 3', sans-serif;
    color: var(--gold);
    font-size: .85rem;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: .7rem;
}
.q-chapter {
    display: inline-block;
    background: rgba(201,168,76,0.15);
    color: var(--gold2);
    font-size: .75rem;
    padding: 2px 10px;
    border-radius: 20px;
    border: 1px solid rgba(201,168,76,0.3);
    margin-bottom: .9rem;
    font-family: 'Source Sans 3', sans-serif;
}
.q-text {
    font-family: 'Source Sans 3', sans-serif;
    font-size: 1.05rem;
    line-height: 1.65;
    color: var(--light);
    margin: 0;
}

/* Radio buttons */
div[data-testid="stRadio"] > label {
    font-family: 'Source Sans 3', sans-serif !important;
    color: var(--light) !important;
}
div[data-testid="stRadio"] > div {
    gap: .5rem !important;
}

/* Feedback boxes */
.feedback-correct {
    background: rgba(30,124,74,0.2);
    border-left: 4px solid var(--green);
    border-radius: 8px;
    padding: 1rem 1.2rem;
    margin-top: 1rem;
    font-family: 'Source Sans 3', sans-serif;
    color: #6fe4a4;
}
.feedback-wrong {
    background: rgba(155,35,53,0.2);
    border-left: 4px solid var(--red);
    border-radius: 8px;
    padding: 1rem 1.2rem;
    margin-top: 1rem;
    font-family: 'Source Sans 3', sans-serif;
    color: #f4a0a0;
}
.feedback-explanation {
    margin-top: .6rem;
    color: #b0bdd4;
    font-size: .93rem;
    line-height: 1.55;
}

/* Score card */
.score-card {
    background: linear-gradient(135deg, #112244, #0d1e3a);
    border: 1px solid var(--gold);
    border-radius: 16px;
    padding: 2.5rem;
    text-align: center;
    margin: 1rem 0;
}
.score-big {
    font-family: 'Playfair Display', serif;
    font-size: 5rem;
    color: var(--gold);
    line-height: 1;
}
.score-label {
    font-family: 'Source Sans 3', sans-serif;
    color: var(--mid);
    font-size: 1rem;
    margin-top: .5rem;
}
.score-verdict {
    font-family: 'Playfair Display', serif;
    font-size: 1.6rem;
    margin-top: 1.2rem;
}
.passed { color: #6fe4a4; }
.failed { color: #f4a0a0; }

/* Buttons */
div[data-testid="stButton"] > button {
    background: linear-gradient(135deg, var(--gold), #a07828) !important;
    color: var(--navy) !important;
    font-family: 'Source Sans 3', sans-serif !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 8px !important;
    padding: .7rem 2rem !important;
    font-size: 1rem !important;
    cursor: pointer !important;
    transition: opacity .2s !important;
}
div[data-testid="stButton"] > button:hover {
    opacity: .85 !important;
}

/* Stats row */
.stats-row {
    display: flex;
    gap: 1rem;
    justify-content: center;
    margin: 1.5rem 0;
    flex-wrap: wrap;
}
.stat-box {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(201,168,76,0.25);
    border-radius: 10px;
    padding: .9rem 1.4rem;
    text-align: center;
    min-width: 120px;
}
.stat-num {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    color: var(--gold);
}
.stat-lbl {
    font-family: 'Source Sans 3', sans-serif;
    font-size: .78rem;
    color: var(--mid);
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Hide Streamlit branding */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  QUESTION BANK  (Chapters 1 & 2 — hard level)
# ─────────────────────────────────────────────
ALL_QUESTIONS = [
    # ── CHAPTER 1: Business Analysis Planning and Monitoring ──────────────
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "A business analyst is deciding how formally to document the business analysis approach. Which factor should have the MOST influence on this decision?",
        "options": [
            "A) The number of stakeholders involved in the project",
            "B) The organizational governance standards and project risk level",
            "C) The personal preference of the project sponsor",
            "D) The BA's prior experience with similar projects",
        ],
        "answer": "B) The organizational governance standards and project risk level",
        "explanation": "Per BABOK® v3 §2.1, the formality of the BA approach is primarily driven by organizational governance requirements and the risk level of the initiative, not by individual preferences or headcount.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "During business analysis planning, a BA discovers that two key stakeholders have fundamentally conflicting interests. What is the BEST course of action?",
        "options": [
            "A) Exclude the less influential stakeholder from requirements sessions",
            "B) Escalate immediately to senior management without further analysis",
            "C) Identify the conflict explicitly in the stakeholder engagement approach and plan mitigation strategies",
            "D) Proceed with elicitation and resolve the conflict when it surfaces naturally",
        ],
        "answer": "C) Identify the conflict explicitly in the stakeholder engagement approach and plan mitigation strategies",
        "explanation": "BABOK® v3 §2.4 requires the BA to understand stakeholder influence and interests, including conflicts, and to plan how those will be managed—not deferred or ignored.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "Which metric is MOST useful for monitoring the performance of the business analysis process itself (not the project)?",
        "options": [
            "A) Number of defects found in user acceptance testing",
            "B) Rate of requirements change requests after baseline",
            "C) Earned value of the overall project",
            "D) Sprint velocity of the development team",
        ],
        "answer": "B) Rate of requirements change requests after baseline",
        "explanation": "A high post-baseline change rate signals deficiencies in elicitation or analysis quality. BABOK® v3 §2.6 lists rework rates and change request volumes as key BA performance indicators.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "A BA is working on a highly uncertain, innovative product. Which business analysis approach is MOST appropriate?",
        "options": [
            "A) Predictive, with a fully documented requirements specification at project start",
            "B) Adaptive, with iterative elicitation and evolving requirements",
            "C) A hybrid approach, documenting all requirements upfront then using sprints",
            "D) No formal approach, relying entirely on stakeholder workshops",
        ],
        "answer": "B) Adaptive, with iterative elicitation and evolving requirements",
        "explanation": "BABOK® v3 §2.1 recommends adaptive approaches for high-uncertainty environments, where requirements are expected to change and early validation provides value.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "Which activity is part of 'Plan Business Analysis Information Management' but NOT 'Plan Business Analysis Approach'?",
        "options": [
            "A) Selecting the BA methodology",
            "B) Deciding how requirements will be stored, accessed, and version-controlled",
            "C) Identifying which stakeholders will review requirements",
            "D) Estimating the time needed for elicitation",
        ],
        "answer": "B) Deciding how requirements will be stored, accessed, and version-controlled",
        "explanation": "BABOK® v3 §2.5 (Plan BA Information Management) focuses on organization, storage, access, and traceability of BA information—distinct from methodology selection in §2.1.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "A sponsor asks a BA to skip formal stakeholder analysis because the project timeline is very short. What is the GREATEST risk of complying?",
        "options": [
            "A) The project budget may be underestimated",
            "B) Critical stakeholders with veto power may be missed, causing late-stage disruptions",
            "C) The BA will lack sufficient documentation for audits",
            "D) The development team may not have enough work to do",
        ],
        "answer": "B) Critical stakeholders with veto power may be missed, causing late-stage disruptions",
        "explanation": "Skipping stakeholder analysis risks overlooking key influencers whose unmet needs or opposition can derail the initiative—one of the most costly consequences described in BABOK® v3 §2.4.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "According to BABOK® v3, what does 'business analysis governance' primarily address?",
        "options": [
            "A) How the organization's strategic objectives are translated into projects",
            "B) Decision-making processes for requirements changes, approvals, and prioritization",
            "C) The reporting structure of the business analysis team",
            "D) Compliance with regulatory and legal requirements",
        ],
        "answer": "B) Decision-making processes for requirements changes, approvals, and prioritization",
        "explanation": "BABOK® v3 §2.3 defines BA governance as establishing who has authority to approve, change, and prioritize requirements—the decision-making framework around BA work products.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "When identifying the tasks to be performed during business analysis, a BA should consider which of the following FIRST?",
        "options": [
            "A) The skills available within the BA team",
            "B) The deliverables required by the project sponsor",
            "C) The overall business need and the context of the initiative",
            "D) Industry benchmarks for similar project types",
        ],
        "answer": "C) The overall business need and the context of the initiative",
        "explanation": "BABOK® v3 §2.1 establishes that the business need and initiative context drive the selection of approach, tasks, and deliverables—they are the primary input to BA planning.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "A BA completes an initial stakeholder analysis and assigns influence/interest scores. Three months into the project, a major reorganization occurs. What should the BA do?",
        "options": [
            "A) Nothing—stakeholder analysis is a one-time activity performed at project initiation",
            "B) Update the stakeholder register and revise the engagement approach to reflect the new organizational reality",
            "C) Ask the project manager to perform a new stakeholder analysis",
            "D) Continue with the original plan to avoid scope creep",
        ],
        "answer": "B) Update the stakeholder register and revise the engagement approach to reflect the new organizational reality",
        "explanation": "BABOK® v3 §2.4 treats stakeholder analysis as an ongoing activity. Changes in organizational structure alter influence, interests, and availability—requiring updates to the stakeholder register and engagement plan.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "Which of the following BEST describes a business analysis work plan?",
        "options": [
            "A) A document listing all project risks and mitigation strategies",
            "B) A schedule of BA tasks, resource assignments, milestones, and dependencies",
            "C) A high-level description of the solution approach chosen by the architect",
            "D) A requirements traceability matrix linking requirements to test cases",
        ],
        "answer": "B) A schedule of BA tasks, resource assignments, milestones, and dependencies",
        "explanation": "Per BABOK® v3 §2.2, the BA work plan details the specific tasks the BA will perform, who will perform them, estimated effort, and timing—distinct from solution design or traceability artifacts.",
    },

    # ── CHAPTER 2: Elicitation and Collaboration ──────────────────────────
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "During a facilitated workshop, two subject-matter experts (SMEs) provide contradictory information about the same business rule. What should the BA do FIRST?",
        "options": [
            "A) Document both versions and let the project manager decide which is correct",
            "B) Discard the less senior SME's input and proceed",
            "C) Acknowledge the discrepancy, probe for the root cause of the difference, and seek consensus or escalate as needed",
            "D) Stop the workshop and reschedule until stakeholders agree beforehand",
        ],
        "answer": "C) Acknowledge the discrepancy, probe for the root cause of the difference, and seek consensus or escalate as needed",
        "explanation": "BABOK® v3 §4.4 (Confirm Elicitation Results) and §4.5 (Communicate BA Information) require the BA to resolve conflicts through facilitation, investigation, and escalation—not unilateral decisions.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA needs to understand undocumented legacy system behavior. Which elicitation technique is MOST effective for capturing tacit knowledge held by long-tenured operators?",
        "options": [
            "A) Survey/Questionnaire",
            "B) Document analysis of legacy code",
            "C) Observation (shadowing / job shadowing)",
            "D) Interface analysis",
        ],
        "answer": "C) Observation (shadowing / job shadowing)",
        "explanation": "BABOK® v3 §10.22 recognizes observation as particularly effective at surfacing tacit, unarticulated knowledge that experienced users cannot easily verbalize—captured by watching them perform real work.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which elicitation technique would BEST reveal the emotional and motivational drivers behind a stakeholder's resistance to a new process?",
        "options": [
            "A) Prototyping",
            "B) Focus group",
            "C) In-depth interview using open-ended questions",
            "D) Requirements workshop with structured templates",
        ],
        "answer": "C) In-depth interview using open-ended questions",
        "explanation": "BABOK® v3 §10.15 highlights interviews—especially with open-ended probing—as the best tool for uncovering personal attitudes, motivations, and emotional context that group settings often suppress.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is the PRIMARY purpose of 'Confirm Elicitation Results' in the BABOK® v3 framework?",
        "options": [
            "A) To obtain formal sign-off from the project sponsor on the requirements",
            "B) To verify that the elicited information accurately represents stakeholder intent and is free of misunderstandings",
            "C) To validate that the requirements align with the business case",
            "D) To test the prototype against documented requirements",
        ],
        "answer": "B) To verify that the elicited information accurately represents stakeholder intent and is free of misunderstandings",
        "explanation": "BABOK® v3 §4.4 defines this task as ensuring the BA accurately captured what stakeholders meant—distinct from formal approval (verification) or business-case alignment (validation).",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA is planning to use a prototype to elicit requirements. Which risk should the BA actively manage throughout the elicitation sessions?",
        "options": [
            "A) Stakeholders may request excessive visual polish before business logic is confirmed",
            "B) The development team will begin building from the prototype prematurely",
            "C) Stakeholders may anchor on the prototype's appearance, mistaking it for the final solution and neglecting functional requirements",
            "D) The prototype will not load correctly on older hardware",
        ],
        "answer": "C) Stakeholders may anchor on the prototype's appearance, mistaking it for the final solution and neglecting functional requirements",
        "explanation": "BABOK® v3 §10.26 warns of 'prototype fixation'—stakeholders may focus on UI/UX minutiae or assume the prototype IS the solution, shifting focus away from validating business needs.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which of the following BEST distinguishes 'elicitation' from 'requirements analysis'?",
        "options": [
            "A) Elicitation produces formal requirements documents; analysis produces test cases",
            "B) Elicitation focuses on drawing out information from stakeholders; analysis focuses on structuring, refining, and interpreting that information",
            "C) Elicitation is performed by the project manager; analysis is performed by the BA",
            "D) Elicitation occurs only at project start; analysis occurs during implementation",
        ],
        "answer": "B) Elicitation focuses on drawing out information from stakeholders; analysis focuses on structuring, refining, and interpreting that information",
        "explanation": "BABOK® v3 Chapter 4 treats elicitation and analysis as distinct knowledge areas: elicitation is about gathering raw information; requirements analysis transforms that information into usable specifications.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA sends a detailed questionnaire to 80 geographically dispersed stakeholders. Response rate is only 15%. What is the MOST likely reason and the BEST corrective action?",
        "options": [
            "A) The questionnaire was too short; add more questions and resend",
            "B) The questions were too closed-ended; convert to open-ended and resend",
            "C) The questionnaire lacked context or perceived relevance; clarify purpose, shorten it, and follow up personally with key non-respondents",
            "D) Stakeholders are resistant to the project; escalate to senior management",
        ],
        "answer": "C) The questionnaire lacked context or perceived relevance; clarify purpose, shorten it, and follow up personally with key non-respondents",
        "explanation": "BABOK® v3 §10.34 identifies low response rates as often caused by unclear purpose, excessive length, or perceived irrelevance—corrected by improving design and personalizing follow-up.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "When planning collaborative games for elicitation, which outcome should the BA prioritize?",
        "options": [
            "A) Ensuring all participants enjoy the activity equally",
            "B) Generating a ranked prioritization list of requirements for the backlog",
            "C) Creating an environment that surfaces creative ideas and breaks through communication barriers",
            "D) Replacing traditional workshops to reduce meeting time",
        ],
        "answer": "C) Creating an environment that surfaces creative ideas and breaks through communication barriers",
        "explanation": "BABOK® v3 §10.6 presents collaborative games as techniques designed to overcome inhibitions, spark creativity, and encourage unconventional thinking—not primarily as prioritization tools.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA conducts a focus group and notices one vocal participant is dominating the discussion, causing others to self-censor. What is the BEST facilitation response?",
        "options": [
            "A) Remove the dominant participant from the session",
            "B) Use structured techniques such as round-robin sharing or anonymous input to give quieter participants equal voice",
            "C) End the session and reschedule with different participants",
            "D) Allow it to continue—dominant voices usually reflect the group consensus",
        ],
        "answer": "B) Use structured techniques such as round-robin sharing or anonymous input to give quieter participants equal voice",
        "explanation": "BABOK® v3 §10.10 and general facilitation best practices recommend structured participation methods to counter groupthink and social dominance effects in group elicitation settings.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which of the following is an OUTPUT of the 'Elicit Elicitation Information' task (§4.1) in BABOK® v3?",
        "options": [
            "A) Approved requirements baseline",
            "B) Elicitation activity plan",
            "C) Elicitation notes (raw, unconfirmed information from sources)",
            "D) Stakeholder requirements specification document",
        ],
        "answer": "C) Elicitation notes (raw, unconfirmed information from sources)",
        "explanation": "BABOK® v3 §4.1 outputs 'elicitation notes'—raw information gathered from stakeholders and sources. Confirmation, analysis, and formal specification occur in subsequent tasks.",
    },
    # ── ADDITIONAL MIXED HARD QUESTIONS ───────────────────────────────────
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "In a predictive (waterfall) project, which business analysis performance metric indicates that elicitation quality was POOR?",
        "options": [
            "A) High velocity in early development sprints",
            "B) High number of defects traced back to ambiguous or missing requirements",
            "C) Low number of change requests during the design phase",
            "D) Stakeholder satisfaction scores above 90% at project close",
        ],
        "answer": "B) High number of defects traced back to ambiguous or missing requirements",
        "explanation": "BABOK® v3 §2.6 cites defect origin analysis as a key BA quality metric; defects traceable to requirements gaps or ambiguity directly measure the quality of elicitation and analysis work.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A business analyst is using benchmarking as an elicitation technique. What is the PRIMARY goal of this technique?",
        "options": [
            "A) Setting quantitative performance targets by comparing the organization against internal historical data or external industry leaders",
            "B) Listing all functional requirements for the system under development",
            "C) Identifying which stakeholders have the highest influence on the project",
            "D) Documenting the current state 'as-is' process in detail",
        ],
        "answer": "A) Setting quantitative performance targets by comparing the organization against internal historical data or external industry leaders",
        "explanation": "BABOK® v3 §10.4 defines benchmarking as comparing processes, products, or performance metrics against best-in-class references to identify improvement targets—not as a process documentation or stakeholder analysis tool.",
    },
]

# ─────────────────────────────────────────────
#  SESSION STATE INIT
# ─────────────────────────────────────────────
def init_state():
    if "started" not in st.session_state:
        st.session_state.started = False
    if "questions" not in st.session_state:
        st.session_state.questions = []
    if "current" not in st.session_state:
        st.session_state.current = 0
    if "answers" not in st.session_state:
        st.session_state.answers = {}
    if "submitted" not in st.session_state:
        st.session_state.submitted = {}
    if "finished" not in st.session_state:
        st.session_state.finished = False
    if "num_questions" not in st.session_state:
        st.session_state.num_questions = 15
    if "start_time" not in st.session_state:
        st.session_state.start_time = None

init_state()

# ─────────────────────────────────────────────
#  HEADER
# ─────────────────────────────────────────────
st.markdown("""
<div class="exam-header">
    <h1>📋 CBAP® Exam Simulator</h1>
    <p>Chapters 1 & 2 · BABOK® v3 · Difficulty: Advanced</p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  START SCREEN
# ─────────────────────────────────────────────
if not st.session_state.started:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style='background:rgba(255,255,255,0.05);border:1px solid rgba(201,168,76,0.3);
                    border-radius:12px;padding:1.8rem;margin-bottom:1.5rem;
                    font-family:"Source Sans 3",sans-serif;color:#b0bdd4;line-height:1.7'>
            <b style='color:#c9a84c;font-size:1.05rem'>📌 Exam Rules</b><br><br>
            • Questions from Chapter 1 (BA Planning & Monitoring) and Chapter 2 (Elicitation & Collaboration)<br>
            • Hard-difficulty questions based on BABOK® v3<br>
            • One attempt per question — confirm before moving on<br>
            • Immediate explanations after each answer<br>
            • Passing score: <b style='color:#f0d080'>70%</b> (CBAP benchmark)
        </div>
        """, unsafe_allow_html=True)

        n = st.slider("Number of questions", min_value=5, max_value=len(ALL_QUESTIONS),
                      value=min(15, len(ALL_QUESTIONS)), step=1)
        st.session_state.num_questions = n

        if st.button("🚀  Start Exam", use_container_width=True):
            pool = ALL_QUESTIONS.copy()
            random.shuffle(pool)
            st.session_state.questions = pool[:n]
            st.session_state.current = 0
            st.session_state.answers = {}
            st.session_state.submitted = {}
            st.session_state.finished = False
            st.session_state.started = True
            st.session_state.start_time = time.time()
            st.rerun()

# ─────────────────────────────────────────────
#  RESULTS SCREEN
# ─────────────────────────────────────────────
elif st.session_state.finished:
    qs = st.session_state.questions
    correct = sum(
        1 for i, q in enumerate(qs)
        if st.session_state.answers.get(i) == q["answer"]
    )
    total = len(qs)
    pct = round(correct / total * 100)
    elapsed = int(time.time() - (st.session_state.start_time or time.time()))
    mins, secs = divmod(elapsed, 60)
    passed = pct >= 70

    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        verdict_class = "passed" if passed else "failed"
        verdict_text = "✅ PASSED" if passed else "❌ NOT PASSED"
        st.markdown(f"""
        <div class="score-card">
            <div class="score-big">{pct}%</div>
            <div class="score-label">{correct} correct out of {total} questions</div>
            <div class="score-verdict {verdict_class}">{verdict_text}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="stats-row">
            <div class="stat-box">
                <div class="stat-num">{correct}</div>
                <div class="stat-lbl">Correct</div>
            </div>
            <div class="stat-box">
                <div class="stat-num">{total - correct}</div>
                <div class="stat-lbl">Incorrect</div>
            </div>
            <div class="stat-box">
                <div class="stat-num">{mins}:{secs:02d}</div>
                <div class="stat-lbl">Time</div>
            </div>
            <div class="stat-box">
                <div class="stat-num">{pct}%</div>
                <div class="stat-lbl">Score</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Per-chapter breakdown
        ch1_q = [(i, q) for i, q in enumerate(qs) if "Chapter 1" in q["chapter"]]
        ch2_q = [(i, q) for i, q in enumerate(qs) if "Chapter 2" in q["chapter"]]
        ch1_c = sum(1 for i, q in ch1_q if st.session_state.answers.get(i) == q["answer"])
        ch2_c = sum(1 for i, q in ch2_q if st.session_state.answers.get(i) == q["answer"])

        if ch1_q or ch2_q:
            st.markdown("<br>", unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                r = f"{ch1_c}/{len(ch1_q)}" if ch1_q else "N/A"
                st.markdown(f"""
                <div class="stat-box" style="width:100%">
                    <div class="stat-num">{r}</div>
                    <div class="stat-lbl">Chapter 1 Score</div>
                </div>""", unsafe_allow_html=True)
            with c2:
                r = f"{ch2_c}/{len(ch2_q)}" if ch2_q else "N/A"
                st.markdown(f"""
                <div class="stat-box" style="width:100%">
                    <div class="stat-num">{r}</div>
                    <div class="stat-lbl">Chapter 2 Score</div>
                </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Review wrong answers
        wrong = [(i, q) for i, q in enumerate(qs)
                 if st.session_state.answers.get(i) != q["answer"]]
        if wrong:
            with st.expander(f"📖  Review {len(wrong)} incorrect answer(s)"):
                for idx, (i, q) in enumerate(wrong):
                    user_ans = st.session_state.answers.get(i, "Not answered")
                    st.markdown(f"""
                    <div style='margin-bottom:1.2rem;padding:1rem;
                                background:rgba(155,35,53,0.12);border-radius:8px;
                                border-left:3px solid #9b2335;
                                font-family:"Source Sans 3",sans-serif'>
                        <div style='color:#c9a84c;font-size:.8rem;margin-bottom:.5rem'>
                            Q{i+1} · {q['chapter']}
                        </div>
                        <div style='color:#f4f1eb;margin-bottom:.7rem'>{q['question']}</div>
                        <div style='color:#f4a0a0'>❌ Your answer: {user_ans}</div>
                        <div style='color:#6fe4a4'>✅ Correct: {q['answer']}</div>
                        <div style='color:#8090aa;margin-top:.5rem;font-size:.9rem'>
                            💡 {q['explanation']}
                        </div>
                    </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔄  New Exam", use_container_width=True):
            for key in ["started","questions","current","answers","submitted","finished","start_time"]:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

# ─────────────────────────────────────────────
#  EXAM SCREEN
# ─────────────────────────────────────────────
else:
    qs = st.session_state.questions
    total = len(qs)
    idx = st.session_state.current
    q = qs[idx]

    # Progress
    progress_pct = int(idx / total * 100)
    st.markdown(f"""
    <div style='font-family:"Source Sans 3",sans-serif;color:#6b7a99;
                font-size:.85rem;display:flex;justify-content:space-between'>
        <span>Question {idx+1} of {total}</span>
        <span>{progress_pct}% complete</span>
    </div>
    <div class="progress-container">
        <div class="progress-bar" style="width:{progress_pct}%"></div>
    </div>
    """, unsafe_allow_html=True)

    # Question card
    st.markdown(f"""
    <div class="q-card">
        <div class="q-number">Question {idx + 1}</div>
        <div class="q-chapter">{q['chapter']}</div>
        <p class="q-text">{q['question']}</p>
    </div>
    """, unsafe_allow_html=True)

    already_submitted = idx in st.session_state.submitted

    if not already_submitted:
        chosen = st.radio(
            "Select your answer:",
            q["options"],
            key=f"radio_{idx}",
            index=None,
        )
        st.session_state.answers[idx] = chosen

        col_a, col_b = st.columns([1, 4])
        with col_a:
            if st.button("✅  Confirm Answer", use_container_width=True):
                if st.session_state.answers.get(idx) is None:
                    st.warning("Please select an answer before confirming.")
                else:
                    st.session_state.submitted[idx] = True
                    st.rerun()
    else:
        user_ans = st.session_state.answers.get(idx)
        correct_ans = q["answer"]
        is_correct = user_ans == correct_ans

        # Show options (disabled appearance via markdown)
        for opt in q["options"]:
            if opt == correct_ans:
                color = "#1e7c4a"
                icon = "✅"
                bg = "rgba(30,124,74,0.15)"
            elif opt == user_ans and not is_correct:
                color = "#9b2335"
                icon = "❌"
                bg = "rgba(155,35,53,0.15)"
            else:
                color = "#6b7a99"
                icon = "○"
                bg = "transparent"
            st.markdown(f"""
            <div style='padding:.6rem 1rem;margin:.3rem 0;border-radius:8px;
                        background:{bg};border:1px solid {color}33;
                        font-family:"Source Sans 3",sans-serif;color:{color}'>
                {icon} {opt}
            </div>""", unsafe_allow_html=True)

        # Feedback
        if is_correct:
            st.markdown(f"""
            <div class="feedback-correct">
                🎯 <b>Correct!</b>
                <div class="feedback-explanation">💡 {q['explanation']}</div>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="feedback-wrong">
                ❌ <b>Incorrect.</b> The correct answer is: <b>{correct_ans}</b>
                <div class="feedback-explanation">💡 {q['explanation']}</div>
            </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Navigation
        is_last = idx == total - 1
        col_nav1, col_nav2 = st.columns([1, 1])
        with col_nav1:
            if idx > 0:
                if st.button("⬅  Previous", use_container_width=True):
                    st.session_state.current -= 1
                    st.rerun()
        with col_nav2:
            if is_last:
                if st.button("🏁  Finish Exam", use_container_width=True):
                    st.session_state.finished = True
                    st.rerun()
            else:
                if st.button("Next  ➡", use_container_width=True):
                    st.session_state.current += 1
                    st.rerun()
