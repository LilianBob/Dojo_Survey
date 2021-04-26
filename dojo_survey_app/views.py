from django.shortcuts import HttpResponse, render, redirect
def index (request):
    return render(request, "form.html")
def add_user(request):
    if request.method =="POST":
        name = request.POST["name"]
        location = request.POST["location"]
        language = request.POST["language"]
        comment = request.POST["comment"]
        context = {
            "name": name,
            "location":location,
            "language": language,
            "comment":comment
        }
        # # return render (request, 'responses.html', context)
        # return redirect ('/')

        request.session["name"]= name
        request.session["location"]= location
        request.session["language"]= language
        request.session["comment"]= comment
        if 'counter' in request.session:
            request.session['counter'] += 1
        else:
            request.session['counter'] = 1
        return redirect('/results')
def results(request):
    return render(request, 'responses.html')
def go_back(request):
    return redirect ('/')
    