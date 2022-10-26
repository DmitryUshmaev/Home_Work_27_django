import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView

from Home_Work_27_django.settings import TOTAL_ON_PAGE
from ads.models import ADS, Category
from users.models import User


def ad(request):
    return JsonResponse({"status": "ok"}, status=200)


# View для отображения и добавления моделей объявлений


class ADListView(ListView):
    model = ADS

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.order_by('-price')
        paginator = Paginator(self.object_list, TOTAL_ON_PAGE)
        page = request.GET.get('page')
        obj = paginator.get_page(page)

        response = {}
        items_list = [{
            "id": ad.id,
            "name": ad.name,
            "author": ad.author.first_name,
            "price": ad.price,
            "description": ad.description,
            "category": ad.category.name,
            "is_published": ad.is_published
        } for ad in obj]

        response['items'] = items_list
        response['total'] = self.object_list.count()
        response['num_pages'] = paginator.num_pages

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class ADCreateView(CreateView):
    model = ADS
    fields = []

    def post(self, request, *args, **kwargs):
        ads_data = json.loads(request.body)
        author = get_object_or_404(User, username=ads_data['author'])
        category = get_object_or_404(Category, name=ads_data['category'])

        ad = ADS.objects.create(name=ads_data['name'],
                                author=author,
                                category=category,
                                price=ads_data['price'],
                                description=ads_data['description'],
                                is_published=ads_data['is_published']
                                )

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author.username,
            "price": ad.price,
            "description": ad.description,
            "category": ad.category.name,
            "is_published": ad.is_published
        })


class ADDetailView(DetailView):
    model = ADS

    def get(self, request, *args, **kwargs):
        try:
            ads = self.get_object()
        except ADS.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author.username,
            "price": ads.price,
            "description": ads.description,
            "category": ads.category.name,
            "is_published": ads.is_published
        }, json_dumps_params={"ensure_ascii": False}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class ADUpdateView(UpdateView):
    model = ADS
    fields = ['name']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        ads_data = json.loads(request.body)
        author = get_object_or_404(User, ads_data['author'])
        category = get_object_or_404(Category, ads_data['category'])

        if 'name' in ads_data:
            self.object.name = ads_data['name']
        if 'price' in ads_data:
            self.object.price = ads_data['price']
        if 'description' in ads_data:
            self.object.description = ads_data['description']
        if 'is_published' in ads_data:
            self.object.is_published = ads_data['is_published']

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": self.object.author.username,
            "price": self.object.price,
            "description": self.object.description,
            "category": self.object.category.name,
            "is_published": self.object.is_published
        })


@method_decorator(csrf_exempt, name='dispatch')
class ADDeleteView(DeleteView):
    model = ADS
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({'status': 'ok'}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class ADUploadImage(UpdateView):
    model = ADS
    fields = ['name']

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES.get('image')
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": self.object.author.username,
            "price": self.object.price,
            "description": self.object.description,
            "category": self.object.category.name,
            "is_published": self.object.is_published,
            "image": self.object.image.url if self.object.image else None
        })
