from django.conf.urls import url
from notebook import views

urlpatterns = [
	url(r'^$', views.notebook, name='notebook'),
	url(r'^notes/$', views.notes, name='note_post'),
	url(r'^notes/(?P<pk>[0-9]+)$', views.note_details, name='note_details'),
	url(r'^notes/delete/(?P<pk>[0-9]+)$', views.note_delete, name='note_delete'),


	url(r'^issues/$', views.issues, name='issues'),

	url(r'^issues/api/$', views.api_issues, name='api_issues'),
	url(r'^issues/api/(?P<pk>[0-9]+)$', views.api_issues_details, name='api_issues_details'),


	url(r'^bullets-notes/api/$', views.api_bulletnotes, name='api_bulletnotes'),
	url(r'^bullets-notes/api/(?P<pk>[0-9]+)$', views.api_bulletnotes_details, name='api_bulletnotes_details'),





	]