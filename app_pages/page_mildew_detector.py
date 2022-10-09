import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
                                                    load_model_and_predict,
                                                    resize_input_image,
                                                    plot_predictions_probabilities
                                                    )

def page_mildew_detector_body():


    images_buffer = st.file_uploader('Upload leaf samples. You may upload more than one.',
                                        type=['jpg','png'],accept_multiple_files=True)
   

    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:
            
            img_pil = (Image.open(image))
            st.info(f"Leaves Sample: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(img_pil, caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")

            resized_img = resize_input_image(img=img_pil, version='v1')
            pred_proba, pred_class = load_model_and_predict(resized_img, version='v1')

            if float(pred_proba) < .9:
                st.warning("## Uncertain Images, can not determine object")

            else:
                plot_predictions_probabilities(pred_proba, pred_class)

                df_report = df_report.append({"Name":image.name, 'Result': pred_class },
                                        ignore_index=True)
        
                if not df_report.empty:
                    st.success(f"##### AI is **{100 * pred_proba:.2f}**% certen it is {pred_class}.")
                    st.table(df_report)

                    st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)
                    
    if st.button("Download test sample images"):

        st.warning(
        f"* You will be able to find a selection of images to use for **testing**  "
        f"[here.](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves) "
        f" opens external link to kaggle."
        )
      