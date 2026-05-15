import pandas as pd
from transformers import pipeline
from sklearn.metrics import accuracy_score

classifier = pipeline("sentiment-analysis")

df = pd.read_csv("data/IMDB Dataset.csv")

# Small sample
df = df.head(20)

predictions = []

for review in df['review']:

    result = classifier(review[:512])

    label = result[0]['label'].lower()

    predictions.append(label)

accuracy = accuracy_score(df['sentiment'], predictions)

print("Accuracy:", accuracy) 