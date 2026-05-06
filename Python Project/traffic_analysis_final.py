# TRAFFIC DATA ANALYSIS SYSTEM
import os, csv          # check if file exists, read/write CSV (Module)
import numpy as np      # for calculations

# TUPLE - fixed constant, cannot be changed
DAYS_OF_WEEK = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
DATA_FILE = "traffic_data.csv"


# CLASSES & OBJECTS - Class is a blueprint; object is created from it
class TrafficRecord:                     # this class represents one traffic record
    def __init__(self, loc, day, hour, vehicles, speed):
        self.loc      = loc              # STRING attribute
        self.day      = day
        
        self.hour     = hour
        self.vehicles = vehicles
        self.speed    = speed

    def show(self):                      # METHOD: prints one record
        print(f"  {self.loc:<15}{self.day:<12}{self.hour:<7}{self.vehicles:<10}{self.speed} kmph")

    def summary(self):                   # METHOD: returns text summary
        return f"{self.loc} | {self.day} | Vehicles: {self.vehicles} | Speed: {self.speed} kmph"


# FILE HANDLING (write) - creates sample CSV if not present
def create_sample_file():
    rows = [                             # LIST of lists = rows of data
        ["Location","Day","Hour","Vehicle_Count","Avg_Speed_kmph"],
        ["MG Road","Monday","8","320","25"],
        ["MG Road","Friday","17","400","22"],
        ["MG Road","Saturday","11","180","45"],
        ["Ring Road","Monday","8","410","20"],
        ["Ring Road","Wednesday","10","350","28"],
        ["Ring Road","Sunday","14","200","55"],
        ["City Center","Monday","9","500","15"],
        ["City Center","Friday","18","480","18"],
        ["City Center","Wednesday","13","260","40"],
        ["Highway 1","Tuesday","7","600","80"],
        ["Highway 1","Thursday","8","580","75"],
        ["Highway 1","Sunday","10","400","90"],
    ]
    with open(DATA_FILE, "w", newline="") as f:   # FILE HANDLING (write mode)
        csv.writer(f).writerows(rows)
    print("  Sample file created.")


# FILE HANDLING (read) + EXCEPTION HANDLING + LIST + DICTIONARY + LOOP
def load_data():
    records = []                         # LIST to store all records
    try:
        with open(DATA_FILE, "r") as f:            # FILE HANDLING (read mode)
            for row in csv.DictReader(f):          # LOOP + DICTIONARY
                records.append(row)
    except FileNotFoundError:                      # EXCEPTION HANDLING
        create_sample_file()
        return load_data()
    except Exception as e:
        print(f"  [ERROR] {e}")
    return records


# SETS + LOOP + STRINGS + DICTIONARY: show summary
def view_summary(records):
    print("\n  ----  TRAFFIC DATA SUMMARY  ----")
    print(f"  Total Records   : {len(records)}")   # LIST len()
    locs = set()    # SET - removes duplicates automatically
    days = set()
    for r in records:                              # LOOP
        locs.add(r["Location"])                   # DICTIONARY key access
        days.add(r["Day"])
    print(f"  Locations       : {', '.join(sorted(locs))}")   # STRINGS .join()
    print(f"  Days in Data    : {', '.join(sorted(days))}")


# CONDITIONAL + LOOP + STRINGS + SETS + TUPLE + CLASSES & OBJECTS: filter
def filter_data(records):
    print("  1. By Day   2. By Location")
    choice = input("  Choice: ").strip()    # STRINGS .strip()
    results = []                            # LIST

    if choice == "1":                       # CONDITIONAL
        print(f"  Days: {', '.join(DAYS_OF_WEEK)}")    # TUPLE display
        day = input("  Enter day: ").strip().title()   # STRINGS .title()
        for r in records:                   # LOOP
            if r["Day"].lower() == day.lower():        # STRINGS .lower()
                results.append(r)
    elif choice == "2":
        locs = set(r["Location"] for r in records)    # SET
        print(f"  Locations: {', '.join(sorted(locs))}")
        loc = input("  Enter location: ").strip()
        for r in records:                   # LOOP
            if r["Location"].lower() == loc.lower():
                results.append(r)
    else:
        print("  Invalid choice."); return  # CONDITIONAL

    if len(results) == 0:                   # CONDITIONAL
        print("  No records found.")
    else:
        print(f"\n  {'Location':<15}{'Day':<12}{'Hour':<7}{'Vehicles':<10}Speed")
        print("  " + "-"*52)
        for r in results:                   # LOOP
            TrafficRecord(r["Location"], r["Day"], r["Hour"],   # OBJECT creation
                          r["Vehicle_Count"], r["Avg_Speed_kmph"]).show()   # METHOD call


# STRINGS + LOOP + CLASSES & OBJECTS: keyword search
def search_records(records):
    kw = input("  Enter keyword: ").strip().lower()   # STRINGS
    found = []                              # LIST
    for r in records:                       # LOOP
        if kw in r["Location"].lower() or kw in r["Day"].lower():  # STRINGS 'in'
            found.append(r)
    if not found:
        print(f"  No results for '{kw}'.")
    else:
        print(f"\n  {'Location':<15}{'Day':<12}{'Hour':<7}{'Vehicles':<10}Speed")
        print("  " + "-"*52)
        for r in found:                     # LOOP
            TrafficRecord(r["Location"], r["Day"], r["Hour"],   # OBJECT creation
                          r["Vehicle_Count"], r["Avg_Speed_kmph"]).show()  # METHOD call


