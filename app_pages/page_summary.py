import streamlit as st


def page_summary_body():

    st.write("\n")

    st.info(
        f" ### General Information \n"
        "**This website** has a built-in machine learning system that is capable of detecting mildew infection of a cherry leaf image. "
        f"It can instantly differ between healthy leaves and ones that have powdery mildew. " 
        f"Click the Mildew Detection (box 3) in the sidebar to upload your image. \n"
        f"You can also have a look at the image montage in the (box 2) *Leaf Visualizer* of how images **are optimized**." 
        )


                
    st.write("---")


    st.success(
        f" ### Requirements and Quality\n"
        f"**Our** goal was to be at over ±2 standard deviations from the mean "
        f"we are well above the *97%*  range and smashing our **goal**. "    
        )


    if st.button("Info"):

        st.write(
            f"* You can find extra information about business requiraments and stastical information in *Project Hypothesis* \n"
            f"* You can find extra information about Machine Learning and Convolutional Neurak Network in *Project Performance*"
            )

        st.warning(
        f"* For additional information, please visit and **read** the "
         f"[Project README file](https://github.com/JoshSandhu/Project5/blob/main/README.md)."
        )