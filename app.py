import streamlit as st
from groq import Groq


def get_api_key():
    """Get Groq API key from Streamlit secrets or user input."""
    try:
        api_key = st.secrets["GROQ_API_KEY"]
        st.sidebar.success("Using API key from Streamlit Secrets.")
        return api_key
    except (FileNotFoundError, KeyError):
        st.sidebar.warning("⚠️ API key not configured in Streamlit Secrets.")

        api_key = st.sidebar.text_input(
            "Enter your Groq API key:",
            type="password",
            help="Enter your Groq API key securely."
        )

        if not api_key:
            st.error("Please provide an API key to continue.")
            st.stop()

        st.sidebar.info("Using API key entered by the user.")
        return api_key


st.title("🔐 Secure API Key Demo")
st.write("Exercise 2: Deploy With Secrets")

api_key = get_api_key()

client = Groq(api_key=api_key)

st.success("API key successfully configured!")

if st.button("Test Groq API"):
    with st.spinner("Testing Groq API..."):
        try:
            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {
                        "role": "user",
                        "content": "Say hello in one short sentence."
                    }
                ],
            )

            st.success("Groq API connection successful!")
            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error(f"API request failed: {e}")