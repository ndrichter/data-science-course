# Classification
## Introduction
- Supervised learning approach to categorize unknown items into a discrete set of categories or classes
- Target attribute is a categorical variable
- Can be binary or multi-class
- Churn detection, customer category, customer responses, email spam filter
- Types:
  - Decision trees
  - Naive bayes
  - K Nearest Neighbor
  - Neural networks

## K-Nearest Neighbors
- Analyzing scatter plot to see closest neighboring data points fit best for predictor
- Classifies cases based on their similarity to other cases
- Algorithm
  - Pick value for k
  - Calculate distance of unknown case from all cases
  - Select k observations in the training data that are nearest to the unknown data point
  - Predict response of unknown data point using most popular response value from k nearest neighbors
- Choosing best value for k
  - Low value could result in over fit
  - High value overly generalizes
  - Test for accuracy in test set
- Can also be used for regression for computing continuous targets

## Evaluation Metrics in Classification
- Jaccard index
  - Comparing intersection actual labels vs predicted labels
  - 0 to 1, higher is more accurate
- F1-Score
  - Comparing confusion matrix of actual/predicted labels
  - Precision and recall scores using true/false positives/negatives
  - F1 uses these, and calculates from 0 to 1
- Log Loss
  - Performance of classifier where the predicted output is a probability value between 0 and 1
  - Want closer to 0 for better accuracy (less log loss)

## Intro to Decision Trees
- Split training set into distinct nodes
- Each internal node corresponds to a test
- Each branch corresponds to a result of the test
- Each leaf node assigns a classification
- Algorithm
  - Choose attribute from your dataset
  - Calculate the significance of attribute in splitting of data
  - Split data based on the value of the best attribute
  - Go to step 1 for another branch

## Building Decision Trees
- Use recursive partitioning to classify
- Which attribute is best?
  - Look for more predictiveness, less impurity and lower entropy
- Entropy
  - Measure of randomness or uncertainty in the data
  - The lower the entropy, the less uniform the distribution, the purer the node
  - 0 to 1, want lower
- Information gain
  - Information that can increase the level of certainty after splitting
  - Information gain = (entropy before split) - (weighted entropy after split)