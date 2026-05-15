import pandas as pd
import re

df = pd.read_csv("data/IMDB Dataset.csv")

def clean_text(text):

    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)

    # Remove special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Convert lowercase
    text = text.lower()

    return text

# Apply cleaning
df['clean_review'] = df['review'].apply(clean_text)

print(df[['review', 'clean_review']].head()) 