from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from .ai import *

# Create your views here.
@csrf_exempt
def main(request):
    if request.method != "POST":
        return HttpResponse("NOT FOUND")
    
    img = Image.open(request.FILES["image"])

    response = HttpResponse(content_type="image/jpeg")

    tensor = image_to_tensor(img)
    out_tensor = predict(tensor)

    out = lab_to_rgb(tensor, out_tensor.detach())[0]

    scaled_out = (out * 255).astype(np.uint8)

    out_img = Image.fromarray(scaled_out, mode="RGB")

    out_img.save(response, "JPEG")

    return response