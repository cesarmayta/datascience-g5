import joblib
import numpy as np
import pandas as pd
import sklearn

model = joblib.load('./model/model.pkl')
scaler_X = joblib.load('./model/scaler_X.pkl')
scaler_y = joblib.load('./model/scaler_y.pkl')

new_car_data_raw = {
    'fuel': ['Gasolina'],
    'location': ['Lima'],
    'brand': ['AUDI'],
    'year': [2023],
    'subcategory': ['Camioneta'],
    'transmission': ['Automática - Secuencial']
}

# Create a DataFrame from the new data
new_df_raw = pd.DataFrame(new_car_data_raw)

# Apply the same 'year' transformation as the original DataFrame
new_df_raw['year'] = new_df_raw['year'] / 1000

# Apply one-hot encoding using the same columns as the training data
# We need to ensure the new data has the exact same columns as the training data (X).
# First, get dummy variables for the new data.
new_df_encoded_temp = pd.get_dummies(new_df_raw, columns=['fuel','location','brand','subcategory','transmission'])

# Get the list of columns used during training (all columns in df_encoded minus 'price')
training_features = ['year', 'fuel_Diesel', 'fuel_Gasolina', 'fuel_electrico', 'fuel_gas',
       'fuel_hibrido', 'location_Ancash', 'location_Arequipa',
       'location_La Libertad', 'location_Lima', 'location_Piura',
       'brand_ASTON MARTIN', 'brand_AUDI', 'brand_BAIC', 'brand_BMW',
       'brand_CHANGAN', 'brand_CHERY', 'brand_CHEVROLET', 'brand_CITROEN',
       'brand_CUPRA', 'brand_DFSK', 'brand_DODGE', 'brand_DONGFENG',
       'brand_DS', 'brand_FIAT', 'brand_FORD', 'brand_GAC', 'brand_GEELY',
       'brand_HAVAL', 'brand_HONDA', 'brand_HYUNDAI', 'brand_JAC',
       'brand_JAGUAR', 'brand_JEEP', 'brand_JETOUR', 'brand_JMEV', 'brand_KIA',
       'brand_LAND ROVER', 'brand_LEXUS', 'brand_LOTUS', 'brand_MASERATI',
       'brand_MAZDA', 'brand_MERCEDES BENZ', 'brand_MG', 'brand_MINI',
       'brand_MITSUBISHI', 'brand_NISSAN', 'brand_OTROS', 'brand_PEUGEOT',
       'brand_PORSCHE', 'brand_RAM', 'brand_RENAULT', 'brand_SEAT',
       'brand_SOUEAST', 'brand_SSANGYONG', 'brand_SUBARU', 'brand_SUZUKI',
       'brand_TOYOTA', 'brand_VOLKSWAGEN', 'brand_VOLVO',
       'subcategory_Camioneta', 'subcategory_Deportivo',
       'subcategory_Hatchback', 'subcategory_Pick Up', 'subcategory_Sedán',
       'subcategory_Station Wagon', 'subcategory_Vans',
       'transmission_Automática', 'transmission_Automática - Secuencial',
       'transmission_Mecánica']

# Reindex the new data's encoded DataFrame to match the training features.
# Any column present in training_features but not in new_df_encoded_temp will be added with 0.
# Any column in new_df_encoded_temp not in training_features will be dropped.
new_data_processed = new_df_encoded_temp.reindex(columns=training_features, fill_value=0)

# Convert boolean columns to int if any are still present (for consistency)
for col in new_data_processed.columns:
    if new_data_processed[col].dtype == 'bool':
        new_data_processed[col] = new_data_processed[col].astype(int)

# Scale the new data using the same scaler (scaler_X) fitted on the training data
new_data_scaled = scaler_X.transform(new_data_processed.values)

# Use the best model (SVR) to make a prediction
predicted_price_scaled = model.predict(new_data_scaled)

# Inverse transform the prediction to get the price in its original scale
predicted_price = scaler_y.inverse_transform(predicted_price_scaled.reshape(-1, 1))

# Print the predicted price
print(f"Predicted price for the new car (in 10,000s units): {predicted_price[0][0]:.2f}")
print(f"Predicted price for the new car (original currency units): {predicted_price[0][0] * 10000:.2f}")
