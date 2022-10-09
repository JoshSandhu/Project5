import streamlit as st
import os
import matplotlib.pyplot as plt
from matplotlib.image import imread
import itertools
import random

def page_leaf_visualizer_body():
    st.write("### Leaf Visualizer")
    st.info(
        f"* To see visual differences or have a look at Image Montage, "
        f"click the button belew. ")
    
    version = 'v1'
    if st.checkbox("Difference between average and variability image"):

      st.warning(
      f"* In the difference between variability, the **darker** area shows " 
      f"where both images are similar. The lighter area shows where variability differences. "
      )

      avg_mildew = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")
      avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")

      st.image(avg_mildew, caption='Unhealthy Leaf - Avegare and Variability')
      st.image(avg_healthy, caption='healthy Leaf - Average and Variability')

      st.write("---")


    if st.checkbox("Differences between average unhealthy and average healthy leaf"):
          diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

          st.image(diff_between_avgs, caption='Difference between average images')
          st.warning(
            f"* In the difference between averages, the **darker** area shows " 
            f"where both average images are similar. The lighter part is where averages are different.\n "
            )


    if st.checkbox("Image Montage"): 
      st.write("* To refresh the montage, click on 'Create Montage' button")
      my_data_dir = 'inputs/cherry_leaves_dataset/cherry-leaves'
      labels = os.listdir(my_data_dir+ '/validation')
      label_to_display = st.selectbox(label="Select label", options=labels, index=0)
      if st.button("Create Montage"):      
        image_montage(dir_path=f"{my_data_dir}/validation",
                      label_to_display=label_to_display,
                      nrows=3, ncols=3, figsize=(10,15))
      st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15,10)):
  labels = os.listdir(dir_path)

  # subset the class you are interested to display
  if label_to_display in labels:

    # checks if your montage space is greater than subset size
    images_list = os.listdir(dir_path+'/'+ label_to_display)
    if nrows * ncols < len(images_list):
      img_idx = random.sample(images_list, nrows * ncols)
   

    # create list of axes indices based on nrows and ncols
    list_rows= range(0,nrows)
    list_cols= range(0,ncols)
    plot_idx = list(itertools.product(list_rows,list_cols))


    # create a Figure and display images
    fig, axes = plt.subplots(nrows=nrows,ncols=ncols, figsize=figsize)
    for x in range(0,nrows*ncols):
      img = imread(f"{dir_path}/{label_to_display}/{img_idx[x]}")
      img_shape = img.shape
      axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
      axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
      axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
      axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
    plt.tight_layout()
    
    st.pyplot(fig=fig)