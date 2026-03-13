with open("accounts.txt", "r") as file:
 file.write("Word \n")
 accounts = file.read().splitlines()

print(accounts)