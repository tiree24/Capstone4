from django.shortcuts import render
from django.http import HttpResponseServerError

# Create your views here.
def my_test_500_view(request):
        # Return an "Internal Server Error" 500 response code.
        return HttpResponseServerError()