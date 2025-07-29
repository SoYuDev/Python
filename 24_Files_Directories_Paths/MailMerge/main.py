# TODO: Create a letter using starting_letter.txt

# For each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Save the names in a list.
with open("Input/Names/invited_names.txt") as names:
    names_list = names.readlines()
# Save the content of the template letter
with open("Input/Letters/starting_letter.txt") as letter_file:
    content = letter_file.read()
    # Loop through all the names in the list
    for name in names_list:
        # Clear the spaces or \n that we currently have in the list
        stripped_name = name.strip()
        new_letter = content.replace("[name]", stripped_name)
        # Create a .txt for each name
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
