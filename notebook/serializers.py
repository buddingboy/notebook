from rest_framework import serializers

from .models import *


class NoteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Note
		fields = ('pk', 'title', 'source', 'details', 'prelims', 'paper', 'topic', 'date')


class IssueSerializer(serializers.ModelSerializer):
	class Meta:
		model = Issue
		fields = '__all__'
		# fields = ('title', 'source',)


class BulletSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bullet
		fields = '__all__'
		# fields = ('title', 'source',)
