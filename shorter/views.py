from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views import View

from analytics.models import ClickEvent

from .models import CutURL
from .forms import SubmitUrlForm


def home_view_fbv(request, *args, **kwargs):
    if request.method == "POST":
        print(request.POST)
    return render(request, "home.html", {})


class HomeView(View):
    def get(self, request , *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "cut",
            "form": the_form
        }
        return render(request, "home.html", context)

    def post(self,request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "cut",
            "form": form
        }
        template = "home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = CutURL.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created,
                "title": "cut",
            }
            if created:
                template = "success.html"
            else:
                template = "in.html"
        return render(request, template, context)


class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = CutURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)


# this the static page
class AboutPage(View):
    def get(self, request):
        return render(request, "about.html")