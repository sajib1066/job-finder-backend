from django.shortcuts import redirect
from django.views.generic import View


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return redirect('/admin/')
