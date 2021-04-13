import random
import time
import os
import sqlite3

conn = sqlite3.connect('main.db')

conn.execute(f'''CREATE TABLE IF NOT EXISTS RESERVATION (
                ID INT PRIMARY KEY     NOT NULL,
                NAME             TEXT   NOT NULL,
                DATE              TEXT   NOT NULL,
                TIME              TEXT   NOT NULL,
                ADULTS            INT    NOT NULL,
                CHILD             INT    NOT NULL,
                TOTAL             INT    NOT NULL);''')

def var():
    print("[a]View All\n[b]View by ID\n[c]Back\n")
    choice = input("PLEASE CHOOSE: ")
    if choice == 'a':
        os.system('cls')
        cursor = conn.execute(f"SELECT id, name, date, time, adults, child from RESERVATION")
        for row in cursor:
            print('\n')
            print("RESERVATION:\n")
            print("ID = ", row[0])
            print("NAME = ", row[1])
            print("DATE = ", row[2])
            print("TIME = ", row[3], '\n')
            print("ADULTS = ", row[4])
            print("CHILDREN = ", row[5], '\n')
        input("Press Enter if Satisfied")
        os.system('cls')

    elif choice == 'b':
        os.system('cls')
        while 1:
            id = input("Input your ID: ")
            os.system('cls')
            if conn.execute(f"SELECT id FROM RESERVATION where id={id}").fetchone():
                cursor = conn.execute(f"SELECT name, date, time, adults, child from RESERVATION WHERE id = {id}")
                for row in cursor:
                    print('\n')
                    print("RESERVATION:\n")
                    print("NAME = ", row[0])
                    print("DATE = ", row[1])
                    print("TIME = ", row[2], '\n')
                    print("ADULTS = ", row[3])
                    print("CHILDREN = ", row[4], '\n')
                    input("Press Enter if satisfied")
                break
            else:
                choice = input("No ID like that. type 'c' to repeat and 'n' to break: ")
                if choice == 'c':
                    os.system('cls')
                    continue
                else:
                    os.system('cls')
                    break
        os.system('cls')
    elif choice == 'c':
        os.system('cls')
        pass
    else:
        print("Wrong Input")

def mr():
    while 1:
        id = random.randint(1, 99)
        print("\nMAKE RESERVATION\n")

        name = input("Name: ")
        date = input("Date: ")
        time = input("Time: ")
        adults = int(input("No. of Adults: "))
        child = int(input("No. of Children: "))
        print('\n')

        tadults = adults * 500
        tchild = child * 300

        total = tadults + tchild

        conn.execute(
            f"INSERT INTO RESERVATION(ID,NAME,DATE,TIME,ADULTS,CHILD,TOTAL) VALUES ( '{id}', '{name}', '{date}', '{time}', '{adults}', '{child}', '{total}')")

        conn.commit()

        print(f"Your ID is {id} \n")

        choice = input("wish to reserve again? y/n: ")

        if choice == 'y':
            print('\n')
            continue
        else:
            break

    os.system('cls')

def dr():
    print("[a]Delete All\n[b]Delete by ID\n[c]Back\n")
    choice = input("YOUR CHOICE: ")
    if choice == 'a':
        os.system('cls')
        conn.execute("DELETE FROM RESERVATION")
        conn.commit()
        input("\nDONE\n\nHIT ENTER TO CONTINUE")
        os.system('cls')

    elif choice == 'b':
        os.system('cls')
        while 1:
            id = input("Enter ID: ")
            os.system('cls')
            if conn.execute(f"SELECT id FROM RESERVATION where id={id}").fetchone():

                conn.execute(f"DELETE FROM RESERVATION WHERE id={id}")

                conn.commit()

                os.system('cls')
            else:
                choice = input("No ID like that. type 'c' to repeat and 'n' to break: ")
                if choice == 'c':
                    os.system('cls')
                    continue
                else:
                    os.system('cls')
                    break

            cho = input("Wish to delete again? y/n: ")

            if cho == 'y' or cho == 'Y':
                os.system('cls')
                continue
            else:
                break
        os.system('cls')

    elif choice == 'c':
        os.system('cls')
        pass
    else:
        print("Wrong Input")

def gr():
    print("[a]Generate All Reports(CLI)\n[b]Generate Specific Reports\n[c]Back\n")
    choice = input("PLEASE CHOOSE: ")
    if choice == 'a':
        os.system('cls')
        cursor = conn.execute(f"SELECT id, name, date, time, adults, child, total from RESERVATION")
        cursor2 = conn.execute("SELECT sum(TOTAL) from RESERVATION")

        for row in cursor:
            print('\n')
            print(f"RESERVATION {row[0]}:\n")
            print("NAME = ", row[1])
            print("DATE = ", row[2])
            print("TIME = ", row[3], '\n')
            print("ADULTS = ", row[4])
            print("CHILDREN = ", row[5], '\n')
            print(f"Total of Reservation {row[0]}: PHP {row[6]}")

        data = cursor2.fetchall()[0][0]
        print("\n\n                                     Over All Total: PHP", data)

        print("\n")
        input("\nPRESS ENTER TO CONTINUE")
        os.system('cls')

    elif choice == 'b':
        while 1:
            os.system('cls')
            id = input("Enter ID: ")
            if conn.execute(f"SELECT id FROM RESERVATION where id={id}").fetchone():
                cursor = conn.execute(f"SELECT name, date, time, adults, child, total from RESERVATION where id={id}")
                for row in cursor:
                    print('\n')
                    print("RESERVATION:\n")
                    print("NAME = ", row[0])
                    print("DATE = ", row[1])
                    print("TIME = ", row[2], '\n')
                    print("ADULTS = ", row[3])
                    print("CHILDREN = ", row[4], '\n')
                    print("TOTAL = ", "PHP", row[5], '\n')
                cho = input("Check another Reservation? y/n: ")
                if cho == 'y' or cho == 'Y':
                    continue
                elif cho == 'n' or cho == 'N':
                    break
            else:
                choice = input("No ID like that. type 'c' to repeat and 'n' to break: ")
                if choice == 'c':
                    os.system('cls')
                    continue
                else:
                    os.system('cls')
                    break
        os.system('cls')

    elif choice == 'c':
        os.system('cls')
        pass
    else:
        print("WRONG INPUT")
        os.system('cls')

while 1:
    print("\n\n         PLEASE RUN IT ON COMMAND PROMPT FOR BETTER USE.")
    input("\n\n         PRESS ENTER \n\n")
    os.system('cls')
    print("\n\n         note** IT MAY NOT LOOK WELL IF YOU ARE USING OTHER TERMINAL OR CONSOLE.")
    input("\n\n         PRESS ENTER \n\n\n")
    os.system('cls')
    break

while 1:
    print("\n")
    print("SYSTEM MENU \n")
    print("[a]View all Reservations\n[b]Make Reservation\n[c]Delete Reservation\n[d]Generate Report\n[e]Exit")
    choice = input("\nYOUR CHOICE?: ")

    if choice == 'a':
        os.system('cls')
        var()
    elif choice == 'b':
        os.system('cls')
        mr()
    elif choice == 'c':
        os.system('cls')
        dr()
    elif choice == 'd':
        os.system('cls')
        gr()
    elif choice == 'e':
        os.system('cls')
        print("\n \nCome Again. Thank You.")
        break
    else:
        print("Please choose, a to e")
        time.sleep(1)
        os.system('cls')
