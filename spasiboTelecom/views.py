from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.
from .settings import DEFAULT_FROM_EMAIL


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Соискатель"
            body = {
                'Фамилия': form.cleaned_data['first_name'],
                'Имя': form.cleaned_data['second_name'],
                'Отчество': form.cleaned_data['last_name'],
                'Почта': form.cleaned_data['email_address'],
                'Телефон': form.cleaned_data['telephone'],
            }
            message = str(body)
            message = message.replace("'", "").replace('{', '').replace('}', '').replace(', ', '\n')
            try:
                send_mail(subject, message, None, ['spasibo.telekom@mail.ru'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect('success')
    form = ContactForm()
    return render(request, "home.html", {'form': form})


def success_view(request):
    return render(request, 'success_view.html')


