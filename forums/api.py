from tastypie.resources import ModelResource
from tastypie.constants import ALL
from django.contrib.auth.models import User
from models import Comment,Subject
from tastypie import fields


class UserResource(ModelResource):
	class Meta:
		queryset=User.objects.all()
		resource_name='user'

class SubjectResource(ModelResource):
	user=fields.ForeignKey(UserResource, 'sub_uid',null=True, blank=True,full=True)
	class Meta:
		queryset=Subject.objects.all()
		resource_name='subject'
		filtering={'id':ALL}	


class CommentResource(ModelResource):
	subject=fields.ForeignKey(SubjectResource, 'subject',null=True, blank=True,full=True)
	user=fields.ForeignKey(UserResource, 'user',null=True, blank=True,full=True)
	class Meta:
		queryset=Comment.objects.all()
		resource_name='comment'
		filtering={'id':ALL}

	