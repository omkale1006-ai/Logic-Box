# 🎯 Main Menu System Program
print("👋 Welcome to the Python Utility Program!")
print("💡 Choose an option from the menu below to get started.")

while True:
    print("\n📜 Main Menu:")
    print("1️⃣  Even or Odd Checker")
    print("2️⃣  Age Eligibility Checker")
    print("3️⃣  Leap Year Finder")
    print("4️⃣  Exit")

    ch = input("👉 Enter your choice (1-4): ")

    if ch == "1":
        number = int(input("🔢 Enter your number: "))
        if number % 2 == 0:
            print(f"✅ The number {number} is Even.")
        else:
            print(f"🔹 The number {number} is Odd.")

    elif ch == "2":
        age = int(input("🎂 Enter your age: "))
        if age >= 18:
            print("🗳️ Congratulations! You are eligible to vote.")
        else:
            print("⏳ Sorry, you are not eligible to vote yet.")

    elif ch == "3":
        year = int(input("📅 Enter a year: "))
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("🌟 Yes! It’s a Leap Year.")
        else:
            print("🚫 Nope! This is not a Leap Year.")

    elif ch == "4":
        print("👋 Thank you for using the program! Goodbye!")
        break

    else:
        print("⚠️ Invalid choice! Please enter a number between 1 and 4.")
