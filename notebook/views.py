# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response

from notebook.models import Note, Paper, Issue, Bullet
from .serializers import *

from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from django.db.models import Q

# results = BlogPost.objects.filter(Q(title__icontains=your_search_query) | Q(intro__icontains=your_search_query))


def notebook(request):

	if request.GET.get('q'):
		query = request.GET.get('q')
		s_area = request.GET.get('s_area')
		if s_area == 'title':
			All_notes = Note.objects.filter(Q(title__icontains=query)).order_by('-id')
		elif s_area == 'details':
			All_notes = Note.objects.filter(Q(details__icontains=query)).order_by('-id')
		else:
			All_notes = Note.objects.filter(Q(title__icontains=query) | Q(details__icontains=query)).order_by('-id')
	else:
		All_notes = Note.objects.all().order_by('-id')
		print All_notes

	page_size = request.GET.get('page_size', 15)
	page = request.GET.get('page', 1)

	paginator = Paginator(All_notes, page_size)

	try:
		task = paginator.page(page)
	except PageNotAnInteger:
		task = paginator.page(1)
	except EmptyPage:
		task = paginator.page(paginator.num_pages)

	papers = Paper.objects.all().order_by('id')

	return render(request,"notebook/notebook.html",{"posts":task, "papers": papers})




@api_view(['GET', 'POST'])
def notes(request):

	if request.method == 'GET':
		task = Note.objects.all()
		serializer = NoteSerializer(task, many=True)
		print serializer.data
		# response_data = {}
		# response_data['mcq']= serializer.data
		print 'lolo'
		return Response(serializer.data)

	elif request.method == 'POST':
		print request.data
		serializer = NoteSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(
				serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def note_details(request, pk):
	"""
	Get, udpate, or delete a specific task
	"""
	try:
		task = Note.objects.get(pk=pk)
		print task
	except Note.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = NoteSerializer(task)
		print serializer
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = NoteSerializer(task, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(
				serilizer.errors, status=status.HTTP_400_BAD_REQUEST)


	elif request.method == 'PUT':
		serializer = NoteSerializer(task, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(
				serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		task.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def note_delete(request, pk):
	"""
	Get, udpate, or delete a specific task
	"""
	try:
		task = Note.objects.get(pk=pk)
		print task
	except Note.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	task.delete()
	return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def issues(request):
	if request.method == 'GET':

		issue_title = request.GET.get('issue')

		if issue_title:
			all_isssue = Issue.objects.filter(title__icontains=issue_title).order_by('-id')
		else:
			all_isssue = Issue.objects.all().order_by('-id')

		page_size = request.GET.get('page_size', 15)
		page = request.GET.get('page', 1)
		paginator = Paginator(all_isssue, page_size)

		try:
			task = paginator.page(page)
		except PageNotAnInteger:
			task = paginator.page(1)
		except EmptyPage:
			task = paginator.page(paginator.num_pages)

		return render(request,"notebook/issue/issue.html",{"issues":task,})

	elif request.method == 'POST':
		print request.data
		serializer = IssueSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(
				serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def api_issues(request):

	if request.method == 'GET':
		task = Issue.objects.all()
		serializer = IssueSerializer(task, many=True)
		print serializer.data
		return Response(serializer.data)

	elif request.method == 'POST':
		print request.data
		serializer = IssueSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(
				serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def api_issues_details(request, pk):
	"""
	Get, udpate, or delete a specific task
	"""
	try:
		task = Issue.objects.get(pk=pk)
		print task
	except Issue.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = IssueSerializer(task)
		print serializer
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = IssueSerializer(task, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(
				serilizer.errors, status=status.HTTP_400_BAD_REQUEST)


	elif request.method == 'PUT':
		serializer = IssueSerializer(task, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(
				serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		task.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def api_bulletnotes(request):

	if request.method == 'GET':
		task = Bullet.objects.all()
		serializer = BulletSerializer(task, many=True)
		print serializer.data
		return Response(serializer.data)

	elif request.method == 'POST':
		print request.data
		serializer = BulletSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(
				serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def api_bulletnotes_details(request, pk):
	"""
	Get, udpate, or delete a specific task
	"""
	try:
		task = Bullet.objects.get(pk=pk)
		print task
	except Bullet.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = BulletSerializer(task)
		print serializer
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = BulletSerializer(task, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(
				serilizer.errors, status=status.HTTP_400_BAD_REQUEST)


	elif request.method == 'PUT':
		serializer = BulletSerializer(task, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(
				serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		task.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)