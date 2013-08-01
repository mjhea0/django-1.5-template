from users.forms import RegistrationForm
from users.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)

		if form.is_valid():
			new_user = User(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password'],
				email=form.cleaned_data['email'],
				dob=form.cleaned_data['dob'],
				)

			new_user.set_password(form.cleaned_data['password'])

			new_user.save()

			return render_to_response('users/register_success.html', {'form': form}, context_instance=RequestContext(request))
	else:
		form = RegistrationForm()

	return render_to_response("users/register.html", {'form': form}, context_instance=RequestContext(request))
