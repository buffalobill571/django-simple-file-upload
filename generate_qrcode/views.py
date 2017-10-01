from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from generate_qrcode.forms import SomeForm
from generate_qrcode.models import Some


@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = SomeForm(request.POST, request.FILES)
        print(form.is_valid())
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('/qr/success/')
    return HttpResponse("ERROR", status=400)


def success(request):
    return HttpResponse('file uploaded')
