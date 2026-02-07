from django.http import HttpRequest
from django.shortcuts import render


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