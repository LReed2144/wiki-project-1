from django.shortcuts import render
from markdown2 import Markdown
import random
from . import util

#convert the markdown files under entry to html files.  
#get the content of the encyclopedia entry
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


#get content of the entry by calling the util function 
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

#all entries 
def entry(request, title):
    #run convert function on markdown entries
    content = convert(title)
    # if content does not exist render 404 page
    if content == None:
        return render(request, "encyclopedia/404.html")
    else:
    #exists- presented with a page
        return render(request, "encyclopedia/entry.html", {
            #key: value
            "title": title,
            "content": content
        })

#search bar
def search(request):
    #going to be adding something to the page so use POST
    if request.method =="POST":
        search = request.POST['q']
        # md to html
        content = convert(search)
        #if someone types in a search item that is not a page display error message
        if content == None: 
            return render(request, "encyclopedia/error.html", {
            "message": "This entry does not exist"
        })
        #if someone types in a search item that is a page display page
        elif content is not None:
            return render(request, "encyclopedia/entry.html", {
            "title": search,
            "content": content
            })
        else: 
            #if someone types in part of a title that is a page, display options of pages that are clickable to that page
            entries = util.list_entries()
            suggestion = []
            for entry in entries:
                #to find parts of words
                if search.lower() in entry.lower():
                    suggestion.append(entry)
            return render(request, "encyclopedia/search.html", {
                "suggestion": suggestion
            })

 

 #new page

def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        #create a variable to get data we have in our form 
        title = request.POST['title']
        content = request.POST['content']
        #use util.py to check the get entry
        titleExist = util.get_entry(title)
        if titleExist is not None:
            return render(request, 'encyclopedia/error.html', {
                "message": "Entry page already exists"
            })
        else:
            util.save_entry(title, content)
            content = convert(title)
            title = convert(content)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": content
            })



#edit
def edit(request):
    if request.method == "POST":
        #grab entry title
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })

#to save the edit 
def save_edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        content = convert(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": content
        })
#####fix the save entry page#####currently returning to layout.html

#random function

def rand(request):
    allEntries =util.list_entries()
    rand_entry = random.choice(allEntries)
    content = convert(rand_entry)
    return render(request, "encyclopedia/entry.html", {
        "title": rand_entry,
        "content": content
    })