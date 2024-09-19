from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse

course_dict = {
    "python" :  "Hello python",
    "java" : "Hello java",
    "kotlin" : "Hello kotlin",
    "swift" : "Hello swift"
}

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def course(request, item):
    return HttpResponse(course_dict.get(item, "Not found!"))

def course_index(request, number):
    course_list = list(course_dict.keys())
    course_index = course_list[number]
    return HttpResponse(course_dict.get(course_index, "Not found!"))

def other_courses(request, item):
    try:
        return HttpResponse(course_dict[item])
    except:
        return HttpResponseNotFound("Not found, please research another course")

def multiply(request, number1, number2, number3):
    return HttpResponse(number1 * number2 * number3)

def course_number_view(request, course_index):
    try:
        page_to_go = reverse('course_index', args=[course_index])
        return HttpResponseRedirect(page_to_go)
    except:
        return HttpResponseNotFound("Not found, please research another course")