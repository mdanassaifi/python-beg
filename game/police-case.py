# Officer aur Case Management System (with Auto ID)

officers = []   # list to store officers
cases = []      # list to store cases

officer_id_counter = 1   # automatic officer id
case_id_counter = 1      # automatic case id

def add_officer():
    global officer_id_counter
    name = input("Enter Officer Name: ")
    department = input("Enter Department: ")
    officer = {"ID": officer_id_counter, "Name": name, "Department": department}
    officers.append(officer)
    print(f"✅ Officer added successfully with ID: {officer_id_counter}\n")
    officer_id_counter += 1

def add_case():
    global case_id_counter
    case_name = input("Enter Case Name: ")
    assigned_officer = input("Enter Assigned Officer ID: ")
    case = {"Case ID": case_id_counter, "Case Name": case_name, "Assigned Officer": assigned_officer}
    cases.append(case)
    print(f"✅ Case added successfully with ID: {case_id_counter}\n")
    case_id_counter += 1

def view_officers():
    if not officers:
        print("⚠️ No officers found.\n")
    else:
        print("\n--- Officers List ---")
        for o in officers:
            print(f"ID: {o['ID']}, Name: {o['Name']}, Department: {o['Department']}")
        print()

def view_cases():
    if not cases:
        print("⚠️ No cases found.\n")
    else:
        print("\n--- Cases List ---")
        for c in cases:
            print(f"Case ID: {c['Case ID']}, Name: {c['Case Name']}, Assigned Officer ID: {c['Assigned Officer']}")
        print()

# Main menu loop
while True:
    print("========= MENU =========")
    print("1. Add Officer")
    print("2. Add Case")
    print("3. View Officers")
    print("4. View Cases")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        add_officer()
    elif choice == '2':
        add_case()
    elif choice == '3':
        view_officers()
    elif choice == '4':
        view_cases()
    elif choice == '5':
        print("👋 Exiting program...")
        break
    else:
        print("❌ Invalid choice! Please try again.\n")
