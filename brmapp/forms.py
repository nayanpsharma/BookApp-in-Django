from django import forms


class NewBookForm(forms.Form):
    title = forms.CharField(max_length=100)
    price = forms.FloatField()
    author = forms.CharField(max_length=100)
    publisher = forms.CharField(max_length=100)



class SearchForm(forms.Form):
    title = forms.CharField( max_length=100)
    


