# IMDb Movie Review Sentiment Analysis using Transformers

## Project Overview

This project is an NLP-based Sentiment Analysis system built using Hugging Face Transformers and the IMDb Movie Reviews Dataset.

The model predicts whether a movie review is:

- Positive
- Negative

The project uses a pretrained DistilBERT transformer model and fine-tunes it on IMDb movie review data.

---

# Technologies Used

- Python
- Hugging Face Transformers
- DistilBERT
- PyTorch
- Pandas
- Scikit-learn
- Streamlit

---

# Project Type

- NLP Project
- Transformer Project
- Sentiment Analysis Project
- Fine-Tuning Project
- Streamlit Deployment Project

---

# Project Structure

```text
imdb_transformer_project/
│
├── data/
│   └── IMDB Dataset.csv
│
├── models/
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── predict.py
│   └── app.py
│
├── requirements.txt
└── README.md
```

---

# Dataset

Dataset Used:
IMDb Movie Reviews Dataset

Dataset contains:
- Movie reviews
- Sentiment labels

Example:

| Review | Sentiment |
|---|---|
| This movie was amazing | positive |
| Worst movie ever | negative |

---

# Workflow

```text
Load Dataset
      ↓
Preprocess Text
      ↓
Convert Labels
      ↓
Train-Test Split
      ↓
Tokenization
      ↓
Fine-Tune DistilBERT
      ↓
Evaluate Model
      ↓
Save Model
      ↓
Build Streamlit App
      ↓
Deploy Project
```

---

# Preprocessing Steps

The following preprocessing steps were performed:

- Removed HTML tags
- Removed special characters
- Converted text to lowercase

---

# Why DistilBERT?

DistilBERT was selected because:

- Lightweight model
- Faster training
- Less memory usage
- Good accuracy
- Beginner-friendly

---

# Tokenization

Tokenizer converts text into numerical token IDs.

Example:

```text
"This movie is good"
        ↓
[101, 2023, 3185, 2003]
```

Transformers understand numbers, not raw text.

---

# Fine-Tuning

The pretrained DistilBERT model was fine-tuned on the IMDb dataset.

Fine-tuning helps the model learn movie-review-specific sentiment patterns.

---

# Model Training

Training was performed using Hugging Face Trainer API.

Important training parameters:

- Epochs: 1
- Batch Size: 8
- Evaluation Strategy: Epoch

---

# Evaluation

Model performance was evaluated using accuracy metrics.

The model predicts:
- Positive sentiment
- Negative sentiment

---

# Streamlit Web Application

A Streamlit web application was created for real-time sentiment prediction.

User can:
1. Enter movie review
2. Click Predict
3. View sentiment result

Run application:

```bash
streamlit run app.py
```

---

# Installation

Clone repository:

```bash
git clone <repository_link>
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

## Windows

```bash
venv\Scripts\activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

---

# Training Model

Run:

```bash
python src/train.py
```

---

# Prediction

Run:

```bash
python src/predict.py
```

---

# Deployment

Deployment platforms:

- Streamlit Cloud
- Hugging Face Spaces

---

# Future Improvements

- Multi-class sentiment analysis
- Better preprocessing
- GPU training
- FastAPI integration
- Docker deployment

---

# Learning Outcomes

Through this project, I learned:

- NLP basics
- Transformers
- Tokenization
- Fine-tuning
- Hugging Face
- Streamlit deployment
- Model evaluation

---

# Author

Aswani
