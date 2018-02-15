from . import models
import datetime

def insertReadings(date,time,readings):
	try:
		datetime1 = datetime.datetime.strptime(date+" "+time, "%d/%m/%Y %H:%M:%S")
		print(datetime1)
		temp = ''
		for k in readings.keys():
			temp+=(k+' = '+str(readings[k])+',')
		temp +='datetime = datetime1'
		exec('obj = models.Readings('+temp+')')
		exec('obj.save()')
		return 1
	except:
		return 0

def getLatestReading():
	obj=models.Readings.objects.filter().order_by('-id')
	if len(obj)==0:
		return {}
	registers = ["3913","3929","3943","3957","3909","3911","3925","3939","3953","3927","3941","3955","3903","3919","3933","3947","3905","3921","3935","3949","3901","3917","3931","3945","3907","3923","3937","3951","3915","3861","3863","3865","3867","3869","3871","3959","3961","3963","3965","3967","3969","3971","3973","3975","3977","3979","3881","3883","3885","3887","3889","3891","3993","3995","3997","3999","3981"]
	readings = {}
	for i in registers:
		temp = "readings['R"+i+"'] = obj[0].R"+i
		exec(temp)
	datetime1 = (obj[0].datetime).strftime("%d/%m/%Y %H:%M:%S")
	datetime1 = datetime1.split(' ')
	return {'date':datetime1[0],'time':datetime1[1],'readings':readings}

def getReadingsByDate(startdate,starttime,enddate,endtime):
	datetime1 = datetime.datetime.strptime(startdate+" "+starttime, "%d/%m/%Y %H:%M:%S")
	datetime2 = datetime.datetime.strptime(enddate+" "+endtime, "%d/%m/%Y %H:%M:%S")
	print("hi")
	obj = models.Readings.objects.filter(datetime__range=(datetime1,datetime2)).order_by('-id')
	print("hi")
	registers = ["3913","3929","3943","3957","3909","3911","3925","3939","3953","3927","3941","3955","3903","3919","3933","3947","3905","3921","3935","3949","3901","3917","3931","3945","3907","3923","3937","3951","3915","3861","3863","3865","3867","3869","3871","3959","3961","3963","3965","3967","3969","3971","3973","3975","3977","3979","3881","3883","3885","3887","3889","3891","3993","3995","3997","3999","3981"]
	result = []
	if len(obj)==0:
		return []
	for j in obj:
		readings = {}
		for i in registers:
			temp = "readings['R"+i+"'] = j.R"+i
			exec(temp)
		datetime1 = (j.datetime).strftime("%d/%m/%Y %H:%M:%S")
		datetime1 = datetime1.split(' ')
		result.append({'date':datetime1[0],'time':datetime1[1],'readings':readings})
	return result