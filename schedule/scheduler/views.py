from django.shortcuts import render, redirect

def home(request):
	return render(request, 'home.html')

def new_appointment(request):
	return render(request, 'new_appointment.html')

def new_client(request):
	return render(request, 'new_client.html')

def directory(request):
	return render(request, 'directory.html')

def statistics(request):
	return render(request, 'statistics.html')