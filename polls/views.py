from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import ExtractedText

from PIL import Image
import pytesseract


# def index(request):

#     return render(request, 'polls/test.html')

def extract_text_from_image(request):
    if request.method == 'POST' and request.FILES['image']:
        category = request.POST.get('category', '')
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\PC\AppData\Local\Programs\Tesseract-OCR\tesseract'
        uploaded_image = request.FILES['image']
        print(category)
        # Open the uploaded image using Pillow (PIL)
        image = Image.open(uploaded_image)

        # Use pytesseract to extract text from thxe image
        extracted_text = pytesseract.image_to_string(image)

        return render(request, 'polls/result.html', {'extracted_text': extracted_text})

    return render(request, 'polls/form.html')

# def save_extracted_text(request):
#     if request.method == 'POST':
#         category = request.POST.get('category', '')
#         comments = request.POST.get('comments', '')
#         extracted_text = request.POST.get('extracted_text', '')

#         # Create a new ExtractedText object and save it to the database
#         extracted_text_obj = ExtractedText(
#             text=extracted_text,
#             category=category,
#             comments=comments
#         )
#         extracted_text_obj.save()

#         return redirect('text_saved')

#     return redirect('form')


def extract_text_form(request):
    return render(request, 'polls/form.html')

@require_POST
def save_extracted_text(request):
    category = request.POST.get('category', '')
    name = request.POST.get('name', '')
    extracted_text = request.POST.get('extracted_text', '')
    # Create a new ExtractedText object and save it to the database
    extracted_text_obj = ExtractedText(
        text=extracted_text,
        category=category,
        name=name,
    )
    extracted_text_obj.save()
    return redirect('text_saved')

def text_saved(request):
    return render(request, 'polls/text_saved.html')