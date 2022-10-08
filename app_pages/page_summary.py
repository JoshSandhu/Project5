import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        )

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/GyanShashwat1611/WalkthroughProject01/blob/main/README.md).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        )