from django.shortcuts import render, redirect
from markdown2 import Markdown
import random
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import bleach

from . import util
from . import forms

def index(request):
    return render(request, "encyclopedia/index.html", {
        "header": "All Pages",
        "entries": util.list_entries()
    })

 
def lookup_entries(request, title):
    """
    Checks if an entry or a substring of an entry exists.
    If entry exists returns entry.
    If no entry but substring returns list of entries with substring.
    If no entry or substring returns error page.
    """
    markdowner = Markdown()
    entries = util.list_entries()
    matches = [entry for entry in entries if title.lower() in entry.lower()]
    if not matches:
        return render(request, "encyclopedia/index.html", {
            "title": title,
            "header": "Error",
            "content": "This entry does not exist"      
        })

    exact_match = [match for match in matches if title.lower() == match.lower()]
    if exact_match:
        return render(request, "encyclopedia/entry.html", {
                "title": exact_match[0],
                "content": markdowner.convert(util.get_entry(exact_match[0])),
            })
    return render(request, "encyclopedia/index.html", {
                "header": "Search Results",
                "entries": matches
            })
    

def search(request):
    """
    Takes user input from search form and returns 
    search result. If no input returns index page.
    """
    if request.method == "POST":
        title = request.POST['q']
        if title:
            return lookup_entries(request, title)
        else:
            return index(request)
        

def random_search(request):
    """
    Returns a random entry.
    """
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return lookup_entries(request, random_entry)
 
    
def edit(request, title):
    """
    Directs user to edit page.
    Edits entry and saves changes, then 
    redirects user to updated entry-page.
    """
    if request.method == "GET":
        return render(request, "encyclopedia/edit.html",{
            "title": title,
            "content": util.get_entry(title)
        })
    if request.method == "POST":
        # bleach to avoid attacks
        content = bleach.clean(request.POST['changes']).encode("utf-8")
        if len(content) > 1e9:
            return render(request, "encyclopedia/index.html", {
                    "title": title,
                    "header": "Error",
                    "content": "This entry exceeds the maximum number of words allowed"      
                })
        util.save_entry(title, content)
    return redirect('wiki:lookup_entries', title)


def new_page(request):
    """
    Allows user to create and save a new entry.
    If entry already exist returns error.
    """
    if request.method == "GET":
        return render(request, "encyclopedia/newentry.html",{
            "title": "Create New Page",
            "form": forms.NewEntry
        })
    if request.method == "POST":
        form = forms.NewEntry(request.POST)
        if form.is_valid():
            # bleach to avoid attacks
            title = bleach.clean(form.cleaned_data["title"])
            content = bleach.clean(form.cleaned_data["content"]).encode("utf-8")
            filename = f"entries/{title}.md"
            if default_storage.exists(filename):
                return render(request, "encyclopedia/index.html", {
                    "title": title,
                    "header": "Error",
                    "content": "This entry already exist"      
                })
            else:
                default_storage.save(filename, ContentFile(content))
                return redirect('wiki:lookup_entries', title)
        else:
            return render(request, "encyclopedia/newentry.html", {
                "form": form
                })


