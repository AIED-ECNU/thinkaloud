
# Create your views here.
from django.shortcuts import render
from django.shortcuts import HttpResponse
from myapp.models import User_infor
from myapp.models import Search_content
import pymysql
import logging
import os;
import json


def index(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'index.html', context)

def info(request):
    return render(request,"info.html")

def warm(request):
    return render(request,"warm.html")

def five(request):
    return render(request,"five.html")

def six(request):
    return render(request,"six.html")

def seven(request):
    return render(request,"seven.html")

def eight(request):
    return render(request,"eight.html")

def nine(request):
    return render(request,"nine.html")

def ten(request):
    return render(request,"ten.html")

def final(request):
    return render(request,"final.html")

def intro(request):
    a = request.GET#获取get()请求
    #通过get()请求获取前段提交的数据
    ID = a.get('id')
    GENDER = a.get('gender')
    SCHOOL = a.get('school')
    F_EDUCATION = a.get('f_education')
    M_EDUCATION = a.get('m_education')
    F_CAREER = a.get('f_career')
    M_CAREER = a.get('m_career')
    request.session["id"] = ID;
    user_infor=User_infor()
    user_infor.ID=ID
    user_infor.GENDER=GENDER
    user_infor.SCHOOL=SCHOOL
    user_infor.F_EDUCATION=F_EDUCATION
    user_infor.M_EDUCATION=M_EDUCATION
    user_infor.F_CAREER=F_CAREER
    user_infor.M_CAREER=M_CAREER
    user_infor.save()
    #return HttpResponse('注册成功')
    return render(request,"intro.html")

def uploadWarm(request):
    files = request.FILES.getlist('upfile') 
    mp3 = files[0];

    if not mp3 :
        return HttpResponse("没有文件上传!") 
    
    id = request.session["id"];

    destination = open(os.path.join(r"C:/Users/15201/Desktop/ecnu_test/res",id+mp3.name),'wb+') 
    for chunk in mp3.chunks():      # 分块写入文件 
        destination.write(chunk) 
    destination.close() 
    return HttpResponse("上传成功!")

def uploadSix(request):
    files = request.FILES.getlist('upfile') 
    mp3 = files[0];

    if not mp3 :
        return HttpResponse("没有文件上传!") 
    
    id = request.session["id"];

    destination = open(os.path.join(r"C:/Users/15201/Desktop/ecnu_test/res",id+mp3.name),'wb+') 
    for chunk in mp3.chunks():      # 分块写入文件 
        destination.write(chunk) 
    destination.close() 
    return HttpResponse("上传成功!")
    
def uploadEight(request):
    files = request.FILES.getlist('upfile') 
    mp3 = files[0];

    if not mp3 :
        return HttpResponse("没有文件上传!") 
    
    id = request.session["id"];

    destination = open(os.path.join(r"C:/Users/15201/Desktop/ecnu_test/res",id+mp3.name),'wb+') 
    for chunk in mp3.chunks():      # 分块写入文件 
        destination.write(chunk) 
    destination.close() 
    return HttpResponse("上传成功!")

def search(request):
    content = request.GET#获取get()请求
    #通过get()请求获取前段提交的数据
    key = content.get("key");
    #连接数据库
    #conn = pymysql.connect('127.0.0.1','root','aaa','ecnuTest')
    #创建游标
    #cursor = conn.cursor();
    #sql语句
    #sql = "SELECT * FROM search_content WHERE content LIKE '%"+key+"%' ";
    search_content=Search_content()
    search_content.title='地球'
    search_content.content='地球（Earth）是太阳系八大行星之一'
    search_content.imgPath='..\\static\\img\\search-img\\earthImg.jpg'
    search_content.save()
    #return HttpResponse('注册成功')
    #res = Search_content.objects.filter(title__icontains=key)
    res =Search_content.objects.filter(title='地球')
    #res=Search_content.objects.values('title')
    #print(res)
    #执行SQL语句
    #resCnt = cursor.execute(sql);
   
    
    #if resCnt > 0 :
    if res:
        resData =   { 'content' : res[0].content, 'imgPath' : res[0].imgPath } ;
        resContent = json.dumps(resData)
        #print(resContent);
        #print(res[1]);
        #print(res[2]);
        return HttpResponse(resContent, content_type='application/json')
    else:
        return HttpResponse(request,"no content");


    '''
    if res > 0 :
        #res = cursor.fetchone();
        resData =   { 'content' : res[1], 'imgPath' : res[2] } ;
        resContent = json.dumps(resData)
        #print(resContent);
        #print(res[1]);
        #print(res[2]);
        return HttpResponse(resContent, content_type='application/json')
    else :
        return HttpResponse(request,"no content");
    ''' 

