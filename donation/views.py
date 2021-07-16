from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def index(request):
    return render(request, 'payments/index.html')

def gateway(request):
    return render(request, 'payments/gateway.html')

def sendanemail(request):
    if request.method == "POST":
        to = request.POST.get('toemail')
        content = request.POST.get('content')
        print(to,content)
        HOST = 'saakethsai2@gmail.com'
        send_mail(
            #subject
            "testing",
            #msg
            content,
            #from email
            HOST,
            #rec_list
            to
        )
        return render(
        request,
        'payments/email.html',
        {
            'title':'send an email'
        }
    )
    else:
        return render(
            request,
            'payments/email.html',
            {
                'title': 'send an email'
            }
        )
