from django import forms

class FormFaleConosco(forms.Form):
    nome = forms.CharField(required=True)
    email_origem = forms.EmailField(required=True, label="Entre com seu email: ")
    mensagem = forms.CharField(required=True, widget=forms.Textarea)