from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load data
iris = load_iris()
X, y = iris.data, iris.target

# Split - 80% learn, 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training on {len(X_train)} samples, Testing on {len(X_test)} samples")

# Build AI Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict
preds = model.predict(X_test)
acc = accuracy_score(y_test, preds)

print(f"\n✅ First AI Model Accuracy: {acc*100:.2f}%")
print("You just built an AI that predicts!")

# Try your own prediction
sample = [[5.1, 3.5, 1.4, 0.2]] # setosa flower
prediction = model.predict(sample)
print(f"\nPrediction for {sample}: {iris.target_names[prediction[0]]}")