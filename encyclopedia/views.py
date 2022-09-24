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
    html_content = convert(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html")
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })