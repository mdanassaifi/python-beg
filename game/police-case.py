# Officer aur Case Management System (with Delete Option)

officers = []   # list to store officers
cases = []      # list to store cases

officer_id_counter = 1   # automatic officer id
case_id_counter = 1      # automatic case id

def add_officer():
    global officer_id_counter
    name = input("Enter Officer Name: ")
    department = input("Enter Department: ")
    officer = {"ID": officer_id_counter, "Name": name, "Department": department, "Cases": []}
    officers.append(officer)
    print(f"✅ Officer added successfully with ID: {officer_id_counter}\n")
    officer_id_counter += 1

def add_case():
    global case_id_counter

    if not officers:
        print("⚠️ No officers available. Please add officer first!\n")
        return

    case_name = input("Enter Case Name: ")
    officer_id = int(input("Enter Officer ID to assign case: "))

    # check officer exist
    assigned_officer = None
    for o in officers:
        if o["ID"] == officer_id:
            assigned_officer = o
            break

    if assigned_officer is None:
        print("❌ Officer ID not found! Please try again.\n")
        return

    mujrim_name = input("Enter Mujrim Name: ")
    mujrim_age = input("Enter Mujrim Age: ")
    saza = input("Enter Saza (in years): ")

    case = {
        "Case ID": case_id_counter,
        "Case Name": case_name,
        "Officer ID": officer_id,
        "Officer Name": assigned_officer["Name"],
        "Mujrim Name": mujrim_name,
        "Mujrim Age": mujrim_age,
        "Saza": saza
    }
    cases.append(case)

    # also add case to officer's personal list
    assigned_officer["Cases"].append(case)

    print(f"✅ Case added successfully with ID: {case_id_counter} and assigned to Officer {assigned_officer['Name']}\n")
    case_id_counter += 1

def view_officers():
    if not officers:
        print("⚠️ No officers found.\n")
    else:
        print("\n--- Officers List ---")
        for o in officers:
            print(f"ID: {o['ID']}, Name: {o['Name']}, Department: {o['Department']}, Total Cases: {len(o['Cases'])}")
        print()

def view_cases():
    if not cases:
        print("⚠️ No cases found.\n")
    else:
        print("\n--- Cases List ---")
        for c in cases:
            print(f"Case ID: {c['Case ID']}, Case Name: {c['Case Name']}")
            print(f"Officer: {c['Officer Name']} (ID: {c['Officer ID']})")
            print(f"Mujrim: {c['Mujrim Name']} (Age: {c['Mujrim Age']})")
            print(f"Saza: {c['Saza']} years\n")

def delete_case():
    if not cases:
        print("⚠️ No cases available to delete.\n")
        return

    case_id = int(input("Enter Case ID to delete: "))
    found_case = None

    for c in cases:
        if c["Case ID"] == case_id:
            found_case = c
            break

    if found_case:
        # remove from cases list
        cases.remove(found_case)

        # also remove from officer's case list
        for o in officers:
            if o["ID"] == found_case["Officer ID"]:
                o["Cases"] = [case for case in o["Cases"] if case["Case ID"] != case_id]

        print(f"🗑️ Case ID {case_id} deleted successfully!\n")
    else:
        print("❌ Case not found!\n")

def delete_officer():
    if not officers:
        print("⚠️ No officers available to delete.\n")
        return

    officer_id = int(input("Enter Officer ID to delete: "))
    found_officer = None

    for o in officers:
        if o["ID"] == officer_id:
            found_officer = o
            break

    if found_officer:
        # remove officer
        officers.remove(found_officer)

        # also remove all cases linked to this officer
        global cases
        cases = [case for case in cases if case["Officer ID"] != officer_id]

        print(f"🗑️ Officer ID {officer_id} and all their cases deleted successfully!\n")
    else:
        print("❌ Officer not found!\n")

# Main menu loop
while True:
    print("========= MENU =========")
    print("1. Add Officer")
    print("2. Add Case")
    print("3. View Officers")
    print("4. View Cases")
    print("5. Delete Officer")
    print("6. Delete Case")
    print("7. Exit")
    
    choice = input("Enter your choice (1-7): ")
    
    if choice == '1':
        add_officer()
    elif choice == '2':
        add_case()
    elif choice == '3':
        view_officers()
    elif choice == '4':
        view_cases()
    elif choice == '5':
        delete_officer()
    elif choice == '6':
        delete_case()
    elif choice == '7':
        print("👋 Exiting program...")
        break
    else:
        print("❌ Invalid choice! Please try again.\n")
