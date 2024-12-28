
import streamlit as st
import pickle
import sklearn
import numpy as np
import pandas as pd

st.title("Laptop Price Predictor")

pipe = pd.read_pickle(open('pipe.pkl', 'rb'))
df = pd.read_pickle(open('data.pkl', 'rb'))

# brand
company = st.selectbox('Brand', df['Company'].unique())

# type of laptop
laptop_type = st.selectbox('Type', df['TypeName'].unique())

# Ram
ram = st.selectbox('Ram(in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])

# weight
weight = st.number_input("Weight of the laptop")

# Touchscreen
touchscreen = st.selectbox('TouchScreen', ['NO', 'YES'])

# Touchscreen
ips = st.selectbox('IPS', ['NO', 'YES'])


# Screen size
Screen_size = st.number_input('Screen Size')

# Resolution
resolution = st.selectbox('Screen Resolution', ['1920x1080', '1366x768', '1600x900', '3840x2160', 
                                                '3200x1800','2880x1800', '2560x1600', '2560x1440', 
                                                '2304x1440'])

# CPU
cpu = st.selectbox('CPU', df['Cpu brand'].unique())

# hardware
hdd = st.selectbox('HDD(in GB)', [0, 128, 256, 512, 1024, 2048])
ssd = st.selectbox('SSD(in GB)', [0, 8, 128, 256, 512, 1024])

# GPU
gpu = st.selectbox('GPU', df['Gpu brand'].unique())

# type of OS
os = st.selectbox('Operating System', df['os'].unique())

if st.button('Predict Price'):

    if touchscreen == 'YES':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'YES':
        ips = 1
    else:
        ips = 0
    try:
            if Screen_size > 0 and weight > 0 :
                x_res = int(resolution.split('x')[0])
                y_res = int(resolution.split('x')[1])
                ppi = ((x_res**2) + (y_res**2))**0.5/Screen_size
                query = np.array([company, laptop_type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os], dtype=object)
                query = query.reshape(1, 12)
                st.title("Predicted Price is : ₹ " + str(int(np.exp(pipe.predict(query)))))
                L = int(np.exp(pipe.predict(query)))
                filtered_data = df[(df['Company'] == company) & (df['TypeName'] == laptop_type)  & (df['Ram'] == ram) & (df['Gpu brand'] == gpu) & (df['Cpu brand'] == cpu) & (df['os'] == os)]
                if filtered_data.empty:
                    st.write(" *If you need anything else, you can call our hotline at 0999999999 for information or assistance.")
                else:
                    filtered_data['Price_diff'] = abs(filtered_data['Price'] - L)
                    filtered_data = filtered_data.sort_values(by='Price_diff')
                    st.title("Best laptop recommendations:")
                    option_number = 1
                    for index, row in filtered_data.head(3).iterrows():
                        ips_display1 = 'YES' if row['IPS'] == 1 else 'NO'
                        ips_display2 = 'YES' if row['Touchscreen'] == 1 else 'NO'
                        st.subheader(f"Option {option_number}")
                        st.write(f"Company: {row['Company']}")
                        st.write(f"TypeName: {row['TypeName']}")
                        st.write(f"CPU: {row['Cpu brand']}")
                        st.write(f"RAM: {row['Ram']}")
                        st.write(f"GPU: {row['Gpu brand']}")
                        st.write(f"OpSys: {row['os']}")
                        st.write(f"Weight: {row['Weight']}")
                        st.write(f"HDD: {row['HDD']}")
                        st.write(f"SSD: {row['SSD']}")
                        st.write(f"Touchscreen: {ips_display2}")
                        st.write(f"IPS: {ips_display1}")
                        st.write(f"Price: ₹ {row['Price']}")
                        option_number += 1  
            else:
                st.title("Please fill in all the necessary information.")
    except ZeroDivisionError:
            ppi = None  
     

