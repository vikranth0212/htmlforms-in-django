from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        t1=request.POST['tn1']

        TO=topic.objects.get_or_create(topic_name=t1)[0]
        TO.save()
        QLTO=topic.objects.all()
        d={'topik':QLTO}
        return render(request,'display_topic.html',d)

    return render(request,'insert_topic.html')    


def insert_webpage(request):
    QLTO=topic.objects.all()
    d={'topik':QLTO}
    if request.method=='POST':
        nm1=request.POST['nm']
        ur1=request.POST['ur']
        em1=request.POST['em']
        tn1=request.POST['tn']

        TO=topic.objects.get(topic_name=tn1)
        WO=webpage.objects.get_or_create(name=nm1,url=ur1,email=em1,topic_name=TO)[0]
        WO.save()

        QLWO=webpage.objects.all()
        d1={'webp':QLWO}
        return render(request,'display_webpage.html',d1)

    return render(request,'insert_webpage.html',d)    

def select_multiple_webpage(request):
    QLTO=topic.objects.all()
    d7={'topi':QLTO}

    if request.method=='POST':
        tl=request.POST.getlist('t8')#['C','kabaddi','VB']
        #print(tn)
        QLWO=webpage.objects.none()#it will create empty folder with none value
        for i in tl:
            QLWO=QLWO|webpage.objects.filter(topic_name=i)

        d9={'webp':QLWO}
        return render(request,'display_webpage.html',d9) 

    return render(request,'multiwebpage.html',d7)   

def checkbox(request):
     QLTO=topic.objects.all()
     d7={'topi':QLTO}
     return render(request,'checkbox.html',d7) #we used url navigation here

#here we are doing normal way
# def checkbox(request):
#     QLTO=topic.objects.all()
#    d7={'topi':QLTO}
#     if request.method=='POST':
#        tl=request.POST.getlist('t8')#['C','kabaddi','VB']
#        #print(tn)
#       QLWO=webpage.objects.none()#it will create empty folder with none value
#        for i in tl:
#            QLWO=QLWO|webpage.objects.filter(topic_name=i)
#
#        d9={'webp':QLWO}
#        return render(request,'display_webpage.html',d9) 
#     
# return render(request,'checkbox.html',d7) #we used url navigation here
# 
# 
# here we are writing the code multiple times code redundancy happened
#  to overcome that we used urlnavifation
# 
#     

def insert_accessrecord(request):
    QLWO=webpage.objects.all()
    d={'wepx':QLWO}
    if request.method=='POST':
        nm=request.POST['tn1']
        at=request.POST['tn2']
        dt=request.POST['tn3']
        

        WO=webpage.objects.get(name=nm)
        AO=accessrecord.objects.get_or_create(name=WO,author=at,date=dt)[0]
        AO.save()

        QLAO=accessrecord.objects.all()
        d1={'access':QLAO}
        return render(request,'display_accessrecord.html',d1)

    return render(request,'insert_accessrecord.html',d)    
       



