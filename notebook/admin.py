# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from notebook.models import Note, Paper, Issue, Bullet

# Register your models here.

# admin.site.register(Topic)


class PaperAdmin(admin.ModelAdmin):
    list_per_page = 50
    search_fields = ['paper_name']
    list_display = ['pk', 'paper_name']
    ordering = ['paper_name']

admin.site.register(Paper, PaperAdmin)


class NoteAdmin(admin.ModelAdmin):
    list_per_page = 50
    search_fields = ['title', 'details', 'topic', 'source', 'date']
    list_display = ['pk', 'prelims', 'title', 'date', 'details', 'topic', 'source']
    filter_horizontal = ['paper']
    list_filter = ['prelims']

admin.site.register(Note, NoteAdmin)


class IssueAdmin(admin.ModelAdmin):
    list_per_page = 50
    search_fields = ['title', 'details', 'source', 'date']
    list_display = ['title', 'details', 'source',]

admin.site.register(Issue, IssueAdmin)



class BulletAdmin(admin.ModelAdmin):
    list_per_page = 50
    search_fields = ['title', 'group', 'source', 'date']
    list_display = ['title', 'group', 'source',]

admin.site.register(Bullet, BulletAdmin)