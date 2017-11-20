# -*- coding: utf-8 -*-

import functools
from django.http import HttpResponseBadRequest

def ajax_required(func):
	@functools.wraps(func)
	def wrapper(request, *args, **kw):
		if not request.is_ajax():
			return HttpResponseBadRequest()
		return func(*args, **kw)
	return wrapper

