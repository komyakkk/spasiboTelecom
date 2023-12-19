from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=30, min_length=2, required=True)
    second_name = forms.CharField(max_length=30, min_length=2, required=True)
    last_name = forms.CharField(max_length=50, min_length=2, required=True)
    email_address = forms.EmailField(max_length=50,min_length=5, help_text='Укажите действующий Email', required=True)
    telephone = forms.CharField(max_length=16, min_length=5, help_text='Укажите номер в формате: +7 000 000-00-00', required=True)
