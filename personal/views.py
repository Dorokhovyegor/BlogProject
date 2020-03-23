from django.shortcuts import render

# Create your views here.

def home_screen_view(request):
	context = {}
	# context['some_string'] = "this is a some string, that i'm passing to the view"
	# context['some_number'] = 123432

	# context = {
	# 	'some_string': "какая-то строчка",
	# 	'some_number': 1234
	# }

	list_of_value = []
	list_of_value.append("first_entry")
	list_of_value.append("second_entry")
	list_of_value.append("third_entry")
	list_of_value.append("fourth_entry")

	context['list'] = list_of_value

	return render(request, "personal/home.html", context)