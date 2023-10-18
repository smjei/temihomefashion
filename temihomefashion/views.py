from django.shortcuts import render, get_object_or_404
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View
from django.contrib import messages
from django.core.mail import send_mail
from django.views import generic
from django.conf import settings



# Create your views here.
def index(request):
   return render(request, 'temihomefashion/index.html')


def sam404(request):
   return render(request, 'temihomefashion/e404.html')
