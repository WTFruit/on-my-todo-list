import streamlit as stream
import functions as es

tasks = es.file_io(None, readwrite="r")

stream.title("My Todo App")
stream.subheader("This is my todo app.")
stream.write("This app is to increase your productivity.")
for task in tasks:
    stream.checkbox(task)

stream.text_input("", placeholder="add a task!")