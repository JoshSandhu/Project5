import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation

from tensorflow import keras

def page_ml_performance_metrics():
    version = 'v1'

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
    st.write("---")


    st.write("### Model History")
    col1, col2 = st.beta_columns(2)
    with col1: 
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Traninig Accuracy')
        st.info(
                f"* accuracy refers to the accuracy from the training set \n" 
                f"* val_accuracy refers to the accuracy against the validation set"
                )
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Traninig Losses')
        st.info(
                f"Loss is the training of of the ML to change its weights and biases \n" 
                f"in order to make better predictions"
                )
        
    



    st.write("---")


    if st.checkbox('Model: "sequential"'): 
        st.text(
            """
            Model: "sequential"
            _________________________________________________________________
            Layer (type)                 Output Shape              Param #   
            =================================================================
            conv2d (Conv2D)              (None, 254, 254, 16)      448       
            _________________________________________________________________
            max_pooling2d (MaxPooling2D) (None, 127, 127, 16)      0         
            _________________________________________________________________
            conv2d_1 (Conv2D)            (None, 125, 125, 32)      4640      
            _________________________________________________________________
            max_pooling2d_1 (MaxPooling2 (None, 62, 62, 32)        0         
            _________________________________________________________________
            conv2d_2 (Conv2D)            (None, 60, 60, 16)        4624      
            _________________________________________________________________
            max_pooling2d_2 (MaxPooling2 (None, 30, 30, 16)        0         
            _________________________________________________________________
            flatten (Flatten)            (None, 14400)             0         
            _________________________________________________________________
            dense (Dense)                (None, 128)               1843328   
            _________________________________________________________________
            dropout (Dropout)            (None, 128)               0         
            _________________________________________________________________
            dense_1 (Dense)              (None, 1)                 129       
            =================================================================
            Total params: 1,853,169
            Trainable params: 1,853,169
            Non-trainable params: 0
            _________________________________________________________________

            """
        )
    

    if st.checkbox('Sequential: Layers"'): 
        st.text(
            """
            model = Sequential()

            model.add(Conv2D(filters=24, kernel_size=(3,3),input_shape=image_shape, activation='relu',))
            model.add(MaxPooling2D(pool_size=(2, 2)))

            model.add(Conv2D(filters=12, kernel_size=(3,3),input_shape=image_shape, activation='relu',))
            model.add(MaxPooling2D(pool_size=(2, 2)))

            model.add(Conv2D(filters=8, kernel_size=(3,3),input_shape=image_shape, activation='relu',))
            model.add(MaxPooling2D(pool_size=(2, 2)))

            model.add(Conv2D(filters=6, kernel_size=(3,3),input_shape=image_shape, activation='relu',))
            model.add(MaxPooling2D(pool_size=(2, 2)))

            model.add(Flatten())
            model.add(Dense(128, activation = 'relu'))

            model.add(Dropout(0.5))
            model.add(Dense(1, activation = 'sigmoid'))

            model.compile(loss='binary_crossentropy',
                        optimizer='adam',
                        metrics=['accuracy'])
            """
        )


    if st.checkbox('Generalised Performance"'): 

        st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))