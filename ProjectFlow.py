import streamlit as st


def show_project_flow():
    st.title("Project Flow")
    st.write("This section outlines the stages that have shaped the development of our project.")

    with st.expander("1. DATA COLLECTION"):
        st.write('''
            The dataset was sourced from Reddit posts spanning October 2023 to December 2023, focusing on both depression-related and non-depression-related content. To avoid domain-specific biases, we constructed a dataset by incorporating subreddits representing various fields and interests.
            -  **Depression Class:** r/depression
            -  **Non-Depression Class:** r/happy, r/indiasocial, r/wallstreetbets, r/gaming, and r/casualconversation
            
            
            Data Source: https://www.reddit.com/r/pushshift/comments/1akrhg3/separate_dump_files_for_the_top_40k_subreddits/
        ''')

    with st.expander("2. DATA PREPROCESSING AND LITERATURE REVIEW"):
        st.write('''
            In this phase, I took the lead in preprocessing the dataset (refer to the diagram below). Concurrently, my team members delved into existing research on depression detection within social media platforms. Based on the Literature Review we wrote a comprehensive review paper, which we successfully presented at the **ICECPCS 2024** conference.
        ''')
        st.image("Images/dataPreprocessing.png", caption = 'Data preprocessing steps')

    with st.expander("3. ANALYZING DEPRESSIVE DATA"):
        st.write('''
            The depression related data was analyzed using BERTopic Topic Modelling technique. (Read more in \'Analysis & Result\' page)             
     
            
            Colab links: 
              -  Lemmatization: https://www.kaggle.com/code/atikabiswas/lemmatization
              -  Topic Modelling: https://colab.research.google.com/drive/1_XEv0VlQqr-Onm1Ah7PDsVg5egsbzbMP?usp=sharing
        ''')

    with st.expander("4. MODELS TRAINING AND TESTING"):
        st.write('''
            Next, we selected 6 Machine Learning (ML) and Neural Network(NN) based models (Logistic Regression, Decision Tree, XGBoost, LSTM, Distil Roberta, and Distil BERT Base) for comparing their performance in detecting depression in our dataset. See the architection followed for these models in the two diagrams below.
              -  ML-Based Models: Logistic Regression, Decision Tree, XGBoost
              -  NN-Based Models: LSTM, Distil Roberta, and Distil BERT Base Uncased
                 
            Colab Links:
              -  Training & Testing of ML models: https://colab.research.google.com/drive/1pl5NQjL-A-0LbKmkCWOghim7y1tmH1M8?usp=sharing
              -  Training & Testing LSTM model: https://colab.research.google.com/drive/1Aszkck8lpNn1Oz3yfc_ZAbweud-Zwxqt?usp=sharing
              -  Training & Testing of Distil Roberta models: https://colab.research.google.com/drive/1RmWkFbqwElxTYO2YKArHx7-V4NQ6YcS0?usp=sharing
              -  Training & Testing Distil BERT Base Uncased model: https://colab.research.google.com/drive/1XubJYdfYZAfDw04BNVdBC77cA8SbOfNa?usp=sharing
        ''')
        st.image("Images/mlArch.jpg", caption='Architecture for ML-based Models')
        st.image("Images/dlArch.png", caption='Architecture for NN-based Models')

    with st.expander("5. JOURNAL WRITING"):
        st.write('''
            The final phase of our project involved a collaborative effort to write and submit a journal paper (currently awaiting review).
        ''')