import uvicorn
from fastapi import FastAPI
import numpy as np
import pandas as pd

app = FastAPI()

import pickle


with open("/Users/akshitbansal/Desktop/anomaly-detection-stgi/regressor_model.pkl", 'rb') as file:
    model = pickle.load(file)

@app.get('/')
def index():
    return {'message': 'Hello, Worlddddd'}

@app.post('/detect')
def anomaly_data(Country, Device_Type, Login_Successful, LoginRatio, Final_Browser_Category, Total_Device_Types, Total_IP_Addresses, 
                    Total_Countries, Total_Browser_Categories, Time_Difference_in_sec):
    Country = int(Country)
    Device_Type = int(Device_Type)
    Login_Successful = int(Login_Successful)
    Final_Browser_Category = int(Final_Browser_Category)
    Total_Device_Types = int(Total_Browser_Categories)
    Total_IP_Addresses  = int(Total_IP_Addresses)
    Total_Countries = int(Total_Countries)
    Total_Browser_Categories = int(Total_Browser_Categories)
    LoginRatio = float(LoginRatio)
    Time_Difference_in_sec = float(Time_Difference_in_sec)
    
   
   
   
    input_data = np.array([[Country, Device_Type, Login_Successful, LoginRatio, Final_Browser_Category, Total_Device_Types, Total_IP_Addresses, 
                        Total_Countries, Total_Browser_Categories, Time_Difference_in_sec]])

    result = model.predict(input_data)
    result = float(result[0])

    return{'anomalous_data': result}


