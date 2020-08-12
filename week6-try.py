#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, redirect, url_for
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# In[2]:


app = Flask(__name__)


# In[3]:


def sentiment_scores(sentence): 
  
    analyzer = SentimentIntensityAnalyzer()
    
    dictionary = analyzer.polarity_scores(sentence) 
      

  
    if dictionary['compound'] >= 0.05 : 
        return("Positive") 
  
    elif dictionary['compound'] <= - 0.05 : 
        return("Negative") 
  
    else : 
        return("Neutral") 


# In[4]:


@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        sentence = request.form.get('sentence')
        return '<h1>The sentence is {}. The sentiment of this sentence is {}.</h1>'.format(sentence, sentiment_scores(sentence))
    
    return '''<form method = "POST">
    Sentence<input type = "text" name = "sentence">
    <input type = "submit">
    </form>'''


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




