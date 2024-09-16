import streamlit as st
import pandas as pd
import plotly.io as pio
from bertopic import BERTopic

# Use BERTopic to perform topic modelling on depressive Reddit post.
model = BERTopic.load('Models\BERTopic_Model')
intertopicDistMap = model.visualize_topics(title=None)
intertopicDistMap.update_layout(template='plotly_dark')
barchart = model.visualize_barchart(top_n_topics = 20, n_words = 10, autoscale = True, title=None)
barchart.update_layout(template='plotly_dark')


# Metrics scores stored as a dataframe
models = ['Evaluation Metrics', 'LSTM', 'Distil Roberta', 'Distil BERT Base', 'Logistic Regression', 'Decision Tree', 'XGBoost']
scores = [['Precision', 90.75, 94.93, 94.78, 93.01, 83.72, 91.51], 
            ['Recall', 92.78, 95.69, 96.30, 91.86, 83.80, 89.48,], 
            ['F1 Score', 91.75, 94.93, 95.53, 92.43, 83.76, 90.48, ], 
            ['Accuracy', 92.49, 95.74, 95.93, 93.24, 85.41, 91.55]]
df = pd.DataFrame(scores, columns = models)


# A function to design the content of AnalysisAndResult page
def show_tabs():
    st.title("Analysis & Result")
    
    # separating the content into two tabs
    tab1, tab2 = st.tabs(["📈Topic Modelling", "📊Comparative Evaluation of Models"])

    #<<--------------------------------------------------------------Tab 1 content------------------------------------------------------------->>
    tab1.subheader("Analyzing Depressive Reddit posts")
    tab1.markdown(
        '''
        After preprocessing the data, the **BERTopic** Topic Modelling technique was used to analyze and discover common factors contributing to depression. Topic modeling is a statistical method used to uncover hidden themes within a set of documents, allowing for extracting meaningful insights and patterns from textual data 

        '''
    )

    tab1.markdown('''#### VISUALIZATION 1: Intertopic Distance Map''')
    tab1.write("An intertopic distance map in BERTopic is a powerful visualization tool that provides a visual representation of the relationships between discovered topics. It helps you understand how similar or dissimilar topics are to each other.")
    tab1.plotly_chart(intertopicDistMap, use_container_width=True, theme = None)
    
    tab1.markdown('''#### VISUALIZATION 2: Top 20 topics discussed in depressive Reddit posts''')
    tab1.write("The analysis revealed a total of 15 distinct major topics, each characterized by a set of keywords, which were discussed by about 100 users. The bar chart generated below offers a visual depiction of the frequency distribution of individual topics identified by the BERTopic model within the dataset. Through the visualization, various possible reasons for depression were identified such as loneliness, physical appearance, unemployment, relationships and work or study pressure. Notably, some topics emerged as the most severe ones, mentioning \'suicide\' and \'self-harm\'.")
    tab1.plotly_chart(barchart, use_container_width=True, theme = None)

    #<<--------------------------------------------------------------Tab 2 content------------------------------------------------------------->>
    tab2.subheader("Evaluating and Comparing Performance of the Models")
    tab2.markdown(
        '''
        Each model was trained and validated using a split of 80% training data and 20% validation data. The performance of the models was assessed using four metrics: accuracy, precision, recall, and F1 score
          -  **Accuracy** is the overall proportion of correct predictions. It is a general measure of how well the model performs on the entire dataset.  
          -  **Precision** is the proportion of positive predictions that are actually correct. It evaluates how accurate the model is when it predicts a positive outcome.                   
          -  **Recall** is the proportion of actual positive instances that are correctly predicted. It evaluates how well the model is able to identify all positive instances.                   
          -  **F1 Score** is the harmonic mean of precision and recall. It provides a balanced measure of both precision and recall. 


          Given below is a bar graph show score achieved by the six models for each evaluation metric.
        '''
    )
    tab2.bar_chart(
        df, 
        x = "Evaluation Metrics", 
        y = ['LSTM', 'Distil Roberta', 'Distil BERT Base', 'Logistic Regression', 'Decision Tree', 'XGBoost'], 
        color = ('#845ec2', '#d65db1', '#ff6f91', '#ff9671', '#ffc75f', '#f9f871'), 
        stack = False,
        use_container_width = True)
    tab2.markdown('''**INFERNCE:**  The DistilBERT Base Uncased model emerged as the top performer, with an accuracy of 95.93 and an F1 score of 95.53. This indicates that the model is highly effective in classifying depression-related content, maintaining a strong balance between precision and recall.''')