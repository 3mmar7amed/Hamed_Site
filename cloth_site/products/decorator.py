
from django.shortcuts import render , redirect


#look any func will have @unauthenticated_user will be sent here 
# if request.user.is_authenticated: apply this cindition on it and never call the method you have that sign above
# else :  okay go to login and apply it as usual
def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('sell')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'employee':
			return redirect('sell')

		if group == 'admin':
			return view_func(request, *args, **kwargs)

	return wrapper_function