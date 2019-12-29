from django import forms


class SearchForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Name of the person you're looking for",
        })
    )


class DateRangeForm(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()