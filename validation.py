season = ["spring", "summer", "fall", "winter", "Spring", "Summer", "Fall", "Winter"]
favorite = input("your favorite season is: ")

if favorite in season:
    print(f"Your favorite season is {favorite}.")
else:
    print("Invalid season. Please choose from Spring, Summer, Fall, or Winter.")


try:
    number = float(input("Enter a price of the item: "))
    if number < 0:
        print("Invalid price! Please enter a valid price.")
    else:
        print(f"The price of the item is {number}.")
except:
    print("Invalid input! Please enter a valid number.")