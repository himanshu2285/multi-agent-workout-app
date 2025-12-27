import streamlit as st
from profiles import get_notes, get_profile, create_profile
from form_submit import update_personal_info, add_note, delete_note


st.title("Multi-Agent Workout App")

@st.fragment()
def personal_data_form():
    with st.form("personal_data"):
        st.header("Personal Data")
        
        profile = st.session_state.profile
        
        name = st.text_input("Name", value=profile["general"]["name"])
        age = st.number_input("Age", min_value=1, max_value=120, step=1, value=profile["general"]["age"])
        weight = st.number_input("Weight (kg)", min_value=0, max_value=300, step=1, value=profile["general"]["weight"])
        height = st.number_input("Height (cm)", min_value=0, max_value=250, step=1, value=profile["general"]["height"])
        gender = st.radio("Gender", ["Male", "Female", "Other"], index=["Male", "Female", "Other"].index(profile["general"]["gender"]))
        fitness_level = st.selectbox("Fitness Level", ["Beginner", "Intermediate", "Advanced"], index=["Beginner", "Intermediate", "Advanced"].index(profile["general"]["fitness_level"]))
        activities = ("Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extra Active")
        activity_level = st.selectbox("Activity Level", activities, index=activities.index(profile["general"].get("activity_level", "Sedentary")))
        goals = st.multiselect("Fitness Goals", ["Weight Loss", "Muscle Gain", "Endurance", "Flexibility"], default=profile["general"].get("goals", []))
        
        personal_data_submit = st.form_submit_button("Save")

        if personal_data_submit:
            if all(name, age, weight, height, gender, fitness_level, activity_level, goals):
                with st.spinner():
                    #save the data
                    update_personal_info(
                        profile,
                        "general", 
                        name=name,
                        age=age, 
                        weight=weight, 
                        height=height, 
                        gender=gender,
                        fitness_level=fitness_level,
                        activity_level=activity_level
                        )
                    st.success("Personal data submitted!")

            # return {
            #     "name": name,
            #     "age": age,
            #     "weight": weight,
            #     "height": height,
            #     "gender": gender,
            #     "fitness_level": fitness_level,
            #     "activity_level": activity_level,
            #     "goals": goals
            # }
        else:
            st.warning("Please fill out all the data!")
            
            
def forms():
    if "profile" not in st.session_state:
        profile_id = 1
        profile = get_profile(profile_id)
        if not profile:
            profile_id, profile = create_profile(profile_id)

        st.session_state.profile = profile
        st.session_state.profile_id = profile_id
        
    if "notes" not in st.session_state:
        st.session_state.notes = get_notes(st.session_state.profile_id)
        
    
    personal_data_form()
    
if __name__ == "__main__":
    forms()