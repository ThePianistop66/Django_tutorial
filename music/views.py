from models import Album
from django.shortcuts import render, get_object_or_404

def index(request):
    albums=Album.objects.all()
    context = {'albums': albums,}
    return render(request,'music/index.html',context)

def detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    '''
    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist.")
    '''
    return render(request, 'music/detail.html', {'album': album})