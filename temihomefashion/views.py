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


class ContactView(FormView):
    template_name = 'temihomefashion/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)
    

class ContactSuccessView(TemplateView):
    template_name = 'temihomefashion/success.html'

# Create your views here.


