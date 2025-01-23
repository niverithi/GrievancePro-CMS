import random
from django.shortcuts import render, redirect, get_object_or_404
from cmsapp.EmailBackEnd import EmailBackEnd
from django.contrib.auth import  logout,login
from django.contrib import messages
from .models import Complaints  # Import your Complaints and ComplaintRemark models
from cmsapp.models import CustomUser,Complaints
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings

User = get_user_model()


from django.contrib.auth.decorators import login_required

def BASE(request):
       return render(request,'base.html')




def LOGIN(request):
    return render(request,'login.html')

def notifications(request):
    complaints1 = Complaints.objects.all()
    newcom_count1 = Complaints.objects.filter(status='0').count() 
    context = {
    'newcom_count1':newcom_count1,
    'complaints1':complaints1        
    }
    return render(request, 'includes/header.html', context)



def doLogout(request):
    logout(request)
    request.session.flush()  # Clear the session including CSRF token
    return redirect('login')

def doLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        keep_signed_in = request.POST.get('keep_signed_in')

        user = EmailBackEnd.authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('admin_home')
            elif user_type == '2':
                return redirect('user_home')
            elif user_type == '3':
                return redirect('dept_dashboard')
        else:
            messages.error(request, 'Email or Password is not valid')
            return redirect('login')  # Redirect back to the login page with an error message
    else:
        # If the request method is not POST, redirect to the login page with an error message
        messages.error(request, 'Invalid request method')
        return redirect('login')


login_required(login_url='/')
def PROFILE(request):
    user = CustomUser.objects.get(id = request.user.id)
    context = {
        "user":user,
    }
    return render(request,'profile.html',context)
@login_required(login_url = '/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        print(profile_pic)
        

        try:
            customuser = CustomUser.objects.get(id = request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            

            
            if profile_pic !=None and profile_pic != "":
               customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request,"Your profile has been updated successfully")
            return redirect('profile')

        except:
            messages.error(request,"Your profile updation has been failed")
    return render(request, 'profile.html')


def CHANGE_PASSWORD(request):
     context ={}
     ch = User.objects.filter(id = request.user.id)
     
     if len(ch)>0:
            data = User.objects.get(id = request.user.id)
            context["data"]:data             # type: ignore
     if request.method == "POST":        
        current = request.POST["cpwd"]
        new_pas = request.POST['npwd']
        user = User.objects.get(id = request.user.id)
        un = user.username
        check = user.check_password(current)
        if check == True:
          user.set_password(new_pas)
          user.save()
          messages.success(request,'Password Change  Succeesfully!!!')
          user = User.objects.get(username=un)
          login(request,user)
        else:
          messages.success(request,'Current Password wrong!!!')
          return redirect("change_password")
     return render(request,'change-password.html')

def user_dashboard(request):
    # Get counts for each status
    total_complaints = Complaints.objects.count()
    not_processed_count = Complaints.objects.filter(status='0').count()
    in_process_count = Complaints.objects.filter(status='Inprocess').count()
    closed_count = Complaints.objects.filter(status='Closed').count()

    context = {
        'complaints_count': total_complaints,
        'newcom_count': not_processed_count,
        'ipcom_count': in_process_count,
        'closed_count': closed_count,
        'complaints': Complaints.objects.all(),  # Pass any other data you need
    }
    return render(request, 'user/userdashboard.html', context)


@login_required(login_url='/')
def register_complaint_email(request):
    
    if request.method == 'POST': 
        # Get form data
        
        cat_id = request.POST.get('cat_id')
        subcat_id = request.POST.get('subcategory_id')
        complaint_type = request.POST.get('complainttype')
        state_id = request.POST.get('stateid')
        noc = request.POST.get('noc')
        complaindetails = request.POST.get('complaindetails')
        compfile = request.FILES.get('compfile')

        # Create a new complaint
        complaint = Complaints.objects.create(
            complaint_number=f"COM-{int(Complaints.objects.count()) + 1:04d}",
            userregid=request.user,
            status='0',
            noc=noc,
            complaindetails=complaindetails,
            compfile=compfile
        )

        # # Send an email to the user
        subject = "Complaint Successfully Submitted"
        message = f"""
        Dear {request.user.first_name},

        Your complaint has been successfully submitted.
        Your complaint ID is: {complaint.complaint_number}

        We will look into the matter and get back to you soon.

        Thanks & Regards,
        Support Team
        """
        recipient_list = [request.user.email]
        print(f"Email will be sent to: {recipient_list}")

    try:
        print("Attempting to send email...")
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
        messages.success(request, "Complaint submitted successfully, and an email has been sent to you.")
    except Exception as e:
        print(f"Error while sending email: {e}")  # Debug the error
        messages.error(request, f"Complaint submitted, but there was an error sending the email.")

    return render(request, 'user/register-complaint.html')





@login_required(login_url='/')
def feedback_form(request, complaint_id):
    # Fetch the complaint based on the complaint_id
    complaint = get_object_or_404(Complaints, id=complaint_id)

    # Only allow feedback submission if the complaint is closed
    if complaint.status != 'Closed':
        messages.error(request, "Feedback can only be given for closed complaints.")
        return redirect('complainthistory')  # Redirect back to the complaint history page

    if 'submitted_feedback' not in request.session:
            request.session['submitted_feedback'] = []
    request.session['submitted_feedback'].append(complaint_id)
    request.session.modified = True  # Mark session as updated

    if request.method == 'POST':
        feedback_text = request.POST.get('feedback')
        rating = request.POST.get('rating')  # Get the star rating

        # Optionally save feedback and rating to your Complaints model (if you have such fields)
        complaint.feedback = feedback_text
        complaint.rating = rating  # Assuming you added a `rating` field in Complaints model
        complaint.save()
        
        # Send email to the user with their feedback and rating
        user_email = complaint.userregid.admin.email
        email_body = f"""
        Dear {complaint.userregid.admin.first_name},

        Thank you for providing feedback on your complaint.

        Here are your feedback details:
        
        Complaint Number: {complaint.complaint_number}
        Feedback: {feedback_text}
        Rating: {rating} Stars

        We appreciate your input and will use this to improve our services.

        Best regards,
        Support Team
        """

        try:
            send_mail(
                subject="Thank you for your feedback",
                message=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user_email],
                fail_silently=False,
            )
            messages.success(request, "Your feedback has been submitted successfully. A confirmation email has been sent.")
        except Exception as e:
            messages.error(request, f"Failed to send email: {str(e)}")

        # If you don't want to save feedback to the model, you can simply show a success message.
        # messages.success(request, "Your feedback has been submitted successfully.")
        return redirect('complainthistory')  # Redirect back to the complaint history page

    context = {
        'complaint': complaint
    }
    return render(request, 'user/feedback_form.html', context)






