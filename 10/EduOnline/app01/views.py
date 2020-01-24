from django.shortcuts import render,HttpResponse

# Create your views here.
import models

def index(request):
    sliders = models.Slider.objects.all()
    context = {
        'sliders' : sliders,
    }
    return render(request,'app01/index.html',context)

def video(request,**kwargs):
    q = {}
    q['status'] = 1
    cid = int(kwargs['cid'])

    direction_list = models.Direction.objects.all()
    if kwargs['did'] == '0':
        class_list = models.Classification.objects.all()

        if kwargs['cid'] != '0':
            q['classification_id__in'] = [cid,]
    else:
        if kwargs['cid'] == '0':
            direction = models.Direction.objects.get(pk=kwargs['did'])
            class_list = direction.classification.all()
            cid_list = map(lambda x: x.id, class_list)

            q['classification_id__in'] = cid_list

        else:
            direction = models.Direction.objects.get(pk=kwargs['did'])
            class_list = direction.classification.all()
            cid_list = map(lambda x:x.id , class_list)

            q['classification_id__in'] = [cid, ]

            if int(kwargs['cid']) not in cid_list:
                url_part = request.path.split('/')
                url_part[3] = '0'
                request.path = '/'.join(url_part)

    level_list = map(lambda x: {'id':x[0],'name':x[1]},models.Video.level_choice)

    video_list = models.Video.objects.filter(**q).all()

    context = {
        'direction_list' : direction_list,
        'class_list' : class_list,
        'level_list' : level_list,
        'video_list' : video_list
    }
    return render(request,'app01/video.html',context)