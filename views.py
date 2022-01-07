from django.contrib import messages
from employee.models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from employee.form import *
from empmanage import settings
from django.core.mail import send_mail


# Create your views here.
def index(request):
    return render(request,"requestforleave.html")

def logpag(request):
    return render(request,"login.html")

def admdash(request):
    return render(request,"admindashboard.html")
        
def empdash(request):
    return render(request,"empdashboard.html")


def login(request):
    print(request.session.get('id'))
    if request.session.get('id') is not None:
        return redirect(index,permanent=True)
    if request.method== "POST":
        if request.POST.get("username") and request.POST.get("password"):
            us=request.POST.get("username")
            pw=request.POST.get("password")
            emp=None
            try:
                emp=addEmp.objects.get(username=us)
            except:
                pass
            if emp is not None:
                if emp.password==pw:
                    if emp.is_admin:
                        return render(request,"admindashboard.html")
                    else:
                        return render(request,"empdashboard.html")
                else:
                    messages.error(request,"Incorrect password!")
                    return render(request,"login.html")
            else:
                messages.error(request,"Incorrect username!")
                return render(request,"login.html")
        else:
            messages.error(request,"All fields are required!")
            return render(request,"login.html")
    return render(request,"login.html")
    

def logout(request):
    request.session.clear()
    return render(request,"home.html")


def insert(request):
    print("insert func")
    if request.method=="POST":
        print("method is post")
        if checkData(request):
        #request.POST.get("fname") and request.POST.get("lname") and request.POST.get("dob") and request.POST.get("age") and request.POST.get("city") and request.POST.get("email"):
            emp=newReg()
            print("POST method")
            emp.id=request.POST.get(id)
            emp.fname=request.POST.get("fname")
            emp.lname=request.POST.get("lname")
            emp.dob=request.POST.get("dob")
            emp.age=request.POST.get("age")
            emp.city=request.POST.get("city")
            emp.email=request.POST.get("email")
            emp.save()
            messages.success(request,"You have been registered.")
            return render(request,"registration.html")
    return render(request,"registration.html")
def checkData(request):
    ans = True
    if not request.POST.get('fname'):
        print("fname")
        messages.error(request, 'No first Name')
        ans = False
    if not request.POST.get('lname'):
        print("lname")
        messages.error(request, 'No Last Name')
        ans = False
    if not request.POST.get('email'):
        print("email")
        messages.error(request, 'no email')
        ans = False
    if not request.POST.get('dob'):
        print("dob")
        messages.error(request, 'no Date of Birth')
        ans = False
    if not request.POST.get('age'):
        print("age")
        messages.error(request, 'no age')
        ans = False
    if not request.POST.get('city'):
        print("city")
        messages.error(request, 'no city')
        ans = False
    return ans

def viewApplicants(request):
    result=newReg.objects.all()
    return render(request,"viewapplicants.html",{"applicants":result})

def viewEmployees(request):
    result=addEmp.objects.all()
    return render(request,"viewemployees.html",{"employees":result})

def viewemp(request):
    result=addEmp.objects.all()
    return render(request,"empviewemp.html",{"employees":result})


