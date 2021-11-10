import pandas as pd
from textblob import TextBlob

def subjectivity(x):
    sub = TextBlob(x).sentiment.subjectivity
    if sub > 0.70:
        print('Highly subjective')
    elif sub >=0.30 and sub <= 0.70:
        print('Neutral')
    else:
        print('Highly Factual')
    return(sub)
