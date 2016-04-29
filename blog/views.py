from django.shortcuts import render
from blog.models import Article,Tag,Classification
from django.template import RequestContext

# Create your views here.
def blog_list(request):
    blogs = Article.objects.all().order_by('-publish_time')
    return render(request,'index.html',{"blogs":blogs}) 
