from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from hrm.api import mentorlist,Courselist,mentorid,courseid

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/mentors/$',mentorlist.as_view(),name='mentorlist'),
    url(r'^api/courses/$',Courselist.as_view(),name='courselist'),
    url(r'^api/courses/(?P<course_id>\d+)/$',courseid.as_view(),name='course-id'),
    url(r'^api/mentors/(?P<mentor_id>\d+)/$',mentorid.as_view(),name='mentor-id'),
]
