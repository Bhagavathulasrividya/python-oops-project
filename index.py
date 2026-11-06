class student:
    def __init__(self,id,name,age,place):
        self.id = id
        self.name = name
        self.age = age
        self.place = place

    def display_details(self):
        print("ID:",self.id)
        print("NAME:",self.name)
        print("AGE:",self.age)
        print("PLACE:", self.place)

class studentmanagement:
    def __init__(self):
        self.student = []

    def add_students(self):
        id = input("ENTER A ID:")
        name = input("Enter a Name:")
        age = input("Enter a Age:")
        place = input("Enter a Place:")

        s = student(id,name,age,place)
        self.student.append(s)
        print("SUCCESSFULLY ADDED")

    def view_all_details(self):
        if len(self.student) == 0:
            print("NO DETAILS AVAILABLE")
        else:
            for i in self.student:
                i.display_details()

    def search_student(self):
        search_id = input("Enter a id for search student:")

        for i in self.student:
             if i.id == search_id:
                 i.display_details()
                 print("Student found")
                 break
        else:
            print("Student not found")

    def update_student(self):
        user_id = input("Enter a id for update:")
        for i in self.student:
            if i.id == user_id:
                user_name = input("Enter a new name:")
                user_age = input("Enter a new age:")
                user_place= input("Enter a new place:")
                i.name = user_name
                i.age = user_age
                i.place = user_place
                i.display_details()
                print("Updated successfully")
                break
        else:
            print("Student not found")

    def delete_student(self):
        delete_id = input("Enter a id for delete:")
        for i in self.student:
            if i.id == delete_id:
                self.student.remove(i)
                print("Student deleted")
                break
        else:
            print("Student not found")    

    def menu(self):
        print("================STUDENT MANAGEMENT SYSTEM============")
       

        while True:
            print("1.Add student")
            print("2.View students")
            print("3.search student")
            print("4.update student")
            print("5.delete student")
            print("6.Exit")
            
            choice = int(input("Enter a choice from above options:"))

            match choice:

                case 1:
                    self.add_students()
                case 2:
                    self.view_all_details()
                case 3:
                    self.search_student()
                case 4:
                    self.update_student()
                case 5:
                    self.delete_student()
                case 6:
                    break
                case _:
                    print("invalid options")

sm = studentmanagement()
sm.menu()