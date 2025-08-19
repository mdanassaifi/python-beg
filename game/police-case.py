from pymongo import MongoClient

# ====== MongoDB Connection ======
# apna connection string yahan paste karo


db = client["PoliceDB"]            # database
officers_collection = db["officers"]
cases_collection = db["cases"]

officer_id_counter = 1
case_id_counter = 1

def get_next_officer_id():
    global officer_id_counter
    last = officers_collection.find_one(sort=[("ID", -1)])
    if last:
        officer_id_counter = last["ID"] + 1
    return officer_id_counter

def get_next_case_id():
    global case_id_counter
    last = cases_collection.find_one(sort=[("Case ID", -1)])
    if last:
        case_id_counter = last["Case ID"] + 1
    return case_id_counter

def add_officer():
    officer_id = get_next_officer_id()
    name = input("Enter Officer Name: ")
    department = input("Enter Department: ")
    officer = {"ID": officer_id, "Name": name, "Department": department}
    officers_collection.insert_one(officer)
    print(f"✅ Officer added with ID: {officer_id}\n")

def add_case():
    case_id = get_next_case_id()
    case_name = input("Enter Case Name: ")
    officer_id = int(input("Enter Officer ID to assign case: "))

    officer = officers_collection.find_one({"ID": officer_id})
    if not officer:
        print("❌ Officer not found! Please add correct Officer ID.\n")
        return

    mujrim_name = input("Enter Mujrim Name: ")
    mujrim_age = input("Enter Mujrim Age: ")
    saza = input("Enter Saza (in years): ")

    case = {
        "Case ID": case_id,
        "Case Name": case_name,
        "Officer ID": officer_id,
        "Officer Name": officer["Name"],
        "Mujrim Name": mujrim_name,
        "Mujrim Age": mujrim_age,
        "Saza": saza
    }
    cases_collection.insert_one(case)
    print(f"✅ Case added with ID: {case_id}, assigned to Officer {officer['Name']}\n")

def view_officers():
    officers = list(officers_collection.find())
    if not officers:
        print("⚠️ No officers found.\n")
    else:
        print("\n--- Officers List ---")
        for o in officers:
            total_cases = cases_collection.count_documents({"Officer ID": o["ID"]})
            print(f"ID: {o['ID']}, Name: {o['Name']}, Department: {o['Department']}, Total Cases: {total_cases}")
        print()

def view_cases():
    cases = list(cases_collection.find())
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
    case_id = int(input("Enter Case ID to delete: "))
    result = cases_collection.delete_one({"Case ID": case_id})
    if result.deleted_count > 0:
        print(f"🗑️ Case ID {case_id} deleted successfully!\n")
    else:
        print("❌ Case not found!\n")

def delete_officer():
    officer_id = int(input("Enter Officer ID to delete: "))
    result = officers_collection.delete_one({"ID": officer_id})
    if result.deleted_count > 0:
        # remove all cases of this officer
        cases_collection.delete_many({"Officer ID": officer_id})
        print(f"🗑️ Officer ID {officer_id} and all their cases deleted!\n")
    else:
        print("❌ Officer not found!\n")

# ========= Main Menu =========
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
