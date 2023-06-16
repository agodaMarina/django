from django import forms
from Blog.models import Articles


class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = '__all__'
