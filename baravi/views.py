from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def result(request):
    if request.method =='GET':
        Roll_no = request.GET.get("Roll_no")
        stud = school.objects.all()
        return render(request,'result.html')
    if request.method =='POST':
         Name = request.POST.get("Name")
         Roll_no = request.POST.get("Roll_no")
         school.objects.create(Name=Name ,Roll_no=Roll_no)
         return redirect('/add')

def add(request):
    if request.method =='GET':
        Roll_no = request.GET.get("Roll_no")
        stud = school.objects.all()
        return render(request,'add.html',{'school':stud},)
        

def edit_view(request,id):
    if request.method == "GET":
        Roll_no = request.GET.get("Roll_no")
        stud = school.objects.all()
        context = {}                    
        if Roll_no != "":
           stud =stud.filter(Roll_no=id)
           if stud:
               context["name"] = stud[0].name
               context["Roll_no"]  = stud[0].roll_no
        return render(request, 'edit_view.html',context)
            
    if request.method == 'POST':
        Roll_no = request.POST.get("Roll_no")
        Name = request.POST.get("name")
        print(Roll_no,Name)
        stud =school.objects.filter(roll_no=Roll_no)
        stud.update(name=name)
        return redirect(edit_view)
        


def delete_view(request,id):
    if request.method == "GET":
        school.objects.get(id=id).delete()
        return redirect(add)