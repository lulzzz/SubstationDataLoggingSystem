from django.shortcuts import render
import json
from django.http import JsonResponse
from . import services
# Create your views here.
def insertReadings(request):
	if request.method == 'POST':
		result = 0
		jsonin = None
		try:
			jsonin = json.loads(request.body)
		except:
			return JsonResponse({'status':'err','message':'Data given to server is invalid'})
		try:
			result = services.insertReadings(jsonin['date'],jsonin['time'],jsonin['readings'])
		except:
			return JsonResponse({'status':'err','message':'Insertion not successful'})
		if result == 1:
			return JsonResponse({'status':'ok','message':'Insertion successful'})
		else:
			return JsonResponse({'status':'err','message':'Insertion not successful'})

def getLatestReading(request):
	if request.method == 'GET':
		result = 0
		# try:
		result = services.getLatestReading()
		# except:
			# return JsonResponse({'status':'err','message':'Server encountered an error'})
		return JsonResponse({'status':'ok','result':result})

def getReadingsByDate(request):
	if request.method == 'POST':
		result = 0
		jsonin = None
		try:
			jsonin = json.loads(request.body)
		except:
			return JsonResponse({'status':'err','message':'Data given to server is invalid'})
		try:
			result = services.getReadingsByDate(jsonin['start_date'],jsonin['start_time'],jsonin['end_date'],jsonin['end_time'])
			return JsonResponse({'status':'ok','result':result})
		except:
			return JsonResponse({'status':'err','message':'Retrieval not successful'})
	else:
		return JsonResponse({'status':'err','message':'Bad request'})