for i, j in enumerate("Shwetha"):
    print(f"{i+1}.{j}")
# output
# 1.S
# 2.h
# 3.w
# 4.e
# 5.t
# 6.h
# 7.a
# -----------------------------------------------------------------------
for i, j in enumerate([["a", "b"], ["c", "d"]]):
    print(f"{i+1}.{j}")
# output :
# 1.['a', 'b']
# 2.['c', 'd']
# -----------------------------------------------------------------------
waiting_list = ["john", "ben", "sen"]
waiting_list.sort()
for i, j in enumerate(waiting_list):
    print(f"{i+1}.{j.capitalize()}")
# output: 1.Ben
# 2.John
# 3.Sen
# -----------------------------------------------------------------------
buttons = [('John', 'Sen', 'Moro'), ('Lin', 'Ajay', 'Filip')]
for first, second, third in buttons:
    print(first, second, third)
# output :
# John Sen Moro
# Lin Ajay Filip
