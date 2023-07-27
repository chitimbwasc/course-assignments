




import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time as tm

st.markdown(
        """
# Sentiment Mining App

"""
    )

st.markdown(
        """
### This simple application is an assignment submission for the Omdena School's Sentiment Analysis course     entitled "Mastering Sentiment Analysis - Building a Powerful web application".
### It uses the  VADER package for sentiment analysis.
"""
    )


def main():
    """## Sentiment Analysis 

    A user can input a text string and outputs a sentiment
    """
  
    text = st.text_area("Write your text")

    if st.button("Submit"):
        result = sentiment_analyzer(text)

        # decide sentiment as positive, negative and neutral
        if result == "Positive" :
            st.text('')
            st.markdown('''The input text is on the''')
            st.success(result)
            st.markdown('''side of the sentiment spectrum.''')
            st.markdown(":+1::+1::+1::+1::+1::+1::+1::+1:")
            st.balloons()
           
            

        elif result == "Negative" :
            st.markdown('''The input text is on the''')
            st.warning(result)
            st.markdown('''side of the sentiment spectrum.''')
            st.markdown(":-1::-1::-1::-1::-1::-1::-1::-1:")
            st.snow()
           

        else :
            st.markdown('''The input text is on the''')
            st.success(result)
            st.markdown('''portion of the sentiment spectrum.''')
            st.markdown(":ok_hand::ok_hand::ok_hand::ok_hand::ok_hand::ok_hand::ok_hand::ok_hand:")
            

@st.cache_data
def sentiment_analyzer(text):

     # Create a SentimentIntensityAnalyzer object.
    sentiment_obj = SentimentIntensityAnalyzer()

    # Get a polarity score dictionary
    sentiment_dict = sentiment_obj.polarity_scores(text)

	# decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
         sentiment_response = "Positive"

    elif sentiment_dict['compound'] <= - 0.05 :
         sentiment_response = "Negative"

    else :
        sentiment_response = "Neutral"
        
    # Return the response 
    return sentiment_response
    
  
main()








    
   
