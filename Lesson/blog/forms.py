from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, label='Тема обращения', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email_address = forms.EmailField(max_length=150, label='Ваша почта', widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), max_length=2000, label='Текст обращения')
