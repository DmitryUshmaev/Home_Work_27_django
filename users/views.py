from django.core.paginator import Paginator
import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from Home_Work_27_django.settings import TOTAL_ON_PAGE
from ads.models import Category
from users.models import User, Location


class UserListView(ListView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.order_by('username')
        paginator = Paginator(self.object_list, TOTAL_ON_PAGE)
        page = request.GET.get('page')
        obj = paginator.get_page(page)

        response = {}
        items_list = [{
            "id": user.pk,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "role": user.role,
            "age": user.age,
            "locations": list(map(user.location.all())),
            "total_ads": user.ads.filter(is_published=True).count()
        } for user in obj]

        response['items'] = items_list
        response['total'] = self.object_list.count()
        response['num_pages'] = paginator.num_pages

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False}, status=200)


class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        try:
            user = self.get_object()
        except User.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse({
            "id": user.pk,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "role": user.role,
            "age": user.age,
            "locations": list(map(str, user.location.all())),
            "total_ads": user.ads.filter(is_published=True).count()
        }, json_dumps_params={"ensure_ascii": False}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ['name']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        data = json.loads(request.body)

        if 'first_name' in data:
            self.object.name = data['first_name']
        if 'price' in data:
            self.object.price = data['price']
        if 'description' in data:
            self.object.description = data['description']
        if 'is_published' in data:
            self.object.is_published = data['is_published']
        if 'locations' in data:
            for loc_name in data['locations']:
                loc, _ = Location.objects.get_or_create(name=loc_name)
                self.object.location.add(loc)

        self.object.save()

        return JsonResponse({
            "id": self.object.pk,
            "first_name": self.object.first_name,
            "last_name": self.object.last_name,
            "username": self.object.username,
            "role": self.object.role,
            "age": self.object.age,
            "locations": list(map(str, self.object.location.all())),
            "total_ads": self.object.ads.filter(is_published=True).count()
        })


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = ['name']

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        user = User.objects.create(
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            age=data['age'],
            role=data['role'],
        )

        if 'locations' in data:
            for loc_name in data['locations']:
                loc, _ = Location.objects.get_or_create(name=loc_name)
                user.location.add(loc)

        self.object.save()

        return JsonResponse({
            "id": user.pk,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "role": user.role,
            "age": user.age,
            "locations": list(map(str, user.location.all())),

        })


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({'status': 'ok'}, status=200)