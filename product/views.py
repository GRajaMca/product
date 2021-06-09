from django.http import JsonResponse


def productList(request):
    data = ["Nokia", "Samsung", "LG"]
    return JsonResponse(data, safe=False)
