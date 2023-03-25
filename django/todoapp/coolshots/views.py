from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods

from .models import Coolshot

# Create your views here.


def index(request):
    coolshots = Coolshot.objects.all()
    return render(request, "coolshot.html", {"coolshot_list": coolshots})
    # return HttpResponse("Hello World!!")


@require_http_methods(["POST"])
def add(request):
    # if request.method == "POST":
    units = request.POST["units"]
    food = request.POST["food"]
    patient = request.POST["patient"]
    coolshot = Coolshot(units=units, food=food, patient=patient)
    coolshot.save()
    return redirect("index")


def update(request, coolshot_id):
    coolshot = Coolshot.objects.get(id=coolshot_id)
    coolshot.complete = not coolshot.complete
    coolshot.save()
    return redirect("index")

def delete(request, coolshot_id):
    coolshot = Coolshot.objects.get(id=coolshot_id)
    coolshot.delete()
    return redirect("index")

def home(request):
    return render(request, "cool.html")

