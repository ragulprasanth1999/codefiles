def main():
    time = str(input("Enter time (e.g., 07:30): "))
    convert(time)

def convert(time):
    hours, minutes = time.split(":")
    h = int(hours)
    m = int(minutes)

    if h == 7 and 0 <= m <= 59:
        print("Breakfast time")
    elif h == 12 and 0 <= m <= 59:
        print("Lunch time")
    elif h == 18 and 0 <= m <= 59:
        print("Dinner time")
    else:
        pass

if __name__ == "__main__":
    main()
