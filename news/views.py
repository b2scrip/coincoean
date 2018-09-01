from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from news.models import Post

from django.views import View
from django.shortcuts import render

class NewsDetail(DetailView):
    model =  Post
    context_object_name = "news"
    template_name = "news/detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        super(NewsDetail, self).get_object().increase_views()
        context["re_posts"] = Post.objects.all().order_by('?')[:15]
        return context

class NewsHome(ListView):
    model = Post
    context_object_name = "qs_news"
    template_name = "news/home.html"
    paginate_by = 20
    ordering = ["-id"]
