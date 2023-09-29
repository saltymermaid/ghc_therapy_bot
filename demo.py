import openai
import streamlit as st

def generate_response(myprompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="You are a trained psychiatrist. Answer the prompts accordingly. ###" + myprompt,
        temperature=0.3,
        max_tokens=1024
    )
    return response.choices[0].text.strip()

def main ():
    st.title("Friendly Chat Therapy")
    myprompt = st.text_input("How can I help you? \n")
    # print(generate_response(myprompt))
    if st.button("Submit"):
        st.write(generate_response(myprompt))
if __name__ == "__main__":
    main()
