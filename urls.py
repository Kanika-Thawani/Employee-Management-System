from django.urls import path
from employee import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[path('',views.index,name="index"),

path('insert',views.insert,name="insert"),
path('logpag',views.logpag,name="logpag"),
path('admdash',views.admdash,name="admdash"),
path('empdash',views.empdash,name="empdash"),
path('login',views.login,name="login"),
path('logout',views.logout,name="logout"),
path('viewApplicants',views.viewApplicants,name="viewApplicants"),
path('viewEmployees',views.viewEmployees,name="viewEmployees"),
path('viewemp',views.viewemp,name="viewemp"),
path('addEmployees/<int:id>',views.addEmployees,name="addEmployees"),
path('update/<int:id>',views.update,name="update"),
path('deleteApplicant/<int:id>',views.deleteApplicant,name="deleteApplicant"),
path('deleteEmployee/<int:id>',views.deleteEmployee,name="deleteEmployee"),
path('requestleave',views.requestleave,name="requestleave"),
path('leaveRequests',views.leaveRequests,name="leaveRequests"),
path('approveLeave/<int:id>',views.approveLeave,name="approveLeave"),
path('rejectleave/<int:id>',views.rejectLeave,name="rejectLeave"),
path('leaveStatus/<int:id>',views.leaveStatus,name="leaveStatus"),
path('issueNotice',views.issueNotice,name="issueNotice"),
path('viewNotice',views.viewNotice,name="viewNotice")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)