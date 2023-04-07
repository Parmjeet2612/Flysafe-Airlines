import subprocess

# Install the Transformers library
subprocess.call(['pip', 'install', 'transformers'])

# Now you can import and use the Transformers library in your script
import transformers
import streamlit as st
import streamlit.components.v1 as components
import streamlit as st
from transformers import pipeline
import pandas as pd
import random


st.set_page_config(layout="wide")



# Define the text to display in the left pane
text = '''
# About Flysafe Airlines Sentiment Analyses

This is a demo application that showcases the use of the LDA model and Streamlit framework for sentiment analysis. 

The application allows you to enter some text and performs sentiment analysis on it. 

The sentiment analysis model classifies the text as either positive or negative, and provides a score associated with that sentiment. The score ranges from 0 to 1, with higher scores indicating more positive sentiment.

You can use this application to analyze customer feedback, monitor social media sentiment, and more. 

Team Members:

        Anshu Saggar
        
    Parmjeet Kaur
        
    Shivam Kapoor
        
    Vineeta Gupta
        
    Yadwinder Singh (Team Lead)
        
    Yudhvir Singh
            

'''

st.title('Team D5')
st.title('Flysafe Airlines Sentiment Analysis')



form = st.form(key='sentiment-form')

# Add a column to the page layout for the left pane
left_column, right_column = st.columns([3,7])

# Display the text in the left pane
with left_column:
    st.markdown(text)

# Display the form in the right pane
with right_column:    
    user_input = form.text_area('Enter your text')
    submit = form.form_submit_button('Submit')

    if submit:
        classifier = pipeline("sentiment-analysis")
        result = classifier(user_input)[0]
        label = result['label']
        score = result['score']

        if label == 'POSITIVE':
            st.success(f'{label} sentiment (score: {score})')
        else:
            st.error(f'{label} sentiment (score: {score})')
        
        
        
    html_temp = """<div class='tableauPlaceholder' id='viz1680490796592' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fl&#47;Flysafe1&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Flysafe1&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fl&#47;Flysafe1&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1680490796592');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 950 ) { vizElement.style.width='100%';vizElement.style.maxWidth='950px';vizElement.style.height=(divElement.offsetWidth*0.85)+'px';vizElement.style.maxHeight='2087px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.maxWidth='650px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';vizElement.style.maxHeight='2087px';} else { vizElement.style.width='100%';vizElement.style.height='977px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(html_temp, width=1000, height=900)
    
 
    # Load data from Excel file
    data = pd.read_excel('review_analysis.xlsx')

    # Choose 10 random comments from the data
    random_indices = random.sample(range(len(data)), 10)
    comments = data.loc[random_indices, 'comment']

    # Perform sentiment analysis on the comments
    classifier = pipeline("sentiment-analysis")
    results = classifier(list(comments))
    labels = [result['label'] for result in results]
    scores = [result['score'] for result in results]

    # Display the comments and their sentiments in a table
    df = pd.DataFrame({'Comment': comments, 'Sentiment': labels, 'Score': scores})
    st.write(df)
    