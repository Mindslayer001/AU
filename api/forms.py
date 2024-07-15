from django import forms

materials = {
    ('aluminium','Aluminium'),
    ('cobalt','Cobalt'),
    ('copper','Copper'),
    ('lead','Lead'),
    ('manganese','Manganese'),
}

months = {
    '1': 'January',
    '2': 'February',
    '3': 'March',
    '4': 'April',
    '5': 'May',
    '6': 'June',
    '7': 'July',
    '8': 'August',
    '9': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December',
}

years= {
    ('2021', 'Year 1'),
    ('2022', 'Year 2'),
    ('2023', 'Year 3'),
    ('2024', 'Future'),
}





class getForecast(forms.Form): 
    month = forms.ChoiceField(choices=months, widget=forms.Select(attrs={'class': 'form-control'}))
    year = forms.ChoiceField(choices=years, widget=forms.Select(attrs={'class': 'form-control'}))
    material = forms.ChoiceField(choices=materials, widget=forms.Select(attrs={'class': 'form-control'}))

class RegisterForm(forms.Form): 
    username = forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})) 
    email = forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})) 
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})) 

class LoginForm(forms.Form): 
    email = forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})) 
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})) 

class getComparision(forms.Form):
    month1=forms.ChoiceField(choices=months, widget=forms.Select(attrs={'class': 'form-control'}))
    month2=forms.ChoiceField(choices=months, widget=forms.Select(attrs={'class': 'form-control'}))