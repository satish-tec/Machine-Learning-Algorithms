import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
import matplotlib.pyplot as plt

# Training dataset
data = {
    'Type': ['HipHop', 'Rock', 'Rock', 'HipHop', 'Jazz', 'Rock', 'Jazz', 'Jazz', 'HipHop', 'Jazz', 'Rock', 'Jazz', 'Rock'],
    'Price': ['Expensive', 'Cheap', 'Expensive', 'Cheap', 'Cheap', 'Expensive', 'Expensive', 'Cheap', 'Expensive', 'Expensive', 'Expensive', 'Cheap', 'Expensive'],
    'Buy': ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No']
}

df = pd.DataFrame(data)

# Convert categorical variables to numerical values
df['Type'] = df['Type'].map({'Rock': 0, 'Jazz': 1, 'HipHop': 2})
df['Price'] = df['Price'].map({'Cheap': 0, 'Expensive': 1})
df['Buy'] = df['Buy'].map({'No': 0, 'Yes': 1})

# Splitting features and target variable
X = df[['Type', 'Price']]
y = df['Buy']

# Train Decision Tree Classifier
dt = DecisionTreeClassifier(criterion='entropy')
dt.fit(X, y)

# Visualizing the decision tree
plt.figure(figsize=(10, 6))
plot_tree(dt, feature_names=['Type', 'Price'], class_names=['No', 'Yes'], filled=True, rounded=True)
plt.show()

# Print decision rules
print(export_text(dt, feature_names=['Type', 'Price']))

# Test dataset
test_data = {
    'Type': ['Rock', 'Jazz', 'Jazz', 'Rock', 'HipHop'],
    'Price': ['Cheap', 'Cheap', 'Expensive', 'Expensive', 'Expensive'],
    'Buy': ['Yes', 'No', 'No', 'Yes', 'Yes']  # Actual values
}

test_df = pd.DataFrame(test_data)
test_df['Type'] = test_df['Type'].map({'Rock': 0, 'Jazz': 1, 'HipHop': 2})
test_df['Price'] = test_df['Price'].map({'Cheap': 0, 'Expensive': 1})

y_pred = dt.predict(test_df[['Type', 'Price']])
accuracy = (y_pred == test_df['Buy'].map({'No': 0, 'Yes': 1})).mean()

print(f"Model Accuracy: {accuracy * 100:.2f}%")
