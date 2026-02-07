class Course:
    def __init__(self, name, level, time):
        self.name = name
        self.level = level
        self.time = time

    def __str__(self):
        return f"{self.name} {self.level}"

courses = []

def add_course(course: Course):
    courses.append(course)

def create_add_course(name, level, time):
    course = Course(name, level, time)
    add_course(course)

def get_course_by_name(name):
    for course in courses:
        if course.name == name:
            return course
    return None

def get_all_courses():
    return courses

def get_courses_by_level(level):
    level_courses = []
    for course in courses:
        if course.level == level:
            level_courses.append(course)
    return level_courses

def get_courses_by_time(time: int):
    time_courses = []
    for course in courses:
        if course.time == time:
            time_courses.append(course)
    return time_courses