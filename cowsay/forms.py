from django import forms

class Newcowsay(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
