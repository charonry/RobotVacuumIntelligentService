"""
前端页面交互

运行 python -m streamlit run .\app.py
"""
import time
import streamlit as st
from agent.react_agent import ReActAgent

st.title("智扫通机器人智能客服")
st.divider()

if "agent" not in st.session_state:
    st.session_state["agent"] = ReActAgent()

if "message" not in st.session_state:
    st.session_state["message"] = [{"role": "assistant", "content": "你好，有什么可以帮助你？"}]

for message in st.session_state["message"]:
    st.chat_message(message["role"]).write(message["content"])

msg = st.chat_input()

if msg:
    st.chat_message("user").write(msg)
    st.session_state["message"].append({"role": "user", "content": msg})

    response_messages = []
    with st.spinner("智能客服思考中..."):
        res_stream = st.session_state["agent"].execute_stream(msg)

        def capture(generator, cache_list):
            for chunk in generator:
                cache_list.append(chunk)
                for char in chunk:
                    time.sleep(0.01)
                    yield char

        st.chat_message("assistant").write_stream(capture(res_stream, response_messages))
        st.session_state["message"].append({"role": "assistant", "content": response_messages[-1]})
        st.rerun()