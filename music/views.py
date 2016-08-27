from models import Album, Song
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.urlresolvers import reverse


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

def favorite(request, album_id):
    album = get_object_or_404(Album, id=album_id)

    try:
        selected_song = album.song_set.get(id=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message':'You did not select a valid song!'
    })
    else:
        if selected_song.is_favorite == True:
            selected_song.is_favorite = False
            selected_song.save()
        else:
            selected_song.is_favorite=True
            selected_song.save()
    return HttpResponseRedirect(reverse('music:detail', args=album_id))

