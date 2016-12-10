from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import ImageUpload
# Create your views here.


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        pass
