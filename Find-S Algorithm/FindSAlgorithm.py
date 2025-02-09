import numpy as np
import pandas as pd

# Read the data from the CVS file
csv_file_data=pd.read_csv('Data.csv')
#print(csv_file_data)

# Extract all the attribute from the data
# By this way make the 2D array of the data
data=np.array(csv_file_data)
print(data)

# Train the Algorithm
def trainModel(trainingData):
    # Number of features in the data
    n=len(trainingData[0])-1
    print(n)
    # Create Most Specific hypothesis
    specific_hypothesis=['$']*(n)
    print("Most Specific Hypothesis:- ",specific_hypothesis)

    # Create Most General Hypothesis
    general_hypothesis=['?']*(n)

    # Change the hypothesis for the first true case
    for instance in trainingData:
        if instance[-1]=='Yes':
            specific_hypothesis=instance[:-1]
            print("Specific Hypothesis:- ",specific_hypothesis)
            break

    # Now train the algorithm on the remaining data
    for instance in trainingData:
        if instance[-1]=='Yes':
            for i in range(n):
                if(specific_hypothesis[i]!=instance[i]):
                    specific_hypothesis[i]='?'
            print("Hypothesis:- ",specific_hypothesis)

            # It indicates that at this stage our hypothesis is converted into most general hypothesis
            if (specific_hypothesis==general_hypothesis).all():
                break


trainModel(data)