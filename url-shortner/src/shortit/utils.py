# this file contains all the utility function for code generator

# for random shortcode generator
import random
import string

from django.conf import settings

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6) # getting this value form projcets settings

# function to generate random shortcode
def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits + string.ascii_uppercase):
	# it will generate a random code of 6 character
	return ''.join(random.choice(chars) for _ in range(size) ) 



# this will generate a shortcode and check whether that shortcode exist in database 
def create_shortcode(instance, size=SHORTCODE_MIN) :
	new_code = code_generator(size=size)

	# url model class -- python method
	url_class = instance.__class__

	# querying whether new shortcode generated is unique or not
	qs_exist = url_class.objects.filter(shortcode = new_code).exists()

	if qs_exist :
		return create_shortcode(size = size) # recursively try until find an unique code

	return new_code