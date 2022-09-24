from django.shortcuts import render

from . import util

# returns a template

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

