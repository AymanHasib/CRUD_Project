from django.shortcuts import render
from crud.models import crudst
from django.contrib import messages
from crud.forms import stform

def stdisplay(request):
    results=crudst.objects.all()
    return render(request, "Index.html", {"crudst":results})

def stinsert(request):
    if request.method=="POST":
        if request.POST.get('stname') and request.POST.get('stemail') and request.POST.get('staddress') and request.POST.get('stmobile') and request.POST.get('stnGender'):
            savest=crudst()
            savest.stname=request.POST.get('stname')
            savest.stemail = request.POST.get('stemail')
            savest.staddress = request.POST.get('staddress')
            savest.stmobile = request.POST.get('stmobile')
            savest.stnGender = request.POST.get('stnGender')
            savest.save()
            messages.success(request, "The Record "+savest.stname+" is saved Successfully")
            return render(request,"Create.html")
    else:
            return render(request,"Create.html")


def stedit(request, id):
    getstudentdetails=crudst.objects.get(id=id)
    return render(request, 'edit.html',{"crudst":getstudentdetails})

def stupdate(request, id):
    stupdate=crudst.objects.get(id=id)
    form=stform(request.POST, instance=stupdate)

    if form.is_valid():
        form.save()
        messages.success(request,"The student record is update successfully")
        return render(request, "edit.html",{"crudst":stupdate})

def stdelete(request, id):
    delstudent=crudst.objects.get(id=id)
    delstudent.delete()
    results = crudst.objects.all()
    return render(request, "Index.html", {"crudst": results})