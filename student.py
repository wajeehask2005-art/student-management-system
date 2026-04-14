# ============================================
#   Student Management System - Python
# ============================================

students = []
next_id = 1

def add_student():
    global next_id
    print("\n--- Add Student ---")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    marks = input("Enter Marks (out of 100): ")
    
    student = {
        "id": next_id,
        "name": name,
        "age": int(age),
        "marks": float(marks)
    }
    students.append(student)
    print(f"✓ Student added! ID: {next_id}")
    next_id += 1

def display_all():
    if not students:
        print("\nNo students found!")
        return
    print("\n--- All Students ---")
    print(f"{'ID':<5} {'Name':<20} {'Age':<5} {'Marks'}")
    print("-" * 40)
    for s in students:
        print(f"{s['id']:<5} {s['name']:<20} {s['age']:<5} {s['marks']}")

def search_student():
    sid = int(input("\nEnter Student ID: "))
    for s in students:
        if s["id"] == sid:
            print(f"\nID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Marks: {s['marks']}")
            return
    print("Student not found!")

def delete_student():
    sid = int(input("\nEnter Student ID to delete: "))
    for i, s in enumerate(students):
        if s["id"] == sid:
            students.pop(i)
            print("✓ Student deleted!")
            return
    print("Student not found!")

def show_average():
    if not students:
        print("\nNo data!")
        return
    avg = sum(s["marks"] for s in students) / len(students)
    print(f"\nAverage Marks: {avg:.2f}")

def main():
    print("=== Student Management System ===")
    while True:
        print("\n1. Add Student")
        print("2. View All")
        print("3. Search")
        print("4. Delete")
        print("5. Average Marks")
        print("0. Exit")
        
        choice = input("Choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            display_all()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            show_average()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()