from django.shortcuts import HttpResponse, render
def index (request):
    return render(request, "form.html")
def results(request):
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
        return render (request, 'responses.html', context)
    return render (request, 'responses.html')
