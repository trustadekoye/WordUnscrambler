from django import forms

class WordForm(forms.Form):
    scrambled_word = forms.CharField(label='Scrambled Word', max_length=100)