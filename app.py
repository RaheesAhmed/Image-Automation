import streamlit as st
import main  # Import your existing image generation script
import os
st.title("Image Generation App")

# Sidebar with user input
project_folder = st.text_input("Enter Project Folder Name:", "Keto")

if st.button("Generate Images"):
    main.open_data(project_folder)
    st.success("Images generated successfully!")

# Display generated images if available
st.header("Generated Images")
images_dir = f"READY/{project_folder}/images"
images = st.image([os.path.join(images_dir, img) for img in os.listdir(images_dir)])

st.sidebar.markdown("### Options")
bottom_section = st.sidebar.checkbox("Enable Bottom Section")
st.sidebar.text("Customize other options as needed.")

st.sidebar.markdown("### About")
st.sidebar.info(
    "This app generates images using your existing script. "
    "Enter the project folder name and click 'Generate Images' to create images."
)
