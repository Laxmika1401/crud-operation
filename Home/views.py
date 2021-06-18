from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect



from .models import Employee

# Create your views here.
def home(request):
    return render(request,"home.html")

def show(request):
    data = Employee.objects.all()
    return render(request,"show.html",{'data':data})
def send(request):
    if request.method == 'POST':
        EMPLOYEE_ID = request.POST['id']
        EMAIL_ID = request.POST['email']
        AGE = request.POST['number']
        OCCUPATION = request.POST['occupation']
        Employee(EMPLOYEE_ID = EMPLOYEE_ID,EMAIL_ID = EMAIL_ID,AGE = AGE, OCCUPATION = OCCUPATION).save()
        msg = "Data Stored Successfully"
        return render(request,"home.html",{'msg':msg})

    else:
        return HttpResponse("404 not found eror")
def delete(request):
    EMPLOYEE_ID = request.GET['id']
    Employee.objects.filter(EMPLOYEE_ID = EMPLOYEE_ID).delete()
    return HttpResponseRedirect("show")


def edit(request):
    EMPLOYEE_ID = request.GET['id']
    EMAIL_ID = AGE= OCCUPATION= "Not_Avialable"
    for data in Employee.objects.filter(EMPLOYEE_ID = EMPLOYEE_ID):
        EMAIL_ID = data.EMAIL_ID
        AGE = data.AGE
        OCCUPATION = data.OCCUPATION
    return render(request, "edit.html",{'EMPLOYEE_ID':EMPLOYEE_ID,'EMAIL_ID':EMAIL_ID,'AGE':AGE,'OCCUPATION':OCCUPATION})
    
def RecordEdited(request):
    if request.method == 'POST':
        EMPLOYEE_ID = request.POST['id']
        EMAIL_ID = request.POST['email']
        AGE = request.POST['number']
        OCCUPATION = request.POST['occupation']
        Employee.objects.filter(EMPLOYEE_ID = EMPLOYEE_ID).update(EMAIL_ID = EMAIL_ID,AGE = AGE, OCCUPATION = OCCUPATION)
        return HttpResponseRedirect("show")
    else:
        return HttpResponse("404 not found eror")

        

