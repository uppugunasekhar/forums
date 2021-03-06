from django.conf.urls import patterns, url,include
from forums import views
from api import CommentResource,SubjectResource

comment_resource=CommentResource()
subject_resource=SubjectResource()

urlpatterns = patterns('',
    url(r'^$',views.index, name ='index'),
    url(r'^(?P<subject_id>\d+)/$', views.discuss, name= 'discuss'),
    url(r'^login/$',views.login, name = 'login'),
    
    url(r'^logout/$',views.logout, name = 'logout'),
    url(r'^comment/(?P<subject_id>\d+)/$',views.comment, name = 'comment'),
    url(r'^invalid/$',views.invalid, name = 'invalid'),
    url(r'^register/$',views.register_user1, name= 'register'),
    url(r'^register1/$',views.register_user, name = 'register1'),
    url(r'^askqu/$',views.ask_question, name = 'askqu'),
    url(r'^questiondb/$',views.question_db, name = 'questiondb'),
    url(r'^api/',include(comment_resource.urls)),
    url(r'^api/',include(subject_resource.urls)),
    
)
