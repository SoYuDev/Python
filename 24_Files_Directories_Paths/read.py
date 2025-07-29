# This file is just for study purposes, it is not used in the snake game.

# Get access to the file
file = open("snake/my_file.txt")
# Read the file and return a String
contents = file.read()
print(contents)
file.close()

# Another way to use files but the program will close them up automatically
with open("snake/my_file.txt") as f:
    contents = f.read()
    print(contents)

with open("snake/my_file.txt", mode="a") as fi:
    fi.write("\nHola buenos días")