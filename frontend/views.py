from django import forms
from django.shortcuts import render, HttpResponse
from .forms import NoteForm
from api.models import Note
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def index(request):
    return render(request, 'frontend/index.html')

def formview(request):
    form = NoteForm()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            summary = note.summary
            context = {'note': note.body, 'summary': summary.summary}
            return render(request, 'frontend/summary.html', context=context)

    context = {'form': form}
    return render(request, 'frontend/forms.html', context=context)

def pdfview(request):
    note = Note.objects.latest('created')
    summary = note.summary
    template_path = 'frontend/pdf.html'
    context = {'note': note.body, 'summary': summary.summary}
    response = HttpResponse(content_type='application/pdf')
    # fro download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # for display
    response['Content-Disposition'] = 'filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
