from django.db import models

# imorting utility functions from utils.py
from .utils import code_generator, create_shortcode

# importing setting from conf
from django.conf import settings

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)


# making a model manager 
class UrlManager(models.Manager) :
	# customizing existing 'all()' method of models class
	def all(self, *args, **kwargs) :
		qs_main = super(UrlManager,self).all(*args,**kwargs)
		qs = qs_main.filter(active=True) # get only active url
		return qs

	# can also write own function to do a specific thing
	# example below function can change the shortcode for all the url in DB
	def refresh_shortcode(self) :
		qs = Url.objects.filter(id__gte=1) # all id greater than equal to 1
		for q in qs :
			q.shortcode = create_shortcode(q)
			q.save()



# it saves and map the url and their shotcode 
class Url(models.Model) :
	url 		 = models.URLField(max_length = 512, )
	shortcode 	 = models.CharField(max_length = SHORTCODE_MAX, unique = True, blank = True, ) # short code must be unique
	updated 	 = models.DateTimeField(auto_now = True, )		   # every time data is updated
	timestamp	 = models.DateTimeField(auto_now_add = True, )	   # when first time data is updated
	active 		 = models.BooleanField(default=True)				   # to check if url is still active
	num_of_click = models.IntegerField(default = 0)


	# link UrlManager with url Model
	objects = UrlManager()

	# alternatively can make own generic mamager
	# my_own = UrlManager()  -- call this like ==> qs = Url.my_own.refresh_shortcode(self)


	# overriding the 'save' method of django
	def save(self, *args, **kwargs) :
		if self.shortcode is None or self.shortcode == "" :
			self.shortcode = create_shortcode(self)
		super(Url, self).save(*args, **kwargs)


	# to display some info about data at django-admin
	def __str__(self) :
		return self.url + ' --> ' + self.shortcode 

	def __unicode__(self) :
		return str(self.url)	