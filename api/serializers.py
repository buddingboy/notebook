from rest_framework import serializers

from notebook.models import *


class NoteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Note
		fields = ('pk', 'title', 'source', 'details', 'prelims', 'paper', 'topic', 'date')


class IssueSerializer(serializers.ModelSerializer):
	class Meta:
		model = Issue
		fields = '__all__'
		# fields = ('title', 'source',)
