from django import forms

from .models import profiles,User


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = profiles
        exclude=(
        'id','Username','User',
        )


class LoginForm(forms.Form):
    username=forms.CharField(
        max_length=50,
        label="UserName",
    )
    password=forms.CharField(
        label="Password",
        widget=(forms.PasswordInput)
    )
    
class RegisterForm(forms.Form):
    username=forms.CharField(
        max_length=50,
        label="UserName",
    )
    password1=forms.CharField(
        label="Password",
        required=False,
       widget=(forms.PasswordInput),
    )
    password2=forms.CharField(
        label="Confirm Password",
        required=False,
       widget=(forms.PasswordInput),

    )
    def clean(self):
        cleaned_username = self.cleaned_data["username"]
        cleaned_password = self.cleaned_data["password1"]
        if User.objects.filter(username=cleaned_username):
            raise forms.ValidationError('Username already exists,Please try another')
        if cleaned_password == '':
            print('done')
            raise forms.ValidationError('Password Cannot be Blank')
        if self.cleaned_data["password1"] != self.cleaned_data["password2"]:
            raise forms.ValidationError('passwords don\'t match')
        
        
