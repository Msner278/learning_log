from django.shortcuts import render
from . import models
from . import form


# Create your views here.
def home(request):
    context = {
        'posts': models.Post.objects.all()
    }
    return render(request, 'blog/home.html', context=context)


def get_post(request):
    if request.method == 'POST':
        form_instance = form.PostForm(request.POST)
        if form_instance.is_valid():
            return
