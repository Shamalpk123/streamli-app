import streamlit as st
import pandas as pd
# st.write("hello welcome to streamlit")
# st.title('Programming')
# st.header("python world")
# st.subheader("streamlit")
# st.markdown('markdown')
# st.code("""print("Welcome to Streamlit Class")""")
# st.code("""for i in range(1,5,1): 
# 	print("java")""")
# dataset = pd.read_csv("titanic.csv")
# st.dataframe(dataset)

# name = st.text_input("enter your name:")
# fname = st.text_input("enter your father name:")
# button = st.button("Done")

# classdata = st.selectbox("enter your class:", (1,2,3,4,5))

# if button:
#     st.markdown(f"""
#     Name:{name}
#     Father Name:{fname}
#     class:{classdata} """)

number = st.slider("pick a number", 0, 100)


