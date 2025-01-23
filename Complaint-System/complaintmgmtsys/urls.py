
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views, adminviews, userviews, deptviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    path('', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),

     # This is admin panel
    path('Admin/AdminHome', adminviews.ADMINHOME, name='admin_home'),
    path('Admin/AddCategory', adminviews.ADD_CATEGORY, name='add_category'),
    path('Admin/ManageCategory', adminviews.MANAGE_CATEGORY, name='manage_category'),
    path('Admin/DeleteCategory/<str:id>', adminviews.DELETE_CATEGORY, name='delete_category'),
    path('UpdateCategory/<str:id>', adminviews.UPDATE_CATEGORY, name='update_category'),
    path('UpdateCategoryDetails', adminviews.UPDATE_CATEGORY_DETAILS, name='update_category_details'),
    path('Admin/AddSubcategory', adminviews.ADD_SUBCATEGORY, name='add_subcategory'),
    path('Admin/ManageSubcategory', adminviews.MANAGE_SUBCATEGORY, name='manage_subcategory'),
    path('Admin/DeleteSubcategory/<str:id>', adminviews.DELETE_SUBCATEGORY, name='delete_subcategory'),
    path('UpdateSubcategory/<str:id>', adminviews.UPDATE_SUBCATEGORY, name='update_subcategory'),
    path('UpdateSubcategoryDetails', adminviews.UPDATE_SUBCATEGORY_DETAILS, name='update_subcategory_details'),
    path('Admin/AddDepartment', adminviews.ADD_STATE, name='add_state'),
    path('Admin/ManageDepartment', adminviews.MANAGE_STATE, name='manage_state'),
    path('Admin/DeleteDepartment/<str:id>', adminviews.DELETE_STATE, name='delete_state'),
    path('UpdateDepartment/<str:id>', adminviews.UPDATE_STATE, name='update_state'),
    path('UpdateDepartmentDetails', adminviews.UPDATE_STATE_DETAILS, name='update_state_details'),
    path('LodgedComplaint', adminviews.LODGEDCOMPLAINTS, name='lodgedcomplaint'),
    #path('view-feedback/<int:complaint_id>/', adminviews.view_feedback, name='view_feedback'),

    path('ViewLodgedComplaint/<str:id>', adminviews.VIEWLODGEDCOMPLAINTS, name='viewlodgedcomplaint'),

    path('LodgedComplaintRemark', adminviews.LODGEDCOMPLAINTSREMARK, name='lodgedcomplaintremark'),
    # path('LodgedComplaintRemark', views.LODGEDCOMPLAINTSREMARKS, name='lodgedcomplaintremark'),
    path('ManageUser', adminviews.MANAGEUSERS, name='manageusers'),
    path('ViewUser/<str:id>',adminviews.VIEWUSERS, name='viewusers'),   
    path('Admin/DeleteUser/<str:id>', adminviews.DELETEUSERS, name='delete_user'),
    path('Admin/UserComplaints/<str:id>', adminviews.USERSCOMPLAINTS, name='view_complaints'),   
    path('NewComplaints', adminviews.NEWCOMPLAINTS, name='newcomplaints'),
    path('InprocessComplaints', adminviews.INPROCESSCOMPLAINTS, name='inprocesscomplaints'),
    #path('inprocess-complaints/', views.update_complaint_status, name='inprocess_complaints'),
    path('ClosedComplaints', adminviews.CLOSEDCOMPLAINTS, name='closedcomplaints'),
    path('ComplaintsBetweenDateReport', adminviews.COMPLAINTSREPORT, name='complaintsreports'),
    path('UserBetweenDateReport', adminviews.USERBDREPORT, name='userbdreports'),
    path('SearchComplaints', adminviews.Search_Complaints, name='searchcomplaints'),
    path('SearchUsers', adminviews.Search_Users, name='searchusers'),
    
    #path('EscalatedComplaints', adminviews.ESCALATEDCOMPLAINTS, name='escalatedcomplaints'),

    

     # This is user panel
    path('Comuser/UserHome', userviews.USERHOME, name='user_home'),
    path('usersignup/', userviews.USERSIGNUP, name='usersignup'),
    path('RegisterComplaint', userviews.REGCOMPLAINT, name='regcomplaint'),
    path('RegisterComplaint', views.register_complaint_email, name='register_complaint'),
    path('get_subcat/', userviews.get_subcat, name='get_subcat'),
    path('ComplaintHistory', userviews.COMPLAINTHISTORY, name='complainthistory'),
    path('ComplaintHistoryDetails/<str:id>', userviews.COMPLAINTHISTORYDETAILS, name='complainthistorydetails'),
    path('feedback/<int:complaint_id>/', views.feedback_form, name='feedback_form'),
    #path('edit_feedback/<int:complaint_id>/', views.edit_feedback, name='edit_feedback'),
    
    # This is dept panel
    path('dept_usersignup/', deptviews.DEPT_USERSIGNUP, name='dept_usersignup'),
    path('dept_login/', deptviews.DEPT_LOGIN, name='dept_login'),
    path('department/dashboard/', deptviews.DEPTHOME, name='dept_dashboard'),
    path('ViewComplaint/<str:id>', deptviews.VIEWCOMPLAINTS, name='viewcomplaint'),


    #profile path
    path('Profile', views.PROFILE, name='profile'),
    path('Profile/update', views.PROFILE_UPDATE, name='profile_update'),
    path('Password', views.CHANGE_PASSWORD, name='change_password'),
    path('notifications/', views.notifications, name='notifications'),
    
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
