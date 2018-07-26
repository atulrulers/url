from django.urls import path
from django.conf.urls import  url

from . import views

urlpatterns = [
	
	# home page of website
	#create a new form
	url(r'^$', views.create_form, name='create_form'), 

	# Display shotened url
	url(r'pboat/(?P<shortcode>\w+)/$', views.display, name='display'),

	# terms-of-use docs
	url(r'^pboat/terms-of-use/$', views.terms_of_use, name='terms_of_use'),

	# shortcode/is_available/ -- to check whether current shortcode is available or not
	url(r'^shortcode/is_available/$', views.is_available , name='is_available'),

	# shortcode/click_count/ -- to check the total number of click that occured on shortened url
	url(r'^shortcode/click_count/$', views.click_count, name='click_count'),

	# a/shortcode[length between 6 and 15]
	url(r'^(?P<shortcode>\w+)/$', views.shortener_redirect, name='shortener_redirect'),
	
]