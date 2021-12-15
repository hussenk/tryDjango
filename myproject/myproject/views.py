from django.http import HttpResponse

h1 ="""
<h1>Hello World </h1>
"""


def home(request):
    return HttpResponse(h1)