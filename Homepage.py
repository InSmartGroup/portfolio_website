import streamlit as st

# GUI design
st.set_page_config(layout='wide')
column_head_1, column_head_2 = st.columns([1, 5])

with column_head_1:
    st.image("images/photo.jpg")

with column_head_2:
    st.title("Gregory Ostapenko")
    content = """
    Hi, I'm Gregory!
    I'm a self-taught Python programmer, a huge fan of Computer Vision, Machine Learning, and AI enthusiast.
    This is my portfolio website at which you can find my recent apps.
    Please feel free to contact me via the 'Contact Me' webpage.
    """
    st.info(content)
    st.write("[LinkedIn](https://www.linkedin.com/in/gregory-ostapenko)")

# GUI design, the projects
st.write("Below you can find some of the apps I have built using Python and frameworks, such as OpenCV.")
st.write("Feel free to contact me using the 'Contact Me' page.")

column_project_1, column_project_2 = st.columns([1, 1])

column_project_1_info, column_project_1_image,\
column_project_2_info, column_project_2_image = st.columns([2, 1, 2, 1])

# project 1, image histogram eq project
column_project_1.subheader("Image Histogram EQ Web App")
column_project_1_info.info(
    "An OpenCV-based web app that provides both automatic and manual CLAHE equalization for color and grayscale images."
    "It also allows the user to see image histograms and how they are changed once processed.")
column_project_1_image.image("images/13.png")

# project 2, todo app project
column_project_2.subheader("ToDo Web App")
column_project_2_info.info(
    "A minimalistic web app that allows you to track and manage your daily todos and increase the productivity.")
column_project_2_image.image("images/1.png")

# project 1 and 2 links
column_project_1.write("[Github source code](https://github.com/InSmartGroup/opencv_image_eq_web_app)")
column_project_1.write("[Check the app](https://insmartgroup-opencv-image-eq-web-app-main-2ia80q.streamlit.app)")

column_project_2.write("[Github source code](https://github.com/InSmartGroup/ToDos_WebApp)")
column_project_2.write("[Check the app](https://insmartgroup-todos-webapp-main-wwp7h4.streamlit.app/)")

# project 3,
