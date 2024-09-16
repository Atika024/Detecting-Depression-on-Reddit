import streamlit as st
from transformers import AutoModelForSequenceClassification, pipeline, AutoTokenizer


def load_model():
    path = "D:\MajorProject\Models\DistilBERTbase_Model"

    model = AutoModelForSequenceClassification.from_pretrained(path)
    tokenizer = AutoTokenizer.from_pretrained(path)
    pipe = pipeline("text-classification", model = model, tokenizer = tokenizer)

    return pipe

classifier = load_model()

def show_predict_page():
    st.title("Depression Detection in Reddit")

    st.subheader("Hi! 🙋🏽‍♀️")
    st.markdown(
        '''
            **Welcome to the walkthrough of my final year project!**  
            

            My two college friends and I worked together, under the guidance of our university professor, with the objective of:
              -  Contributing to ongoing efforts to improve mental health care practices by reviewing literature on depression detection in Social media. 
              -  Collecting and analyzing recent depression related posts on Reddit to recognize the root causes of depression effectively. 
              -  Evaluating performance of several ML and DL models in classifying depression content. 

              
            Check out the best-performing depression predicting model of our project by pasting a Reddit post or maybe... writing how was your day 🤗
        '''
    )

    text = st.text_input('Reddit Post', placeholder = 'Write here...', autocomplete = "I've been feeling worse and worse the last few days, probably gonna be in a low spot soon. I'm scared that people i know will see I'm not normal because any time I manage to feel happy I just get numb and feel awful right after, I can't stop telling myself how useless I am and I want to cry, it feels like only sh helps me then. Then I feel horrible to doing it and I do it again to punish myself I know nobody's going to see this I just had to say it to someone, it feels so bad when I'm numb and empty inside and I have to fake the happiness I felt for real just a minute ago")
    ok = st.button ("Detect Depression")

    if ok:
        result = classifier(text)
        result = result[0]['label']
        if result == 'LABEL_0':
            result = 'not depressed'
        else:
            result = 'depressed'

        st.subheader(f"The user is {result}")