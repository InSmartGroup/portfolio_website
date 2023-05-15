import streamlit as st

# GUI design
st.set_page_config(layout='wide')
column_head_1, column_head_2 = st.columns([1, 3])

with column_head_1:
    st.image("images/photo.jpg")

with column_head_2:
    st.title("Gregory Ostapenko")
    content = """
    Hi, I'm Gregory!
    I'm a self-taught Python programmer, a huge fan of Computer Vision, Machine Learning and AI enthusiast.
    This is my portfolio website at which you can find my recent apps.
    Please feel free to contact me via the 'Contact Me' webpage or by sending me a message using the LinkedIn link below.
    """
    st.info(content)
    st.write("[LinkedIn](https://www.linkedin.com/in/gregory-ostapenko)")

# GUI design, the projects
st.write("Below you can find some of the apps I have built using Python and frameworks, such as OpenCV.")

# block of projects, projects 1 and 2
column_project_1, column_project_2 = st.columns([1, 1])

column_project_1_info, column_project_1_image,\
column_project_2_info, column_project_2_image = st.columns([2, 1, 2, 1])

# project 1, image histogram eq web app
column_project_1.subheader("Image Histogram EQ Web App")
column_project_1_info.info(
    "An OpenCV-based web app that provides both automatic and manual CLAHE equalization for color and grayscale images."
    "It also allows the user to see image histograms and how they are changed once processed.")
column_project_1_image.image("images/13.png")

# project 2, todo app web app
column_project_2.subheader("ToDo Web App")
column_project_2_info.info(
    "A minimalistic web app that allows you to track and manage your daily todos and increase the productivity.")
column_project_2_image.image("images/1.png")

# projects 1 and 2 links
column_project_1_info.write("[Github source code](https://github.com/InSmartGroup/opencv_image_eq_web_app)")
column_project_1_info.write("[Check the app](https://insmartgroup-opencv-image-eq-web-app-main-2ia80q.streamlit.app)")

column_project_2_info.write("[Github source code](https://github.com/InSmartGroup/ToDos_WebApp)")
column_project_2_info.write("[Check the app](https://insmartgroup-todos-webapp-main-wwp7h4.streamlit.app/)")


# new block of projects, projects 3 and 4
column_project_1, column_project_2 = st.columns([1, 1])

column_project_1_info, column_project_1_image,\
column_project_2_info, column_project_2_image = st.columns([2, 1, 2, 1])

# project 3, pdf file generator
column_project_1.subheader("PDF Generator")
column_project_1_info.info("A script that generates a .pdf workbook from a .csv dataframe")
column_project_1_image.image("images/3.png")

# project 4, random password generator web app
column_project_2.subheader("Random Password Generator Web App")
column_project_2_info.info("A minimalistic web app that allows generating random passwords and saving them locally as text files.")
column_project_2_image.image("images/17.png")

# project 3 and 4 links
column_project_1_info.write("[Github source code](https://github.com/InSmartGroup/pdf_documents_generation)")
column_project_2_info.write("[Github source code](https://github.com/InSmartGroup/random_password_generator_web_app)")
column_project_2_info.write("[Check the app](https://insmartgroup-random-password-generator-web-app-main-4r305p.streamlit.app/)")


# new block of projects, projects 5 and 6
column_project_1, column_project_2 = st.columns([1, 1])

column_project_1_info, column_project_1_image,\
column_project_2_info, column_project_2_image = st.columns([2, 1, 2, 1])

# project 5,
