import numpy as np
import pandas as pd
import nltk
import matplotlib.pyplot as plt
from datetime import datetime
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score

# Download required NLTK data
nltk.download('stopwords')
nltk.download('punkt')


def load_and_preprocess_data():
    # Load dataset
    df = pd.read_csv(r'C:\Users\aksha\PycharmProjects\M_D_threat_dectection\myapp\static\email.csv', encoding='latin1')

    # Drop unnecessary columns safely
    df.drop(columns=['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], inplace=True, errors='ignore')

    # Rename columns for clarity
    df.rename(columns={'Category': 'target', 'Message': 'text'}, inplace=True)

    # Convert target labels to numeric values
    df['target'] = df['target'].map({'ham': 0, 'spam': 1})

    # Handle missing values and convert types
    df.dropna(subset=['target', 'text'], inplace=True)
    df['target'] = df['target'].astype(int)
    df['text'] = df['text'].astype(str)
    df.drop_duplicates(inplace=True)

    return df


# Initialize stemmer
ps = PorterStemmer()


def transform_text(text):
    # Ensure text is a string
    if not isinstance(text, str):
        text = str(text)

    text = text.lower()
    text = nltk.word_tokenize(text)
    text = [word for word in text if word.isalnum()]
    text = [word for word in text if word not in stopwords.words('english')]
    text = [ps.stem(word) for word in text]
    return " ".join(text)


def train_model():
    # Load and preprocess data
    df = load_and_preprocess_data()

    # Apply text transformation
    df['transformed_text'] = df['text'].apply(transform_text)

    # Vectorization using TF-IDF
    tfid = TfidfVectorizer(max_features=3000)
    X = tfid.fit_transform(df['transformed_text']).toarray()
    y = df['target'].values

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

    # Train Random Forest Classifier
    rfc = RandomForestClassifier(n_estimators=50, random_state=2)

    rfc.fit(X_train, y_train)

    # Model evaluation
    y_pred = rfc.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")

    return tfid, rfc


# Train the model and get components
tfid, rfc = train_model()


def predict_spam(message):
    try:
        transformed_message = transform_text(message)
        vectorized_message = tfid.transform([transformed_message]).toarray()
        prob = rfc.predict_proba(vectorized_message)[0][1] * 100  # Convert to percentage

        if prob < 40:
            risk_level = "Low Risk"
        elif prob < 70:
            risk_level = "Medium Risk"
        else:
            risk_level = "High Risk"

        prediction = "Spam" if prob >= 50 else "Not Spam"
        result = f"Prediction: {prediction} (Risk Level: {risk_level}, Probability: {prob:.2f}%)"

        # Visualization
        plt.figure(figsize=(6, 4))
        plt.plot([0, 40, 70, 100], [0, 1, 2, 3], marker='o', linestyle='-', color='b')
        plt.axvline(x=prob, color='r', linestyle='--', label=f'Probability: {prob:.2f}%')
        plt.xticks([0, 40, 70, 100], ['0%', '40%', '70%', '100%'])
        plt.yticks([0, 1, 2, 3], ['No Risk', 'Low Risk', 'Medium Risk', 'High Risk'])
        plt.xlabel('Spam Probability')
        plt.ylabel('Risk Level')
        plt.title('Spam Risk Level Visualization')
        plt.legend()

        date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        image_path = "C:\\Users\\aksha\\PycharmProjects\\M_D_threat_dectection\\media\\emgraph" + date
        plt.savefig(image_path)
        plt.close()  # Close the figure to free memory

        return result, date
    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        return f"Error: {str(e)}", ""
