from django.http import HttpRequest
from django.shortcuts import render

from main.course import Course, add_course


# Create your views here.

def home(request: HttpRequest):
    return render(request, 'home.html')

data = ["ELEMENT1", "ELEMENT2", "ELEMENT3", "ELEMENT4"]

def page_elements(request: HttpRequest, index: int, name: str):
    element = data[index]

    context = {
        "element": element,
        "name": name,
    }

    return render(request, "home.html", context=context)

def calc(request: HttpRequest):
    return render(request, "calc.html")

def calculate(request: HttpRequest, operation: str, a: int, b: int):
    result = None
    text = "Calculation complete."
    operation_sign = ""

    if operation == "add":
        result = a + b
        operation_sign = "+"
    elif operation == "sub":
        result = a - b
        operation_sign = "−"
    elif operation == "mul":
        result = a * b
        operation_sign = "×"
    elif operation == "div":
        if b == 0:
            text = "ERROR: division by zero. Please try again."
        else:
            result = a / b
        operation_sign = "÷"
    else:
        text = "ERROR: invalid operation. Please use 'add', 'sub', 'mul' or 'div'"

    context = {
        "error": text,
        "operation": operation_sign,
        "a": a,
        "b": b,
        "result": result,
    }

    return render(request, "calculate.html", context=context)

def website(request: HttpRequest):
    return render(request, "website.html")

def post_handler(request: HttpRequest):
    if request.method == "POST":
        data = request.POST
        name = data["name"]
        age = data["age"]

        str_data = f"Name: {name}, age: {age}"
        context = {
            "str_data":str_data
        }
        return render(request, "profile_view.html", context = context)
    return render(request, "profile.html")

def courses(request: HttpRequest):
    if request.method == "POST":
        data = request.POST
        name = data["name"]
        level = data["level"]
        time = int(data["time"])
        course = Course(name, level, time)
        add_course(course)
        context = {
            "name": name,
            "level": level,
            "time": time,
        }

        return render(request, "course_post.html", context = context)
    return render(request, "course.html")

def course_by_level(request: HttpRequest, level: str):
    course_list = []