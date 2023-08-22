from multiprocessing import context
from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee 

def index(request):
    form=EmployeeForm()

    if request.method=='POST':
        form=EmployeeForm(request.POST)
        form.save()

    data=Employee.objects.all()

    context={
        'form':form,
        'data':data,
    }
    return render(request,'index.html',context)


def update(request,id):
    if request.method=='POST':
        data=Employee.objects.get(pk=id)
        form=EmployeeForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
    else:
        data=Employee.objects.get(pk=id)
        form=EmployeeForm(instance=data)
    context={
        'form':form
    }
    return render(request,'update.html',context)
 

def delete(request,id):
    a=Employee.objects.get(pk=id)
    a.delete()
    return redirect('/')