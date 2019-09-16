# Create your views here.
# 当有人调用view时，显示templates中test.html
# Class-Based Views根据不同场景需求,django提供各种view类型，可继承相似类型 class dog : animal继承

from django.views.generic import TemplateView

# HelloWorld is-a TemplateView

# class-based view
class HelloWorld(TemplateView):
    template_name = 'test.html'