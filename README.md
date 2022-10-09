## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We created then a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from client's crop fields. The images show cherry leaves that are healthy and cherry leaves that contain powdery mildew, which is a fungal disease that affects a wide range of plants. The cherry plantation crop is one of their finest products in the portfolio and the company is concerned about supplying the market with a product of compromised quality.

## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is to manually verify if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If it has powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees located in multiple farms across the country. As a result, this manual process is not scalable due to time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that is capable of detecting instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project to all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

* 1 - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy and that contains powdery mildew.
* 2 - The client is interested to predict if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and how to validate?

### Hypothesis

* With high accuracy and the help of Machine Learning models we want to seperate leaves with mildew and those without.

### Validation

In order to validate high accuracy (97%+) we require a large sample set. With a binary classification of objects:
* Leaf with mildew
* Leaf without mildew

There is misleading information in this validation of whether the leaf is healthy. It only states with or without mildew with high precision. It is also possible for the leaf to suffer from Mildew except a human will not be able to see it, the deep learning algorithm however can differentiate.
Validation is made from a separate folder from the test and training set. This tests the algorithm on **new** data ensuring true results.

The train test and validation ratio is 70%, 20%, and 10%.

## Rationale to map the business requirements to the Data Visualizations and ML tasks

### Business requirements
* The client is interested to conduct a study which visually can differentiate between a healthy cherry leaf and one that contains powdery mildew.
* The client will also be intrerested in predicting if a cherry leaf  is infected with powdery mildew or not.

#### Visually differentiate
It will be beneficial to automate the visual differences between infected and healthy cherry leaves. The difference is determinded using greyscale which seems to be the standard, however it is important to note that not every colour map converts linear to greyscale.

#### Predicting algorithm
This algorithm is used to analyse the nominal categorical variable of leaves with mildew mold or not. This algorithm can be expanded to also cover other visual diseases due to its uses of greyscale.

## ML Business Case
This particular business idea was created by the stakeholders, as it was their idea to study the difference between healthy and unhealthy leaves. This was based on the hypothesis that the difference could be accurately identified by an algorithm with a high rate of acuracy.

The data understanding was sorted by the team at Code Institute. A model of deep neaural networks to eliminate the null hypothesis and show great results. Any output data was then shown by a streamlit dashboard and deployed using Heroku. (See steps below)

This is to help ease any repatative workload on employees.

## Dashboard Design

The design and colour's are sourced from the streamlit library. It has a responsive design for use accross devices and a sidebar collapse going to table size at 768px. Sidebar's initial state is expanded to enhance user experience.

### Sidebar

The sidebar contains 5 boxes for navigation.
* Box1: Quick project summary.
* Box2: Leaf visualizer.
* Box3: Mildew detection.
* Box4: Project hypothesis.
* Box5: ML performace metrics.


*Box1: Quick project summary*

Package of use:
* Streamlit

The user is given information on how to get started and the quality of outcome. A button which displays Info when clicked shows where to find business requirements, machine learning information and an external link to README file.


*Box2: Leaf visualizer.*

Package of use:
* Streamlit
* Matplotlib

There are three checkbox alternatives. These include:
* Difference between the average and variability image:
    - Matplotlib shows an average of 20 leaves images in both categories.
* Differences between average unhealthy and average healthy leaves.
    - Matplotlib shows the difference between the two categories.
* Image montage.
    - Randomly show images from selected category in a 3x3 with matplotlib subplot.\
        The category is chosen from a select box.


*Box3: Mildew detection.*

Package of use:
* Streamlit
* PIL
* Numpy
* Plotly
* Pandas

Here the AI will be able to evaluate new unclassified content. The design is clean with a Streamlit file_uploader. The result is then shown via info text and plotly bar. With finally a HTML `<a>` tag to dowenload the result in a CSV file.


*box4: Project hypothesis*

Package of use:
* Streamlit 

The project hypothesis is shown in a success box. 


*box5: ML performance metrics*

Package of use:
* Streamlit
* Matplotlib
* Pandas

Matplotlib shows us a png fil over seaborn barplot of the train, validation, and test sets. Next are two dot-line plots of the model history in a png as shown by matplotlib. 
Next there are three streamlit checkboxes, the first two will show you text about the deep layers and the last is a pandas DataFrame opened up by streamlits dataframe.

## Deployment
### Heroku

* The App live link is: https://mildew-detector.herokuapp.com/ 
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly in case all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.


## Main Data Analysis and Machine Learning Libraries
* numpy==1.19.2
    - Used to convert numbers and objects to arrays and operate on them.
* pandas==1.1.2
    - Is used to struckture data. Index data series or a "table" of data in a DataFrames
* matplotlib==3.3.1
    - .pyplot (v. 4.12.0) is used to creat almost all graph plots  
* seaborn==0.11.0
    - Seaborn helps "styling and ordering pyplots graphs"
* streamlit==0.85.0
    - Is used to connect frontend and backend fast and easy.  
* tensorflow-cpu==2.6.0
    - Multidimensional array operator building the core of the CNN operations
* keras==2.6.0
    - Setting the sequal for the model and hadels operations on the multidimensional arrays


## Credits 

* This object-oriented website layout is made by GyanShashwat1611 at [Github site](https://github.com/GyanShashwat1611/WalkthroughProject01/).
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves)
