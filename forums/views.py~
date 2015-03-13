from django.shortcuts import render, get_object_or_404, render_to_response 
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from forums.models import Subject,Comment,User
from django.utils import timezone
import datetime
import urllib2
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    sub_list = Subject.objects.order_by('-pub_date')[:]
    context = {'sub_list' : sub_list}
    return render(request, 'forums/index.html',context)
    
def discuss(request, subject_id):
    s = get_object_or_404(Subject, pk = subject_id)
    c = s.comment_set.filter(subject = subject_id)
    return render(request, 'forums/discuss.html', {'c' : c, 's' : s})

#@login_required  
def comment(request, subject_id):
    #ipdb.set_trace()
    com = request.POST.get('txt_comment', '')
    com_time = timezone.now()
    subject_obj =Subject.objects.get(id = subject_id)
    d = Comment()
    d.subject = subject_obj
    d.text = com
    d.time = com_time
    d.user = request.user
    d.save()
    return HttpResponseRedirect(reverse('forums:discuss', args=(subject_id,)))
 

def ask_question(request):
	g={}
	g.update(csrf(request))
	return render(request,'forums/askquestion.html',g)

def question_db(request):
	if request.method=='POST':
		question = request.POST.get('askqu','')
		questiondes = request.POST.get('askdes', '')
		current_time=timezone.now()	
		questionask = Subject(subject_title=question, subject_desc=questiondes, pub_date=current_time,sub_uid=request.user)
		questionask.save()
		return HttpResponseRedirect('/')
    
def login(request):
	if request.method=='POST':
		username = request.POST.get('username','')
		password = request.POST.get('password', '')
		askques=urllib2.unquote(request.GET.get('next'))
		user=auth.authenticate(username=username, password=password)
	
		if user is not None:
			auth.login(request, user)
			if askques is None:
				return HttpResponseRedirect('/')
			else:
				return HttpResponseRedirect('/askqu')
		else:	
			return HttpResponseRedirect('/invalid')	
	else:
		return render(request,'forums/login.html')


		

def invalid(request):
	return render_to_response('forums/invalid_login.html')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/login')

def register_user1(request):
	args={}
	args.update(csrf(request))
	return render_to_response('forums/register.html',args)	

def register_user(request):
	if request.method=='POST':
		username = request.POST.get('username','')
		password = request.POST.get('password', '')
		email=request.POST.get('email','')	
		user = User.objects.create_user(username, email, password)
		user.save()
		return HttpResponseRedirect('/login')
