from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Index(request):
	test_dict = {'1': 'one', '2': 'two'}
	return render(request, 'index.html', {'test_dict': test_dict})
