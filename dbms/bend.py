import sqlite3
from datetime import datetime
import os


###########################################################################################
# initialization
def initialize_db():
    con = sqlite3.connect("rvms.db")
    cur = con.cursor()

    cur.execute("PRAGMA foreign_keys = ON")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS rto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        location TEXT NOT NULL,
        phone_no TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS driving_license (
        dl_no TEXT NOT NULL UNIQUE PRIMARY KEY,
        cov TEXT NOT NULL,
        issue_date TEXT NOT NULL,
        expiry_date TEXT NOT NULL,
        status TEXT NOT NULL CHECK (status IN ('valid', 'expired'))
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS vehicle (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        veh_name TEXT NOT NULL,
        veh_type TEXT NOT NULL,
        manufacturer TEXT NOT NULL,
        model TEXT NOT NULL,
        year INTEGER NOT NULL,
        engine_no TEXT NOT NULL UNIQUE,
        chassis_no TEXT NOT NULL UNIQUE,
        owner_id TEXT NOT NULL,
        FOREIGN KEY (owner_id) REFERENCES owner(id)
        
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS owner (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL CHECK (age > 17),
        address TEXT NOT NULL,
        pincode TEXT NOT NULL,
        phone TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        driving_license TEXT NOT NULL UNIQUE,
        FOREIGN KEY (driving_license) REFERENCES driving_license(dl_no) ON UPDATE CASCADE
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS insurance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        provider TEXT NOT NULL,
        policy_no TEXT NOT NULL UNIQUE,
        start_date TEXT NOT NULL,
        end_date TEXT NOT NULL,
        veh_id INTEGER NOT NULL,
        status TEXT NOT NULL CHECK (status IN ('active', 'expired')),
        FOREIGN KEY (veh_id) REFERENCES vehicle(id) ON DELETE CASCADE ON UPDATE CASCADE
    )            
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS registration (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        reg_no TEXT NOT NULL UNIQUE,
        veh_id INTEGER NOT NULL,
        rto_id INTEGER NOT NULL,
        reg_date TEXT NOT NULL,
        status TEXT NOT NULL CHECK (status IN ('pending', 'approved', 'rejected')),
        FOREIGN KEY (veh_id) REFERENCES vehicle(id) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (rto_id) REFERENCES rto(id) ON DELETE CASCADE ON UPDATE CASCADE
    )
    """)

    con.commit()
    con.close()


###########################################################################################
# misc
def col_exists(
    col_name, tbl_name
):  # gets column name and checks if it exists in the table
    cur.execute(f"PRAGMA table_info({tbl_name});")
    q = cur.fetchall()
    if col_name.lower() not in q.lower():
        return True
    return False


def col_names(tbl_name):  # return list of column names or 0 if no columns
    cur.execute(f"PRAGMA table_info({tbl_name});")
    rows = cur.fetchall()
    names = []
    if not rows:
        return 0
    else:
        for row in rows:
            names.append(row[1])
        return names


def col_types(tbl_name):  # return list of column types or 0 if no columns
    cur.execute(f"PRAGMA table_info({tbl_name});")
    rows = cur.fetchall()
    types = []
    if not rows:
        return 0
    else:
        for row in rows:
            types.append(row[2])
        return types


def frametbl(
    ctl, cnl
):  # creates a frame(horizontal) for the table display, ctl-column type list, cnl-column name list
    print("", end="+")
    for ct, cn in zip(ctl, cnl):
        if ct == "INTEGER":
            print("-" * 7, end="+")
        elif ct == "REAL":
            print("-" * 7, end="+")
        elif cn == "email":
            print("-" * 20, end="+")
        else:
            print("-" * 16, end="+")
    print("")


###########################################################################################
# functions
def add_rto():
    global msg
    location = input("Enter RTO location: ").strip()
    phone_no = input("Enter RTO phone number: ").strip()
    email = input("Enter RTO email: ").strip()
    if not (location and phone_no and email):
        print("All fields are required.")
        msg = "FAILURE: RTO not added"
        return
    if not (phone_no.isdigit() and len(phone_no) == 10):
        print("Phone number must be 10 digits long.")
        msg = "FAILURE: RTO not added"
        return
    if "@" not in email or "." not in email.split("@")[-1]:
        print("Invalid email format.")
        msg = "FAILURE: RTO not added"
        return

    cur.execute(
        "INSERT INTO rto (location, phone_no, email) VALUES (?, ?, ?)",
        (location, phone_no, email),
    )
    con.commit()
    print("RTO added successfully.")
    msg = "SUCCESS: RTO added"


def add_driving_license():  # 2
    global msg
    date_now=f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day}"
    dl_no = input("Enter Driving License number: ").strip()
    cov = (
        input("Enter Class of Vehicle (MCWG, MCWOG, LMV, HMV, MGV, HGV): ")
        .strip()
        .upper()
    )
    issue_date = input("Enter Issue Date (YYYY-MM-DD): ").strip()
    expiry_date = input("Enter Expiry Date (YYYY-MM-DD): ").strip()
    # status = input("Enter Status (valid/expired): ").strip().lower()
    if not (dl_no and cov and issue_date and expiry_date):
        print("All fields are required.")
        msg = "FAILURE: Driving License not added"
        return
    if cov not in ("MCWG", "MCWOG", "LMV", "HMV", "MGV", "HGV"):
        print(
            "Invalid Class of Vehicle. Must be one of: MCWG, MCWOG, LMV, HMV, MGV, HGV."
        )
        msg = "FAILURE: Driving License not added"
        return
    if expiry_date > date_now:
        status = "valid"
    else:
        status = "expired"
    # if status.lower() not in ("valid", "expired"):
    #     print("Invalid status. Must be 'valid' or 'expired'.")
    #     msg = "FAILURE: Driving License not added"
    #     return
    cur.execute(
        "INSERT INTO driving_license (dl_no, cov, issue_date, expiry_date, status) VALUES (?, ?, ?, ?, ?)",
        (dl_no, cov, issue_date, expiry_date, status),
    )
    con.commit()
    print("Driving License added successfully.")
    msg = "SUCCESS: Driving License added"


def add_vehicle():  # 3
    global msg
    veh_name = input("Enter Vehicle Name: ").strip()
    veh_type = input("Enter Vehicle Type (e.g., Car, Bike, Truck): ").strip()
    manufacturer = input("Enter Manufacturer: ").strip()
    model = input("Enter Model: ").strip()
    year = input("Enter Year of Manufacture : ").strip()
    engine_no = input("Enter Engine Number: ").strip()
    chassis_no = input("Enter Chassis Number: ").strip()
    owner_id = input("Enter Owner ID: ").strip()
    if not (
        veh_name
        and veh_type
        and manufacturer
        and model
        and year
        and engine_no
        and chassis_no
        and owner_id
    ):
        print("All fields are required.")
        msg = "FAILURE: Vehicle not added"
        return
    if not year.isdigit() or not (1886 < int(year) <= datetime.now().year):
        print("Year must be a valid year greater than 1885 and not in the future.")
        msg = "FAILURE: Vehicle not added"
        return
    cur.execute(
        "INSERT INTO vehicle (veh_name, veh_type, manufacturer, model, year, engine_no, chassis_no, owner_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (
            veh_name,
            veh_type,
            manufacturer,
            model,
            int(year),
            engine_no,
            chassis_no,
            owner_id,
        ),
    )
    con.commit()
    print("Vehicle added successfully.")


def add_owner():  # 4
    global msg
    name = input("Enter Owner Name: ").strip()
    age = input("Enter Owner Age: ").strip()
    address = input("Enter Owner Address: ").strip()
    pincode = input("Enter Owner Pincode: ").strip()
    phone = input("Enter Owner Phone Number: ").strip()
    email = input("Enter Owner Email: ").strip()
    driving_license = input("Enter Driving License ID: ").strip()
    if not (
        name and age and address and pincode and phone and email and driving_license
    ):
        print("All fields are required.")
        return
    if not age.isdigit() or int(age) <= 17:
        print("Age must be a number greater than 17.")
        return
    if not (phone.isdigit() and len(phone) == 10):
        print("Phone number must be 10 digits long.")
        return
    if "@" not in email or "." not in email.split("@")[-1]:
        print("Invalid email format.")
        return
    cur.execute(
        "INSERT INTO owner (name, age, address, pincode, phone, email, driving_license) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (name, int(age), address, pincode, phone, email, driving_license),
    )
    if cur.rowcount == 0:
        msg = "FAILURE: Owner not added"
        print("Failed to add owner. Please check the details and try again.")
        return
    con.commit()
    print("Owner added successfully.")


def add_insurance():  # 5
    provider = input("Enter Insurance Provider: ").strip()
    policy_no = input("Enter Policy Number: ").strip()
    start_date = input("Enter Start Date (YYYY-MM-DD): ").strip()
    end_date = input("Enter End Date (YYYY-MM-DD): ").strip()
    veh_id = input("Enter Vehicle ID: ").strip()
    status = input("Enter Status (active/expired): ").strip().lower()
    if not (provider and policy_no and start_date and end_date and veh_id and status):
        print("All fields are required.")
        return
    if status not in ("active", "expired"):
        print("Invalid status. Must be 'active' or 'expired'.")
        return
    cur.execute(
        "INSERT INTO insurance (provider, policy_no, start_date, end_date, veh_id, status) VALUES (?, ?, ?, ?, ?, ?)",
        (provider, policy_no, start_date, end_date, veh_id, status),
    )
    con.commit()
    print("Insurance added successfully.")


def add_registration():  # 6
    reg_no = input("Enter Registration Number: ").strip()
    veh_id = input("Enter Vehicle ID: ").strip()
    rto_id = input("Enter RTO ID: ").strip()
    reg_date = input("Enter Registration Date (YYYY-MM-DD): ").strip()
    if len(reg_date) != 10:
        return
    status = input("Enter Status (pending/approved/rejected): ").strip().lower()
    if not (reg_no and veh_id and rto_id and reg_date and status):
        print("All fields are required.")
        return
    if status not in ("pending", "approved", "rejected"):
        print("Invalid status. Must be 'pending', 'approved', or 'rejected'.")
        return
    cur.execute(
        "INSERT INTO registration (reg_no, veh_id, rto_id, reg_date, status) VALUES (?, ?, ?, ?, ?)",
        (reg_no, veh_id, rto_id, reg_date, status),
    )
    con.commit()
    reg_id = cur.lastrowid
    print(f"Registration added successfully.Your registation id is {reg_id}")


def view_table():  # 7
    print(
        "Available tables: rto, driving_license, vehicle, owner, insurance, registration"
    )
    tbl_name = input("Enter table name to view : ")
    cnl = col_names(tbl_name)
    ctl = col_types(tbl_name)
    if cnl == 0 or ctl == 0:
        print("Table does not have no columns or does not exist")
        return
    cur.execute(f"SELECT * FROM {tbl_name};")
    rows = cur.fetchall()
    if not rows:
        print("Table is empty")
        return
    frametbl(ctl, cnl)
    for cn, ct in zip(cnl, ctl):
        if ct == "INTEGER":
            print(f"| {cn:<6}", end="")
        elif ct == "REAL":
            print(f"| {cn:<6}", end="")
        elif cn == "email":
            print(f"| {cn:<19}", end="")
        else:
            print(f"| {cn:<15}", end="")
    print("|")
    frametbl(ctl, cnl)
    for row in rows:
        for item in row:
            if isinstance(item, (int, float)):
                print(f"| {str(item):<6}", end="")
            elif isinstance(item, str) and "@" in item:
                print(f"| {str(item):<19}", end="")
            else:
                print(f"| {str(item):<15}", end="")
        print("|")
    frametbl(ctl, cnl)


###########################################################################################

### Main program starts here
initialize_db()
msg = "program initialized"
con = sqlite3.connect("rvms.db")
cur = con.cursor()
while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(f"♦ Tracking message: {msg} @ {datetime.now():%H:%M:%S}")
    print("""Welcome to the RVMS (Road Vehicle Management System)!
    Please choose an option:
        1. Add RTO\t\t2. Add Driving License
        3. Add Vehicle\t\t4. Add Owner
        5. Add Insurance\t6. Add Registration
        7. View tables
        99. Exit
          """)
    op = input("Enter your choice: ")
    if op == "1":
        add_rto()
        input("Press Enter to continue...")
    elif op == "2":
        add_driving_license()
        input("Press Enter to continue...")
    elif op == "3":
        add_vehicle()
        input("Press Enter to continue...")
    elif op == "4":
        add_owner()
        input("Press Enter to continue...")
    elif op == "5":
        add_insurance()
        input("Press Enter to continue...")
    elif op == "6":
        add_registration()
        input("Press Enter to continue...")
    elif op == "7":
        view_table()
        input("Press Enter to continue...")
    elif op == "99":
        print("Exiting the program. Goodbye!")
        con.close()
        break
    else:
        print("Invalid option. Please try again.")
        input("Press Enter to continue...")

con.close()
