import pandas as pd
import json

df = pd.read_csv('car_detection.csv')

records = df.to_dict(orient='records')

with open('data.json', 'w') as f:
    json.dump(records, f)
