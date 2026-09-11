FILE_NAME = "study_log.txt"

def classify_session(duration):
    if duration < 30:
        return "Short"
    if duration >= 30 and duration <= 90:
        return "Medium"
    if duration > 90:
        return "Long"

def load_sessions():
    sessions = []
    try:
        f = open(FILE_NAME, "r")
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            subject = parts[0]
            topic = parts[1]
            date = parts[2]
            duration = float(parts[3])
            d = {"subject": subject, "topic": topic, "date": date, "duration": duration}
            sessions.append(d)
        f.close()
    except FileNotFoundError:
        print("No old file found, starting new")
    return sessions

def save_sessions(sessions):
    f = open(FILE_NAME, "w")
    for s in sessions:
        line = s["subject"] + "," + s["topic"] + "," + s["date"] + "," + str(s["duration"])
        f.write(line + "\n")
    f.close()
    print("Saved!")

def add_session(sessions):
    print("\n--- Add Session ---")
    subject = input("Enter subject name: ")
    topic = input("Enter topic: ")
    date = input("Enter date/day: ")
    while True:
        try:
            duration = float(input("Enter duration in minutes: "))
            if duration <= 0:
                print("Must be more than 0")
            else:
                break
        except:
            print("Enter valid number")
    d = {"subject": subject, "topic": topic, "date": date, "duration": duration}
    sessions.append(d)
    print("Added, type is", classify_session(duration))

def view_sessions(sessions):
    print("\n--- All Sessions ---")
    if len(sessions) == 0:
        print("No sessions yet")
        return
    print("Subject | Topic | Date | Duration | Type")
    for s in sessions:
        print(s["subject"], "|", s["topic"], "|", s["date"], "|", s["duration"], "|", classify_session(s["duration"]))

def search_by_subject(sessions):
    key = input("\nEnter subject to search: ")
    key = key.lower()
    found = []
    total = 0
    for s in sessions:
        if s["subject"].lower() == key:
            found.append(s)
            total = total + s["duration"]
    if len(found) == 0:
        print("No sessions found for", key)
    else:
        for s in found:
            print(s["subject"], "-", s["topic"], "-", s["date"], "-", s["duration"], "mins")
        print("Total for", key, "is", total, "minutes")

def study_statistics(sessions):
    if len(sessions) == 0:
        print("No data yet")
        return
    total_all = 0
    for s in sessions:
        total_all = total_all + s["duration"]
    print("\n--- Statistics ---")
    print("Total hours:", total_all / 60)
    print("Total mins:", total_all)
    subs = {}
    for s in sessions:
        sub = s["subject"]
        if sub not in subs:
            subs[sub] = 0
        subs[sub] = subs[sub] + s["duration"]
    print("\nHours per subject:")
    for sub in subs:
        print(sub, ":", subs[sub] / 60, "hours")
    least_sub = ""
    least_time = 9999999
    for sub in subs:
        if subs[sub] < least_time:
            least_time = subs[sub]
            least_sub = sub
    print("\nWeakest area:", least_sub, "-", least_time, "mins")
    longest = sessions[0]
    for s in sessions:
        if s["duration"] > longest["duration"]:
            longest = s
    print("Longest session:", longest["subject"], longest["topic"], longest["duration"], "mins")

def main():
    sessions = load_sessions()
    while True:
        print("\n===== SMART STUDY PLANNER =====")
        print("1. Add a study session")
        print("2. View all sessions")
        print("3. Search sessions by subject")
        print("4. View statistics")
        print("5. Save and exit")
        choice = input("Enter choice (1-5): ")
        if choice == "1":
            add_session(sessions)
        elif choice == "2":
            view_sessions(sessions)
        elif choice == "3":
            search_by_subject(sessions)
        elif choice == "4":
            study_statistics(sessions)
        elif choice == "5":
            save_sessions(sessions)
            print("Bye bye")
            break
        else:
            print("Wrong choice, try 1-5")

if __name__ == "__main__":
    main()