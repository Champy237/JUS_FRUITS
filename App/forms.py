from django import forms 
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class jusModelForm(forms.ModelForm):
    class Meta:
        model = jus
        fields = ['name','price']




class InstriptionForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class  Meta:
        model = User
        fields = ['username','email','password1','password2',]

# class InscriptionForm ( UserCreationForm ) :
# 6
# email = forms . EmailField ( required = True )
# 5
# 7
# 8
# 9
# 10
# class Meta :
# model = User
# fields = [ ’ username ’ , ’ email ’ , ’ password1 ’ , ’

# class ArticleModelForm ( forms . ModelForm ) :
# class Meta :

# model = Article

# fields = [ ’ titre ’ , ’ contenu ’]
# # Ou utilisez ’ __all__ ’ pour inclure tous les champs
# # fields = ’ __all__ ’
# # Personnalisation des widgets
# widgets = {
# ’ titre ’: forms . TextInput ( attrs ={ ’ class ’: ’ form -
# control ’}) ,
# ’ contenu ’: forms . Textarea ( attrs ={ ’ class ’: ’ form -
# control ’ , ’ rows ’: 5}) ,
# }
# # Personnalisation des labels
# labels = {
# ’ titre ’: ’ Titre de l \ ’ article ’ ,
# ’ contenu ’: ’ Contenu de l \ ’ article ’ ,
# }
# # Personnalisation des messages d ’ erreur
# error_messages = {
# ’ titre ’: {
# ’ max_length ’: ’ Le titre est trop long . ’ ,