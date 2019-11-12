from django.shortcuts import render
from .models import AccountDetails
def details(request):
    return render(request,"view.html")

def getdetails(request):
    return render(request,"details.html")

def viewdetails(request):
    acc = AccountDetails.objects.all()
    return render(request,"viewetail.html",{"acc":acc})

def savedetails(request):
    accno = request.POST.get("accno")
    name = request.POST.get("name")
    salary = request.POST.get("salary")
    AccountDetails(accno=accno,name=name,salary=salary).save()
    return render(request,"view.html",{"message":"details saved"})

def showupdate(request):
    uid = request.GET.get("update_id")
    res = AccountDetails.objects.get(accno=uid)
    return render(request,"update.html",{"data":res, })

def saveupdate(request):
    ac = request.POST.get("u_accno")
    na = request.POST.get("u_name")
    sal = request.POST.get("u_salary")
    AccountDetails.objects.filter(accno=ac).update(name=na,salary=sal)
    return viewdetails(request)

def deleteEmployee(request):
    daccno = request.POST.get("del_accno")
    AccountDetails.objects.filter(accno=daccno).delete()
    return viewdetails(request)