from datetime import date

def create_fullName(firstname, lastname, middlename = ""):
    if (middlename != ""):
        full_name = firstname + " " + middlename + " " + lastname
    else:
        full_name = firstname + " " + lastname
    return full_name

def calculate_age(DateOfBirth):
    if (DateOfBirth != ""):
        today = date.today()
        age = today.year - DateOfBirth.year - ((today.month, today.day) < (DateOfBirth.month, DateOfBirth.day))
    return age
        