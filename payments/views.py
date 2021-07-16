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
        name = request.POST.get('Name')
        message = "This is a confirmation mail regarding the payment of "+content+"$ from "+name+"\n\n \t \t Thank you for the payment!"
        #print(to,content)
        send_mail(
            #subject
            "PAYMENT RECIEVED FROM "+ name.upper(),
            #msg
            message,
            #from email
            settings.EMAIL_HOST_USER,
            #rec_list
            [to]
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
