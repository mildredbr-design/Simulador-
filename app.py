import streamlit as st

st.set_page_config(page_title="BABOK Chapter 1 Quiz", page_icon="📘")

st.title("BABOK Guide v3 - Chapter 1 Practice Quiz")
st.write("Answer the following questions related to Chapter 1 (Introduction and BACCM).")

questions = [
    {
        "question": "According to BABOK, what is the definition of Business Analysis?",
        "options": [
            "The process of developing software applications",
            "The practice of enabling change in an enterprise by defining needs and recommending solutions that deliver value",
            "The management of IT infrastructure",
            "The documentation of technical specifications"
        ],
        "answer": 1,
        "explanation": "BABOK defines Business Analysis as the practice of enabling change by defining needs and recommending solutions that deliver value."
    },
    {
        "question": "Which of the following is NOT one of the six core concepts of the Business Analysis Core Concept Model (BACCM)?",
        "options": [
            "Change",
            "Stakeholder",
            "Value",
            "Budget"
        ],
        "answer": 3,
        "explanation": "The six BACCM concepts are: Change, Need, Solution, Stakeholder, Value, and Context."
    },
    {
        "question": "In the BACCM, what does the concept 'Need' represent?",
        "options": [
            "A problem or opportunity to be addressed",
            "A software system implementation",
            "A financial investment",
            "A project schedule"
        ],
        "answer": 0,
        "explanation": "Need represents a problem or opportunity that must be addressed."
    },
    {
        "question": "Which concept in BACCM refers to the environment in which change occurs?",
        "options": [
            "Solution",
            "Context",
            "Value",
            "Need"
        ],
        "answer": 1,
        "explanation": "Context refers to the circumstances that influence, are influenced by, and provide understanding of the change."
    },
    {
        "question": "What does the 'Solution' concept represent in BACCM?",
        "options": [
            "A set of changes to processes, systems, or organizations that address a need",
            "A project budget",
            "A marketing strategy",
            "A stakeholder meeting"
        ],
        "answer": 0,
        "explanation": "Solution represents the specific way a need is satisfied by implementing changes."
    }
]

user_answers = []

for i, q in enumerate(questions):
    st.subheader(f"Question {i+1}")
    answer = st.radio(q["question"], q["options"], key=i)
    user_answers.append(q["options"].index(answer))

if st.button("Submit Quiz"):

    score = 0

    st.subheader("Results")

    for i, q in enumerate(questions):
        if user_answers[i] == q["answer"]:
            score += 1
            st.success(f"Question {i+1}: Correct")
        else:
            st.error(f"Question {i+1}: Incorrect")

        st.write(f"Explanation: {q['explanation']}")
        st.write("---")

    st.subheader(f"Final Score: {score} / {len(questions)}")

    if score == 5:
        st.success("Excellent! You mastered Chapter 1.")
    elif score >= 3:
        st.info("Good job! You're on the right track.")
    else:
        st.warning("Keep reviewing Chapter 1 and try again.")
