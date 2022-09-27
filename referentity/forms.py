from django import forms

class ReferralForm(forms.Form):
    name=forms.CharField(label='Your name', max_length=100,required=False)
    phonenumber=forms.CharField(label='Your phonenumber', max_length=12,required=False)
    city=forms.CharField(label='Your city', max_length=100,required=False)
    code=forms.CharField(label='Your code', max_length=10,required=False)
