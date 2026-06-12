import requests
import pandas as pd
url = "https://api.mfapi.in/mf/125497"

#Get data from API
response=requests.get(url)

#Convert JSON response
data = response.json()

#print available keys
print(data.keys())

#Convert NAV history into DataFrame
df= pd.DataFrame(data['data'])

#show first 5 rows
print(df.head())

#save CSV file
df.to_csv("data/raw/hdfc_top100_nav.csv",index=False)

print("CSV saved successfully!")
