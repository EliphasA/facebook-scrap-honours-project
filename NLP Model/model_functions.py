# Impporting packages
import nltk
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.collocations import *
import string
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Downloading stopwords
nltk.download('stopwords')
nltk.download('words')
words = set(nltk.corpus.words.words())

# Creating sentiment analyzer object
sentiment_analyser = SentimentIntensityAnalyzer()

# Removing non-english words function
def remove_non_engl_word(text):
    text = " ".join(w for w in nltk.wordpunct_tokenize(text) if w.lower() in words or not w.isalpha())
    
    return text

# Text processing function
def text_processing(text):
    # Removing stop words
    stopwords = nltk.corpus.stopwords.words('english')
    text = ' '.join([word for word in text.split() if word not in stopwords])
    
    # Removing panctuations
    text = text.translate(str.maketrans('','',string.punctuation))
    
    # Steming the words
    stemmer = nltk.stem.porter.PorterStemmer()
    text = ' '.join([stemmer.stem(word) for word in text.split()])
    
    #Return processed text
    return text

# Creating sentiment analyzer function
def analyze_sentiment(text):
    # Getting sentiment scores
    sentiment_score = sentiment_analyser.polarity_scores(text)
    sentiment = ''
    
    # Classifying the sentiments
    if sentiment_score['compound'] > 0:
      sentiment = 'positive'
    elif sentiment_score['compound'] < 0:
      sentiment = 'negative'
    else:
      sentiment = 'neutral'
      
    return sentiment

# Cinvert text to lowercase function
def to_lowercase(text):
    text = text.lower()
    
    return text

# Remove special characters function
def remove_sp_char(text):
    text = re.sub(string=text,
                  pattern="[{}]".format(string.punctuation),
                  repl="")
    
    return text
    
# Tokenization function
def tokenization(text):
    text = nltk.sent_tokenize(text)
    
    return text

# Text lemmatise function
def lemmatize(text):
    lemmatizer = WordNetLemmatizer()
    
    return [lemmatizer.lemmatize(token) for token in text]

# Stemming functions
def stemming(text):
    stemmer = PorterStemmer()
    
    return [stemmer.stem(token) for token in text]

# Remove stop-words function
def remove_stopword(text):
    stop_words = set(stopwords.words('englist'))
    
    return [item for item in text if item not in stop_words]

# Remove numbers functions
def remove_num(text):
    text.replace('\d+', '')
    
    return text

# Remove words with less that 2 char function
def remove_short_tokens(text):
    return [token for token in text if len(text) > 2]

def processing_with_lemmatisation(org_text):
    text = remove_sp_char(org_text)
    text = to_lowercase(text)
    # text = tokenization(text)
    text = lemmatize(text)
    text = remove_num(text)
    text = remove_stopword(text)
    text = remove_short_tokens(text)
    
def processing_with_stemming(df):
    text = remove_sp_char(df)
    text = to_lowercase(text)
    text = tokenization(text)
    text = lemmatize(text)
    text = remove_num(text)
    text = remove_stopword(text)
    text = remove_short_tokens(text)
    

def add_labels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i],ha='center')