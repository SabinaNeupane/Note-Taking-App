# assignment project:

def add():
    with open("notes.txt","a") as f:
        f.write(f"{input("add a note : ")}\n")
    print(f"Note added succesfully")
    print()

def view():
    with open("notes.txt","r") as f:
        content=f.read()
        print(content)
    
def clear():
    with open("notes.txt","w") as f:
        f.write("")
    print(f"All Notes Cleared")
    print()

def main():
    print(f"1. Add")
    print(f"2. View")
    print(f"3. Clear")    
    print(f"4. Exit")
    val=int(input("Enter your choice (1-4) : "))
    print()
    return val

while True:
    main_output=main()
    if main_output==4:
        print("Goodbye!")
        break
    if main_output==1:
        add()
    if main_output==2:
        view()
    if main_output==3:
        clear()