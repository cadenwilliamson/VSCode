file_path = "Python\\MessinAround\\foobar.py"


### FULL STYLE, IDK ###
# file = open(file_path)
# content = file.read()

# print(f'Filename: {file.name}')
# print(f'Mode: {file.mode}')
# print(f'Is Closed?: {file.closed}')

# print(f"\nContent:\n{content}")

# file.close()
# print("-" * 30)

# print(f'Filename: {file.name}')
# print(f'Mode: {file.mode}')
# print(f'Is Closed?: {file.closed}')


### WITH STATEMENT ###
# with open(file_path) as file:
#     content = file.read()
#     print(content)


### TRY and FINALLY ###
try:
    file = open(file_path)
    content = file.read()
    print(content)
finally:
    file.close()