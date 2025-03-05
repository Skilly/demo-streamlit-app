import streamlit as st

# -----------------------------------------------------------------------------
# FUNCTIONS
# -----------------------------------------------------------------------------
# Define a function to update the button's appearance
def update_button():
    if st.session_state.button_color == "green":
        st.session_state.button_label = "Press me to change colour to green!"
        st.session_state.button_color = "red"
    else:
        st.session_state.button_label = "Press me to change colour to red!"
        st.session_state.button_color = "green"

# -----------------------------------------------------------------------------
# MAIN APP
# -----------------------------------------------------------------------------
# wite a title using streamlit
st.title('🎈 Dem Streamlit App')

# write some text using streamlit
st.write('Hello demo App!')

# display a button and handle its onclick event using streamlit
st.subheader('Working with buttons')

if "button_label" not in st.session_state:
    st.session_state.button_label = "Press me to change colour to red!"
if "button_color" not in st.session_state:
    st.session_state.button_color = "green"

# Use st.markdown with custom CSS to style the button
button_style = f"""
    <style>
    div.stButton > button:first-child {{
        background-color: {st.session_state.button_color};
        color: white;
    }}
    </style>
"""
st.markdown(button_style, unsafe_allow_html=True)

# Display the button with dynamic label
## if st.button(st.session_state.button_label):
##    update_button()
##    st.rerun()
## The following statement effectivey implements the commented out code above
st.button(
    label=st.session_state.button_label,
    on_click=update_button,
    key="color_changer_button",
)

# Inform the user about the current button colour
if st.session_state.button_color == 'green':
    st.write("The button is now green!")
else:
    st.write("The button is now red!")


# display a slider using streamlit
st.subheader('Working with Sliders')
st.slider("slider", 0, 10)