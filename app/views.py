from django.shortcuts import render,redirect
from .models import student
from django.contrib import messages
# Create your views here.
def index(request):
    data=student.objects.all()
    student_count=data.count()
    print(data)
    context={'data':data, 'student_count':student_count}
    return render(request,'index1.html',context)


def insertdata(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name,email,age,gender)
        query=student(name=name,email=email,age=age,gender=gender)
        query.save()

        messages.info(request,"Data Inserted Successfully")
        return redirect('/')

    return render(request,'index1.html')

def updatedata(request,id):
    
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')

        edit=student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.age=age
        edit.gender=gender
        edit.save()
        messages.warning(request,"Data Updated Successfully")

        return redirect('/')
    
    d=student.objects.get(id=id)
    context={'d':d}
    return render(request,'update.html',context)

def deletedata(request,id):
    d=student.objects.get(id=id)
    d.delete()
    messages.error(request,"Data Deleted Successfully")

    return redirect('/')

def analytics(request):
    # Get all students
    students = student.objects.all()
    
    # Calculate statistics
    total_students = students.count()
    
    # Gender distribution
    male_count = students.filter(gender='male').count()
    female_count = students.filter(gender='female').count()
    others_count = students.filter(gender='others').count()
    
    # Age distribution
    age_groups = {
        '18-25': students.filter(age__gte=18, age__lte=25).count(),
        '26-35': students.filter(age__gte=26, age__lte=35).count(),
        '36-45': students.filter(age__gte=36, age__lte=45).count(),
        '46+': students.filter(age__gte=46).count(),
    }
    
    # Recent students (last 10)
    recent_students = students.order_by('-id')[:10]
    
    # Performance metrics (mock data for demonstration)
    performance_data = {
        'excellent': 35,
        'good': 45,
        'average': 15,
        'needs_improvement': 5
    }
    
    context = {
        'total_students': total_students,
        'male_count': male_count,
        'female_count': female_count,
        'others_count': others_count,
        'age_groups': age_groups,
        'recent_students': recent_students,
        'performance_data': performance_data,
    }
    
    return render(request, 'analytics.html', context)
