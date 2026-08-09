import streamlit as st
from core.predictor import predict_and_recommend

st.set_page_config(page_title="Learning Engagement Analyzer", layout="centered")

st.title("🎓 Student Learning Engagement Analyzer")
st.write("This tool helps identify early learning risks and provides personalized study recommendations.")

with st.expander("ℹ️ How do we measure engagement?"):
    st.write(
    """
    Engagement is measured as the number of meaningful learning actions, such as:
    - Watching videos
    - Opening study materials
    - Navigating course pages
    - Participating in activities

    Time spent is not required only interaction count.
    """
    )

st.subheader("Student Engagement Information")
st.info("📌 Interaction means actions like watching videos, opening study materials, clicking course pages, or participating in course activities.")

# user friendly input

engagement_level = st.slider(
    "Overall course interaction (number of learning actions)",
    min_value=0,
    max_value=30000,
    value=750,
    help=(
        "Total count of learning actions such as opening materials, watching videos, or navigating course pages during the course."
    )
)

early_interaction = st.slider(
    "Early course interaction (number of actions in the first few days)",
    min_value=0,
    max_value=5000,
    value=80,
    help=(
        "Number of learning actions performed during the first few days of the course. Strong early engagement often predicts success."
    )
)
early_active_days = st.slider(
    "Days engaged during early course period",
    min_value=0,
    max_value=15,
    value=5,
    help=(
        "Number of distinct days the student was active early in the course, even if activity was brief."
    )
)


first_activity_day = st.number_input(
    "Days after course start when the student first engaged",
    min_value=-25,
    max_value=60,
    value=-5,
    help=(
        "Negative values mean the student engaged before the course officially started. Positive values indicate delayed engagement."
    )
)

pre_course_engaged = st.radio(
    "Did the student interact with the course before the official start?",
    options=[0,1],
    format_func=lambda x : "Yes" if x==1 else "No",
    help="Includes any interaction before the course start date."
)

student_input = {
        "total_click" : engagement_level,
        "early_click" : early_interaction,
        "early_active_days" : early_active_days,
        "first_activity_day" : first_activity_day,
        "pre_course_engaged" : pre_course_engaged
    }

if st.button("Analyze Engagement"):
    result = predict_and_recommend(student_input)

    st.markdown(f"## ⚠️ Engagement Risk: **{result['risk_level']}**")

    st.write(f"**Risk Probability:** `{result['risk_probability']}`")

    st.subheader("🔍 Key Observations")
    if result["observations"]:
        for obs in result["observations"]:
            st.write(f"- {obs}")
    else :
        st.write("No concerning behavior detected so far.")

    st.subheader("✅ Recommended Next Steps")
    for action in result["recommendations"]:
        st.write(f"- {action}")

    with st.expander("🧠 Why was this risk predicted?"):
        for rule in result["model_explanation"]:
            st.write(f"- {rule}")
