from django import forms


class PostForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    content = forms.CharField(label='Text')
    image = forms.ImageField(label='Image')
