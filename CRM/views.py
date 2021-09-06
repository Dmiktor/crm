import mimetypes

from django.http import HttpResponse
from django.templatetags.static import static


def download_file(request, file):
    # fill these variables with real values
    fl_path = static / file
    filename = file

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
