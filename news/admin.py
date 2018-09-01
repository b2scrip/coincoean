from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import Post


admin.site.register(Post)
