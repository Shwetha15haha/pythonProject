for i,j in enumerate("Shwetha"):
    print(f"{i+1}.{j}")
# -----------------------------------------------------------------------
for i,j in enumerate([["a", "b"], ["c", "d"]]):
    print(f"{i+1}.{j}")
# -----------------------------------------------------------------------
waiting_list = ["john", "ben", "sen"]
waiting_list.sort()
for i, j in enumerate(waiting_list):
    print(f"{i+1}.{j.capitalize()}")
# --------------------------------------------------------------------------------
buttons = [('John', 'Sen', 'Morro'), ('Lin', 'Ajay', 'Filip')]
for first, second, third in buttons:
    print(first, second, third)