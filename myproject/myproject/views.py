from django.http import HttpResponse
from articles.models import Article




def home(request):

    obj = Article.objects.get(id=1)
    h1 =f"""
    <h1>{obj.title}</h1>
    <p>{obj.content}</p>
    """
    return HttpResponse(h1)