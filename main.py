# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from datetime import date, datetime, timedelta
import pytz
import json


def main():
    print_hi("Matthew")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press ⌘F8 to toggle the breakpoint.
    # today = date.today() + timedelta(days=-1)

    x = datetime(2018, 9, 15)
    print(x.strftime("%b %d %Y %H:%M:%S"))

    today = date.today()
    PST = pytz.timezone("Canada/Pacific")
    d2 = datetime.now().astimezone(PST)
    #d2 = datetime.now().astimezone().isoformat()
    today = datetime.now().astimezone(PST)
    #today = today.strftime("%B %d, %Y")
    print(today, "is Today's date:")
    print(d2, "is TToday's date:")
    weight = int(150)
    """data = {
        "entry": {
            "date": today,
            "weight": new_weight
        }
    }
    """


    with open('weight.txt', 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        print(f"{last_line} was the last time you weighed yourself")

    append_choice = str(input(f"Would you like to append your weight file? "))
    
    new_weight = str(input(f"How much do you weigh today? "))
    print(f"This is where the program finds your weight")
    
    data = {
        "entry": {
            "date": today,
            "weight": new_weight
        }
    }
    
    if append_choice.lower() == "y":
        print(f"This is where the file would be appended {data}")
        with open('weight.txt', 'a') as f:
            json.dump(data, f)
            f.write(f"{d2} {new_weight}\n")
            #f.write(str(d2) + str(new_weight) + "\n")

        #file = open('weight.txt', 'a')
        #file.write(str(today) + '\n')
        #file.close()
    

    
    """with open('weight.txt', 'a') as f:
        #json.dump(data, f)
        f.write(str(d2) + "\n")
    """

    #file = open('weight.txt', 'a')
    #file.write(str(today) + '\n')
    #file.close()


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
