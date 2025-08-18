# FOOBAR Code Challenge - Easy
for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0:
        print(f"{i} FOOBAR!")
    elif i % 5 == 0:
        print(f"{i} BAR!")
    elif i % 3 == 0:
        print(f"{i} FOO!")
    else:
        print(i)