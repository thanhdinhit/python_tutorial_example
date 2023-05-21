# with open('readme.txt', 'w') as f:
#     f.write('Create a new text file!')

# with open('docs/readme.txt', 'w') as f:
#     f.write('Create a new text file!')

try:
    with open('readme.txt', 'w') as f:
        f.write('Create a new text file01!')
except FileNotFoundError:
    print("The 'docs' directory does not exist")

# with open('readme.txt', 'x') as f:
#     f.write('Create a new text file!')