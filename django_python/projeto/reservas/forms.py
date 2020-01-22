from django import forms

class formContato(forms.Form):
    email = forms.EmailField()
    assunto = forms.CharField(label='Assunto', max_length=150)
    comentarios = forms.CharField(label='Comentarios', widget= forms.Textarea)