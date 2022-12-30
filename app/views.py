from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def home(request):
    return render(request, 'app/pages/home.html')

def services(request):
    context = {}
    context['service'] = ''

    if request.method == 'POST':
        if request.FILES.get('img_1') != None:
            uploaded_file = request.FILES['img_1']
            context['service'] = 'img_1'
            
        if request.FILES.get('img_2') != None:
            uploaded_file = request.FILES['img_2']
            context['service'] = 'img_2'

        fileSystemStorage = FileSystemStorage()
        fileSystemStorage.save(uploaded_file.name, uploaded_file)
        context['url'] = fileSystemStorage.url(uploaded_file)
    return render(request, 'app/pages/services.html', context)
