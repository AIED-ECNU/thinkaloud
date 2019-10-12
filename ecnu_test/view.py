from django.shortcuts import render
from django.shortcuts import HttpResponse
import pymysql
import logging
import os;
 
def index(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'index.html', context)

def info(request):
    return render(request,"info.html")

def warm(request):
    return render(request,"warm.html")

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

    #连接数据库
    conn = pymysql.connect('127.0.0.1','root','aaa','ecnuTest')
    #创建游标
    cursor = conn.cursor()
    #sql语句
    sql = 'insert into user_info(id,gender,school,f_education,m_education,f_career,m_career) values (%s,%s,%s,%s,%s,%s,%s);'
    #执行SQL语句
    cursor.execute(sql,(ID,GENDER,SCHOOL,F_EDUCATION,M_EDUCATION,F_CAREER,M_CAREER))
    conn.commit()
    cursor.close()
    conn.close()
    #return HttpResponse('注册成功')
    return render(request,"intro.html")

def uploadWarm(request):
    files = request.FILES.getlist('upfile') 
    mp3 = files[0];

    if not mp3 :
        return HttpResponse("没有文件上传!") 
    
    id = request.session["id"];

    destination = open(os.path.join(r"C:\Users\15201\Desktop\mp3",id+mp3.name),'wb+') 
    for chunk in mp3.chunks():      # 分块写入文件 
        destination.write(chunk) 
    destination.close() 
    return HttpResponse("上传成功!")

def five(request):
    return render(request,"five.html")

def six(request):
    return render(request,"six.html")

def uploadSix(request):
    files = request.FILES.getlist('upfile') 
    mp3 = files[0];

    if not mp3 :
        return HttpResponse("没有文件上传!") 
    
    id = request.session["id"];

    destination = open(os.path.join(r"C:\Users\15201\Desktop\mp3",id+mp3.name),'wb+') 
    for chunk in mp3.chunks():      # 分块写入文件 
        destination.write(chunk) 
    destination.close() 
    return HttpResponse("上传成功!")

def seven(request):
    return render(request,"seven.html")

def eight(request):
    return render(request,"eight.html")

def nine(request):
    return render(request,"nine.html")

def ten(request):
    return render(request,"ten.html")

def eleven(request):
    return render(request,"eleven.html")   

