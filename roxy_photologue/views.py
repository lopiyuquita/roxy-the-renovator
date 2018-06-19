from django.conf import settings
from django.views.generic.list import ListView
from photologue.models import Gallery


class GalleryArchiveListView(ListView):
    paginate_by = 20
    template_name = 'photologue/gallery_archive_list.html'

    def get_queryset(self):
        queryset = Gallery.objects.filter(is_public=False)
        queryset = queryset.exclude(slug=settings.SLIDE_SHOW_SLUG)
        queryset = queryset.on_site().order_by('title')
        return queryset


class GalleryListView(ListView):
    queryset = Gallery.objects.on_site().is_public().order_by('-pk')
    paginate_by = 20
