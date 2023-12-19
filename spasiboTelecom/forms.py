from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=30, min_length=2)
    second_name = forms.CharField(max_length=30, min_length=2)
    last_name = forms.CharField(max_length=50, min_length=2)
    email_address = forms.EmailField(max_length=50,min_length=5, help_text='Укажите действующий Email')
    telephone = forms.CharField(max_length=16, min_length=5, help_text='Укажите номер в формате: +7 000 000-00-00')
