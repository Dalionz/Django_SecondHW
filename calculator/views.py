from django.http import HttpResponse
from django.shortcuts import render


def omlet(request):
    person = int(request.GET.get("servings", 1))
    print(person)
    context = {
        'recipe': {
            'яйца, шт': 2 * person,
            'молоко, л': 0.1 * person,
            'соль, ч.л.': 0.5 * person,
        }
    }

    return render(request, 'calculator/index.html', context)


def pasta(request):
    person = int(request.GET.get("servings", 1))
    print(person)
    context = {
        'recipe': {
            'макароны, г': 0.3 * person,
            'сыр, г': 0.05 * person,
        }
    }

    return render(request, 'calculator/index.html', context)

def buter(request):
    person = int(request.GET.get("servings", 1))
    print(person)
    context = {
        'recipe': {
            'хлеб, ломтик': 1 * person,
            'колбаса, ломтик': 1 * person,
            'сыр, ломтик': 1 * person,
            'помидор, ломтик': 1 * person,
        }
    }

    return render(request, 'calculator/index.html', context)
