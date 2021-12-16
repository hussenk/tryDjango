from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string



def home(request):

    obj = Article.objects.get(id=1)

    doc = {
        'id':obj.id,
        'title' : obj.title,
        'content':obj.content
    }

    Html = render_to_string('home-view.html',context=doc )
    return HttpResponse(Html)