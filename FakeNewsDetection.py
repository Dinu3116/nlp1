import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Sample data for illustration
data = {
    'text': ['Real news example', 'Fake news example', 'Another real news', 'Yet another fake news'],
    'label': [1, 0, 1, 0]  # 1 for real news, 0 for fake news
}

df = pd.DataFrame(data)

# Split the data into training and testing sets
train_data, test_data, train_labels, test_labels = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# Convert the text data into TF-IDF features
vectorizer = TfidfVectorizer()
train_features = vectorizer.fit_transform(train_data)
test_features = vectorizer.transform(test_data)

# Train a Random Forest classifier
classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(train_features, train_labels)

# Make predictions on the test set
predictions = classifier.predict(test_features)

# Evaluate the model
accuracy = accuracy_score(test_labels, predictions)
report = classification_report(test_labels, predictions)

print(f"Accuracy: {accuracy}")
print("Classification Report:\n", report)
