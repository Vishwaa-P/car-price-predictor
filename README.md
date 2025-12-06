# Car Price Predictor

This project is a Car Price Predictor web application. It estimates the market value of a used car based on five key factors:
- **Company (Manufacturer)**
- **Car Model (Specific Name)**
- **Year of Purchase**
- **Fuel Type (Petrol, Diesel, LPG)**
- **Kilometers Driven**

## Demo
Runs locally as a Streamlit web app. Users select car features from dropdown menus and click "Predict Price" to see the result.

## Installation

**Step 1:** Clone the repository.

```bash
git clone https://github.com/Vishwaa-P/car-price-predictor.git
cd car-price-predictor
```

**Step 2:** Install the required Python packages.

```bash
pip install streamlit pandas numpy scikit-learn
```

## Usage

1. Make sure you're in the project folder.
2. Run the app with Streamlit:

```bash
streamlit run app.py
```

3. The app usually opens at [http://localhost:8501](http://localhost:8501).
4. Fill in the car details and click "Predict Price" to see the estimated market value.

## Project Structure

- `app.py` - Main file for the Streamlit web interface.
- `main.ipynb` - Jupyter Notebook used for data cleaning and model training.
- `LinearRegressionModel.pkl` - Saved Scikit-Learn model (pipeline with encoder and regressor).
- `Cleaned Car.csv` - Cleaned dataset for dropdowns and model input.
- `quikr_car.csv` - Original raw dataset for reference.

## Model Details

- **Algorithm:** Linear Regression
- **Pipeline:** OneHotEncoder (categorical features) + Linear Regression (numerical prediction)
- **Optimization:** Multiple random states are tested to maximize R² score during train-test split.

## Data

Both datasets are included:
- `quikr_car.csv`: Raw data from Quikr
- `Cleaned Car.csv`: Cleaned, processed dataset

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Fork this repository and submit a Pull Request.

## Contact

Maintained by [Vishwaa-P](https://github.com/Vishwaa-P)
