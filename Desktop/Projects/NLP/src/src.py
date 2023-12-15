"""__imports__"""
import string
import re

import json
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob

def strip_characters(sentence: str) -> str:
  """__doc__
  Remove special characters, punctuation, and unnecessary whitespaces from a sentence.
  """
  sentence = re.sub(r"[^a-zA-Z0-9\s]", "", sentence)
  sentence = sentence.translate(str.maketrans('', '', string.punctuation))
  sentence = " ".join(sentence.split())
  return sentence.lower()

def tokenize(sentence: str) -> list:
  """__doc__
  Tokenize a sentence into a list of words.
  """
  return nltk.word_tokenize(sentence)

def remove_stopwords(sentence: list) -> list:
  """__doc__
  Remove stopwords from a sentence.
  """
  stopwords = nltk.corpus.stopwords.words('english')
  return [word for word in sentence if word not in stopwords]

def stem(sentence: list) -> list:
  """__doc__
  Stem a sentence.
  """
  stemmer = nltk.stem.PorterStemmer()
  return [stemmer.stem(word) for word in sentence]

def lemmatize(sentence: list) -> list:
  """__doc__
  Lemmatize a sentence.
  """
  lemmatizer = nltk.stem.WordNetLemmatizer()
  return [lemmatizer.lemmatize(word) for word in sentence]

def preprocess(sentence: str) -> list:
  """__doc__
  Preprocess a sentence.
  """
  sentence = strip_characters(sentence)
  sentence = tokenize(sentence)
  sentence = remove_stopwords(sentence)
  sentence = lemmatize(sentence)
  sentence = stem(sentence)
  return sentence

def get_polarity(sentence: str) -> float:
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(sentence)
    return sentiment_scores['compound']

def get_subjectivity(sentence: str) -> float:
    blob = TextBlob(sentence)
    return blob.sentiment.subjectivity

def get_polarity_category(polarity: float) -> str:
    if polarity > 0.5:
        return "Very Positive"
    elif polarity > 0.0:
        return "Positive"
    elif polarity == 0.0:
        return "Neutral"
    elif polarity >= -0.5:
        return "Slightly Negative"
    else:
        return "Very Negative"

def get_subjectivity_category(subjectivity: float) -> str:
    if subjectivity >= 0.5:
        return "Subjective"
    else:
        return "Objective"
      
def get_sentiment(sentence: str) -> dict:
    polarity = get_polarity(sentence)
    subjectivity = get_subjectivity(sentence)

    return {
    "Sentiment": 
      {
        "sentence": sentence,
        "polarity_score": polarity,
        "subjectivity_score": subjectivity,
        "polarity": get_polarity_category(polarity),
        "subjectivity": get_subjectivity_category(subjectivity)
      }
    }

"""  
def main() -> None:
  sentence = input("\nEnter a sentence: ")
  data = get_sentiment(sentence)
  json_data = json.dumps(data, indent=4, separators=(',', ': '))
  print("\n" + json_data)   

if __name__ == "__main__":
  main()
"""