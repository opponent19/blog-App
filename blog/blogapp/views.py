from django.shortcuts import render, HttpResponse,redirect
from blogapp.models import Blog
import datetime
from blogapp.forms import StudentFormClass
# Create your views here.

def aboutpage(request):
    #return HttpResponse("Hello from the about")
    return redirect('/contact')

def contactpage(request):
    return HttpResponse("Hello from the contact")

def edit(request,rid):
    #print("ID to be edited:",rid)
    if request.method=="GET":
        b=Blog.objects.filter(id=rid)
        context={}
        context['blog']=b
        return render(request,'editblog.html',context)
    else:
        #fetch new changes from the form
        utitle=request.POST['title']
        udetails=request.POST['details']
        ucat=request.POST['cat']
        
        #print("Updated title:",utitle)
        #print("Updated details:",udetails)
        #print("Updated Category:",ucat)
        b=Blog.objects.filter(id=rid)
        b.update(title=utitle,details=udetails,cat=ucat)
        return redirect('/userdashboard')
        
        
        return HttpResponse("Updated details Fetch")
        

def delete(request,rid):
    #print("ID to be deleted:",rid)
    b=Blog.objects.filter(id=rid)
    #print(b)
    b.delete()
    return redirect('/userdashboard')
'''
def homepage(request,x,y):
    print("value of x:",x)
    print("value of y:",y)
    return HttpResponse("Value of x and y :"+x+" "+y)
'''
def hellowview(request):
    context={}
    context['uname']="Mahendra"
    context['x']=1000
    context['y']=200
    context['l']=[10,20,'Mahendra',90.8]
    return render(request,'hello.html',context)

# blog app view function start
def homepage(request):
    b=Blog.objects.filter(is_published=True)
    #select * from blogapp_blog where is_published=1;
    context={}
    context['blog']=b
    return render(request,'home.html',context)

def user_dashboard(request):
    b=Blog.objects.all()  #select * from blogapp_blog
    context={}
    context['blogs']=b
    '''print(b)
    for x in b:
        print(x)
        print("ID:",x.id)
        print("Title:",x.title)
        print("Detail:",x.details)
        print("cat:",x.cat)
        print("Created_at:",x.created_at)
        print()'''
    return render(request,'dashboard.html',context)

def create_blog(request):
    #print("Method Type:",request.method)
    if request.method=="GET":
        #print("In GET Section")
        return render(request,'create_blog.html')
    else:
        #print("In POST Section")
        #Fetching data from form request using POST dictionary
        btitle=request.POST['title']
        bdet=request.POST['details']
        bcat=request.POST['cat']
        
        #print("Title:",btitle)
        #print("Detail:",bdet)
        #print("Category:",bcat)
        
        b=Blog.objects.create(title=btitle,details=bdet,cat=bcat,created_at=datetime.datetime.now())
        b.save()
        
        #return HttpResponse("Data inserted Sucessfull")
        return redirect('/userdashboard')
    
def view_details(request,rid):
    #print("Id to be used for detais:",rid)
    b=Blog.objects.filter(id=rid)
    #print(b)
    context={}
    context['blog']=b
    return render(request,"blog_details.html",context)

def is_published(request,status,rid):
    #print("Status is:",status)
    #print("Id to be edited:",rid)
    
    b=Blog.objects.filter(id=rid)
    #print(b)
    context={}
    context['blog']=b
    if status=='P':
        b.update(is_published=True)
        context['pmsg']="Blog has been published Successfully"
        # return HttpResponse("Blog has been published Successfull")
    else:
        b.update(is_published=False)
        context['umsg']="Blog has been Unpublished Successfully"
        # return HttpResponse("Blog is Unpublished")
        
    return render(request,"blog_details.html",context)

def setcookies(request):
    res=render(request,'set_cookies.html')
    print("Response object:",res)
    res.set_cookie('name','ITVEDANT')
    return res

def getcookies(request):
    cdata=request.COOKIES['name']
    print("Data in the cookies:",cdata)
    context={}
    context['data']=cdata
    return render(request,'getcookies.html',context)

def setsession(request):
    
    request.session['learning']="Session and cookies"
    return render(request,'set_session.html')

def getsession(request):
    sdata=request.session['learning']
    print("Data in the cookies:",sdata)
    context={}
    context['data']=sdata
    return render(request,'get_session.html',context)

def djangoForm(request):
    context={}
    if request.method=="GET":
        s=StudentFormClass()
        #print(s)
        context['fm']=s
        return render(request,'studentform.html',context)
    else:
        n=request.POST['name']
        r=request.POST['roll_number']
        per=request.POST['percentage']
        
        print(n)
        print(r)
        print(per)
        # s=Student.objects.create(name=n,rno=r,per=per)
        # s.save()
        return HttpResponse ("Data Inserted")