def HR():
    import os
    print("\nChecking if the file \"emp.txt\" exists: ")
    if os.path.exists("emp.txt"):
        print("Exists")
    else:
        print("Does not exist.\nPlease exit the program and create this file.")
    while True:
        print("\nPLEASE CHOOSE :)")
        print("\n==============HR Management System==============")
        print("               1. View all Employees"           )
        print("               2. Add New Employee"             )
        print("               3. Search Employee's Information")
        print("               4. Update Employee's Information")
        print("               5. Delete Employee's Information")
        print("               6. Exit")
        print("{Employee's ID are unique}")
        c=int(input("\nEnter your choice: "))
        if c==1:
            view() 
        elif c==2:
            add()
        elif c==3:
            search()
        elif c==4:
            update()
        elif c==5:
            delete()
        elif c==6:
            print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print("\nExiting HR Management Program.")
            print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            break
        else:
            print("Invalid Choice! Please Enter Again.")


def view():
        print("\n")
        with open("emp.txt","r") as f:
            for l in f:
                id, emp, dept, post, jd, sal = l.strip().split(',')
                print(f"ID: {id}, Name: {emp}, Department: {dept}, Designation: {post}, Joining day: {jd}, Salary:{sal}")
                print("\n")
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

def add():
    print("\n")
    i=int(input("\nEnter no.of Employee details to add: "))
    for i in range(i):
        print("\nDetails of Employee",i+1)
        id = input("Enter Employee ID: ")
        emp = input("Enter Employee Name: ")
        dept = input("Enter Department: ")
        post = input("Enter Designation: ")
        jd = input("Enter the Joining Date(dd/mm/yyyy):")
        sal = input("Enter Salary: ")
        print("============Added Employee's Details============")
        with open("emp.txt","a") as f:
            f.write(f"{id}, {emp}, {dept}, {post}, {jd}, {sal}\n")
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


def search():
    print("\n")
    i=input("Enter the Employee ID: ")
    with open("emp.txt","r") as f:
        for l in f:
            id, emp, dept, post, jd, sal = l.strip().split(',')
            if i==id:
                print(f"Employee's Detail :->\nName: {emp}, Department: {dept}, Designation: {post}, Joining day: {jd}, Salary: {sal}")
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


def update():
        print("\n")
        i=input("Enter Employee ID to update: ")
        with open("emp.txt","r") as f:
            lines=f.readlines()                                 # lines is a list where each element represents a line from file
            up=[]               
            f=False
            for l in lines:
                id, emp, dept, post, jd, sal = l.strip().split(',')
                if i in l:
                    print(f"Employee's detail :->\nName: {emp}, Department: {dept}, Designation: {post}, Joining day:{jd}, Salary:{sal}")
                    print("Enter the current value if do not want to change.")
                    id=input(f"Updated Employee ID: ")
                    emp=input(f"Updated Name: ")
                    dept=input(f"Updated Department: ")
                    post=input(f"Updated Designation: ")
                    dj=input(f"Updated Joining Day(dd/mm/yyyy): ")
                    sal=input(f"Updated Salary: ")
                    l=f"{id},{emp},{dept},{post},{dj},{sal}\n"
                    f=True
                    up.append(l)
                    print("========Updated Employee's Detail=======")
                else:
                    up.append(l)
            if not f:
                print("Enter a valid Employee ID please.")
            with open("emp.txt","w") as f:
                f.writelines(up)
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


def delete():
    print("\n")
    i=input("Enter Employee ID to delete: ")
    with open("emp.txt","r") as f:
        lines=f.readlines()                                 
        up=[]               
        f=False
        for l in lines:
            if i in l:
                print("========Deleted Employee's Detail=======")
                f=True
            else:
                up.append(l)
        if not f:
            print("Enter a valid Employee ID please.")
        with open("emp.txt","w") as f:
            f.writelines(up)
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


