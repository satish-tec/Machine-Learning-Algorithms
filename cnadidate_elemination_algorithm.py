import numpy as np
import pandas as pd

csv_file_data = pd.read_csv("Data1.csv")
# print(csv_file_data)

data = np.array(csv_file_data)
# print(data)

# Separate Features and Labels
X = data[:,:-1] # Features
Y = data[:,-1] # Labels
# print(x)
# print(y)

# Initialize Most General and Most Specific Hypothesis
num_features = X.shape[1] 
# print(num_fearures)
S = ['Ø']*num_features # Most specific hypothesis
G = [['?']*num_features] # Most general hypothesis
# print(S)
# print(G)

# Candidate Elimination Algorithm
for i, x in enumerate(X):
    if Y[i] == 'Yes':  # Positive Example
        for j in range(num_features):
            if S[j] == 'Ø':  # Initialize S
                S[j] = x[j]
            elif S[j] != x[j]:  # Generalize S
                S[j] = '?'
        G = [g for g in G if all(g[j] == '?' or g[j] == x[j] for j in range(num_features))]
    
    else:  # Negative Example
        new_G = []
        for g in G:
            for j in range(num_features):
                if g[j] == '?':
                    g_new = g[:]
                    g_new[j] = S[j]  # Specialize G
                    new_G.append(g_new)
        G = new_G
        G = [g for g in G if not all(g[j] == '?' or g[j] == x[j] for j in range(num_features))]

# Output Final S and G
print("Final Specific Hypothesis (S):", S)
print("Final General Hypothesis (G):", G)
