# -*- coding: utf-8 -*-
"""bookpredan.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rE5juJbAa-4OcW9c5_6ecc1IrQWQL7BV
"""

import pandas as pd
from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/customer_booking.csv", encoding="ISO-8859-1")
df.head()

"""The `.head()` method allows us to view the first 5 rows in the dataset, this is useful for visual inspection of our columns"""

df.info()

"""The `.info()` method gives us a data description, telling us the names of the columns, their data types and how many null values we have. Fortunately, we have no null values. It looks like some of these columns should be converted into different data types, e.g. flight_day.

To provide more context, below is a more detailed data description, explaining exactly what each column means:

- `num_passengers` = number of passengers travelling
- `sales_channel` = sales channel booking was made on
- `trip_type` = trip Type (Round Trip, One Way, Circle Trip)
- `purchase_lead` = number of days between travel date and booking date
- `length_of_stay` = number of days spent at destination
- `flight_hour` = hour of flight departure
- `flight_day` = day of week of flight departure
- `route` = origin -> destination flight route
- `booking_origin` = country from where booking was made
- `wants_extra_baggage` = if the customer wanted extra baggage in the booking
- `wants_preferred_seat` = if the customer wanted a preferred seat in the booking
- `wants_in_flight_meals` = if the customer wanted in-flight meals in the booking
- `flight_duration` = total duration of flight (in hours)
- `booking_complete` = flag indicating if the customer completed the booking

Before we compute any statistics on the data, lets do any necessary data conversion
"""

df["flight_day"].unique()

mapping = {
    "Mon": 1,
    "Tue": 2,
    "Wed": 3,
    "Thu": 4,
    "Fri": 5,
    "Sat": 6,
    "Sun": 7,
}

df["flight_day"] = df["flight_day"].map(mapping)

df["flight_day"].unique()

df.describe()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
!pip install shap
import shap
!pip install my_module
import sys
sys.path.append('/path/to/my_module')
import my_module
print(hasattr(my_module, "model"))

df.head()

# Define target variable and features
X = df.drop('booking_complete', axis=1)
y = df['booking_complete']

# Convert categorical variables to numerical using Label Encoding
label_encoder = LabelEncoder()
categorical_columns = ['sales_channel', 'trip_type', 'flight_day', 'route', 'booking_origin']

for col in categorical_columns:
    X[col] = label_encoder.fit_transform(X[col])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Classifier
model = RandomForestClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print("Classification Report:\n", classification_report(y_test, y_pred))

# Feature Importance
feature_importances = model.feature_importances_
feature_importance_pairs = list(zip(X.columns, feature_importances))
feature_importance_pairs.sort(key=lambda x: x[1], reverse=True)
print("\nFeature Importances:")
for feature, importance in feature_importance_pairs:
    print(f"{feature}: {importance}")

from sklearn.model_selection import GridSearchCV
# Hyperparameter Tuning (optional)
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3)
grid_search.fit(X_train, y_train)
print("\nBest Hyperparameters:", grid_search.best_params_)

# SHAP (optional for model interpretability)
!pip install shap
import shap
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

import sys
sys.path.append('/path/to/my_module')

# Summary plot to visualize feature importance
shap.summary_plot(shap_values, X_test)