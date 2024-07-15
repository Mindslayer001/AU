import joblib
import pandas as pd

# Load the saved model and label encoder
model = joblib.load('xgb_model.pkl')
le = joblib.load('label_encoder.pkl')

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

# Example usage
year = 2024
month = 5
material = 'lead'

predicted_volume = predict_volume(year, month, material, model, le)
if predicted_volume is not None:
    print(f'Predicted Volume for {material} in {year}-{month:02}: {predicted_volume}')

def login(request):
    global dict
    error=''
    data = {}
    isLogged = False
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(dict)
            
            try:
                data = users_collection.find_one({'email': email})
                if data.get('password') == password:
                    data['userId'] = str(data['_id'])
                    print(data)

                    dict = {
                    'userId': data['userId'],
                    'username': data["username"],
                    'email': data["email"],
                    'password': data["password"],
                    'usertype': data["usertype"],
                    'gender':data['gender'],
                    'age':data['age'],
                    'weight' : data['weight'],
                    'height':data['height'],
                    'bmi': data['bmi'],
                    'status':data['status'],
                    "isLogged" :True,
                    }
                    print('This is Dict')
                    print(dict)
                
                else:
                    form = LoginForm()
                    error = 'Wrong credentials. Please try again.'
                    
            except:
                form = LoginForm()
                error = 'User not found!! Please try again.'
        else:
            form = LoginForm()
            error = 'Wrong credentials. Please try again.'
    else:
        form = LoginForm()
    
    context = {'form': form, 'dict': dict, 'data': data, 'error': error}
    return render(request, 'nutritionAssistance/login.html', context)
