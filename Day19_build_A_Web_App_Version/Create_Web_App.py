import streamlit as st
import functions

result_read = functions.get_read_lines()

st.title("My Todo App")
st.subheader("This is SubHead of Todo App ")
st.write("This is a simple text")

for item in result_read :
    st.checkbox(item)

st.text_input(label="", placeholder="Add New Todo's" )