from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hellp, world. You're at the polls index.")