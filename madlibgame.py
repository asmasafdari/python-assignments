import streamlit as st

#streamlit app tltle
st.title('🎈Fun Mad Lib Game 🎈')

#streamlit header
st.sidebar.header("Fill In The Blanks Below")

#Taking user input
verb = st.sidebar.text_input("Verb")
adjective = st.sidebar.text_input("Adjective")
noun = st.sidebar.text_input("Noun")

# Fun Sentences
madLib_sentence =[
    f"Today I went to the zoo. I saw a {noun} jumping up and down in its tree {adjective} fast.",
    f"We are going to {verb} a loud. The {noun} is very {adjective}!",
]
if st.sidebar.button("Tell Me A Mad Lib"):
    selected_madLib=(random.choice(madLib_sentence))
    st.subheader("Here's your Mad Lib")
    st.write(selected_madLib)
# Footer
st.markdown("Made By Samina")
