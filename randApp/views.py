from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .utils import process_text

def form_page(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        if 'text_file' not in request.FILES:
            return redirect('form_page')

        file = request.FILES['text_file']

        try:
            file_content = file.read().decode('utf-8-sig')
        except:
            return redirect('form_page')

        mixed_text = process_text(file_content)

        request.session['result_text'] = mixed_text

        return redirect('result_page')
    return render(request, 'randApp/form.html')

def result_page(request: HttpRequest) -> HttpResponse:
    result = request.session.pop('result_text', 'No text provided.')

    context = {
        'result_text': result,
    }
    return render(request, 'randApp/result.html', context)