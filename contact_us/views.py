from django.shortcuts import render, redirect
from .forms import ContactForm
# for email
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
# Create your views here.
def contactViews(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            email_subject = form.cleaned_data['sub']
            print(name, from_email, content)

            email_subject = email_subject
            email_body = render_to_string('mail.html', {'name':name, 'from_email':from_email, 'content':content})

            email = EmailMultiAlternatives(email_subject, '', from_email, to=['hmnizum1714032@gmail.com'])
            email.attach_alternative(email_body, "text/html")
            email.send()

            
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})