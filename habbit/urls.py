from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from hrm.api import mentorlist,Courselist,mentorid,courseid
from accounts.api import Registrationlist
from appointment.api import Appointmentlist,Appointmentid,Appointmentuserid,Appointmentmentorid
#from accounts.serializers import UserSerializer
from django.conf.urls import include
import rest_framework.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/mentors/$',mentorlist.as_view(),name='mentorlist'),
    url(r'^api/courses/$',Courselist.as_view(),name='courselist'),
    url(r'^api/courses/(?P<course_id>\d+)/$',courseid.as_view(),name='course-id'),
    url(r'^api/mentors/(?P<mentor_id>\d+)/$',mentorid.as_view(),name='mentor-id'),
    url(r'^api/accounts/$',Registrationlist.as_view(),name='signup'),
    url(r'^api/appointment/$',Appointmentlist.as_view(),name='appointment'),
    url(r'^api/appointment/(?P<id>\d+)/$',Appointmentid.as_view(),name='appointment-id'),
    url(r'^api/appointment/user/(?P<user_id>\d+)/$',Appointmentuserid.as_view(),name='appointment-user-id'),
    url(r'^api/appointment/mentor/(?P<mentor_id>.+)/$',Appointmentmentorid.as_view(),name='appointment-mentor-id'),
    #path('api/auth/',include('djoser.urls.authtoken')),
   
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]