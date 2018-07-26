from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# importing models
from .models import Url
# importing forms
from .forms import UrlForm


# redirects the short url
def shortener_redirect(request, shortcode=None):
	url_object = get_object_or_404(Url, shortcode=shortcode)
	url_object.num_of_click = url_object.num_of_click + 1
	url_object.save()
	return HttpResponseRedirect(url_object.url)


# create form to provide user to create a new url
def create_form(request) :
	context = {}
	if request.method == 'POST' :
		form = UrlForm(request.POST)
		if form.is_valid() :
			form.save(commit=False)
			invalid_url = False
			shrinked_url = form.save()
			form = UrlForm()
			context = {
				'form' : form,
				'shrinked_url' : shrinked_url,
				'invalid_url' : invalid_url,
			}
			print(shrinked_url.shortcode)
			return HttpResponseRedirect(reverse('display', kwargs = {'shortcode' : shrinked_url.shortcode } ))
			# return render(request,'shortit/short-url.html', context)

		else :
			count = Url.objects.count()
			invalid_url = True
			context = {
				'form' : form,
				'invalid_url' : invalid_url,
				'count' : count,
			}

			return render(request,'shortit/index.html', context)
	else :
		count = Url.objects.count()
		form    = UrlForm()
		context = {
			'form' : form,
			'count' : count,
		}
	return render (request,'shortit/index.html', context)


# display newly shortened url

def display(request, shortcode) :
	shrinked_url = get_object_or_404(Url, shortcode=shortcode)
	form = UrlForm()
	invalid_url = False
	count = Url.objects.count()
	context = {
		'form' : form,
		'shrinked_url' : shrinked_url,
		'invalid_url' : invalid_url,
		'count' 	  : count,
	}
	return render(request,'shortit/short-url.html', context)


# This function will check whether custom shortcode is available or not
def is_available(request) :
	context = {}
	is_available = False
	if request.method == "POST" :
		shortcode = request.POST['shortcode']
		try :
			obj = get_object_or_404(Url, shortcode=shortcode)
			is_available = False
		except Http404:
			is_available = True

	context['is_available'] = is_available;

	return JsonResponse(context)


# This function returns the total number of click on shortened url if url is created
def click_count(request) :
	context = {}
	is_available = False
	total_click = 0
	if request.method == "POST":
		shortcode = request.POST['shortcode']
		print(shortcode)
		try :
			url_object = get_object_or_404(Url, shortcode=shortcode)
			is_available = False
			total_click = url_object.num_of_click
			print(url_object)
		except Http404 :
			is_available = True
	context = {
		'is_available' : is_available,
		'total_click'  : total_click,
	}
	return JsonResponse(context)


#redirect to terms of use
def terms_of_use(request) :
	return render(request, 'shortit/terms-of-use.html', {})
