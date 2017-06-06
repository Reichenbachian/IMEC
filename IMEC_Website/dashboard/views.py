from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from django.contrib.auth.views import login as loginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from itertools import chain

from IMEC import settings
from .models import Entry, User, Employee, GroupID, VolunteerID
from .forms import LoginForm

import urllib


def index(request):
	# Render the HTML template index.html with the data in the context variable
	return render(request, 'dashboard/index.html')

def scan(request):
	return render(request, 'dashboard/scan.html')

def search(request):
	return render(request, 'dashboard/search.html')

def login_page(request):
	next = request.GET.get('next', '/employee')
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(next)
			else:
				return HttpResponse("Inactive user.")
		else:
			return HttpResponseRedirect("/login/")

	return render(request, "dashboard/login.html", {'redirect_to': next})

# def employeeHome(request, username):
def employeeHome(request):
    #user = get_object_or_404(User, username=username)
	if request.method == 'POST':
		# for now we're assuming that all POST requests are to create groupIDs
		u = request.user
		emp = u.employee
		groupName = request.POST['groupName']
		new_group_id = GroupID(groupName=groupName, issuedBy=emp)
		new_group_id.save()
	return render(request, 'dashboard/employee.html', {'profile_user': request.user})

def test(request):
	return render(request, "dashboard/test.html")

def getSearchResults(request, limit=10):
	# try:
	query = request.POST.get("queryBar")
	catNumberResults = queryToDict(Entry.objects.filter(catNumber__contains=query))
	siteNumberResults = queryToDict(Entry.objects.filter(siteNumber__contains=query))
	localityResults = queryToDict(Entry.objects.filter(locality__contains=query))
	siteResults = queryToDict(Entry.objects.filter(site__contains=query))
	nameResults = queryToDict(Entry.objects.filter(name__contains=query))
	situationResults = queryToDict(Entry.objects.filter(situation__contains=query))
	results = catNumberResults+siteNumberResults+localityResults+siteResults+nameResults+situationResults
	return JsonResponse(results[:limit], safe=False)
	# except:
		# return HttpResponseRedirect("/dashboard")

def queryToDict(queryResults):
	daList = []
	for res in queryResults:
		daList.append(Entry.toDict(res))
	return daList
