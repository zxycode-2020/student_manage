from django.shortcuts import render

# Create your views here.
import models

def index(request):
    banner_list = models.Banner.objects.filter(status=1).order_by('-weight').all()[0:2]
    notice_list = models.Notice.objects.filter(status=1).order_by('-weight').all()[0:3]
    course_list = models.Course.objects.filter(status=1).order_by('-weight').all()[0:6]
    stu_detail = models.StuDetail.objects.order_by('-weight').first()
    recruit_list = models.Recruit.objects.filter(status=1).order_by('-weight').all()[0:10]
    student_list = models.Student.objects.filter(status=1).order_by('-weight').all()[0:5]
    friend_list = models.Cooperation.objects.order_by('-weight').all()[0:5]


    context = {
        'banner_list' : banner_list,
        'notice_list' : notice_list,
        'course_list' : course_list,
        'stu_detail' : stu_detail,
        'recruit_list' : recruit_list,
        'student_list' : student_list,
        'friend_list' : friend_list,
    }
    return render(request,'home/index.html',context)



def student(request):
    return render(request,'home/student.html')