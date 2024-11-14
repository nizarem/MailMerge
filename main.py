import os

with open('MailMerge/Input/Letters/starting_letter.txt', 'r') as file:
    sjabloon = file.read()

with open('MailMerge/Input/Names/invited_names.txt', 'r') as file:
    namen = file.readlines()


for naam in namen:
    naam = naam.strip()
    ReadyToSend = sjabloon.replace("[naam]", naam).replace("[jouw naam]", "Nizar")
    output_path = os.path.join('MailMerge/Output/ReadyToSend/', f"{naam}_letter.txt")


    with open(output_path, 'w') as file:
        file.write(ReadyToSend)
