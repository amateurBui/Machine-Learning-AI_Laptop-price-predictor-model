import streamlit as st
import time


st.title("DT Assistant")
st.write("Welcome to DT STORE! How can I help you today?")

if "messages" not in  st.session_state:
    st.session_state.messages = []
    
if prompt := st.chat_input("Talk to a bot"):
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message('user'):
        st.markdown(prompt)
    if "price " in prompt and "laptop" in prompt:
        with st.chat_message('assistant'):
            full_res = ""
            holder = st.empty()
            A = ("Please visit the following link: http://localhost:8502/ for assistance.")
            for word in A.split():
                full_res += word + " "
                time.sleep(0.5)
                holder.markdown(full_res)
    elif "DT STORE page" in prompt:
        with st.chat_message('assistant'):
            full_res = ""
            holder = st.empty()
            A = ("Please access the following link: https://10web-site.ai/9/neutral-mackerel/")
            for word in A.split():
                full_res += word + " "
                time.sleep(0.5)
                holder.markdown(full_res)
    else:
        with st.chat_message('assistant'):
            full_res = ""
            holder = st.empty()
            A = ("I don't understand what you're talking. Please call our hotline at 0999999999 for information or assistance.")
            for word in A.split():
                full_res += word + " "
                time.sleep(0.5)
                holder.markdown(full_res)