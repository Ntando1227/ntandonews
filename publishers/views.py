from django.shortcuts import render
from .models import Publisher


def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, "publishers/publisher_list.html", {"publishers": publishers})