def IV():
    import os
    print("\nChecking if the file \"item.txt\" exists: ")
    if os.path.exists("item.txt"):
        print("Exists")
    else:
        print("Does not exist.\nPlease exit the program and create this file.")
    while True:
        print("\nPLEASE CHOOSE :)")
        print("\n==============Inventory Management System==============")
        print("              1. View all Items"              )
        print("              2. Add New Item"                )
        print("              3. Search Item"                 )
        print("              4. Update Item Details"         )
        print("              5. Delete Item"                 )
        print("              6. Exit")
        print("\{Item's ID are unique\}")
        c=int(input("\nEnter your choice: "))
        if c==1:
            viewitem()
        elif c==2:
            additem()
        elif c==3:
            searchitem()
        elif c==4:
            updateitem()
        elif c==5:
            deleteitem()
        elif c==6:
            print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print("\nExiting Inventory Management System.")
            print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            break
        else:
            print("Invalid Choice! Please Enter Again.")


def viewitem():
    print("\n")
    with open("item.txt","r") as f:
        for l in f:
            id,item, quan, mfgd, expd = l.strip().split(',')
            print(f"ID: {id}, Item Name: {item}, Qunatity: {quan}, Manufacturing Date: {mfgd}, Expiry Date: {expd}")
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

def additem():
    print("\n")
    i=int(input("\nEnter the no.of Item details to add: "))
    for i in range(i):
        print("\nItem",i+1 ,"Details:->\n")
        id = input("Enter Item ID: ")
        item = input("Enter Item Name: ")
        quan = input("Enter Item Quantity: ")
        mfgd = input("Enter Manufacturing Date: ")
        expd = input("Enter Expiry Date: ")
        print("\n========Added Item's Detail=======")
        with open("item.txt","a") as f:
            f.write(f"{id}, {item}, {quan}, {mfgd}, {expd}\n")
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

def searchitem():
    print("\n")
    i=input("Enter Item ID: ")
    with open("item.txt","r") as f:
        for l in f:
            id,item, quan, mfgd, expd = l.strip().split(',')
            if i==id:
                print(f"Item's Detail :->\nItem Name: {item}, Qunatity: {quan}, Manufacturing Date: {mfgd}, Expiry Date: {expd}")
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


def updateitem():
    print("\n")
    i=input("Enter Item ID to update: ")
    with open("item.txt","r") as f:
        ls=f.readlines()                    
        upitem=[]               
        f=False
        for l in ls:
            id,item, quan, mfgd, expd = l.strip().split(',')
            if i in l:
                print(f"Item Found:\nID:{id}, Item Name: {item}, Qunatity: {quan}, Manufacturing Date: {mfgd}, Expiry Date: {expd}")
                print("Enter current value if do not want to change.")
                id=input(f"Updated ID: ")
                item=input(f"Updated Item Name: ")
                quan=input(f"Updated Quantity: ")
                mfgd=input(f"Updated Manufacturing Date(dd/mm/yyyy): ")
                expd=input(f"Updated Expiry Date(dd/mm/yyyy): ")
                l=f"{id},{item},{quan},{mfgd},{expd}\n"
                upitem.append(l)
                f=True
                print("========Updated Item's Details=======")
            else:
                upitem.append(l)
        if not f:
            print("Enter a valid Employee ID please.")
        with open("emp.txt","w") as f:
            f.writelines(upitem)
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


def deleteitem():
    i=input("Enter the Item ID to be deleted: ")
    with open("item.txt","r") as f:
        ls=f.readlines()                 
        upitem=[]               
        f=False
        for l in ls:
            if i in l:
                print("========Deleted Item's Detail=======")
                f=True
            else:
                upitem.append(l)
        if not f:
            print("Enter a valid Employee ID please.")
        with open("item.txt","r+") as f:
            f.writelines(upitem)
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


while True:
    print("\n\nWelcome to the Management Sytem of VED Corporations.")
    print("\n==========Choose the System you want to work on============")
    print("\n          1. Human Resources Management System")
    print("          2. Inventory Management System")
    print("          3. Exit")
    c=int(input("\nEnter your choice: "))
    if c==1:
        HR()
    elif c==2:
        IV()
    elif c==3:
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("\nExiting Management Sytems.")
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        break
    else :
        print("Invalid Choice! Please Enter Again.")