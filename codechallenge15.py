
print("DLL STUDENT INFORMATION SYSTEM")
print("------------------------------------------")

stud_record = {}

while True:
    print("Select from the following options -  ")
    print(" A - Add student")
    print(" B - Print all student info")
    print(" C - Search student record")
    print(" D - Delete student record")
    print(" E - Edit student record")
    print("F - Export data")
    print("G - Exit")
    

    choice = input("What is your choice?  ").lower().strip()

    if choice == 'a':
        print("ADD STUDENT INFO")
        student_id = input("What is your student id number? ")
        first = input("First name - ")
        last = input("Last name - ")
        course = input("Your course - ")
        section = input("your section - ")
        email = input("Whats your email? ")

        stud_record[student_id] =  [first, last, course , section, email]
        print("DATA SAVED")

        continue
    elif choice == 'b':
        print("PRINTING STUDENT RECORD")
        
        for id, info in stud_record.items():
                print(f"STUDEN ID {id} - RECORD- {info}")

        continue
    elif choice == 'c':
        print("SEARCH STUDENT RECORD")

        search_id = input("INPUT STUDENT ID ===> ").lower()
        for each_student in stud_record.keys():
            if search_id in stud_record.keys():
                print("\n\nRECORD")
                print("==========")
                for id in stud_record[search_id]:
                    print(f"--{id}")
            else:
                print("NO RECORD FOUND")

    elif choice == 'd':
        print("Delete STUDENT RECORD")

        search_id = input("INPUT STUDENT ID ===> ").lower()
        for each_student in stud_record.keys():
            if search_id in stud_record.keys():
                print("\n\nRECORD")
                print("==========")
                for id in stud_record[search_id]:
                    print(f"--{id}")

                print("=======")
                stud_record.pop(search_id)
                print("record deleted")
            else:
                print("NO RECORD FOUND")
        
        continue
    elif choice == 'e':
        print("edit STUDENT RECORD")

        search_id = input("INPUT STUDENT ID ===> ").lower()
        for each_student in stud_record.keys():
            if search_id in stud_record.keys():
                print("\n\nRECORD")
                print("==========")
                for id in stud_record[search_id]:
                    print(f"--{id}")
                print("=======")
                first = input("First name - ")
                last = input("Last name - ")
                course = input("Your course - ")
                section = input("your section - ")
                email = input("Whats your email? ")

                stud_record[search_id][0]= first
                stud_record[search_id][1]= first
                stud_record[search_id][2]= first
                stud_record[search_id][3]= first
                stud_record[search_id][4]= first
                print("info edited")
    
    else:
        print("Invalid")

        continue