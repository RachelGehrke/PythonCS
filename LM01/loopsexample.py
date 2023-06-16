# Create Variables
os = input("Enter OS:")
osList = ["Windows 10", "MacOS Catalina", "Kali 2023.1"]

# While loop
while os not in osList:
    print("Please enter only one of the following")
    for x in osList:
        print(x)
    os = input("Enter OS:")

print(f'Thank you for entering {os}')