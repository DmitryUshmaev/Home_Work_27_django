import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category, ADS


def ads(request):
    return JsonResponse({"status": "ok"}, status=200)


# View для отображения и добавления моделей категорий


@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()

        response = []

        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name,

            })

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False}, status=200)

    def post(self, request):
        category_data = json.loads(request.body)

        category = Category()
        category.name = category_data["name"]
        category.save()

        return JsonResponse({
            "id": category.id,
            "name": category.name
        })


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        try:
            category = self.get_object()
        except Category.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse({
            "id": category.id,
            "name": category.name
        }, json_dumps_params={"ensure_ascii": False}, status=200)


# View для отображения и добавления моделей объявлений


@method_decorator(csrf_exempt, name='dispatch')
class ADSView(View):
    def get(self, request):
        adss = ADS.objects.all()

        response = []

        for ads in adss:
            response.append({
                "id": ads.id,
                "name": ads.name,
                "author": ads.author,
                "price": ads.price,
                "description": ads.description,
                "address": ads.address,
                "is_published": ads.is_published

            })

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False}, status=200)

    def post(self, request):
        ads_data = json.loads(request.body)

        ads = ADS()
        ads.name = ads_data["name"]
        ads.author = ads_data["author"]
        ads.price = ads_data["price"]
        ads.description = ads_data["description"]
        ads.address = ads_data["address"]
        ads.is_published = ads_data["is_published"]
        ads.save()

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published
        })


class ADSDetailView(DetailView):
    model = ADS

    def get(self, request, *args, **kwargs):
        try:
            ads = self.get_object()
        except ADS.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published
        }, json_dumps_params={"ensure_ascii": False}, status=200)
