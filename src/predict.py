# from transformers import pipeline

# classifier = pipeline("sentiment-analysis")

# review = input("Enter review: ")

# result = classifier(review)

# label = result[0]['label']
# score = result[0]['score']

# print(f"Sentiment : {label}")
# print(f"Confidence: {score:.2f}") 


import pandas as pd
from transformers import pipeline

# Load model
classifier = pipeline("sentiment-analysis")

# Load dataset
df = pd.read_csv("data/IMDB Dataset.csv")

# Take first 5 reviews
reviews = df['review'].head()

for review in reviews:

    result = classifier(review[:512])

    label = result[0]['label']

    print(label) 