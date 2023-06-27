from ecom.models import Student

def subscribe (request, subID):
    #user enrolled
    try:
        student = Student(user_id = request.user.id, subscribed = True, subID = subID)
        student.save()
    #user un-enrolled
    except:
        student = Student.objects.get(user_id = request.user.id)
        student.delete()