from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from . models import StudentData

# Create your views here.

def upload_report(request):

    if request.method=="POST":
        student_name=request.POST.get('student_name')
        lab_name=request.POST.get('lab_name')
        lab_file=request.FILES.get('lab_file')

        StudentData.objects.create(
            student_name=student_name,#table attribute name = form input field variable
            lab_name=lab_name,
            lab_file=lab_file
            
        )
        return render(request,"reports/upload.html",{
        'success': True
            })
        
    return render(request,'reports/upload.html')
   

def report_list(request):
    reports = StudentData.objects.all().order_by('-uploaded_at')
    return render(request,'reports/report_list.html',
         {"reports":reports
          })

def delete(request,id):
    report = get_object_or_404(StudentData,id=id)
    report.delete()
    return redirect('report_list')