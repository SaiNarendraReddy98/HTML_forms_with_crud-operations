from django.shortcuts import render
from app.models import *

# Create your views here.
def insert_topic(request):
    if request.method == 'POST':
        tn=request.POST['tn']

        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()

        QLTO=Topic.objects.all()
        d={'topics':QLTO}
        
        return render(request,'display_topic.html',d)
    
    return render(request,'insert_topic.html')



def insert_webpage(request):
    QLTO=Topic.objects.all()
    d1={'topics':QLTO}
    if request.method == 'POST':
        tn=request.POST['tn']
        n=request.POST['na']
        u=request.POST['ur']
        e=request.POST['em']

        TO=Topic.objects.get(topic_name=tn)
        QLWO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
        QLWO.save()
        QLWO=Webpage.objects.all()
        d2={'webpage':QLWO}

        return render(request,'display_webpage.html',d2)


    return render(request,'insert_webpage.html',d1)




def insert_acessrecord(request):
    QLWO=Webpage.objects.all()
    d3={'webpages':QLWO}
    if request.method == 'POST':
        wn=request.POST['na']
        dt=request.POST['dt']
        au=request.POST['au']

        WO=Webpage.objects.get(pk=wn)

        QLAO=AcessRecord.objects.get_or_create(name=WO,date=dt,author=au)[0]
        QLAO.save()
        QLAO=AcessRecord.objects.all()

        d4={'ar':QLAO}
        return render(request,'display_acessrecord.html',d4)

    return render(request,'insert_acessrecord.html',d3)



def select_multiple(request):
    QLTO = Topic.objects.all()
    QLAO = AcessRecord.objects.all()
    d={'topics':QLTO , 'ar':QLAO}
    if request.method == 'POST':
        topic_list = request.POST.getlist('tn')
        QLWO=Webpage.objects.none()
        for i in topic_list:
            QLWO = QLWO|Webpage.objects.filter(topic_name=i)

        d2={'webpage':QLWO}
        return render(request,'display_webpage.html',d2)
    

    return render(request,'select_multiple.html',d)


