from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ExtractedText  # Import your ExtractedText model

@login_required
def manage_extracted_text(request):
    user = request.user
    extracted_texts = ExtractedText.objects.filter(user=user)
    
    if request.method == 'POST':
        # Handle the form submission and text extraction here
        # You can use a similar approach as shown in previous answers
        
        return redirect('manage_extracted_text')
    
    return render(request, 'manage_extracted_text.html', {'extracted_texts': extracted_texts})