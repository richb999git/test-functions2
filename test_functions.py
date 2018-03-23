def hello_func():
    return "Hello function"

def hello_func2(greeting="Howdy"):
    return "{} Function".format(greeting)

def student_info(*args, **kwargs):     # * means single bits of data
    print(args)                        # ** means two bits (key words) (dictionary)
    print(kwargs)                      # args and kwargs is convention

print(hello_func().upper())

print(hello_func2("Hi").lower())

print(hello_func2().lower())

student_info("Maths", "Art", name = "John Barn", Age = 21, student_num = 25764)
# this produces a tuple containing Maths and Art
# and a dictionary containing name, age, student number

courses = ["History", "Physics"]
info = {"name":"Dave glut", "Age":20, "student_num": 83957}

student_info(courses, info)    #not what we wanted  (first 2 "fields" populated only)
student_info(*courses, **info)    #* and ** make it treat it as we want

print("bit on th end")

