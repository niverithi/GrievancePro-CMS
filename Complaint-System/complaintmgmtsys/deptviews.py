from django.shortcuts import render,redirect,HttpResponse
from cmsapp.EmailBackEnd import EmailBackEnd
from django.contrib.auth import  logout,login
from django.contrib import messages
from cmsapp.models import CustomUser,Complaints, Category, ComplaintRemark
from django.contrib.auth import get_user_model
from cmsapp.models import CustomUser,UserReg
from django.contrib.auth.decorators import login_required


@login_required(login_url='dept_login/')

def DEPTHOME(request):
    complaints = Complaints.objects.all()
    user_count = UserReg.objects.all().count
    category_count = Category.objects.all().count   
    complaints_count = Complaints.objects.all().count
    newcom_count = Complaints.objects.filter(status='0').count()
    ipcom_count = Complaints.objects.filter(status='Inprocess').count()
    closed_count = Complaints.objects.filter(status='Closed').count()
    context = {'user_count':user_count,
    'category_count': category_count,
    'complaints_count':complaints_count,
    'newcom_count':newcom_count,
    'ipcom_count':ipcom_count,
    'closed_count':closed_count,
    'complaints':complaints        
    }
    return render(request,'department/dept_dashboard.html',context)


def DEPT_LOGIN(request):
    return render(request, 'department/dept_login.html')


def DEPT_USERSIGNUP(request):
   
    if request.method == "POST":
        pic = request.FILES.get('pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobno = request.POST.get('mobno')        
        password = request.POST.get('password')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email already exist')
            return redirect('dept_usersignup')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username already exist')
            return redirect('dept_usersignup')
        else:
            user = CustomUser(
               first_name=first_name,
               last_name=last_name,
               username=username,
               email=email,
               user_type=2,
               profile_pic = pic,
            )
            user.set_password(password)
            user.save()            
            comuser = UserReg(
                admin = user,                
                mobilenumber = mobno,              
                
            )
            comuser.save()            
            messages.success(request,'Signup Successfully')
            return redirect('dept_usersignup')
    
    

    return render(request,'department/dept_reg.html')

@login_required(login_url='/')
def VIEWCOMPLAINTS(request,id):
    complaints = Complaints.objects.filter(id=id)
    complaintsremarks = ComplaintRemark.objects.filter(comp_id_id=id)
      
    context = {
         'complaints':complaints,
         'complaintsremarks':complaintsremarks,
    }
    return render(request,'department/view-complaints.html',context)

