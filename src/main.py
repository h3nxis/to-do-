import sqlite3
from datetime import datetime
def main():
    conn = sqlite3.connect("works.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS works (date TEXT, work TEXT, description TEXT, time TEXT)")


    try:
        whats_to_do = int(input("what's to do? (enter 1 for add, 2 for view, 3 for delete, 4 for today's works, 5 for completed works, 0 for exit)"))
    except ValueError:
        print("invalid input")
        return
    


    if whats_to_do == 1:
        work = input("work: ")
        description = input("description: ")
        time = input("time: (example 10:00-11:00)")
        try:
            date = datetime.strptime(input("date: "), "%Y-%m-%d")
            date = date.strftime("%Y-%m-%d")
        except ValueError:
            print("invalid date")
            return
        cursor.execute("INSERT INTO works (date, work, description, time) VALUES (?, ?, ?, ?)", (date, work, description, time))
        conn.commit()

    elif whats_to_do == 2:
        cursor.execute("SELECT * FROM works")
        works = cursor.fetchall()
        for work in works:
            print(f" date: {work[0]} work: {work[1]} description: {work[2]} time: {work[3]}")
    elif whats_to_do == 3:
        work_for_delete = input("work:")
        date_for_delete = input("date:")
        time_for_delete = input("time:")
        try:
            cursor.execute("DELETE FROM works WHERE work = ? AND date = ? AND time = ?", (work_for_delete, date_for_delete, time_for_delete))
            conn.commit()
        except sqlite3.OperationalError:
            print("no such work at this date")
            return
    elif whats_to_do == 4:
        today = datetime.now().strftime("%Y-%m-%d")
        cursor.execute("SELECT * FROM works WHERE date = ?", (today,))
        works = cursor.fetchall()
        for work in works:
            print(f" date: {work[0]} work: {work[1]} description: {work[2]} time: {work[3]}")
        return
    elif whats_to_do == 5:
        work_for_complete = input("work:")
        date_for_complete = input("date:")
        time_for_complete = input("time:")
        try:
            cursor.execute("UPDATE works SET completed = 1 WHERE work = ? AND date = ? AND time = ?", (work_for_complete, date_for_complete, time_for_complete))
            conn.commit()
        except sqlite3.OperationalError:
            print("no such work at this date")
            return        
        return
    elif whats_to_do == 0:
        return
    else:
        print("invalid input")
        return

main()