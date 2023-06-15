# variable and collection assignment
osList = ["Windows 10", "MacOS Catalina", "Kali 2023.1"]
osCheck = "Ubuntu 22.04"

# if statement
if osCheck in osList:
    print(f'{osCheck} already in list')
elif osCheck not in osList:
    osList.append(osCheck)
    print(f'{osCheck} added to list')
    print(osList)