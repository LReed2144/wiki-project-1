from django.shortcuts import render
from markdown2 import Markdown

from . import util

#convert the markdown files under entry to html files.  
def convert(title):
    #gets title from util.py
    content = util.get_entry(title)
    #convert
    markdowner = Markdown()
    #checking to see if title exists 
    if content == None:
        return None
    else:
        return markdowner.convert(content)

# returns a template

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

#all entries 
def entry(request, title):
    #run convert function on markdown entries
    content = convert(title)
    if content == None:
        return render(request, "encyclopedia/error.html")
    else:
        return render(request, "encyclopedia/entry.html", {
            #key: value
            "title": title,
            "content": content
        })

def search(request):
    if request.method =="POST":
        search = request.POST['q']
        content = convert(search)
        if content is not None:
            return render(request, "encyclopedia/entry.html", {
            "title": search,
            "content": content
            })
        else: 
            entries = util.list_entries()
            suggestion = []
            for entry in entries:
                if search.lower() in entry.lower():
                    suggestion.append(entry)
            return render(request, "encyclopedia/search.html", {
                "suggestion": suggestion
            })