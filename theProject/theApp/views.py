from django.shortcuts import render
from django.http import HttpResponse
from .models import Mom, Child

# Create your views here.
def index(request):
    return HttpResponse("Test URL")


def getmom(request):
    print('*** in moms ---')
    mummy = Mom.objects.all()
    for eachmom in mummy:
        print(f'MOM: {eachmom.mom_first_name} {eachmom.mom_last_name}')
        for eachchild in Child.objects.filter(child_mom__mom_first_name=eachmom.mom_first_name):
            print('Kid')
    return HttpResponse("mom")


def getchild(request):
    mummy = Mom.objects.all()
    for eachmom in mummy:

        for eachchild in Child.objects.filter(child_mom__mom_first_name=eachmom.mom_first_name):
            print(eachchild.child_first_name)

        print(f'MOM: {eachmom.mom_first_name} {eachmom.mom_last_name}')

    return HttpResponse("child")



    # return HttpResponse("get child")

