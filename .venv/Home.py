import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1,col2=st.columns(2)

with col1:
    st.image("./images/photo.jpg", width=600)

with col2:
    st.title("Ravali Goud")
    content="""
    Hey!! I am Ravali in the final year of my B.Tech in Computer Science and Engineering at Vignan's Institute of Management and Technology for Women. 
    I completed my schooling at PBDAV Model School and my intermediate education at Sri Chaitanya Junior College.
     I am originally from a village in Mahabubabad district and currently reside in Hyderabad.
     I have earned certifications in Core Java from Internshala, Career Essentials in Generative AI and Software Development from LinkedIn and Microsoft, and ChatGPT and AI skills from Skill Nation.
      Additionally, I completed a Power BI workshop conducted by Office Master. 
    """
    st.info(content)
content2="""
Below you can find some of the apps I have built in Python.Feel free to contact me!
"""
st.write(content2)

col3,empty_col,col4=st.columns([1.5,0.5,1.5])

df=pandas.read_csv("pythonProject/.venv/data.csv")


with col3:
    for index,row in df[1:10].iterrows():
        st.header(row["Column1"])
        st.write(row["Column2"])
        st.image("images/"+row["Column4"])
        st.write(f"[Souce code]({row["Column3"]})")

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["Column1"])
        st.write(row["Column2"])
        st.image("images/" + row["Column4"])
        st.write(f"[Souce code]({row["Column3"]})")

