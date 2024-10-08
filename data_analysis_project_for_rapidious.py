
"""Data Analysis Project for Rapidious.ipynb"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset

dishes_data = pd.read_csv('Food_Recipes_Data.csv')


## DATA CLEANING PROCESS ##

# Check for missing values
missing_values = dishes_data.isnull().sum()

# Fill missing values with the median
dishes_data['calories'].fillna(dishes_data['calories'].median(), inplace=True)
dishes_data['protein'].fillna(dishes_data['protein'].median(), inplace=True)
dishes_data['fat'].fillna(dishes_data['fat'].median(), inplace=True)
dishes_data['sodium'].fillna(dishes_data['sodium'].median(), inplace=True)

# Check for duplicate entries
dishes_data.drop_duplicates(inplace=True)

# Filter for highly rated recipes
highly_rated_recipes = dishes_data[dishes_data['rating'] >= 4.0]
highly_rated_recipes

# List of ingredient columns (ingredients start at column 7)
ingredient_columns = dishes_data.columns[7:]  # Adjust index as necessary
ingredient_count_high_rated = highly_rated_recipes[ingredient_columns].sum().sort_values(ascending=False)

# Display the top 10 most common ingredients in highly rated recipes
top_10_ingredients = ingredient_count_high_rated.head(10)

# Plot the bar chart
plt.figure(figsize=(8, 5))
ax = top_10_ingredients.plot(kind='bar', color='green')
plt.title('Top 10 Most Common Ingredients in Highly Rated Recipes', fontsize=15 , color='red')
plt.xlabel('Ingredients', fontsize=10)
plt.ylabel('Count', fontsize=10)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Define preparation-related columns, including time-related and nutrition-related factors
prep_columns = ['22-minute meals', 'advance prep required', 'calories', 'protein', 'fat', 'sodium']

# Calculate the correlation matrix between the preparation-related columns and the rating
correlation_prep_ratings = dishes_data[prep_columns + ['rating']].corr()

#  Heatmap to visualize correlations Data
sns.heatmap(correlation_prep_ratings, annot=True, cmap='coolwarm')
plt.title('Correlation between Preparation Time and Ratings')
plt.show()
