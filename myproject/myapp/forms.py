from django import forms

class PDFForm(forms.Form):
    file = forms.FileField(label='Select a PDF file')
