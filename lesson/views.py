from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.


def all_materials(request):
    materials = models.Material.objects.all()
    return render(request,
                  'materials/all_materials.html',
                  {"materials": materials})


def material_details(requests, year, month, day, slug):
    material = get_object_or_404(models.Material,
                                 slug=slug,
                                 publish__year=year,
                                 publish__month=month,
                                 publish__day=day)
    return render(requests,
                  'materials/detail.html',
                  {'material': material})
