from django.shortcuts import render
from utilities import subscribe
from .models import *
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.models import User

# for pdf
import io
import textwrap
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

#for pagintion 
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    course_list = Course.objects.all()
    context = {
        'courses' : course_list,
    }
    return render(request, 'mysite/index.html', context)

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        courses =  Course.objects.filter(title__startswith = searched)
        context = {
            'searched': searched,
            'courses': courses,
        }
        return render(request, 'mysite/search.html', context)
    else:
        return render(request, 'mysite/search.html')

def notes(request):
    if request.method == 'POST':
        user_name = request.POST.get('uname') # we need to get the fname because in form field the name is fname
        notes = request.POST.get('notes') 
        course_name = request.POST.get('courseName')
        lesson_name = request.POST.get('lessonName')
        info = Notes(user_name = user_name, notes = notes, course_name = course_name, lesson_name = lesson_name) # creating an object of type Person where we need to save the informations
        info.save() # saving the data in the info object and when we press submit in optin.html page, the data are sent to the django admin database
        send_message = True # this variable is for redirect to a message after we send successful the data, we make it true
        context = {'send_message': send_message} # here optedin will receive the value of opt which is true; by default it is false; this will be cheked in optin.html file; if it is true then we will display the message; if not then we have the form
        return render(request, 'mysite/notes.html', context) # we display the request togheter with the result of the contet
    else:
        return render(request, 'mysite/notes.html')

def courses(request):
    course_list = Course.objects.all()
    #pagination 
    p = Paginator(Course.objects.all(), 3)
    page = request.GET.get('page')
    courses = p.get_page(page)
    nums = "a" * courses.paginator.num_pages
    context = {
        'courses' : course_list,
        'course': courses,
        'nums': nums,
    }
    return render(request, 'mysite/courses.html', context)

def course_detail(request, num):
    course_name = Course.objects.get(id = num) # get the course id to be displayed on the course detail page
    lessons = Lessons.objects.filter(course = course_name) # get the lessons of every course
    sections = Section.objects.filter(course = course_name)
    # creating the dictionary whith the informations that we need 
    context = {
        'course_id' : num,
        'course_obj' : course_name,
        'lessons' : lessons,
        'sections': sections,
    }
    
    return render(request, 'mysite/course_detail.html', context)

def lessons_detail(request, num, num1):    
    course_name = Course.objects.get(id = num) # get the course id to be displayed on the course detail page
    lessons = Lessons.objects.filter(course = course_name) # get the lessons of every course
    sections = Section.objects.filter(course = course_name)
    lesson = Lessons.objects.get(id = num1)
    context = {
        'course_obj' : course_name,
        'lessons' : lessons,
        'sections': sections,
        'current_lesson' : lesson,
    }
    return render(request, 'mysite/lessons_detail.html', context)

def quiz(request):
    return render(request, 'mysite/quiz.html')

def pricing(request):
    # contact form settings
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, 'ctnonisim@gmail.com', ['ctnonisim@gmail.com'])
            except:
                return HttpResponse('Invalid header found')
            mess = True # this variable is for redirect to a message after we send successful the data, we make it true
            context = {'message_sent': mess}
            return render(request, 'mysite/pricing.html', context)
    form = ContactForm()
    return render(request, 'mysite/pricing.html', {'form':form})

#Saving the subscription data from optin.html
def optin(request):
    if request.method == 'POST':
        name = request.POST.get('fname') # we need to get the fname because in form field the name is fname
        country = request.POST.get('country') # same
        email = request.POST.get('email') # same
        info = Person(name = name, country = country, email = email) # creating an object of type Person where we need to save the informations
        info.save() # saving the data in the info object and when we press submit in optin.html page, the data are sent to the django admin database
        opt = True # this variable is for redirect to a message after we send successful the data, we make it true
        context = {'optedin': opt} # here optedin will receive the value of opt which is true; by default it is false; this will be cheked in optin.html file; if it is true then we will display the message; if not then we have the form
        return render(request, 'mysite/optin.html', context) # we display the request togheter with the result of the contet
    else:
        return render(request, 'mysite/optin.html')

def profile(request):
    return render(request, 'mysite/profile.html')

def activate(request, subID):
    subscribe(request, subID)
    print(subID)
    return render(request, 'mysite/activate.html')

# this is the correct one; it prints all the notes
# import io
# import textwrap
# from django.http import FileResponse
# from reportlab.lib.pagesizes import letter
# from reportlab.lib.units import cm
# from reportlab.pdfgen import canvas

# def course_pdf(request):
#     user_account = User.objects.get(username=request.user.username)
#     buf = io.BytesIO()
#     c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
#     text_ob = c.beginText()
#     text_ob.setTextOrigin(cm, cm)
#     text_ob.setFont("Helvetica", 14)

#     notes = Notes.objects.filter(user_name=user_account)  # Filter notes for current user

#     for note in notes:
#         lines = []
#         lines.append(note.user_name)
#         lines.append(note.course_name)
#         lines.append(note.lesson_name)
#         lines.append(note.notes)

#         for line in lines:
#             wrapped_lines = textwrap.wrap(line, width=40)  # Specify the desired width to wrap the text
#             for wrapped_line in wrapped_lines:
#                 text_ob.textLine(wrapped_line)

#     c.drawText(text_ob)
#     c.showPage()
#     c.save()
#     buf.seek(0)
#     return FileResponse(buf, as_attachment=True, filename='course.pdf')


# this one prints just the last note of the user
def course_pdf(request):
    user_account = User.objects.get(username=request.user.username)
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    text_ob = c.beginText()
    text_ob.setTextOrigin(cm, cm)
    text_ob.setFont("Helvetica", 14)
    # Retrieve the latest notes for each user
    latest_notes = {}
    notes = Notes.objects.filter(user_name = user_account).order_by('-id')
    for note in notes:
        if note.user_name not in latest_notes:
            latest_notes[note.user_name] = note
    # Iterate over the latest notes and add them to the PDF
    for note in latest_notes.values():
        lines = []
        lines.append("Student username: " + note.user_name)
        lines.append("Course name: " + note.course_name)
        lines.append("Lesson name: " + note.lesson_name)
        lines.append(note.notes)
        for line in lines:
            wrapped_lines = textwrap.wrap(line, width=80)  # Specify the desired width to wrap the text
            for wrapped_line in wrapped_lines:
                text_ob.textLine(wrapped_line)
    c.drawText(text_ob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='course.pdf')
