for i,j in enumerate("Shwetha"):
    print(f"{i+1}.{j}")
print("")
for i,j in enumerate([["a", "b"], ["c", "d"]]):
    print(f"{i+1}.{j}")
print("")
waiting_list = ["john", "ben", "sen"]
waiting_list.sort()
for i, j in enumerate(waiting_list):
    print(f"{i+1}.{j.capitalize()}")
