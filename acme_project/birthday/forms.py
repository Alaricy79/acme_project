from django import forms


from .models import Birthday


class BirthdayForm(forms.ModelForm):
    birthday = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Birthday
        fields = '__all__'  
