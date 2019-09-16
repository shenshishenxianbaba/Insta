# Create your views here.
# 当有人调用view时，显示templates中test.html
# Class-Based Views根据不同场景需求,django提供各种view类型，可继承相似类型 class dog : animal继承

from django.views.generic import TemplateView, ListView, DetailView
from Insta.models import Post

# HelloWorld is-a TemplateView

# class-based view
class HelloWorld(TemplateView):
    template_name = 'test.html'

#这个继承的时listview
class PostsView(ListView):
    model = Post
    template_name = 'index.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'