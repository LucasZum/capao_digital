from django.http import HttpResponse
from django.shortcuts import redirect, render

from . import forms


def home(req):
    return render(req, 'pages/home.html')


def register(req):

    register_form_data = req.session.get('register_form_data', None)

    form = forms.RegisterForm(register_form_data)

    return render(req, 'pages/register.html', context={
        'form': form
    })


def create_user(req):

    POST = req.POST

    if not POST:
        return HttpResponse('Erro', status=404)
    
    req.session['register_form_data'] = POST
    form = forms.RegisterForm(POST)

    return redirect('authors:register')