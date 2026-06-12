import pandas as pd
import requests
import time
schemes= {
    "SBI Bluechip": 119551,
    "ICICI Bluechip": 120503,
    "Nippon Large Cap": 118632,
    "Axis Bluechip": 119092,
    "Kotak Bluechip": 120841
}
all_dfs=[]
for scheme_name, amfi_code in schemes.items():
    print(f"Fetching {scheme_name}")
    url=f"https://api.mfapi.in/mf/{amfi_code}"
    response=requests.get(url) #calling API 
    data=response.json() #converting to JSON
    df= pd.DataFrame(data["data"])
    df['scheme_name']=scheme_name #to know which row belongs to which fund
    all_dfs.append(df)
    time.sleep(0.5)
all_nav= pd.concat(all_dfs, ignore_index=True) #to combine all 5 dataframes
print(all_nav.head())
print(all_nav.shape)
print(all_nav["scheme_name"].unique())
all_nav.to_csv("data/raw/bluechip_nav_combined.csv",index=False)
print("combined NAV file saved successfully!")
