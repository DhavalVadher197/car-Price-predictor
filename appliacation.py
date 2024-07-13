from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load and clean the data
car = pd.read_csv("Cleaned car.csv")

# Ensure all entries in 'fuel_type' are strings
car['fuel_type'] = car['fuel_type'].fillna('Unknown').astype(str)

@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique(), reverse=True)
    fuel_types = sorted(car['fuel_type'].unique())
    return render_template('index.html', companies=companies, car_models=car_models, years=years, fuel_types=fuel_types)

@app.route('/predict', methods=['POST'])
def predict():
    # Extract form data
    company = request.form.get('Company')
    model = request.form.get('car_model')
    year = request.form.get('Year')
    fuel_type = request.form.get('Fuel_type')
    kilo_driven = request.form.get('kilo_driven')

    # Implement your prediction logic here
    # Example (dummy logic):
    predicted_price = 20000  # Replace with actual prediction logic
    
    return jsonify({"price": predicted_price})

if __name__ == "__main__":
    app.run(debug=True)
