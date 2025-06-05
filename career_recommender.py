import streamlit as st

st.set_page_config(page_title="Smart Career Recommender")
st.title("Smart Career Path Recommender")

#//Question
name = st.text_input("Your Name")
interest = st.selectbox("What are you interested in?", ["Software Development","Data Science", "Cybersecurity", 'UI/UX Design',"Business/Management"])
skill_level = st.selectbox("How would you rate your current skill level?", ["Beginner", "Intermediate", "Advanced"])
qualification = st.selectbox("What is your highest qualification?", ["10th", "12th", "Diploma", "Graduate", "Post-Graduate"])
submit = st.button("Get Career Recommendations")

#//Recommendation Logic
if submit:
    st.subheader(f"Hi {name}! Based on your input, here are some recommendations:")

    if interest == "Software Development":
        st.markdown("""
        - **Recommended Role**: Junior Software Developer
        - Skills Needed: Python, Git, OOPs, HTML/CSS/JS)
        - Learn: [freeCodeCamp](https://www.freecodecamp.org/), [W3Schools](https://www.w3schools.com/) 
        """)

    elif interest == "Data Science":
        st.markdown("""
        - **Recommended Role**: Data Analyst
        - Skills Needed: Python, Pandas, NumPy, Matplotlib)
        - Learn: [Kaggle](https://www.kaggle.com/learn), [DataCamp](https://www.datacamp.com/) 
        """)

    elif interest == "Cybersecurity":
        st.markdown("""
        - **Recommended Role**: Security Analyst
        - Skills Needed: Python, Networking, Linux, OWASP Top 10)
        - Learn: [TryHackMe](https://www.tryhackme.orgs/), [Hack The Box](https://www.hackthebox.com/) 
        """)

    elif interest == "UI/UX Design":
        st.markdown("""
        - **Recommended Role**: UI/UX Designer
        - Skills Needed: Figma, Adobe XD, HTML/CSS Basics)
        - Learn: [freeCodeCamp](https://www.freecodecamp.orgs/), [W3Schools](https://www.w3schools.com/) 
        """)
    
    elif interest == "Business/Management":
        st.markdown("""
        - **Recommended Role**: Business Analyst
        - Skills Needed: Excel, SQL, PowerBI, Communication)
        - Learn: [edX](https://www.edx.org/), [LinkedIn Learning](https://www.linkedin.com/learning/) 
        """)
        