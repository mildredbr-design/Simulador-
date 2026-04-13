import streamlit as st
import random
import time

st.set_page_config(
    page_title="Simulador CBAP",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Source+Sans+3:wght@400;600&display=swap');

:root {
    --navy:  #0a1628;
    --blue:  #1a3a6b;
    --gold:  #c9a84c;
    --gold2: #f0d080;
    --light: #f4f1eb;
    --green: #1e7c4a;
    --red:   #9b2335;
    --mid:   #6b7a99;
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--navy) !important;
    color: var(--light) !important;
}
[data-testid="stAppViewContainer"] > .main { background-color: var(--navy) !important; }

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
.exam-header p { font-family:'Source Sans 3',sans-serif; color:var(--mid); margin:0; font-size:1rem; }

.progress-container { background:rgba(255,255,255,0.08); border-radius:8px; height:10px; margin:1rem 0 1.5rem; overflow:hidden; }
.progress-bar { background:linear-gradient(90deg,var(--gold),var(--gold2)); height:100%; border-radius:8px; transition:width .5s ease; }

.q-card {
    background: linear-gradient(160deg,#112244 0%,#0d1e3a 100%);
    border: 1px solid rgba(201,168,76,0.3);
    border-radius: 12px;
    padding: 1.8rem 2rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 24px rgba(0,0,0,0.4);
}
.q-number { font-family:'Source Sans 3',sans-serif; color:var(--gold); font-size:.85rem; font-weight:600; letter-spacing:2px; text-transform:uppercase; margin-bottom:.7rem; }
.q-chapter { display:inline-block; background:rgba(201,168,76,0.15); color:var(--gold2); font-size:.75rem; padding:2px 10px; border-radius:20px; border:1px solid rgba(201,168,76,0.3); margin-bottom:.9rem; font-family:'Source Sans 3',sans-serif; }
.q-text { font-family:'Source Sans 3',sans-serif; font-size:1.05rem; line-height:1.65; color:var(--light); margin:0; }

/* FIX: radio label color */
div[data-testid="stRadio"] label p,
div[data-testid="stRadio"] label span,
div[data-testid="stRadio"] label {
    font-family: 'Source Sans 3', sans-serif !important;
    color: #f4f1eb !important;
    font-size: 1rem !important;
}
div[data-testid="stRadio"] > div { gap:.5rem !important; }

.feedback-correct { background:rgba(30,124,74,0.2); border-left:4px solid var(--green); border-radius:8px; padding:1rem 1.2rem; margin-top:1rem; font-family:'Source Sans 3',sans-serif; color:#6fe4a4; }
.feedback-wrong   { background:rgba(155,35,53,0.2);  border-left:4px solid var(--red);   border-radius:8px; padding:1rem 1.2rem; margin-top:1rem; font-family:'Source Sans 3',sans-serif; color:#f4a0a0; }
.feedback-explanation { margin-top:.6rem; color:#c8d4e8; font-size:.93rem; line-height:1.55; }

.score-card { background:linear-gradient(135deg,#112244,#0d1e3a); border:1px solid var(--gold); border-radius:16px; padding:2.5rem; text-align:center; margin:1rem 0; }
.score-big  { font-family:'Playfair Display',serif; font-size:5rem; color:var(--gold); line-height:1; }
.score-label { font-family:'Source Sans 3',sans-serif; color:var(--mid); font-size:1rem; margin-top:.5rem; }
.score-verdict { font-family:'Playfair Display',serif; font-size:1.6rem; margin-top:1.2rem; }
.passed { color:#6fe4a4; } .failed { color:#f4a0a0; }

div[data-testid="stButton"] > button {
    background: linear-gradient(135deg,var(--gold),#a07828) !important;
    color: var(--navy) !important;
    font-family: 'Source Sans 3',sans-serif !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 8px !important;
    padding: .7rem 2rem !important;
    font-size: 1rem !important;
}
div[data-testid="stButton"] > button:hover { opacity:.85 !important; }

.stats-row { display:flex; gap:1rem; justify-content:center; margin:1.5rem 0; flex-wrap:wrap; }
.stat-box { background:rgba(255,255,255,0.06); border:1px solid rgba(201,168,76,0.25); border-radius:10px; padding:.9rem 1.4rem; text-align:center; min-width:120px; }
.stat-num { font-family:'Playfair Display',serif; font-size:2rem; color:var(--gold); }
.stat-lbl { font-family:'Source Sans 3',sans-serif; font-size:.78rem; color:var(--mid); text-transform:uppercase; letter-spacing:1px; }

#MainMenu, footer, header { visibility:hidden; }
</style>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────
#  QUESTION BANK  —  150 questions  (Chapters 1 & 2, hard)
# ──────────────────────────────────────────────────────────────
ALL_QUESTIONS = [
    # ═══════════════════════════════════════════════════════════
    #  CHAPTER 1 – Business Analysis Planning and Monitoring
    # ═══════════════════════════════════════════════════════════
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "A business analyst is deciding how formally to document the business analysis approach. Which factor should have the MOST influence on this decision?",
        "options": ["A) The number of stakeholders involved","B) The organizational governance standards and project risk level","C) The personal preference of the project sponsor","D) The BA's prior experience with similar projects"],
        "answer": "B) The organizational governance standards and project risk level",
        "explanation": "Per BABOK® v3 §2.1, the formality of the BA approach is primarily driven by organizational governance requirements and the risk level of the initiative.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "During BA planning, two key stakeholders have fundamentally conflicting interests. What is the BEST course of action?",
        "options": ["A) Exclude the less influential stakeholder from requirements sessions","B) Escalate immediately to senior management without further analysis","C) Identify the conflict in the stakeholder engagement approach and plan mitigation strategies","D) Proceed with elicitation and resolve the conflict when it surfaces naturally"],
        "answer": "C) Identify the conflict in the stakeholder engagement approach and plan mitigation strategies",
        "explanation": "BABOK® v3 §2.4 requires the BA to understand stakeholder conflicts and plan how they will be managed proactively.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "Which metric is MOST useful for monitoring the performance of the business analysis process itself?",
        "options": ["A) Number of defects found in UAT","B) Rate of requirements change requests after baseline","C) Earned value of the overall project","D) Sprint velocity of the development team"],
        "answer": "B) Rate of requirements change requests after baseline",
        "explanation": "BABOK® v3 §2.6 lists rework rates and post-baseline change request volumes as key BA performance indicators.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "A BA is working on a highly uncertain, innovative product. Which business analysis approach is MOST appropriate?",
        "options": ["A) Predictive, with fully documented requirements at project start","B) Adaptive, with iterative elicitation and evolving requirements","C) Hybrid: document all requirements upfront, then use sprints","D) No formal approach, relying entirely on stakeholder workshops"],
        "answer": "B) Adaptive, with iterative elicitation and evolving requirements",
        "explanation": "BABOK® v3 §2.1 recommends adaptive approaches for high-uncertainty environments where requirements are expected to evolve.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "Which activity is part of 'Plan Business Analysis Information Management' but NOT 'Plan Business Analysis Approach'?",
        "options": ["A) Selecting the BA methodology","B) Deciding how requirements will be stored, accessed, and version-controlled","C) Identifying which stakeholders will review requirements","D) Estimating the time needed for elicitation"],
        "answer": "B) Deciding how requirements will be stored, accessed, and version-controlled",
        "explanation": "BABOK® v3 §2.5 (Plan BA Information Management) focuses on storage, access, and traceability—distinct from methodology selection in §2.1.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "A sponsor asks a BA to skip formal stakeholder analysis because the timeline is very short. What is the GREATEST risk?",
        "options": ["A) The project budget may be underestimated","B) Critical stakeholders with veto power may be missed, causing late-stage disruptions","C) The BA will lack sufficient documentation for audits","D) The development team may not have enough work to do"],
        "answer": "B) Critical stakeholders with veto power may be missed, causing late-stage disruptions",
        "explanation": "Skipping stakeholder analysis risks overlooking key influencers whose opposition can derail the initiative—described in BABOK® v3 §2.4.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "According to BABOK® v3, what does 'business analysis governance' primarily address?",
        "options": ["A) How strategic objectives are translated into projects","B) Decision-making processes for requirements changes, approvals, and prioritization","C) The reporting structure of the BA team","D) Compliance with regulatory and legal requirements"],
        "answer": "B) Decision-making processes for requirements changes, approvals, and prioritization",
        "explanation": "BABOK® v3 §2.3 defines BA governance as establishing who has authority to approve, change, and prioritize requirements.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "When identifying the tasks to be performed during business analysis, a BA should consider which of the following FIRST?",
        "options": ["A) The skills available within the BA team","B) The deliverables required by the project sponsor","C) The overall business need and the context of the initiative","D) Industry benchmarks for similar project types"],
        "answer": "C) The overall business need and the context of the initiative",
        "explanation": "BABOK® v3 §2.1 establishes that the business need and initiative context drive the selection of approach, tasks, and deliverables.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "A BA completes a stakeholder analysis. Three months into the project, a major reorganization occurs. What should the BA do?",
        "options": ["A) Nothing—stakeholder analysis is a one-time activity","B) Update the stakeholder register and revise the engagement approach","C) Ask the project manager to perform a new stakeholder analysis","D) Continue with the original plan to avoid scope creep"],
        "answer": "B) Update the stakeholder register and revise the engagement approach",
        "explanation": "BABOK® v3 §2.4 treats stakeholder analysis as ongoing. Organizational changes alter influence and availability, requiring updates.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "Which of the following BEST describes a business analysis work plan?",
        "options": ["A) A document listing all project risks and mitigation strategies","B) A schedule of BA tasks, resource assignments, milestones, and dependencies","C) A high-level description of the solution approach chosen by the architect","D) A requirements traceability matrix linking requirements to test cases"],
        "answer": "B) A schedule of BA tasks, resource assignments, milestones, and dependencies",
        "explanation": "BABOK® v3 §2.2 defines the BA work plan as detailing specific tasks, who performs them, estimated effort, and timing.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "In a predictive project, which BA performance metric indicates poor elicitation quality?",
        "options": ["A) High velocity in early development sprints","B) High number of defects traced back to ambiguous or missing requirements","C) Low number of change requests during the design phase","D) Stakeholder satisfaction scores above 90% at project close"],
        "answer": "B) High number of defects traced back to ambiguous or missing requirements",
        "explanation": "BABOK® v3 §2.6 cites defect origin analysis as a key BA quality metric—defects traceable to requirements gaps directly measure elicitation quality.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "Which input is REQUIRED to begin the 'Plan Business Analysis Approach' task?",
        "options": ["A) Validated requirements baseline","B) Business need and organizational process assets","C) Approved project charter signed by the sponsor","D) Completed stakeholder register"],
        "answer": "B) Business need and organizational process assets",
        "explanation": "BABOK® v3 §2.1 lists the business need and organizational process assets (standards, templates, guidelines) as the primary inputs to planning the BA approach.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "A BA is estimating effort for business analysis activities. Which technique accounts for UNCERTAINTY most explicitly?",
        "options": ["A) Bottom-up estimation","B) Expert judgment only","C) Three-point estimation (optimistic, most likely, pessimistic)","D) Parametric estimation based on historical data"],
        "answer": "C) Three-point estimation (optimistic, most likely, pessimistic)",
        "explanation": "Three-point estimation explicitly models uncertainty by considering best-case, expected, and worst-case scenarios—recommended in BABOK® v3 §2.2 for uncertain work.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "Which of the following is the PRIMARY purpose of a RACI chart in business analysis planning?",
        "options": ["A) To track requirements changes over time","B) To clarify who is Responsible, Accountable, Consulted, and Informed for each BA task","C) To document the sequence of BA activities","D) To prioritize requirements based on stakeholder importance"],
        "answer": "B) To clarify who is Responsible, Accountable, Consulted, and Informed for each BA task",
        "explanation": "BABOK® v3 §2.4 uses RACI charts to define roles and responsibilities, reducing ambiguity and ensuring appropriate stakeholder involvement.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "When should a BA tailor the business analysis approach to use less documentation?",
        "options": ["A) When the project is high-risk and complex","B) When the organization has strong governance requirements","C) When the team is co-located, collaborative, and the domain is well-understood","D) When the project timeline is short regardless of other factors"],
        "answer": "C) When the team is co-located, collaborative, and the domain is well-understood",
        "explanation": "BABOK® v3 §2.1 notes that less formal documentation is appropriate when the team works closely together and the domain is familiar, reducing communication risks.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "What is the MAIN difference between 'plan-driven' and 'change-driven' business analysis approaches?",
        "options": ["A) Plan-driven uses agile sprints; change-driven uses waterfall phases","B) Plan-driven defines scope upfront and controls changes; change-driven embraces evolving requirements","C) Plan-driven is used for small projects; change-driven for large ones","D) Plan-driven requires more stakeholders; change-driven requires fewer"],
        "answer": "B) Plan-driven defines scope upfront and controls changes; change-driven embraces evolving requirements",
        "explanation": "BABOK® v3 §2.1 distinguishes these approaches: plan-driven (predictive) stabilizes scope early, while change-driven (adaptive) welcomes scope evolution.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "A BA discovers that a critical requirement has changed AFTER the requirements baseline was approved. What should happen FIRST?",
        "options": ["A) Implement the change and inform stakeholders after development","B) Reject the change to protect the project timeline","C) Submit the change through the established change control process","D) Renegotiate the project scope and budget immediately"],
        "answer": "C) Submit the change through the established change control process",
        "explanation": "BABOK® v3 §2.3 requires that changes to baselined requirements go through the defined change control process to maintain governance and traceability.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "Which characteristic of requirements information management is addressed by BABOK® v3 §2.5?",
        "options": ["A) Ensuring requirements are written in active voice","B) Defining how requirements will be organized, stored, and accessible throughout the project lifecycle","C) Setting the order in which requirements will be implemented","D) Determining which requirements will be included in the MVP"],
        "answer": "B) Defining how requirements will be organized, stored, and accessible throughout the project lifecycle",
        "explanation": "§2.5 focuses on the structure, repositories, access controls, and retention policies for BA information assets.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "A BA notices that scheduled elicitation sessions are consistently running over time with no useful output. Which corrective action is MOST appropriate?",
        "options": ["A) Cancel remaining sessions and rely on documented legacy requirements","B) Evaluate the preparation, facilitation techniques, and participant selection; adjust accordingly","C) Add more participants to each session to increase input","D) Switch entirely to surveys to save time"],
        "answer": "B) Evaluate the preparation, facilitation techniques, and participant selection; adjust accordingly",
        "explanation": "BABOK® v3 §2.6 (Monitor BA Performance) calls for root-cause analysis of performance issues and corrective action—not abandonment of the process.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "Which stakeholder is MOST likely to have the highest interest AND the highest influence in a business analysis initiative?",
        "options": ["A) End users who will interact with the system daily","B) The project sponsor who approved the funding","C) External auditors reviewing compliance","D) IT support staff who will maintain the system"],
        "answer": "B) The project sponsor who approved the funding",
        "explanation": "BABOK® v3 §2.4 notes that sponsors typically hold both high influence (decision authority, funding control) and high interest (accountable for outcomes).",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "In an adaptive project, how does the BA work plan differ from one in a predictive project?",
        "options": ["A) There is no work plan in adaptive projects","B) The work plan is created once at project start and never changed","C) The work plan is updated iteratively at the start of each iteration or sprint","D) The work plan is owned entirely by the Scrum Master"],
        "answer": "C) The work plan is updated iteratively at the start of each iteration or sprint",
        "explanation": "BABOK® v3 §2.2 notes that in adaptive environments the BA work plan is a living document, re-evaluated and adjusted at each iteration boundary.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "A BA has been asked to assess whether the current business analysis process is delivering value. Which approach is MOST aligned with BABOK® v3?",
        "options": ["A) Survey stakeholders on their satisfaction with BA deliverables","B) Compare BA effort hours against project budget","C) Review BA performance metrics, lessons learned, and compare actual vs. planned outcomes","D) Count the total number of requirements documented"],
        "answer": "C) Review BA performance metrics, lessons learned, and compare actual vs. planned outcomes",
        "explanation": "BABOK® v3 §2.6 prescribes monitoring performance through defined metrics, comparing actuals to the plan, and incorporating lessons learned.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "When does traceability add the MOST value in business analysis?",
        "options": ["A) On small, simple projects with a single stakeholder","B) On large, complex projects with multiple layers of requirements and many change requests","C) Only during the testing phase of the project","D) When the sponsor requires a traceability matrix as a contractual deliverable"],
        "answer": "B) On large, complex projects with multiple layers of requirements and many change requests",
        "explanation": "BABOK® v3 §2.5 notes traceability value scales with complexity, the number of requirement relationships, and the frequency of changes.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "Which tool is BEST suited for visualizing stakeholder influence and interest levels simultaneously?",
        "options": ["A) Requirements traceability matrix","B) Power/Interest grid","C) RACI chart","D) Work Breakdown Structure"],
        "answer": "B) Power/Interest grid",
        "explanation": "The Power/Interest grid (BABOK® v3 §10.38) maps stakeholders by their level of influence (power) and engagement interest, guiding tailored engagement strategies.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "What is the BEST indicator that a BA work plan needs to be revised?",
        "options": ["A) A new BA joins the team","B) The project sponsor changes","C) Actual BA task durations consistently exceed planned estimates","D) The development team requests additional documentation"],
        "answer": "C) Actual BA task durations consistently exceed planned estimates",
        "explanation": "BABOK® v3 §2.6 states that significant variance between planned and actual performance is a trigger for re-planning and corrective action.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "A BA must decide whether requirements will be stored in a dedicated requirements management tool or in shared documents. Which factor is LEAST relevant to this decision?",
        "options": ["A) The volume and complexity of requirements","B) The personal preference of the lead developer","C) The organization's existing tool landscape and licensing","D) The need for traceability and version control"],
        "answer": "B) The personal preference of the lead developer",
        "explanation": "BABOK® v3 §2.5 bases information management decisions on requirements complexity, traceability needs, and organizational capabilities—not individual preferences outside BA scope.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "Which of the following BEST describes the relationship between the BA approach and the overall project methodology?",
        "options": ["A) The BA approach is always independent of the project methodology","B) The BA approach is defined after the project methodology and must align with it","C) The project methodology is derived from the BA approach","D) Both are defined by the steering committee, not the BA"],
        "answer": "B) The BA approach is defined after the project methodology and must align with it",
        "explanation": "BABOK® v3 §2.1 states the BA approach must be consistent with and tailored to the selected project methodology (predictive, adaptive, or hybrid).",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "What does 'level of formality' in business analysis governance mean?",
        "options": ["A) How many signatures are required on requirements documents","B) The degree to which governance processes, roles, and decisions are documented and enforced","C) Whether the BA uses automated or manual tracking tools","D) The number of approval layers before requirements are baselined"],
        "answer": "B) The degree to which governance processes, roles, and decisions are documented and enforced",
        "explanation": "BABOK® v3 §2.3 describes formality as spanning a spectrum from informal verbal agreements to rigorous, documented change control boards.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "Which output of 'Identify Business Analysis Performance Improvements' feeds BACK into the planning process?",
        "options": ["A) Validated requirements","B) Updated business analysis approach and work plan","C) Approved change requests submitted to the CCB","D) Stakeholder engagement assessment"],
        "answer": "B) Updated business analysis approach and work plan",
        "explanation": "BABOK® v3 §2.6 closes the loop: performance findings lead to updates in the BA approach and work plan, improving future performance.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "When identifying stakeholders, which source is MOST likely to reveal hidden or informal influencers not on the org chart?",
        "options": ["A) The formal organizational hierarchy","B) The project charter","C) Interviews with known stakeholders asking who else impacts or is impacted by the initiative","D) The HR system's employee directory"],
        "answer": "C) Interviews with known stakeholders asking who else impacts or is impacted by the initiative",
        "explanation": "BABOK® v3 §2.4 recommends snowball sampling through interviews to surface informal influencers and champions not visible in formal structures.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "A BA is starting a project in a regulated industry with strict audit requirements. Which information management characteristic is MOST critical?",
        "options": ["A) Speed of retrieval","B) Visual presentation of requirements","C) Auditability and traceability of all changes to requirements","D) Integration with the development team's code repository"],
        "answer": "C) Auditability and traceability of all changes to requirements",
        "explanation": "BABOK® v3 §2.5 emphasizes that regulated environments demand complete change histories and traceability to satisfy audit and compliance requirements.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "A BA is asked to justify the time spent on business analysis planning on a very small project. What is the STRONGEST justification?",
        "options": ["A) It is mandatory per the PMI standard","B) Even on small projects, undefined roles and unclear scope lead to rework","C) The BA will need the plan for performance reviews","D) Clients expect formal documentation regardless of project size"],
        "answer": "B) Even on small projects, undefined roles and unclear scope lead to rework",
        "explanation": "BABOK® v3 §2.1 notes that some level of planning is always beneficial; even light-touch planning prevents common failure modes like unclear accountability and scope creep.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "Which of the following is NOT a typical element of a stakeholder engagement approach?",
        "options": ["A) Communication frequency and channel preferences","B) Conflict management strategies","C) Technical architecture decisions for the solution","D) Level of formality expected in interactions"],
        "answer": "C) Technical architecture decisions for the solution",
        "explanation": "BABOK® v3 §2.4 defines the stakeholder engagement approach as covering communication, collaboration, and conflict strategies—technical architecture belongs to solution design.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "What does 'business analysis performance management' primarily involve?",
        "options": ["A) Managing the performance appraisals of BA team members","B) Monitoring, evaluating, and improving the effectiveness of BA work throughout the initiative","C) Tracking the project schedule and cost","D) Reviewing vendor performance against SLAs"],
        "answer": "B) Monitoring, evaluating, and improving the effectiveness of BA work throughout the initiative",
        "explanation": "BABOK® v3 §2.6 defines BA performance management as continuously measuring and improving BA process outputs—not HR performance management.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "Which scenario BEST justifies using a highly formal, document-heavy BA approach?",
        "options": ["A) A startup building its first mobile app with a 2-person team","B) A government agency replacing a mission-critical system with strict compliance requirements","C) A marketing team redesigning its internal newsletter","D) A data science team running 2-week experiments"],
        "answer": "B) A government agency replacing a mission-critical system with strict compliance requirements",
        "explanation": "BABOK® v3 §2.1 recommends higher formality when regulatory compliance, auditability, and mission-criticality demand rigorous documentation and approval trails.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "A BA plans to use a requirements management tool for the first time on a project. What should the BA do BEFORE configuring the tool?",
        "options": ["A) Start entering all known requirements immediately to save time","B) Define the information architecture: attribute sets, status values, relationship types, and traceability model","C) Ask the development team which tool they prefer","D) Obtain tool vendor training before any configuration"],
        "answer": "B) Define the information architecture: attribute sets, status values, relationship types, and traceability model",
        "explanation": "BABOK® v3 §2.5 recommends defining the information management structure before populating any tool, to ensure consistency and usability.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "Which of the following is the MOST important consideration when selecting BA elicitation techniques during planning?",
        "options": ["A) The BA's personal comfort with each technique","B) The characteristics of the stakeholder population and the type of information needed","C) The techniques used on the previous project","D) The time available for each elicitation session"],
        "answer": "B) The characteristics of the stakeholder population and the type of information needed",
        "explanation": "BABOK® v3 §2.1 ties technique selection to stakeholder characteristics (expertise, availability, geography) and the nature of the information to be gathered.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "How does a BA determine the appropriate level of abstraction for requirements in an early project phase?",
        "options": ["A) Always write requirements at the lowest level of detail possible","B) Match the level of detail to the decisions that need to be made at that point in the lifecycle","C) Ask the project manager for the required template","D) Use the same level of detail as the previous project"],
        "answer": "B) Match the level of detail to the decisions that need to be made at that point in the lifecycle",
        "explanation": "BABOK® v3 §2.1 and §7 note that requirements detail should be progressive and sufficient to support upcoming decisions—over-specification too early wastes effort.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "A BA is planning for an agile project. How should requirements attributes differ from those in a traditional project?",
        "options": ["A) No attributes are needed in agile projects","B) Attributes should focus on priority, acceptance criteria, and story points rather than detailed IDs and versions","C) All attributes remain the same; only the format changes","D) Attributes are assigned by the Scrum Master, not the BA"],
        "answer": "B) Attributes should focus on priority, acceptance criteria, and story points rather than detailed IDs and versions",
        "explanation": "BABOK® v3 §2.5 notes that adaptive approaches emphasize attributes supporting iteration planning (priority, acceptance criteria) over traceability-heavy attributes common in predictive approaches.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "What is the PRIMARY reason to establish a requirements baseline?",
        "options": ["A) To prevent any future changes to requirements","B) To provide a stable reference point from which changes can be identified and managed","C) To signal that elicitation is complete and the BA's work is finished","D) To satisfy a contractual obligation with the client"],
        "answer": "B) To provide a stable reference point from which changes can be identified and managed",
        "explanation": "BABOK® v3 §5.4 defines baselining as creating a controlled snapshot that allows change impact to be assessed against a known state.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "When planning stakeholder collaboration, which factor MOST affects the choice between synchronous and asynchronous communication?",
        "options": ["A) The BA's preference for email over meetings","B) Geographic distribution and time-zone differences among stakeholders","C) The number of requirements to be discussed","D) The project manager's communication style"],
        "answer": "B) Geographic distribution and time-zone differences among stakeholders",
        "explanation": "BABOK® v3 §2.4 highlights that geographic and time-zone constraints often necessitate asynchronous channels when real-time collaboration is impractical.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "A BA is asked to define key performance indicators (KPIs) for monitoring BA work. Which of the following is the MOST outcome-focused KPI?",
        "options": ["A) Number of requirements documents produced","B) Average hours spent per elicitation session","C) Percentage of requirements traced to business objectives","D) Number of stakeholder meetings attended"],
        "answer": "C) Percentage of requirements traced to business objectives",
        "explanation": "BABOK® v3 §2.6 emphasizes outcome-oriented metrics; traceability to business objectives measures whether BA work is contributing to value delivery.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "Which of the following is an example of a BA performance IMPROVEMENT action resulting from a lessons-learned review?",
        "options": ["A) Hiring additional developers to reduce defect rates","B) Introducing early prototype reviews after discovering that late UI feedback caused major rework","C) Extending the project deadline to allow more elicitation time","D) Replacing the project manager after scope creep occurred"],
        "answer": "B) Introducing early prototype reviews after discovering that late UI feedback caused major rework",
        "explanation": "BABOK® v3 §2.6 calls for actionable process improvements based on root-cause analysis of performance issues—process change is more effective than resource addition.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "The BA work plan includes tasks, estimates, and dependencies. Which planning technique is BEST for identifying the CRITICAL PATH of BA activities?",
        "options": ["A) MoSCoW prioritization","B) Precedence diagramming / network analysis","C) Affinity mapping","D) SWOT analysis"],
        "answer": "B) Precedence diagramming / network analysis",
        "explanation": "Network analysis (PDM) identifies task dependencies and the critical path—the longest sequence of dependent activities—essential for BA schedule management.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "Why is it important to align the BA information management approach with the organization's document retention policies?",
        "options": ["A) To minimize the BA team's storage costs","B) To ensure legal, regulatory, and audit compliance across the project lifecycle","C) To make requirements accessible to all internet users","D) To reduce the time BAs spend managing files"],
        "answer": "B) To ensure legal, regulatory, and audit compliance across the project lifecycle",
        "explanation": "BABOK® v3 §2.5 notes that retention policies exist for legal and compliance reasons; BA artifacts must align with these policies to protect the organization.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "Which element of the stakeholder analysis determines HOW a BA communicates requirements information to each stakeholder group?",
        "options": ["A) Stakeholder interest level","B) Stakeholder communication preferences and needs","C) Stakeholder influence on the project","D) Stakeholder geographic location"],
        "answer": "B) Stakeholder communication preferences and needs",
        "explanation": "BABOK® v3 §2.4 states that understanding stakeholders' preferred communication channels, formats, and frequency guides how the BA packages and delivers information.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "A BA realizes that two separate teams are using different definitions for a key business term, causing conflicting requirements. What is the MOST appropriate action?",
        "options": ["A) Pick the most senior team's definition and apply it everywhere","B) Initiate the creation or update of a business glossary to establish a shared vocabulary","C) Document both definitions and let the solution architect decide","D) Avoid using the term and replace it with a technical one"],
        "answer": "B) Initiate the creation or update of a business glossary to establish a shared vocabulary",
        "explanation": "BABOK® v3 §2.5 and the 'Glossary' technique (§10.12) address semantic conflicts by establishing authoritative term definitions shared across stakeholders.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "According to BABOK® v3, which of the following is a characteristic of GOOD business analysis performance measures?",
        "options": ["A) They focus exclusively on BA output volume","B) They are measurable, relevant to BA outcomes, and actionable","C) They are defined by the project manager, not the BA","D) They remain constant regardless of project type or phase"],
        "answer": "B) They are measurable, relevant to BA outcomes, and actionable",
        "explanation": "BABOK® v3 §2.6 calls for performance measures that are quantifiable, tied to BA value delivery, and capable of driving improvement decisions.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "A BA is operating in a hybrid project environment (part waterfall, part agile). What is the BEST approach to requirements traceability?",
        "options": ["A) Apply full waterfall traceability to all requirements","B) Use no traceability—agile doesn't need it","C) Tailor traceability: heavier for stable, regulated requirements; lighter for evolving backlog items","D) Use a separate tool for each methodology"],
        "answer": "C) Tailor traceability: heavier for stable, regulated requirements; lighter for evolving backlog items",
        "explanation": "BABOK® v3 §2.5 advocates tailoring traceability to the nature and stability of requirements, balancing rigor with agility in hybrid environments.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "Which statement BEST reflects the BABOK® v3 view on the relationship between business analysis and project management?",
        "options": ["A) Business analysis is a subset of project management","B) They are separate but complementary disciplines with distinct focuses","C) Project management is a subset of business analysis","D) They are interchangeable roles on small projects"],
        "answer": "B) They are separate but complementary disciplines with distinct focuses",
        "explanation": "BABOK® v3 Introduction distinguishes BA (solution focus: understand need, define solution) from PM (delivery focus: manage timeline, budget, risk) as complementary.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "Which of the following is a risk of NOT documenting the business analysis approach?",
        "options": ["A) The BA will have too much documentation to manage","B) Stakeholders may have conflicting expectations about BA deliverables and timelines","C) The development team will lack technical specifications","D) The project sponsor will approve an insufficient budget"],
        "answer": "B) Stakeholders may have conflicting expectations about BA deliverables and timelines",
        "explanation": "BABOK® v3 §2.1 notes that an undocumented BA approach leaves stakeholders without a shared understanding of what the BA will produce and when.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "A BA is planning activities for a project that involves significant organizational change. Which additional stakeholder category should receive particular attention?",
        "options": ["A) External vendors and suppliers","B) End users whose daily work processes will be directly impacted","C) The project management office","D) Regulatory agencies overseeing the industry"],
        "answer": "B) End users whose daily work processes will be directly impacted",
        "explanation": "BABOK® v3 §2.4 emphasizes that change-impacted end users are high-interest, high-influence stakeholders whose engagement is critical to adoption success.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "What is the purpose of 'performance analysis' in the context of BA performance monitoring?",
        "options": ["A) Evaluating the personal performance of individual BA team members","B) Comparing actual BA task outcomes and timelines against planned benchmarks to identify variances","C) Analyzing the financial performance of the project","D) Reviewing the performance of the solution in production"],
        "answer": "B) Comparing actual BA task outcomes and timelines against planned benchmarks to identify variances",
        "explanation": "BABOK® v3 §2.6 describes performance analysis as assessing variance between planned and actual results and determining causes and corrective actions.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "Which of the following scenarios represents a VIOLATION of good requirements information management practices?",
        "options": ["A) Storing requirements in a versioned repository with access controls","B) Maintaining a single master copy of requirements with a change log","C) Allowing multiple team members to edit requirements simultaneously without a merge process","D) Archiving superseded requirement versions for audit purposes"],
        "answer": "C) Allowing multiple team members to edit requirements simultaneously without a merge process",
        "explanation": "BABOK® v3 §2.5 requires version control and controlled access; concurrent unmanaged edits create inconsistencies and loss of the authoritative requirements version.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "Which BABOK® v3 task specifically addresses how a BA will COMMUNICATE analysis information to stakeholders?",
        "options": ["A) Plan Business Analysis Approach","B) Plan Stakeholder Engagement","C) Plan Business Analysis Information Management","D) Identify Business Analysis Performance Improvements"],
        "answer": "C) Plan Business Analysis Information Management",
        "explanation": "BABOK® v3 §2.5 includes how BA information will be communicated, not just stored—covering format, timing, and audience for each type of BA artifact.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "A BA asks each team member to independently estimate BA task effort, then compares results and discusses differences. Which estimation technique is being used?",
        "options": ["A) Three-point estimation","B) Parametric estimation","C) Wideband Delphi","D) Bottom-up estimation"],
        "answer": "C) Wideband Delphi",
        "explanation": "Wideband Delphi uses anonymous individual estimates followed by structured group discussion to converge on consensus—reducing anchoring bias in effort estimation.",
    },
    {
        "chapter": "Chapter 1 – BA Planning & Monitoring",
        "question": "Which of the following MOST accurately describes 'organizational process assets' as an input to BA planning?",
        "options": ["A) The financial assets available for the project","B) The organization's existing standards, templates, lessons learned, and methodologies","C) The physical resources such as meeting rooms and equipment","D) The software tools procured for requirements management"],
        "answer": "B) The organization's existing standards, templates, lessons learned, and methodologies",
        "explanation": "BABOK® v3 §2.1 defines organizational process assets as accumulated knowledge—templates, guidelines, historical data—that inform and constrain BA planning.",
    },
    # ═══════════════════════════════════════════════════════════
    #  CHAPTER 2 – Elicitation and Collaboration
    # ═══════════════════════════════════════════════════════════

    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "During a facilitated workshop, two SMEs provide contradictory information about the same business rule. What should the BA do FIRST?",
        "options": ["A) Document both versions and let the PM decide","B) Discard the less senior SME's input","C) Acknowledge the discrepancy, probe for root cause, and seek consensus or escalate","D) Stop the workshop and reschedule until stakeholders agree beforehand"],
        "answer": "C) Acknowledge the discrepancy, probe for root cause, and seek consensus or escalate",
        "explanation": "BABOK® v3 §4.4 requires the BA to resolve elicitation conflicts through facilitation and investigation—not unilateral decisions.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA needs to understand undocumented legacy system behavior. Which technique is MOST effective for capturing tacit knowledge?",
        "options": ["A) Survey/Questionnaire","B) Document analysis of legacy code","C) Observation (job shadowing)","D) Interface analysis"],
        "answer": "C) Observation (job shadowing)",
        "explanation": "BABOK® v3 §10.22 recognizes observation as particularly effective at surfacing tacit knowledge that experienced users cannot easily verbalize.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which elicitation technique BEST reveals the emotional and motivational drivers behind stakeholder resistance?",
        "options": ["A) Prototyping","B) Focus group","C) In-depth interview using open-ended questions","D) Requirements workshop with structured templates"],
        "answer": "C) In-depth interview using open-ended questions",
        "explanation": "BABOK® v3 §10.15 highlights open-ended interviews as the best tool for uncovering personal attitudes and emotional context suppressed in group settings.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is the PRIMARY purpose of 'Confirm Elicitation Results' in BABOK® v3?",
        "options": ["A) To obtain formal sign-off from the project sponsor","B) To verify that elicited information accurately represents stakeholder intent","C) To validate that requirements align with the business case","D) To test the prototype against documented requirements"],
        "answer": "B) To verify that elicited information accurately represents stakeholder intent",
        "explanation": "BABOK® v3 §4.4 defines this task as ensuring the BA accurately captured what stakeholders meant—distinct from formal approval.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA uses a prototype to elicit requirements. Which risk should be actively managed?",
        "options": ["A) Stakeholders may request excessive visual polish before business logic is confirmed","B) The dev team will begin building from the prototype prematurely","C) Stakeholders may anchor on the prototype's appearance, neglecting functional requirements","D) The prototype will not load correctly on older hardware"],
        "answer": "C) Stakeholders may anchor on the prototype's appearance, neglecting functional requirements",
        "explanation": "BABOK® v3 §10.26 warns of 'prototype fixation'—stakeholders may focus on UI details and assume the prototype IS the solution.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which BEST distinguishes 'elicitation' from 'requirements analysis'?",
        "options": ["A) Elicitation produces formal requirements docs; analysis produces test cases","B) Elicitation draws information from stakeholders; analysis structures and interprets that information","C) Elicitation is performed by the PM; analysis by the BA","D) Elicitation occurs only at project start; analysis during implementation"],
        "answer": "B) Elicitation draws information from stakeholders; analysis structures and interprets that information",
        "explanation": "BABOK® v3 Chapter 4 treats elicitation as gathering raw information; requirements analysis transforms it into usable specifications.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA sends a questionnaire to 80 stakeholders and gets 15% response. What is the MOST likely root cause and BEST corrective action?",
        "options": ["A) The questionnaire was too short; add more questions","B) Questions were too closed-ended; convert to open-ended","C) The questionnaire lacked context; clarify purpose, shorten it, and follow up personally","D) Stakeholders are resistant; escalate to management"],
        "answer": "C) The questionnaire lacked context; clarify purpose, shorten it, and follow up personally",
        "explanation": "BABOK® v3 §10.34 identifies unclear purpose and excessive length as the main drivers of low survey response rates.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "When planning collaborative games for elicitation, which outcome should the BA prioritize?",
        "options": ["A) Ensuring all participants enjoy the activity equally","B) Generating a ranked prioritization list of requirements","C) Creating an environment that surfaces creative ideas and breaks communication barriers","D) Replacing traditional workshops to reduce meeting time"],
        "answer": "C) Creating an environment that surfaces creative ideas and breaks communication barriers",
        "explanation": "BABOK® v3 §10.6 presents collaborative games as designed to overcome inhibitions and spark creative thinking.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "One vocal participant dominates a focus group, causing others to self-censor. What is the BEST facilitation response?",
        "options": ["A) Remove the dominant participant","B) Use round-robin sharing or anonymous input to give quieter participants equal voice","C) End the session and reschedule with different participants","D) Allow it to continue—dominant voices usually reflect group consensus"],
        "answer": "B) Use round-robin sharing or anonymous input to give quieter participants equal voice",
        "explanation": "BABOK® v3 §10.10 recommends structured participation methods to counter social dominance effects in group elicitation.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which of the following is an OUTPUT of 'Elicit Elicitation Information' (§4.1)?",
        "options": ["A) Approved requirements baseline","B) Elicitation activity plan","C) Elicitation notes (raw, unconfirmed information)","D) Stakeholder requirements specification document"],
        "answer": "C) Elicitation notes (raw, unconfirmed information)",
        "explanation": "BABOK® v3 §4.1 outputs 'elicitation notes'—raw information gathered. Confirmation and formal specification occur in subsequent tasks.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is the PRIMARY goal of benchmarking as an elicitation technique?",
        "options": ["A) Setting quantitative performance targets by comparing against best-in-class references","B) Listing all functional requirements for the system","C) Identifying which stakeholders have the highest influence","D) Documenting the current 'as-is' process in detail"],
        "answer": "A) Setting quantitative performance targets by comparing against best-in-class references",
        "explanation": "BABOK® v3 §10.4 defines benchmarking as comparing performance metrics against internal history or external leaders to identify improvement targets.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which elicitation technique is MOST effective when the business domain is new to the BA and few existing documents exist?",
        "options": ["A) Document analysis","B) Interface analysis","C) Interviews with domain experts combined with observation","D) Surveys sent to a large stakeholder population"],
        "answer": "C) Interviews with domain experts combined with observation",
        "explanation": "BABOK® v3 §10.15 and §10.22 recommend interviews and observation when tacit domain knowledge must be surfaced and few written artifacts exist.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA conducts a requirements workshop. Which preparation activity has the GREATEST impact on workshop success?",
        "options": ["A) Booking the largest available meeting room","B) Defining clear objectives and preparing structured exercises aligned to those objectives","C) Inviting every possible stakeholder to maximize input","D) Distributing a detailed agenda 1 hour before the session"],
        "answer": "B) Defining clear objectives and preparing structured exercises aligned to those objectives",
        "explanation": "BABOK® v3 §10.43 identifies clear objectives and pre-designed activities as the most critical success factors for facilitated workshops.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is the key difference between 'elicitation' and 'requirements discovery'?",
        "options": ["A) They are synonymous—BABOK® uses both terms interchangeably","B) Elicitation is active and stakeholder-facing; discovery also includes mining existing artifacts and systems","C) Discovery is performed by developers; elicitation by BAs","D) Discovery occurs after elicitation to validate findings"],
        "answer": "B) Elicitation is active and stakeholder-facing; discovery also includes mining existing artifacts and systems",
        "explanation": "BABOK® v3 §4.1 notes that requirements come from both stakeholder interactions and existing information sources (documents, systems, data)—together called discovery.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "During an elicitation session, a stakeholder describes a solution rather than a need. What should the BA do?",
        "options": ["A) Document the solution as a requirement","B) Redirect the conversation by probing for the underlying business need the solution is intended to address","C) Involve the architect to evaluate the solution's feasibility","D) Defer the topic until the design phase"],
        "answer": "B) Redirect the conversation by probing for the underlying business need the solution is intended to address",
        "explanation": "BABOK® v3 §4.1 warns against prematurely accepting solution statements as requirements; the BA must uncover the need behind the proposed solution.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which of the following BEST describes a 'brainstorming' session in the context of BABOK® v3 elicitation?",
        "options": ["A) A structured meeting where the BA presents requirements for stakeholder approval","B) A technique for generating a large quantity of ideas rapidly without immediate evaluation","C) A workshop format where requirements are prioritized using MoSCoW","D) A technique for resolving conflicting requirements between two stakeholder groups"],
        "answer": "B) A technique for generating a large quantity of ideas rapidly without immediate evaluation",
        "explanation": "BABOK® v3 §10.5 defines brainstorming as divergent thinking—generating many ideas quickly, deferring judgment to avoid premature filtering.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is the primary reason for conducting a post-elicitation review of notes before presenting them to stakeholders?",
        "options": ["A) To remove any information the BA believes is incorrect","B) To check for completeness, clarity, and internal consistency before confirmation","C) To translate technical language into business language","D) To obtain management approval for the elicitation findings"],
        "answer": "B) To check for completeness, clarity, and internal consistency before confirmation",
        "explanation": "BABOK® v3 §4.3 (Confirm Elicitation Results preparation) requires the BA to review raw notes for gaps and inconsistencies before returning them to stakeholders for validation.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which elicitation technique is MOST appropriate for identifying system interfaces and integration requirements?",
        "options": ["A) Observation","B) Interface analysis","C) Focus groups","D) Mind mapping"],
        "answer": "B) Interface analysis",
        "explanation": "BABOK® v3 §10.14 defines interface analysis as examining how systems and actors interact at boundaries—making it the primary technique for integration and interface requirements.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA is planning elicitation for a culturally diverse global team. Which factor requires the MOST careful planning?",
        "options": ["A) Selecting the right whiteboarding tool","B) Differences in communication norms, language proficiency, and attitudes toward authority and directness","C) Scheduling across time zones","D) Choosing between video and phone for remote sessions"],
        "answer": "B) Differences in communication norms, language proficiency, and attitudes toward authority and directness",
        "explanation": "BABOK® v3 §4.1 highlights cultural factors as critical to elicitation planning—mismatched communication norms can silence key stakeholders and distort input.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is the MAIN advantage of using a 'fishbone diagram' (Ishikawa) during elicitation?",
        "options": ["A) It helps visually map stakeholder influence levels","B) It structures root-cause analysis to reveal contributing factors to a problem","C) It is the best tool for prioritizing requirements","D) It documents data flows between system components"],
        "answer": "B) It structures root-cause analysis to reveal contributing factors to a problem",
        "explanation": "BABOK® v3 §10.8 presents the cause-and-effect diagram as a tool for systematically exploring the causes of a business problem during elicitation.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "When is a 'focus group' MOST appropriate as an elicitation technique?",
        "options": ["A) When the BA needs to understand one expert's deep technical knowledge","B) When gathering attitudes, perceptions, and opinions from a representative sample of a user population","C) When documenting the current system's data model","D) When validating requirements with senior management"],
        "answer": "B) When gathering attitudes, perceptions, and opinions from a representative sample of a user population",
        "explanation": "BABOK® v3 §10.10 identifies focus groups as ideal for understanding shared perspectives, attitudes, and reactions from a homogeneous user segment.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA has completed multiple elicitation sessions but stakeholders keep introducing new requirements. What is the BEST response?",
        "options": ["A) Close elicitation immediately to prevent scope creep","B) Assess whether the new requirements represent genuine unmet needs or scope expansion, then apply governance","C) Accept all new requirements to maintain stakeholder satisfaction","D) Defer all new requirements to a future project phase automatically"],
        "answer": "B) Assess whether the new requirements represent genuine unmet needs or scope expansion, then apply governance",
        "explanation": "BABOK® v3 §4.1 and §2.3 distinguish between emergent valid needs and scope creep; governance (change control) determines how new inputs are handled.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is the purpose of 'mind mapping' in elicitation?",
        "options": ["A) To create a data flow diagram for the solution","B) To visually organize and explore topics, ideas, and their relationships during information gathering","C) To document the system's use cases","D) To model stakeholder communication paths"],
        "answer": "B) To visually organize and explore topics, ideas, and their relationships during information gathering",
        "explanation": "BABOK® v3 §10.18 presents mind mapping as a visual brainstorming technique for capturing complex idea networks and revealing new associations.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which of the following represents an ELICITATION activity (not an analysis activity)?",
        "options": ["A) Modeling requirements in a use case diagram","B) Decomposing a high-level requirement into sub-requirements","C) Conducting a structured interview to gather stakeholder needs","D) Reviewing requirements for testability"],
        "answer": "C) Conducting a structured interview to gather stakeholder needs",
        "explanation": "BABOK® v3 Chapter 4 distinguishes elicitation (drawing information from sources) from analysis (structuring, decomposing, verifying information).",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is the MAIN risk of relying exclusively on document analysis for elicitation?",
        "options": ["A) Documents are always too technical for business stakeholders to understand","B) Existing documents may be outdated, incomplete, or reflect how the process was designed rather than how it actually operates","C) Document analysis takes longer than any other elicitation technique","D) Stakeholders will object to the BA reading internal documents"],
        "answer": "B) Existing documents may be outdated, incomplete, or reflect how the process was designed rather than how it actually operates",
        "explanation": "BABOK® v3 §10.9 notes that documents describe intended or historical states; discrepancies with actual practice must be validated through other techniques.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA notices that a key stakeholder consistently provides vague answers during interviews. Which technique is MOST useful for eliciting more specific information?",
        "options": ["A) Switch to a written survey","B) Use probing questions and scenario-based questioning to ground responses in concrete examples","C) Invite additional stakeholders to the next interview to fill the gaps","D) Document the vague responses and move on"],
        "answer": "B) Use probing questions and scenario-based questioning to ground responses in concrete examples",
        "explanation": "BABOK® v3 §10.15 recommends scenario-based and 'what would you do if…' probing to anchor abstract responses in real-world specifics.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is the PRIMARY difference between a 'structured' and 'unstructured' interview in elicitation?",
        "options": ["A) Structured interviews use a predefined set of questions; unstructured interviews follow the conversation organically","B) Structured interviews are conducted in person; unstructured interviews are virtual","C) Structured interviews only gather quantitative data; unstructured gather qualitative","D) Unstructured interviews are used for executives; structured for end users"],
        "answer": "A) Structured interviews use a predefined set of questions; unstructured interviews follow the conversation organically",
        "explanation": "BABOK® v3 §10.15 distinguishes structured (predetermined questions, easier to compare responses) from unstructured (free-flowing, better for depth and discovery).",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which collaboration technique helps a geographically distributed team agree on a single shared understanding of a complex business process?",
        "options": ["A) Individual interviews with each team member","B) Asynchronous email threads","C) Virtual facilitated workshop with visual process modeling shared in real time","D) Distributing a written process description for individual review"],
        "answer": "C) Virtual facilitated workshop with visual process modeling shared in real time",
        "explanation": "BABOK® v3 §10.43 notes that facilitated workshops with real-time visual artifacts overcome distance barriers and build shared understanding more effectively than asynchronous methods.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What does BABOK® v3 mean by 'elicitation results' needing to be 'confirmed'?",
        "options": ["A) The project sponsor must sign off on all elicitation findings","B) The BA must verify with the source stakeholders that the captured information is accurate and complete","C) The development team must confirm that requirements are technically feasible","D) The QA team must confirm that requirements are testable"],
        "answer": "B) The BA must verify with the source stakeholders that the captured information is accurate and complete",
        "explanation": "BABOK® v3 §4.4 defines confirmation as the BA returning captured information to its sources to validate accuracy, completeness, and intent.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which factor MOST affects the selection of an elicitation technique?",
        "options": ["A) The BA's personal toolkit and experience","B) The nature of the information needed and the characteristics of the stakeholders who hold it","C) The organization's corporate branding guidelines","D) The cost of travel to meet with stakeholders"],
        "answer": "B) The nature of the information needed and the characteristics of the stakeholders who hold it",
        "explanation": "BABOK® v3 §4.1 aligns technique selection with the type of information sought (tacit vs. explicit, attitudinal vs. factual) and stakeholder characteristics.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA is using 'card sorting' as an elicitation technique. What is its PRIMARY purpose?",
        "options": ["A) To prioritize requirements by business value","B) To understand how users mentally categorize concepts, revealing their implicit mental models","C) To generate requirements from user stories","D) To map system entities to database tables"],
        "answer": "B) To understand how users mentally categorize concepts, revealing their implicit mental models",
        "explanation": "Card sorting (related to BABOK® §10.6 collaborative techniques) uncovers users' mental categorization, useful for information architecture and navigation design.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is the role of 'active listening' in elicitation interviews?",
        "options": ["A) Repeating every statement the stakeholder makes to confirm accuracy","B) Fully concentrating on the stakeholder's words, tone, and body language, and probing for deeper meaning","C) Taking verbatim notes on everything said","D) Avoiding interruption at all times during the interview"],
        "answer": "B) Fully concentrating on the stakeholder's words, tone, and body language, and probing for deeper meaning",
        "explanation": "BABOK® v3 §10.15 identifies active listening as a core interviewing skill that includes verbal and non-verbal cues, reflective questioning, and attentive presence.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which scenario represents an example of 'passive observation' as an elicitation technique?",
        "options": ["A) A BA asks a user to walk through a process while explaining each step aloud","B) A BA sits quietly beside a customer service agent, watching their workflow without interaction","C) A BA conducts a structured walkthrough of a use case with the development team","D) A BA reviews video recordings of user testing sessions"],
        "answer": "B) A BA sits quietly beside a customer service agent, watching their workflow without interaction",
        "explanation": "BABOK® v3 §10.22 distinguishes passive observation (silent watching) from active observation (interactive shadowing)—passive avoids influencing natural behavior.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which BABOK® v3 task involves preparing the questions, materials, and logistics for an elicitation activity?",
        "options": ["A) Confirm Elicitation Results","B) Communicate Business Analysis Information","C) Prepare for Elicitation","D) Plan Stakeholder Engagement"],
        "answer": "C) Prepare for Elicitation",
        "explanation": "BABOK® v3 §4.2 (Prepare for Elicitation) covers all pre-session preparation: objectives, participant selection, questions, logistics, and materials.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is the MOST effective way to handle a stakeholder who provides contradictory requirements in different sessions?",
        "options": ["A) Use the most recent version since it supersedes earlier input","B) Escalate the conflict to the project sponsor for resolution","C) Document both versions, bring them back to the stakeholder for clarification, and trace the resolution","D) Average the two versions to reach a compromise requirement"],
        "answer": "C) Document both versions, bring them back to the stakeholder for clarification, and trace the resolution",
        "explanation": "BABOK® v3 §4.4 and §5.3 require the BA to surface, document, and resolve contradictions with the source—ensuring requirements reflect true stakeholder intent.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which BEST describes the concept of 'elicitation scope' in business analysis planning?",
        "options": ["A) The total number of requirements expected from elicitation","B) The boundaries of what information will be sought, from whom, and through what channels","C) The geographic area in which elicitation sessions will take place","D) The duration allocated for all elicitation activities"],
        "answer": "B) The boundaries of what information will be sought, from whom, and through what channels",
        "explanation": "BABOK® v3 §4.2 defines elicitation scope as the planned coverage of stakeholder groups, topic domains, and channels—preventing over- or under-elicitation.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA uses a 'five whys' technique during elicitation. What is the PRIMARY purpose?",
        "options": ["A) To validate that a requirement is stated correctly","B) To iteratively drill down from a symptom to its root cause","C) To prioritize requirements by frequency of stakeholder mention","D) To classify requirements by MoSCoW category"],
        "answer": "B) To iteratively drill down from a symptom to its root cause",
        "explanation": "The Five Whys (BABOK® §10.8 root cause analysis) repeatedly asks 'why' to move from surface symptoms to underlying causes, ensuring the right problem is addressed.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is a key characteristic of 'requirements workshops' that distinguishes them from standard meetings?",
        "options": ["A) They are attended only by executives","B) They are structured, collaborative sessions focused on achieving specific BA outcomes with a skilled facilitator","C) They replace all other elicitation techniques","D) They are always conducted remotely"],
        "answer": "B) They are structured, collaborative sessions focused on achieving specific BA outcomes with a skilled facilitator",
        "explanation": "BABOK® v3 §10.43 defines workshops as purposeful, facilitator-led collaborative events—distinguishing them from unstructured meetings by their design and BA-specific focus.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "When a BA is eliciting requirements from executives, which approach is MOST effective?",
        "options": ["A) Long detailed sessions focused on system features","B) Brief, outcome-focused conversations tied to strategic goals and business value","C) Written surveys to respect their time constraints","D) Group workshops with all organizational levels present"],
        "answer": "B) Brief, outcome-focused conversations tied to strategic goals and business value",
        "explanation": "BABOK® v3 §10.15 and §2.4 note that executives operate at a strategic level; elicitation should focus on goals, outcomes, and constraints rather than operational detail.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is the MAIN benefit of using multiple elicitation techniques on the same topic?",
        "options": ["A) It justifies a larger BA budget","B) It provides triangulation, improving confidence that the picture of requirements is complete and accurate","C) It satisfies more stakeholders by giving them choice","D) It is required by BABOK® for all projects"],
        "answer": "B) It provides triangulation, improving confidence that the picture of requirements is complete and accurate",
        "explanation": "BABOK® v3 §4.1 recommends combining techniques to cross-validate findings—each technique reveals different facets of the same requirement domain.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is the FIRST step a BA should take when preparing for a requirements elicitation session?",
        "options": ["A) Schedule the meeting room and send calendar invites","B) Define the objectives and the specific information to be elicited","C) Create templates for recording requirements","D) Draft a preliminary requirements list based on prior knowledge"],
        "answer": "B) Define the objectives and the specific information to be elicited",
        "explanation": "BABOK® v3 §4.2 identifies defining elicitation objectives as the foundational first step—all other preparation (logistics, questions, materials) follows from clear objectives.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is 'elicitation bias' and why is it a concern for BAs?",
        "options": ["A) The tendency of BAs to document too many requirements","B) Systematic distortion in requirements caused by how questions are framed or how the elicitation is conducted","C) The preference of stakeholders for digital over paper-based elicitation","D) The BA's tendency to favor technical over business requirements"],
        "answer": "B) Systematic distortion in requirements caused by how questions are framed or how the elicitation is conducted",
        "explanation": "BABOK® v3 §4.1 warns that leading questions, anchoring, and other biases can cause elicitation to produce requirements that reflect the BA's assumptions rather than stakeholder needs.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA is eliciting requirements for a system that will replace a manual process. Which technique would BEST reveal the informal 'workarounds' users have developed?",
        "options": ["A) Reviewing the official process documentation","B) Structured interviews with the process designer","C) Ethnographic observation of users performing the actual task","D) Benchmarking against competitor systems"],
        "answer": "C) Ethnographic observation of users performing the actual task",
        "explanation": "BABOK® v3 §10.22 notes that observation—especially in the real work environment—surfaces unarticulated workarounds not captured in official documentation.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "According to BABOK® v3, what is an 'elicitation activity plan'?",
        "options": ["A) A list of all requirements gathered in elicitation sessions","B) A schedule and description of planned elicitation activities, participants, and expected outputs","C) The project plan for the overall business analysis effort","D) A stakeholder map showing who was consulted"],
        "answer": "B) A schedule and description of planned elicitation activities, participants, and expected outputs",
        "explanation": "BABOK® v3 §4.2 describes the elicitation activity plan as detailing which techniques will be used, with whom, when, and what information is expected from each activity.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which of the following is the BEST example of a 'non-functional requirement' discovered through elicitation?",
        "options": ["A) 'The system shall allow users to submit expense reports.'","B) 'The system shall process transactions within 2 seconds under peak load of 10,000 concurrent users.'","C) 'The system shall display a confirmation message after form submission.'","D) 'The system shall integrate with the existing ERP.'"],
        "answer": "B) 'The system shall process transactions within 2 seconds under peak load of 10,000 concurrent users.'",
        "explanation": "BABOK® v3 §6.5 defines non-functional requirements as quality constraints on system behavior (performance, reliability, usability)—the 2-second response time is a clear performance NFR.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What does BABOK® v3 recommend when a stakeholder is unavailable for scheduled elicitation activities?",
        "options": ["A) Proceed without their input and note the gap","B) Identify alternative sources of the required information or reschedule with a suitable proxy","C) Cancel the elicitation activity entirely","D) Ask the project manager to mandate their participation"],
        "answer": "B) Identify alternative sources of the required information or reschedule with a suitable proxy",
        "explanation": "BABOK® v3 §4.2 recommends contingency planning: identifying alternative stakeholders or information sources when primary sources are unavailable.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "When using a 'future state scenario' during elicitation, what is the BA trying to achieve?",
        "options": ["A) Documenting existing business rules in the current system","B) Helping stakeholders articulate needs by imagining and narrating desired future experiences","C) Obtaining sign-off on the technical architecture","D) Validating that the prototype matches the requirements"],
        "answer": "B) Helping stakeholders articulate needs by imagining and narrating desired future experiences",
        "explanation": "Future-state scenarios (related to BABOK® §10.1, Acceptance and Evaluation Criteria) help stakeholders surface implicit expectations by thinking through how they would ideally work.",
    },
    {

     "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which elicitation challenge is MOST commonly associated with subject-matter experts (SMEs)?",
        "options": ["A) SMEs have too little knowledge to provide useful input","B) SMEs may struggle to articulate tacit knowledge because expert skills become automatic and hard to explain","C) SMEs always overstate requirements to justify their team's importance","D) SMEs prefer written surveys over face-to-face interaction"],
        "answer": "B) SMEs may struggle to articulate tacit knowledge because expert skills become automatic and hard to explain",
        "explanation": "BABOK® v3 §4.1 identifies the 'curse of expertise'—SMEs have deeply internalized knowledge that they perform unconsciously, making verbalization difficult without the BA's help.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA is using a 'storyboarding' technique to elicit requirements. What is its MAIN advantage?",
        "options": ["A) It produces legally binding requirements","B) It uses visual narrative sequences to make abstract processes tangible and elicit feedback from stakeholders","C) It eliminates the need for further requirements workshops","D) It is the fastest way to document all requirements"],
        "answer": "B) It uses visual narrative sequences to make abstract processes tangible and elicit feedback from stakeholders",
        "explanation": "Storyboarding (a BABOK® §10.26 prototyping variant) externalizes user journeys visually, making it easier for stakeholders to identify gaps and confirm understanding.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which of the following BEST defines 'collaboration' in the context of BABOK® v3 Chapter 4?",
        "options": ["A) The act of distributing requirements documents to stakeholders for review","B) Working with stakeholders interactively to elicit, analyze, and refine requirements through ongoing dialogue","C) Holding formal project status meetings","D) Assigning requirements ownership to specific business units"],
        "answer": "B) Working with stakeholders interactively to elicit, analyze, and refine requirements through ongoing dialogue",
        "explanation": "BABOK® v3 frames collaboration as an ongoing, iterative engagement—not a one-time information transfer—enabling requirements to be co-created and refined.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA notices that elicitation notes from two different sessions contradict each other on a business rule. What is the CORRECT sequence of next steps?",
        "options": ["A) Apply the most recent session's version and close the issue","B) Document the contradiction, investigate its source, bring it to affected stakeholders for resolution, and record the decision","C) Ask the PM to decide which version to use","D) Remove the business rule from scope until stakeholders resolve the conflict themselves"],
        "answer": "B) Document the contradiction, investigate its source, bring it to affected stakeholders for resolution, and record the decision",
        "explanation": "BABOK® v3 §4.4 and §5.3 require documenting conflicts, tracing their source, facilitating resolution, and recording decisions for auditability.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which statement about 'confirmed elicitation results' is MOST accurate according to BABOK® v3?",
        "options": ["A) They are formally approved and cannot be changed","B) They represent a shared understanding between the BA and the source, but are not yet analyzed requirements","C) They are equivalent to baselined requirements ready for development","D) They only include quantitative data gathered during surveys"],
        "answer": "B) They represent a shared understanding between the BA and the source, but are not yet analyzed requirements",
        "explanation": "BABOK® v3 §4.4 notes that confirmed results are validated information—not yet structured or approved requirements—they still require analysis before becoming actionable.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA wants to elicit the prioritization preferences of 30 geographically dispersed stakeholders efficiently. Which technique is MOST appropriate?",
        "options": ["A) In-person requirements workshop","B) Individual structured interviews with each stakeholder","C) Online structured survey with forced-rank or scoring questions","D) Focus group with a representative sample"],
        "answer": "C) Online structured survey with forced-rank or scoring questions",
        "explanation": "BABOK® v3 §10.34 recommends surveys for efficiently gathering quantitative input from large, dispersed populations where group interaction is impractical.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is the MOST important output of the 'Communicate Business Analysis Information' task (§4.5)?",
        "options": ["A) Requirements specification document signed by the sponsor","B) BA information delivered to stakeholders in a form and at a time that supports their needs","C) A log of all stakeholder communications for audit purposes","D) An updated elicitation activity plan"],
        "answer": "B) BA information delivered to stakeholders in a form and at a time that supports their needs",
        "explanation": "BABOK® v3 §4.5 defines the task's goal as ensuring the right information reaches the right people in the right format at the right time—enabling decision-making and collaboration.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which of the following is an example of an UNSTRUCTURED elicitation source?",
        "options": ["A) A formal system requirements specification document","B) Casual conversations, overheard discussions, and informal stakeholder feedback","C) A structured requirements workshop with pre-defined agenda","D) A survey instrument with Likert-scale questions"],
        "answer": "B) Casual conversations, overheard discussions, and informal stakeholder feedback",
        "explanation": "BABOK® v3 §4.1 acknowledges that valuable requirements information sometimes surfaces informally—BAs must recognize and capture these unstructured inputs.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which elicitation technique MOST effectively surfaces NEGATIVE requirements (things the solution must NOT do)?",
        "options": ["A) Brainstorming positive capabilities","B) Reviewing regulatory and compliance documentation","C) Risk-focused workshops that explore scenarios of failure and unwanted outcomes","D) Benchmarking competitor products"],
        "answer": "C) Risk-focused workshops that explore scenarios of failure and unwanted outcomes",
        "explanation": "Negative requirements (constraints and exclusions) are best surfaced by explicitly exploring failure modes and unacceptable behaviors—a risk-based elicitation approach.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is the PRIMARY purpose of 'Prepare for Elicitation' (BABOK® v3 §4.2)?",
        "options": ["A) To create the final requirements document","B) To plan and prepare everything needed to conduct elicitation activities effectively","C) To obtain management approval to begin requirements gathering","D) To review prior project lessons learned"],
        "answer": "B) To plan and prepare everything needed to conduct elicitation activities effectively",
        "explanation": "BABOK® v3 §4.2 covers objective setting, participant identification, question design, logistics planning, and material preparation—all foundational to effective elicitation.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "When a BA uses 'document analysis' as an elicitation technique, which risk is MOST important to manage?",
        "options": ["A) Copyright violations from reproducing internal documents","B) Accepting documented processes as accurate when actual practices differ","C) Taking too long to read all available documentation","D) Stakeholders objecting to the BA accessing confidential documents"],
        "answer": "B) Accepting documented processes as accurate when actual practices differ",
        "explanation": "BABOK® v3 §10.9 warns that documents may describe intended or legacy processes—validation through other techniques (observation, interviews) is needed to confirm current reality.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA is eliciting requirements for a mobile banking app. Which technique BEST reveals how users actually interact with financial apps in real life?",
        "options": ["A) Survey about desired features","B) Focus group asking about banking preferences","C) Contextual inquiry—observing users in their real environment while using comparable apps","D) Interface analysis of competitor apps"],
        "answer": "C) Contextual inquiry—observing users in their real environment while using comparable apps",
        "explanation": "Contextual inquiry (a form of observation, BABOK® §10.22) combines observation and interview in the user's real context, revealing actual usage patterns and pain points.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which of the following BEST describes 'requirements workshops' as a collaborative elicitation technique?",
        "options": ["A) One-on-one sessions between the BA and the project sponsor","B) Large company-wide information briefings about the project","C) Focused sessions bringing the right stakeholders together to collectively define, elaborate, or validate requirements","D) Training sessions teaching stakeholders how to write requirements"],
        "answer": "C) Focused sessions bringing the right stakeholders together to collectively define, elaborate, or validate requirements",
        "explanation": "BABOK® v3 §10.43 defines requirements workshops as structured collaborative events designed to achieve specific BA outcomes through group engagement.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA conducts an elicitation workshop and captures a list of requirements. Before the next session, what should the BA do with the captured information?",
        "options": ["A) Immediately circulate it to the development team for estimation","B) Review, organize, and distribute the information to participants to confirm accuracy","C) Submit it to the change control board for approval","D) Archive it without review until all elicitation sessions are complete"],
        "answer": "B) Review, organize, and distribute the information to participants to confirm accuracy",
        "explanation": "BABOK® v3 §4.3–4.4 require organizing raw elicitation output and confirming accuracy with sources before proceeding—preventing misunderstandings from compounding.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which of the following describes 'requirements elicitation' as a CONTINUOUS activity rather than a phase?",
        "options": ["A) Elicitation is completed during the initiation phase and never revisited","B) Elicitation occurs throughout the project lifecycle as new information, changes, and refinements emerge","C) Elicitation only resumes after a formal change request is approved","D) Elicitation is limited to the first three iterations of an agile project"],
        "answer": "B) Elicitation occurs throughout the project lifecycle as new information, changes, and refinements emerge",
        "explanation": "BABOK® v3 §4.1 emphasizes that elicitation is iterative and ongoing—new requirements and clarifications emerge at every stage, especially in complex or adaptive environments.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is the MOST significant challenge when using surveys for elicitation?",
        "options": ["A) Surveys are too expensive to administer","B) Response options may constrain answers, limiting discovery of unexpected or novel requirements","C) Surveys cannot be distributed to more than 20 stakeholders","D) Survey results cannot be used as formal requirements input"],
        "answer": "B) Response options may constrain answers, limiting discovery of unexpected or novel requirements",
        "explanation": "BABOK® v3 §10.34 notes that closed survey questions can anchor respondents, preventing them from sharing information outside the predefined categories.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA receives conflicting feedback from users and management about a proposed feature. Which approach BEST resolves this elicitation conflict?",
        "options": ["A) Choose the management position since they have higher authority","B) Facilitate a joint session where both groups articulate the business need behind their positions, and seek a solution that satisfies both underlying needs","C) Average the two positions to find a middle-ground requirement","D) Remove the feature from scope to avoid the conflict"],
        "answer": "B) Facilitate a joint session where both groups articulate the business need behind their positions, and seek a solution that satisfies both underlying needs",
        "explanation": "BABOK® v3 §4.4 and negotiation best practices recommend interest-based resolution: understanding the WHY behind each position often reveals compatible needs.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which technique is MOST appropriate when the BA needs to quickly understand the SCOPE boundaries of a new system?",
        "options": ["A) In-depth interviews with all end users","B) Context diagram or system scope diagram developed collaboratively with stakeholders","C) Reviewing the project budget","D) Document analysis of technical specifications"],
        "answer": "B) Context diagram or system scope diagram developed collaboratively with stakeholders",
        "explanation": "BABOK® v3 §10.27 (Scope Modeling) recommends context diagrams to quickly establish system boundaries and external interactions—ideal for scoping a new initiative.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is the MAIN purpose of 'requirements visualization' techniques such as mockups and wireframes during elicitation?",
        "options": ["A) To finalize the user interface design before development starts","B) To make abstract requirements tangible, enabling stakeholders to identify gaps and validate understanding","C) To replace the need for detailed written requirements","D) To test system performance under load"],
        "answer": "B) To make abstract requirements tangible, enabling stakeholders to identify gaps and validate understanding",
        "explanation": "BABOK® v3 §10.26 positions prototypes and mockups as communication tools that externalize requirements, helping stakeholders react to something concrete rather than abstract descriptions.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which of the following represents the BEST use of 'data mining' as an elicitation technique?",
        "options": ["A) Searching the internet for industry requirements standards","B) Analyzing existing operational data to identify patterns, anomalies, and implicit business rules","C) Mining the project backlog for unresolved requirements","D) Using keyword search to find relevant information in documentation"],
        "answer": "B) Analyzing existing operational data to identify patterns, anomalies, and implicit business rules",
        "explanation": "BABOK® v3 §10.9 (Document Analysis) and data analysis techniques involve examining existing data to surface undocumented rules and behaviors embedded in actual transactions.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA is facilitating a workshop and the group reaches consensus too quickly without exploring alternatives. What should the BA do?",
        "options": ["A) Accept the consensus to avoid disrupting group dynamics","B) Introduce devil's advocate questions or alternative scenarios to stress-test the consensus","C) End the workshop early since objectives are met","D) Document the consensus and proceed to the next topic"],
        "answer": "B) Introduce devil's advocate questions or alternative scenarios to stress-test the consensus",
        "explanation": "BABOK® v3 §10.43 and group dynamics literature warn of premature consensus (groupthink); the facilitator should challenge assumptions to ensure robust, considered requirements.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is the BABOK® v3 term for requirements information that has been gathered but not yet validated or organized?",
        "options": ["A) Confirmed requirements","B) Elicitation notes","C) Business requirements","D) Prioritized backlog items"],
        "answer": "B) Elicitation notes",
        "explanation": "BABOK® v3 §4.1 uses 'elicitation notes' to describe the raw, unprocessed output of elicitation activities—preceding confirmation and analysis.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA is eliciting requirements for a complex regulatory compliance system. Which technique MOST effectively uncovers all mandatory constraints?",
        "options": ["A) Brainstorming sessions with end users","B) Systematic review of all applicable laws, regulations, and industry standards combined with legal expert interviews","C) Observation of current compliance workflows","D) Benchmarking against non-regulated peer organizations"],
        "answer": "B) Systematic review of all applicable laws, regulations, and industry standards combined with legal expert interviews",
        "explanation": "BABOK® v3 §10.9 (Document Analysis) combined with expert interviews (§10.15) is most effective for surfacing mandatory legal and regulatory constraints.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which of the following MOST accurately describes 'stakeholder collaboration' as defined in BABOK® v3 Chapter 4?",
        "options": ["A) Distributing requirements documents to stakeholders for one-way review","B) Active, ongoing partnership with stakeholders to gather, validate, and refine requirements throughout the initiative","C) Formal approval sessions where stakeholders sign off on requirements","D) Communication of project status updates to stakeholder groups"],
        "answer": "B) Active, ongoing partnership with stakeholders to gather, validate, and refine requirements throughout the initiative",
        "explanation": "BABOK® v3 Chapter 4 treats collaboration as a bidirectional, continuous engagement process—not episodic approval events or one-way communication.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "When documenting elicitation results, what level of detail is MOST appropriate at the point of initial capture?",
        "options": ["A) Fully structured, formally worded requirements ready for sign-off","B) Sufficient detail to accurately represent what was said without premature interpretation or formatting","C) High-level summaries only, with detail deferred to later","D) Verbatim transcripts of all conversations"],
        "answer": "B) Sufficient detail to accurately represent what was said without premature interpretation or formatting",
        "explanation": "BABOK® v3 §4.3 recommends capturing enough detail to preserve meaning without over-processing raw input—interpretation and structuring occur in the analysis phase.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which technique is MOST useful when the BA needs to elicit requirements from a stakeholder who has difficulty articulating abstract needs?",
        "options": ["A) Sending a detailed written questionnaire","B) Using concrete scenarios, examples, or 'day-in-the-life' stories to ground the conversation","C) Asking the stakeholder to review an existing system's documentation","D) Conducting a structured requirements workshop with other stakeholders present"],
        "answer": "B) Using concrete scenarios, examples, or 'day-in-the-life' stories to ground the conversation",
        "explanation": "BABOK® v3 §10.15 recommends scenario-based and example-driven questioning to help stakeholders articulate needs they cannot express abstractly.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is a 'pilot elicitation session' and when is it MOST valuable?",
        "options": ["A) A session conducted with the project sponsor before other stakeholders are engaged","B) A test run of a planned elicitation technique with a small group to identify issues before full-scale deployment","C) The first iteration of an agile sprint focused entirely on elicitation","D) A session designed to pilot the new solution with real users"],
        "answer": "B) A test run of a planned elicitation technique with a small group to identify issues before full-scale deployment",
        "explanation": "A pilot session (related to BABOK® §4.2 preparation) validates that the planned technique, questions, and logistics will work as intended before committing to large-scale elicitation.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA realizes mid-project that a significant stakeholder group was never engaged during elicitation. What is the MOST appropriate action?",
        "options": ["A) Continue without engaging them since elicitation is already complete","B) Conduct targeted elicitation sessions with that group, assess impact on existing requirements, and update accordingly","C) Add their names to the stakeholder list for documentation purposes","D) Ask the project manager to inform them of the requirements baseline"],
        "answer": "B) Conduct targeted elicitation sessions with that group, assess impact on existing requirements, and update accordingly",
        "explanation": "BABOK® v3 §4.1 and §2.4 treat elicitation as continuous; missing stakeholders must be engaged, and their input assessed for impact on existing requirements.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is the relationship between 'elicitation' and 'validation' in BABOK® v3?",
        "options": ["A) Elicitation and validation are the same activity","B) Elicitation gathers information; validation checks that the solution or requirements will satisfy the business need","C) Validation occurs before elicitation to confirm the business case","D) They are in separate BABOK® knowledge areas with no overlap"],
        "answer": "B) Elicitation gathers information; validation checks that the solution or requirements will satisfy the business need",
        "explanation": "BABOK® v3 distinguishes elicitation (Chapter 4—gathering information) from validation (Chapter 7—confirming requirements will deliver value), though both are ongoing.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA is planning to use 'nominal group technique' in a workshop. What is its PRIMARY advantage over standard brainstorming?",
        "options": ["A) It produces a larger volume of ideas","B) It reduces the influence of dominant personalities by having participants generate ideas independently before group discussion","C) It eliminates the need for a facilitator","D) It is faster than other brainstorming methods"],
        "answer": "B) It reduces the influence of dominant personalities by having participants generate ideas independently before group discussion",
        "explanation": "Nominal group technique structures idea generation to give every participant equal voice before social dynamics influence the discussion—addressing a key group elicitation risk.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which BABOK® v3 task covers the selection and scheduling of specific elicitation techniques for an upcoming initiative?",
        "options": ["A) Confirm Elicitation Results","B) Plan Business Analysis Approach","C) Prepare for Elicitation","D) Communicate Business Analysis Information"],
        "answer": "C) Prepare for Elicitation",
        "explanation": "BABOK® v3 §4.2 (Prepare for Elicitation) explicitly covers technique selection, participant identification, objective setting, and scheduling for each planned elicitation activity.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA is working in a regulated healthcare environment. Which elicitation challenge is MOST unique to this context?",
        "options": ["A) Stakeholders lack computer skills","B) Privacy regulations (e.g., HIPAA) restrict which patient data can be discussed or referenced in elicitation sessions","C) Healthcare workflows are too simple to require detailed elicitation","D) Clinicians prefer written requirements over workshops"],
        "answer": "B) Privacy regulations (e.g., HIPAA) restrict which patient data can be discussed or referenced in elicitation sessions",
        "explanation": "BABOK® v3 §4.1 notes that regulatory constraints shape elicitation boundaries; healthcare privacy rules require anonymization and special handling even during internal requirements sessions.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "When a BA uses 'reverse engineering' as an elicitation technique, what is the PRIMARY goal?",
        "options": ["A) To redesign the solution architecture","B) To reconstruct undocumented requirements by analyzing an existing system's behavior and outputs","C) To eliminate legacy requirements that no longer apply","D) To convert informal requirements into formal specifications"],
        "answer": "B) To reconstruct undocumented requirements by analyzing an existing system's behavior and outputs",
        "explanation": "BABOK® v3 §10.9 includes reverse engineering of existing systems under document/system analysis—used to recover requirements lost over time.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is the BEST way to handle a stakeholder who consistently provides requirements outside the agreed scope?",
        "options": ["A) Document the out-of-scope requirements but ignore them","B) Acknowledge the input, log it, and route it through the change control process for scope assessment","C) Ask the stakeholder to stop attending elicitation sessions","D) Add the requirements to scope immediately to maintain the relationship"],
        "answer": "B) Acknowledge the input, log it, and route it through the change control process for scope assessment",
        "explanation": "BABOK® v3 §4.1 and §2.3 call for capturing all stakeholder input with respect, then applying governance to determine whether out-of-scope items merit a change request.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which statement about 'assumed requirements' is MOST accurate in the BABOK® v3 context?",
        "options": ["A) Assumed requirements are valid as long as a senior BA approves them","B) Assumed requirements are risky because they may not reflect actual stakeholder needs and should be validated","C) Assumed requirements are always documented and baselined at project start","D) Assumed requirements are used only in agile projects"],
        "answer": "B) Assumed requirements are risky because they may not reflect actual stakeholder needs and should be validated",
        "explanation": "BABOK® v3 §4.1 warns that assumptions substitute for elicited knowledge—they carry risk and must be explicitly identified and validated through stakeholder engagement.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is the MOST effective way to build rapport with a new stakeholder group at the beginning of an elicitation engagement?",
        "options": ["A) Send a detailed requirements survey before the first meeting","B) Explain the project benefits, clarify the BA's role, and demonstrate genuine interest in their perspectives and challenges","C) Present the preliminary requirements list to get feedback immediately","D) Request their manager's approval before engaging them"],
        "answer": "B) Explain the project benefits, clarify the BA's role, and demonstrate genuine interest in their perspectives and challenges",
        "explanation": "BABOK® v3 §4.1 and collaboration best practices emphasize trust-building through transparency about purpose, role clarity, and genuine listening—foundations of productive elicitation relationships.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is meant by 'requirements triage' in the context of elicitation?",
        "options": ["A) Sorting requirements alphabetically for documentation","B) Quickly assessing newly elicited items to determine their validity, priority, and scope status","C) Removing duplicate requirements from the backlog","D) Assigning requirements to development team members for implementation"],
        "answer": "B) Quickly assessing newly elicited items to determine their validity, priority, and scope status",
        "explanation": "Requirements triage applies quick assessment criteria to incoming elicited items to determine immediate next steps—analogous to medical triage for urgency and relevance.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which of the following BEST describes the concept of 'elicitation completeness'?",
        "options": ["A) All requirements have been formally approved by stakeholders","B) There is sufficient confidence that all significant requirements have been identified for the current decision horizon","C) Every possible requirement has been documented in exhaustive detail","D) The requirements baseline has been signed off by all stakeholders"],
        "answer": "B) There is sufficient confidence that all significant requirements have been identified for the current decision horizon",
        "explanation": "BABOK® v3 §4.1 and §5.3 note that completeness is contextual—'good enough' for the current phase, not an unachievable 100%. Over-elicitation has diminishing returns.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "Which type of question is MOST effective for opening an elicitation interview?",
        "options": ["A) Closed questions to quickly establish yes/no facts","B) Leading questions to confirm the BA's assumptions","C) Open-ended, broad questions that allow the stakeholder to set the agenda and surface their most pressing concerns","D) Hypothetical questions that explore future scenarios immediately"],
        "answer": "C) Open-ended, broad questions that allow the stakeholder to set the agenda and surface their most pressing concerns",
        "explanation": "BABOK® v3 §10.15 recommends starting with open questions to discover what matters most to stakeholders—narrowing to specific topics only after the broad landscape is established.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "A BA is eliciting requirements for a data warehouse project. Which technique is MOST effective for discovering data quality and lineage requirements?",
        "options": ["A) User story mapping","B) Data profiling and analysis of existing source systems combined with SME interviews","C) Entity-relationship diagramming","D) Prototyping dashboard mockups"],
        "answer": "B) Data profiling and analysis of existing source systems combined with SME interviews",
        "explanation": "BABOK® v3 §10.9 (Document/Data Analysis) applied to source system data reveals quality issues and lineage rules; SME interviews provide business context for interpreting findings.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is the key risk of conducting elicitation ONLY through formal, scheduled sessions?",
        "options": ["A) Too much information is gathered, making analysis difficult","B) Informal, emergent requirements that arise in daily work are missed because stakeholders only share what they remember at session time","C) Formal sessions take too long and delay the project schedule","D) Formal sessions make stakeholders uncomfortable and reduce cooperation"],
        "answer": "B) Informal, emergent requirements that arise in daily work are missed because stakeholders only share what they remember at session time",
        "explanation": "BABOK® v3 §4.1 recognizes that relying solely on scheduled sessions leaves a gap for in-context, situational insights that only surface during actual work performance.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "According to BABOK® v3, which of the following is a DIRECT input to the 'Conduct Elicitation' task (§4.3)?",
        "options": ["A) Validated requirements","B) Elicitation activity plan and prepared materials from the 'Prepare for Elicitation' task","C) Approved project charter","D) Stakeholder satisfaction survey results"],
        "answer": "B) Elicitation activity plan and prepared materials from the 'Prepare for Elicitation' task",
        "explanation": "BABOK® v3 §4.3 specifies that the outputs of §4.2 (Prepare for Elicitation)—the activity plan and prepared materials—are the direct inputs to conducting each elicitation event.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "What is the MAIN reason a BA should avoid using jargon from their own technical background during elicitation sessions?",
        "options": ["A) Regulatory requirements prohibit jargon in BA sessions","B) Unfamiliar terminology can cause stakeholders to misunderstand questions and provide inaccurate or misleading responses","C) Stakeholders may report the BA for using inappropriate language","D) Jargon increases the duration of sessions unnecessarily"],
        "answer": "B) Unfamiliar terminology can cause stakeholders to misunderstand questions and provide inaccurate or misleading responses",
        "explanation": "BABOK® v3 §4.1 emphasizes clear communication aligned to the stakeholder's vocabulary; BA or technical jargon creates barriers that distort elicitation quality.",
    },
    {
        "chapter": "Chapter 2 – Elicitation & Collaboration",
        "question": "When a BA reviews and confirms elicitation results with stakeholders, which outcome indicates the task is COMPLETE?",
        "options": ["A) All stakeholders have signed a formal requirements document","B) Stakeholders agree that the captured information accurately and completely represents their input","C) The project manager approves the elicitation summary","D) The development team confirms that the requirements are technically feasible"],
        "answer": "B) Stakeholders agree that the captured information accurately and completely represents their input",
        "explanation": "BABOK® v3 §4.4 defines completion of 'Confirm Elicitation Results' as achieving shared agreement between the BA and information sources on accuracy and completeness.",
    },
]

# ──────────────────────────────────────────────────────────────
#  SESSION STATE
# ──────────────────────────────────────────────────────────────
def init_state():
    defaults = {
        "started": False, "questions": [], "current": 0,
        "answers": {}, "submitted": {}, "finished": False,
        "num_questions": 20, "start_time": None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ──────────────────────────────────────────────────────────────
#  HEADER
# ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="exam-header">
    <h1>📋 CBAP® Exam Simulator</h1>
    <p>Chapters 1 & 2 · BABOK® v3 · Difficulty: Advanced · 150 Questions</p>
</div>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────
#  START SCREEN
# ──────────────────────────────────────────────────────────────
if not st.session_state.started:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style='background:rgba(255,255,255,0.05);border:1px solid rgba(201,168,76,0.3);
                    border-radius:12px;padding:1.8rem;margin-bottom:1.5rem;
                    font-family:"Source Sans 3",sans-serif;color:#c8d4e8;line-height:1.7'>
            <b style='color:#c9a84c;font-size:1.05rem'>📌 Exam Rules</b><br><br>
            • 150 hard-difficulty questions from Chapter 1 & 2 of BABOK® v3<br>
            • One attempt per question — confirm before moving on<br>
            • Immediate explanations after each answer<br>
            • Passing score: <b style='color:#f0d080'>70%</b> (CBAP benchmark)
        </div>
        """, unsafe_allow_html=True)

        n = st.slider("Number of questions", min_value=5,
                      max_value=len(ALL_QUESTIONS),
                      value=min(20, len(ALL_QUESTIONS)), step=1)
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


# ──────────────────────────────────────────────────────────────
#  RESULTS SCREEN
# ──────────────────────────────────────────────────────────────
elif st.session_state.finished:
    qs = st.session_state.questions
    correct = sum(1 for i, q in enumerate(qs)
                  if st.session_state.answers.get(i) == q["answer"])
    total = len(qs)
    pct = round(correct / total * 100)
    elapsed = int(time.time() - (st.session_state.start_time or time.time()))
    mins, secs = divmod(elapsed, 60)
    passed = pct >= 70

    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        vclass = "passed" if passed else "failed"
        vtext  = "✅ PASSED" if passed else "❌ NOT PASSED"
        st.markdown(f"""
        <div class="score-card">
            <div class="score-big">{pct}%</div>
            <div class="score-label">{correct} correct out of {total} questions</div>
            <div class="score-verdict {vclass}">{vtext}</div>
        </div>""", unsafe_allow_html=True)

        st.markdown(f"""
        <div class="stats-row">
            <div class="stat-box"><div class="stat-num">{correct}</div><div class="stat-lbl">Correct</div></div>
            <div class="stat-box"><div class="stat-num">{total-correct}</div><div class="stat-lbl">Incorrect</div></div>
            <div class="stat-box"><div class="stat-num">{mins}:{secs:02d}</div><div class="stat-lbl">Time</div></div>
            <div class="stat-box"><div class="stat-num">{pct}%</div><div class="stat-lbl">Score</div></div>
        </div>""", unsafe_allow_html=True)

        ch1_q = [(i,q) for i,q in enumerate(qs) if "Chapter 1" in q["chapter"]]
        ch2_q = [(i,q) for i,q in enumerate(qs) if "Chapter 2" in q["chapter"]]
        ch1_c = sum(1 for i,q in ch1_q if st.session_state.answers.get(i)==q["answer"])
        ch2_c = sum(1 for i,q in ch2_q if st.session_state.answers.get(i)==q["answer"])

        if ch1_q or ch2_q:
            st.markdown("<br>", unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                r = f"{ch1_c}/{len(ch1_q)}" if ch1_q else "N/A"
                st.markdown(f'<div class="stat-box" style="width:100%"><div class="stat-num">{r}</div><div class="stat-lbl">Chapter 1</div></div>', unsafe_allow_html=True)
            with c2:
                r = f"{ch2_c}/{len(ch2_q)}" if ch2_q else "N/A"
                st.markdown(f'<div class="stat-box" style="width:100%"><div class="stat-num">{r}</div><div class="stat-lbl">Chapter 2</div></div>', unsafe_allow_html=True)

        wrong = [(i,q) for i,q in enumerate(qs)
                 if st.session_state.answers.get(i) != q["answer"]]
        if wrong:
            st.markdown("<br>", unsafe_allow_html=True)
            with st.expander(f"📖  Review {len(wrong)} incorrect answer(s)"):
                for _, (i, q) in enumerate(wrong):
                    user_ans = st.session_state.answers.get(i, "Not answered")
                    st.markdown(f"""
                    <div style='margin-bottom:1.2rem;padding:1rem;background:rgba(155,35,53,0.12);
                                border-radius:8px;border-left:3px solid #9b2335;
                                font-family:"Source Sans 3",sans-serif'>
                        <div style='color:#c9a84c;font-size:.8rem;margin-bottom:.5rem'>Q{i+1} · {q["chapter"]}</div>
                        <div style='color:#f4f1eb;margin-bottom:.7rem'>{q["question"]}</div>
                        <div style='color:#f4a0a0'>❌ Your answer: {user_ans}</div>
                        <div style='color:#6fe4a4'>✅ Correct: {q["answer"]}</div>
                        <div style='color:#c8d4e8;margin-top:.5rem;font-size:.9rem'>💡 {q["explanation"]}</div>
                    </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔄  New Exam", use_container_width=True):
            for k in ["started","questions","current","answers","submitted","finished","start_time"]:
                st.session_state.pop(k, None)
            st.rerun()

# ──────────────────────────────────────────────────────────────
#  EXAM SCREEN
# ──────────────────────────────────────────────────────────────
else:
    qs    = st.session_state.questions
    total = len(qs)
    idx   = st.session_state.current
    q     = qs[idx]

    progress_pct = int(idx / total * 100)
    st.markdown(f"""
    <div style='font-family:"Source Sans 3",sans-serif;color:#8090aa;
                font-size:.85rem;display:flex;justify-content:space-between'>
        <span>Question {idx+1} of {total}</span>
        <span>{progress_pct}% complete</span>
    </div>
    <div class="progress-container">
        <div class="progress-bar" style="width:{progress_pct}%"></div>
    </div>""", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="q-card">
        <div class="q-number">Question {idx+1}</div>
        <div class="q-chapter">{q["chapter"]}</div>
        <p class="q-text">{q["question"]}</p>
    </div>""", unsafe_allow_html=True)

    already_submitted = idx in st.session_state.submitted

    if not already_submitted:
        chosen = st.radio("Select your answer:", q["options"],
                          key=f"radio_{idx}", index=None)
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
        user_ans    = st.session_state.answers.get(idx)
        correct_ans = q["answer"]
        is_correct  = user_ans == correct_ans

        for opt in q["options"]:
            if opt == correct_ans:
                color, icon, bg = "#1e7c4a", "✅", "rgba(30,124,74,0.15)"
            elif opt == user_ans and not is_correct:
                color, icon, bg = "#9b2335", "❌", "rgba(155,35,53,0.15)"
            else:
                color, icon, bg = "#8090aa", "○", "transparent"
            st.markdown(f"""
            <div style='padding:.6rem 1rem;margin:.3rem 0;border-radius:8px;
                        background:{bg};border:1px solid {color}33;
                        font-family:"Source Sans 3",sans-serif;color:{color}'>
                {icon} {opt}
            </div>""", unsafe_allow_html=True)

        if is_correct:
            st.markdown(f"""
            <div class="feedback-correct">
                🎯 <b>Correct!</b>
                <div class="feedback-explanation">💡 {q["explanation"]}</div>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="feedback-wrong">
                ❌ <b>Incorrect.</b> Correct answer: <b>{correct_ans}</b>
                <div class="feedback-explanation">💡 {q["explanation"]}</div>
            </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        is_last = idx == total - 1
        col_nav1, col_nav2 = st.columns(2)
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

