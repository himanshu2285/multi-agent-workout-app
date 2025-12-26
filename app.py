import streamlit as st

st.title("Multi-Agent Workout App")

@st.fragment()
def personal_data_form():
    with st.form("personal_data"):
        st.header("Personal Data")
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=1, max_value=120, step=1)
        weight = st.number_input("Weight (kg)", min_value=0, max_value=300, step=1)
        height = st.number_input("Height (cm)", min_value=0, max_value=250, step=1)
        gender = st.radio("Gender", ["Male", "Female", "Other"]), 
        fitness_level = st.selectbox("Fitness Level", ["Beginner", "Intermediate", "Advanced"])
        activities = ("Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extra Active")
        activity_level = st.selectbox("Activity Level", activities)
        goals = st.multiselect("Fitness Goals", ["Weight Loss", "Muscle Gain", "Endurance", "Flexibility"])
        
        submitted = st.form_submit_button("Save")
        
        if submitted:
            st.success("Personal data submitted!")
            return {
                "name": name,
                "age": age,
                "weight": weight,
                "height": height,
                "gender": gender,
                "fitness_level": fitness_level,
                "activity_level": activity_level,
                "goals": goals
            }
        else:
            st.warning("Please fill out all the data!")
            
            
def forms():
    personal_data_form()
    
if __name__ == "__main__":
    forms()