from django.shortcuts import render
from CURD.models import Employee

# Create your views here.
def input_data(request):
    return render(request,'input_form.html')

def insertion(request):
    eid=int(request.GET['id'])
    ename=request.GET['name']
    esal=float(request.GET['salary'])
    edno=int(request.GET['dno'])
    e=Employee(id=eid,name=ename,sal=esal,dno=edno)
    e.save()
    return render(request,'insertion_result.html')

def retreival(request):
    data=Employee.objects.all()
    context={'records':data}
    return render(request,'retreival_result.html',context)

def edit(request,id):
    employee=Employee.objects.get(id=id)
    return render(request,'edit.html',{'employee':employee})

def update(request,id):
    eid = int(request.GET['id'])
    ename = request.GET['name']
    esal = float(request.GET['salary'])
    edno = int(request.GET['dno'])
    e = Employee(id=eid, name=ename, sal=esal, dno=edno)
    e.save()
    return render(request,'update.html')

def delete(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return render(request,'delete.html')