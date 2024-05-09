---

# Customer Booking Prediction Notebook

This notebook contains code for analyzing a dataset of customer bookings and building a predictive model to predict whether a booking will be completed or not.

## Getting Started

To run this notebook, you'll need Python installed on your machine, along with Jupyter Notebook or another compatible environment. You'll also need the necessary libraries installed, which are listed in the requirements.txt file.

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Jupyter Notebook
- Required libraries (install using `pip install -r requirements.txt`)

### Installing

Clone this repository to your local machine:

```
git clone https://github.com/yourusername/customer-booking-prediction.git
```

Navigate to the project directory:

```
cd customer-booking-prediction
```

Start Jupyter Notebook:

```
jupyter notebook
```

Open the notebook `bookpredan.ipynb` and execute the cells to run the code.

## Dataset

The dataset used in this notebook (`customer_booking.csv`) contains information about customer bookings, including various features such as sales channel, trip type, flight details, booking origin, etc. The target variable is `booking_complete`, indicating whether the booking was completed or not.

## Analysis and Modeling

The notebook performs the following tasks:

1. Data loading and inspection
2. Data preprocessing
3. Model training using Random Forest Classifier
4. Evaluation of model performance
5. Feature importance analysis
6. Hyperparameter tuning (optional)
7. Model interpretability using SHAP (optional)

## Authors

- Pascal Obala (@pascalobala9@gmail.com)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---