def addEmployees(request,id=None):
    def checkData(request):
        ans = True
        if not request.POST.get('fname'):
            print("fname")
            messages.error(request, 'No first Name')
            ans = False
        if not request.POST.get('lname'):
            print("lname")
            messages.error(request, 'No Last Name')
            ans = False
        if not request.POST.get('email'):
            print("email")
            messages.error(request, 'no email')
            ans = False
        if not request.POST.get('dob'):
            print("dob")
            messages.error(request, 'no Date of Birth')
            ans = False
        if not request.POST.get('age'):
            print("age")
            messages.error(request, 'no age')
            ans = False
        if not request.POST.get('city'):
            print("city")
            messages.error(request, 'no city')
            ans = False
        if not request.POST.get('username'):
            print("username")
            messages.error(request, 'no username')
            ans = False
        if not request.POST.get('password'):
            print("password")
            messages.error(request, 'no password')
            ans = False
        if not request.POST.get('joining_date'):
            print("joining_date")
            messages.error(request, 'no joining date')
            ans = False
        if not request.POST.get('rem_leaves'):
            print("rem_leaves")
            messages.error(request, 'no leaves')
            ans = False
        if not request.POST.get('position'):
            print("position")
            messages.error(request, 'no position')
            ans = False
        if not request.POST.get('department'):
            print("department")
            messages.error(request, 'no department')
            ans = False
        if not request.POST.get('current_project'):
            print("current_project")
            messages.error(request, 'no project')
            ans = False
        return ans
    emp=newReg.objects.get(id=id)
    empmail=addEmp.objects.values_list('email')
    emails=[]
    for email in empmail:
        emails+=email
    emails=set(emails)
    if emp.email in emails:
        messages.error(request,'Already an employee')
        return redirect(viewApplicants)
    x = emp.dob
    username=emp.fname[0].upper()+emp.fname[1:].lower()+emp.lname[0].upper()+emp.lname[1:].lower()
    password=emp.fname[0:3].lower()+str(emp.id)+emp.lname[4:].lower()
    if request.method=="POST":
        #if request.POST.get("fname") and request.POST.get("lname") and request.POST.get("dob") and request.POST.get("age") and request.POST.get("city") and request.POST.get("email") and request.POST.get("username") and request.POST.get("password") and request.POST.get("joining_date") and request.POST.get("rem_leaves") and request.POST.get("position") and request.POST.get("department") and request.POST.get("current_project"):
        if checkData(request):    
            empn=addEmp()
            empn.id=request.POST.get(id)
            empn.fname=request.POST.get("fname")
            empn.lname=request.POST.get("lname")
            empn.dob=request.POST.get("dob")
            empn.age=request.POST.get("age")
            empn.city=request.POST.get("city")
            empn.email=request.POST.get("email")
            empn.username=request.POST.get("username")
            empn.password=request.POST.get("password")
            empn.joining_date=request.POST.get("joining_date")
            empn.rem_leaves=request.POST.get("rem_leaves")
            empn.position=request.POST.get("position")
            empn.department=request.POST.get("department")
            empn.current_project=request.POST.get("current_project")
            empn.save()
            emp.delete()
            messages.success(request,"The Employee record is added.")
            msg = 'Hi' + request.POST.get('fname') + '' + request.POST.get('lname') + \
                ', You have been selected.\nPlease check below for your username and password. \n\n \
                Your Username: ' + request.POST.get('username') + '\n' + 'Your Password: ' + request.POST.get('password') + \
                '.\n\nFurther details will be provided soon.'
            res = send_mail(msg,settings.EMAIL_HOST_USER,[request.POST.get('email')])
            if res == 1:
                print('done')
            else:
                print('Mail not sent')
            return render(request,"addemployee.html")
        else:
            messages.error(request,"All fields are required!")
            return render(request,"addemployee.html")
    return render(request,"addemployee.html",{"employee":emp,'dob':x,"username":username,"password":password})

def update(request,id):
    emp=addEmp.objects.get(id=id)
    form=regForm(request.POST,instance=emp)
    if form.is_valid():
        form.save()
        messages.success(request,"The record is successfully updated.")
        return redirect(viewEmployees,id=id)
    else:
        return render(request,"edit.html",{"employee":emp})

def deleteApplicant(request,id):
    applicant=newReg.objects.get(id=id)
    applicant.delete()
    messages.success(request,"Applicant's record deleted.")
    return redirect(viewApplicants)

def deleteEmployee(request,id):
    emp=addEmp.objects.get(id=id)
    emp.delete()
    messages.success(request,"Employee's record deleted.")
    return redirect(viewEmployees)

def requestleave(request):
    if request.method=="POST":
        if request.POST.get('leaveType') and request.POST.get('startDate') and request.POST.get('endDate') and request.POST.get('leaveDesc'):
            leave = leaveRequest()
            leave.empId = addEmp.objects.get(id=id)
            leave.leaveType = request.POST.get('leaveType')
            leave.startDate = request.POST.get('startDate')
            leave.endDate = request.POST.get('endDate')
            leave.leaveDesc = request.POST.get('leaveDesc')
            leave.save()
            messages.success(request, "Leave request sent successfully.")
            return render(request,"requestforleave.html")
        else:
            messages.error(request,"All fields required!")
            return render(request,"requestforleave.html")
    return render(request,"requestforleave.html")

def leaveRequests(request):
    requests=leaveRequest.objects.filter(decision="Pending")
    return render(request,"managelevreq.html",{'requests':requests})

def approveLeave(request,id):
    lev=leaveRequest.objects.get(id=id)
    emp=lev.empId
    if emp.rem_leaves > 0:
        emp.rem_leaves -= 1
    else:
        messages.error(request,"No remaining leaves!")
        return render(request,"managelevreq.html")
    emp.save()
    lev.decision = "Approved"
    lev.save()
    messages.success(request,"Leave Approved.")
    return render(request,"managelevreq.html")

def rejectLeave(request,id):
    lev = leaveRequest.objects.get(id=id)
    lev.decision = "Rejected"
    lev.save()
    messages.success(request,"Leave request rejected.")
    return render(request,"managelevreq.html")


def leaveStatus(request,id):
    emp=addEmp.objects.get(id=id)
    leavereqList = leaveRequest.objects.get(empId=emp)
    return render(request,"leavestatus.html",{"leaves":leavereqList,'employee':emp,'leavesTaken':30-emp.rem_leaves})

def issueNotice(request):
    if request.method=='POST':
        if request.POST.get('title') and request.POST.get('body'):
            notices = notice()
            notices.title = request.POST.get('title')
            notices.body = request.POST.get('body')
            notices.save()
            messages.success(request,"Notice Issued Successfully.")
            return render(request,"admindashboard.html")
        else:
            messages.error(request,"All fields are required!")
    return render(request,"issuenotice.html")

def viewNotice(request):
    notices=notice.objects.order_by('-id')
    return render(request,"viewnotice.html",{"notices":notices})



 












    





