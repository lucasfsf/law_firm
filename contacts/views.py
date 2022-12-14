from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from .forms import ContactForm

from articles.company_fields import default_company_values

context = default_company_values

def contact(request):
    
    if request.method != 'POST':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():

            # TODO You might want to update the text based on your language. I.E  "Artigos"/"Articles"
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'phone': form.cleaned_data['phone'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                # TODO You might want to update the text based on your language. I.E  "Artigos"/"Articles"
                return HttpResponse('Invalid header found.')
            return redirect("articles:index")
    context['form'] = form
    return render(request, "contacts/contact_form.html", context)

