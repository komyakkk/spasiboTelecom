from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.


def mainPage(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Пробное сообщение"
            body = {
                'Фамилия': form.cleaned_data['first_name'],
                'Имя': form.cleaned_data['second_name'],
                'Отчество': form.cleaned_data['last_name'],
                'очта': form.cleaned_data['email_address'],
                'telephone': form.cleaned_data['telephone'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message,
                          'admin@example.com',
                          ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect("main:mainPage")
    form = ContactForm()
    return render(request, "contact.html", {'form': form})