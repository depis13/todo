from django.contrib import admin

from tasks.models import Commentary, Task, TaskDesk, MidTextFile, HeadTextFile, CommentaryFile


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'create_user',
        'task_id',
        'head_text',
        'mid_text',
        'task_desk',
        'creation_timestamp'
    )


@admin.register(TaskDesk)
class TaskDeskAdmin(admin.ModelAdmin):
    list_display = (
        'create_user',
        'organisation',
        'name',
        'creation_timestamp'
    )


@admin.register(HeadTextFile)
class HeadTextFileAdmin(admin.ModelAdmin):
    list_display = (
        'create_user',
        'file',
        'task',
        'creation_timestamp',
    )


@admin.register(MidTextFile)
class MidTextFileAdmin(admin.ModelAdmin):
    list_display = (
        'create_user',
        'file',
        'task',
        'creation_timestamp',
    )


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = (
        'create_user',
        'task',
        'text',
        'creation_timestamp',
    )


@admin.register(CommentaryFile)
class CommentaryFile(admin.ModelAdmin):
    list_display = (
        'commentary',
        'file',
        'creation_timestamp',
    )
