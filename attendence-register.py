from datetime import date

class Register:
    def __init__(self, date):                                  
        self.date = date
        self.students_present = []

    def check_in(self, student_name):                      #input
        if student_name not in self.students_present:      #checks
            self.students_present.append(student_name)      #if not adds n confirms
            print(f"{student_name} checked in.")            
        else:
            print(f"{student_name} is already checked in.") 

    def is_present(self, student_name):                 #checks
        return student_name in self.students_present    #true or false

    def list_students(self):
        print(f"Students present on {self.date}:")
        for student in self.students_present:
            print("-", student)


# 1. Create a register for today's date
today_register = Register(date.today())

# 2. Add at least 5 students
today_register.check_in("Travis")
today_register.check_in("Shantal")
today_register.check_in("Keith")
today_register.check_in("Noel")
today_register.check_in("Ethan")

# Stretch: Try to add a duplicate
today_register.check_in("Travis")  # Should not add again

# 3. Check attendance for 2 names
print("\nAttendance check:")
print("Is Travis present?", today_register.is_present("Travis"))
print("Is Shantal present?", today_register.is_present("Shantal"))

# Display all present students
print("\nFull Attendance List:")
today_register.list_students()
