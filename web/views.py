from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from Prediction_Module.mnist_nn_predict import predict
from .forms import ImageUploadForm
import json
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def upload_image(request):
    print '+'*100
    if request.method == 'POST':

        print request.FILES
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_object = form.save(commit=True)
            resut_dict = dict()
            resut_dict['name'] = image_object.image.name.split('/')[1]
            resut_dict['path'] = image_object.image.url
            resut_dict['label'], resut_dict['confidence'] = predict(image_object.image.path)
            return HttpResponse(json.dumps(resut_dict))
