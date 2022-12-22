from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import PDFForm
from .models import PDF
from PyPDF2 import PdfFileReader

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFForm(request.POST, request.FILES)
        if form.is_valid():
            # extract text from PDF
            pdf_file = request.FILES['file']
            pdf = PdfFileReader(pdf_file)
            text = ""
            for page in pdf.pages:
                text += page.extractText()
            # save PDF and text to database
            pdf_obj = PDF(file=pdf_file, text=text)
            pdf_obj.save()
            return redirect('pdf_list')
    else:
        form = PDFForm()
    return render(request, 'myapp/upload_pdf.html', {'form': form})




def pdf_list(request):
    pdfs = PDF.objects.all()
    return render(request, 'myapp/pdf_list.html', {'pdfs': pdfs})