# FILE HANDLING (append) + EXCEPTION + TUPLE + CONDITIONAL + CLASSES: add record
def add_record(records):
    try:                                    # EXCEPTION HANDLING
        loc = input("  Location      : ").strip().title()   # STRINGS
        print(f"  Days: {', '.join(DAYS_OF_WEEK)}")         # TUPLE
        day = input("  Day           : ").strip().title()
        if day not in DAYS_OF_WEEK:         # CONDITIONAL + TUPLE
            print("  [ERROR] Invalid day."); return
        hour = int(input("  Hour (0-23)   : "))
        if not (0 <= hour <= 23):           # CONDITIONAL
            print("  [ERROR] Invalid hour."); return
        veh = int(input("  Vehicle Count : "))
        spd = float(input("  Speed (kmph)  : "))
        if veh < 0 or spd < 0:             # CONDITIONAL
            print("  [ERROR] Negative values not allowed."); return

        obj = TrafficRecord(loc, day, str(hour), str(veh), str(spd))  # OBJECT
        print(f"\n  Preview - {obj.summary()}")    # METHOD call

        rec = {"Location": obj.loc, "Day": obj.day, "Hour": obj.hour,   # DICTIONARY
               "Vehicle_Count": obj.vehicles, "Avg_Speed_kmph": obj.speed}

        with open(DATA_FILE, "a", newline="") as f:    # FILE HANDLING (append mode)
            w = csv.DictWriter(f, fieldnames=list(rec.keys()))
            w.writerow(rec)
        records.append(rec)                 # LIST .append()
        print("  [SUCCESS] Record saved!")

    except ValueError:                      # EXCEPTION HANDLING
        print("  [ERROR] Enter valid numbers.")
    except Exception as e:
        print(f"  [ERROR] {e}")


# NUMPY + LOOP + EXCEPTION HANDLING: statistical analysis
def analyze_traffic(records):
    try:                                    # EXCEPTION HANDLING
        if not records:                     # CONDITIONAL
            print("  No data."); return
        vc = np.array([int(r["Vehicle_Count"])    for r in records])  # NUMPY + LOOP
        sp = np.array([float(r["Avg_Speed_kmph"]) for r in records])  # NUMPY + LOOP
        print("\n  -- Vehicle Count --")
        print(f"  Sum    : {np.sum(vc)}    Mean : {np.mean(vc):.1f}")  # NUMPY
        print(f"  Max    : {np.max(vc)}    Min  : {np.min(vc)}")       # NUMPY
        print(f"  Std Dev: {np.std(vc):.2f}")                          # NUMPY
        print("\n  -- Speed (kmph) --")
        print(f"  Mean   : {np.mean(sp):.1f}   Median: {np.median(sp):.1f}")  # NUMPY
        print(f"  Max    : {np.max(sp)}    Min   : {np.min(sp)}")              # NUMPY
    except Exception as e:
        print(f"  [ERROR] {e}")


# SETS + LOOP + STRINGS + TUPLE: unique locations and days
def show_unique(records):
    locs = set()    # SET
    days = set()
    for r in records:           # LOOP
        locs.add(r["Location"])
        days.add(r["Day"])
    print(f"\n  Unique Locations : {', '.join(sorted(locs))}")  # STRINGS .join()
    print(f"  Unique Days      : {', '.join(sorted(days))}")
    missing = set(DAYS_OF_WEEK) - days      # SET difference + TUPLE
    if missing:                             # CONDITIONAL
        print(f"  No data for      : {', '.join(sorted(missing))}")


# MAIN - menu loop
def main():
    if not os.path.exists(DATA_FILE):   # CONDITIONAL
        create_sample_file()
    records = load_data()               # LIST of dicts
    print(f"\n  Loaded {len(records)} records.")

    # CLASSES & OBJECTS - create object at startup to show first record
    if records:
        r0 = records[0]
        obj = TrafficRecord(r0["Location"], r0["Day"], r0["Hour"],  # OBJECT
                            r0["Vehicle_Count"], r0["Avg_Speed_kmph"])
        print(f"  First Record: {obj.summary()}")    # METHOD call

    while True:                         # LOOP (while)
        print("\n  ====  TRAFFIC DATA ANALYSIS SYSTEM  ====")
        print("  1. View Summary       4. Add Record")
        print("  2. Filter Data        5. NumPy Analysis")
        print("  3. Search Records     6. Unique Values")
        print("  0. Exit")
        try:                            # EXCEPTION HANDLING
            ch = input("  Choice: ").strip()   # STRINGS .strip()
        except KeyboardInterrupt:
            break

        if   ch == "1": view_summary(records)   # CONDITIONAL (if-elif-else)
        elif ch == "2": filter_data(records)
        elif ch == "3": search_records(records)
        elif ch == "4": add_record(records)
        elif ch == "5": analyze_traffic(records)
        elif ch == "6": show_unique(records)
        elif ch == "0":
            print("  Goodbye!"); break
        else:
            print("  Invalid choice.")

        input("\n  Press Enter to continue...")

if __name__ == "__main__":
    main()