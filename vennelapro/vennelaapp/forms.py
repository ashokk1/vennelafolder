from django import forms
class ContactForm(forms.Form):
    fname=forms.CharField(label='FirstName',
                          widget=forms.TextInput(
                              attrs={
                                  'class':'form-control',
                                  'placeholder':'Enter your First Name'
                              }
                          )
                          )
    lname=forms.CharField(label='LastName',
                          widget=forms.TextInput(
                              attrs={
                                  'class':'form-control',
                                  'placeholder':'Enter your Last Name'
                              }
                          )
                          )
    username=forms.CharField(label='UserName',
                          widget=forms.TextInput(
                              attrs={
                                  'class':'form-control',
                                  'placeholder':'Enter your user Name'
                              }
                          )
                          )
    email=forms.EmailField(label='Email Id',
                          widget=forms.EmailInput(
                              attrs={
                                  'class':'form-control',
                                  'placeholder':'Enter your email id'
                              }
                          )
                          )
    password=forms.CharField(label='Password',
                          widget=forms.PasswordInput(
                              attrs={
                                  'class':'form-control',
                                  'placeholder':'Enter your Password'
                              }
                          )
                          )
    mobile=forms.IntegerField(label='Mobile',
                          widget=forms.NumberInput(
                              attrs={
                                  'class':'form-control',
                                  'placeholder':'Enter your mobile number'
                              }
                          )
                          )