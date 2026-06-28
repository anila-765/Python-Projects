import json

class Student:
    def __init__(self,roll,name,mark):
        self.name=name
        self.roll_num=roll
        self.mark=mark
    
    def to_dict(self):
       return {
            "roll":self.roll_num,
            "name":self.name,
            "mark":self.mark
        }
    
class StudentManager: #to store each object
    def __init__(self):
        self.students=[]
        self.load_data()

    def add_student(self):
        roll=int(input("enter roll number "))
        for student in self.students:
            if roll==student.roll_num:
                print("roll number present")
                return
            
        name=input("enter ur name ")
        if name.strip()=="":
            print("name cant be empty")
            return
            
        mark=int(input("enter ur mark "))
        if mark<0 or mark>100:
            print("mark not valid")
            return

        student=Student(roll,name,mark)
        self.students.append(student)
        print("Successfully added !!!!")
        

    def view_student(self):
        if not self.students:
            print("students not available")
            return
        for student in self.students:
            print(student.roll_num,student.name,student.mark)

    def search_student(self):
        roll=int(input("enter roll to search "))
        for stu in self.students:
            if roll==stu.roll_num:
                print(stu.roll_num,stu.name,stu.mark)
                return
        print("not found")

    def update_mark(self):
        roll=int(input("enter roll number "))
        mark=int(input("enter mark to change "))
        if mark < 0 or mark > 100:
           print("invalid marks")
           return
        for stu in self.students:
            if roll==stu.roll_num:
                stu.mark=mark
                print("mark updated successfully")
                return
        print("student not found!!!")

    def delete_student(self):
        roll=int(input("enter roll number "))
        for i,stu in enumerate(self.students):
            if roll==stu.roll_num:
                del self.students[i]
                print("successfully deleted")
                return
        print("student not found")

    def save_data(self):
        data=[]

        for stu in self.students:
            data.append(stu.to_dict())
        with open("students.json","w") as f:
            json.dump(data,f,indent=4)

        print("successfully saved")
    
    def load_data(self):
        try:
            with open("students.json","r") as f:
                data=json.load(f)
            
            for item in data:
                stu = Student(item["roll"],
                              item["name"],
                              item["mark"])
                self.students.append(stu)
        except FileNotFoundError:
             self.students = []

manager=StudentManager()

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Save Data")
    print("7. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
          manager.add_student()

    elif choice == "2":
          manager.view_student()

    elif choice == "3":
             manager.search_student()

    elif choice == "4":
             manager.update_mark()

    elif choice == "5":
             manager.delete_student()

    elif choice == "6":
             manager.save_data()

    elif choice == "7":
             manager.save_data()
             print("Exiting... Data saved.")
             break

    else:
             print("Invalid choice. Try again.")

