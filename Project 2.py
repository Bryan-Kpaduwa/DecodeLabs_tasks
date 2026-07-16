"""Basic Classification Model

Dataset: Iris (built into scikit-learn) — 150 flower samples,
4 numeric features, 3 species classes. It's small and clean,
making it ideal for learning the basics.

NOTICE: If the program isn't working, it is probably because you don't have the sklearn dataset on ur computer.
to fix it, open cmd as admin and run this command "pip install scikit-learn pandas" then try the code again.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd


def load_and_explore_data():
    """Load the Iris dataset and print a quick summary."""
    data = load_iris()

    # Convert to a DataFrame for easier viewing
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df["species"] = [data.target_names[i] for i in data.target]

    print("=" * 50)
    print("Dataset preview:")
    print(df.head())
    print("\nDataset shape:", df.shape)
    print("\nClass distribution:")
    print(df["species"].value_counts())
    print("=" * 50)

    return data


def split_data(data):
    """Split features and labels into training and testing sets."""
    X = data.data          # features (sepal/petal length & width)
    y = data.target        # labels (species, encoded as 0, 1, 2)

    # 80% training, 20% testing. random_state fixes the shuffle
    # so results are reproducible each time you run the script.
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print(f"\nTraining samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")

    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train):
    """Train a simple K-Nearest Neighbors classifier."""
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test, target_names):
    """Evaluate the trained model on the test set."""
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print("\n" + "=" * 50)
    print(f"Accuracy: {accuracy:.2%}")
    print("\nClassification report:")
    print(classification_report(y_test, predictions, target_names=target_names))
    print("=" * 50)


def main():
    data = load_and_explore_data()
    X_train, X_test, y_train, y_test = split_data(data)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test, data.target_names)


if __name__ == "__main__":
    main()