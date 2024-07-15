from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import io
import urllib, base64
from .forms import getForecast, getComparision

model = joblib.load('test/xgb_model.pkl')
le = joblib.load('test/label_encoder.pkl')



def predict_volume(year, month, material, model, le):
    # Create a DataFrame for the input data
    input_data = pd.DataFrame({
        'YEAR': [year],
        'Month': [month],
        'Material': [material]
    })

    # Encode the material
    try:
        input_data['Material'] = le.transform(input_data['Material'])
    except ValueError:
        # Handle unseen materials
        print(f"Material '{material}' is not recognized. Please provide a known material.")
        return None

    # Predict the volume
    predicted_volume = model.predict(input_data)

    return predicted_volume[0]





# Load the dataset for visualization purposes
data = pd.read_csv('data.csv')


def index(request):
    return render(request,"api/homepage.html")

def comparemonths(month1,month2):
    
    material = ['aluminium','cobalt','copper','lead','manganese']
    m1=[]
    m2=[]
    for i in range(5):
        input_data_month1 = pd.DataFrame({
            'YEAR': [2024],
            'Month': [month1],
            'Material': [material[i]]
        })
        m1.append(model.predict(input_data_month1))
        input_data_month2 = pd.DataFrame({
            'YEAR': [2024],
            'Month': [month2],
            'Material': [material[i]]
        })
        m2.append(model.predict(input_data_month2))
        data=list(m1,m2)
        print(data)
    return data


def compare(request):
    global model, le  # Assuming model and le are defined and loaded
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    if request.method == 'POST':
        form = getComparision(request.POST)
        if form.is_valid():
            month1 = form.cleaned_data['month1']
            month2 = form.cleaned_data['month2']

            # Perform prediction using model and le
            month1 = int(month1)
            month2 = int(month2)
            context = {
                "m1":months[month1-1],
                "m2":months[month2-1]
            }

            return render(request, "api/comparemon.html",context)

    else:
        form = getComparision()

    return render(request, 'api/index1.html', {'form': form})






def forecast(request):
    global model, le  # Assuming model and le are defined and loaded

    if request.method == 'POST':
        form = getForecast(request.POST)
        if form.is_valid():
            month = form.cleaned_data['month']
            year = form.cleaned_data['year']
            material = form.cleaned_data['material']

            # Perform prediction using model and le
            year = int(year)
            month = int(month)
            material = str(material)
            predicted_volume = predict_volume(year, month, material, model, le)

            return HttpResponse(f'<h1>Predicted Volume: {predicted_volume}</h1>')

    else:
        form = getForecast()

    return render(request, 'api/index.html', {'form': form})




def dash(request):
    return render(request, "api/dashboard.html")