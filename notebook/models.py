# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Paper(models.Model):
	paper_name = models.CharField(max_length=100, default=None, unique=True)


	def __unicode__(self):
		return u'%s' % (self.paper_name)


class Note(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    source = models.CharField(max_length=200, null=True, blank=True)
    details = models.TextField(max_length=5000, null=True, blank=True)
    paper = models.ManyToManyField(Paper, blank=True, related_name='paper')
    prelims = models.BooleanField(default=False)
    topic = models.CharField(max_length=100, null=True, blank=True)
    date = models.CharField(max_length=30, null=True, blank=True)


    def __unicode__(self):
		return u'%s %s' % (self.pk, self.title)



class Issue(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    details = models.TextField(max_length=5000, null=True, blank=True)
    source = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'[%s] %s' % (self.pk, self.title)



class Bullet(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, null=True, blank=True)
    label = models.CharField(max_length=200, null=True, blank=True)
    group = models.CharField(max_length=200, null=True, blank=True)
    meta = models.CharField(max_length=200, null=True, blank=True)
    source = models.CharField(max_length=200, null=True, blank=True)
    details = models.TextField(max_length=10000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return u'%s ---- %s %s %s' % (self.issue, self.pk, self.title, self.group)