import random

'''''''''''''''''''''
main()

runs code
'''''''''''''''''''''


def main():
    print("Welcome to the RNT System!!!")
    print("RNT stands for Random Naruto Teams\n")
    random.seed()
    name = initializer()
    profile_filename = nametofile(name)
    repeat_str = "\nDo you want to (a) add another team, (b) choose a random team, or (c) end session?: "
    user_file = 'users.txt'
    if infile(user_file, name + "\n"):
        user_prof = validator("\nI see you have used this system before. Would you like"\
         " to (a) add on to your previous list or (b) choose a random team?: ", ['a', 'b'])
    else:
        print("\nCreating a profile for you...")
        addtofile(user_file, name)
        print("Done.\n")
        print("Now, let's add a team to your profile.")
        addTeam(profile_filename)
        user_prof = validator(repeat_str, ['a', 'b', 'c'])
    while user_prof[0] != 'c':
        if user_prof[0].lower() == 'a':
            print("Now, let's add a team to your profile.")
            addTeam(profile_filename)
        elif user_prof[0].lower() == 'b':
            print("Your team is...")
            print(randTeam(profile_filename))
        user_prof = validator(repeat_str, ['a', 'b', 'c'])
    print("Thank you for using the RNT system!!!")


'''''''''''''''''''''
initializer()

returns the inputted
name if correct
'''''''''''''''''''''


def initializer():
    correct = " "
    name = ""
    while not correct[0].lower() == 'y':
        name = validator("What is your name?: ")
        correct = validator("Is your name " + name + "? (Y/N): ", ['y', 'n'])
    return name


'''''''''''''''''''''
nametofile()

parameters:
    user's name

returns:
    the file
    associated with
    the user
'''''''''''''''''''''


def nametofile(name):
    temp_name = name.split()
    filename = ""
    length_tn = len(temp_name)
    for i in range(length_tn):
        if i == length_tn - 1:
            filename += temp_name[i] + ".txt"
            return filename
        filename += temp_name[i] + "_"
    

'''''''''''''''''''''
infile()

parameters:
    filename
    
    query term 

returns:
    true if query is
    in the file
'''''''''''''''''''''


def infile(file, name):
    all_names = Lister(file)
    return name in all_names


'''''''''''''''''''''
Lister()

parameters:
    read-version of
    file

returns:
    List of every
    line in the file
    without the
    break
    character
'''''''''''''''''''''


def Lister(read):
    with open(read) as f:
        all_teams = f.readlines()
    for i in range(len(all_teams)):
        all_teams[0].rstrip("\n")
    return all_teams


'''''''''''''''''''''
addtofile()

parameters:
    write-version of
    file
    
    string to be
    added to file
'''''''''''''''''''''


def addtofile(file, name):
    name += "\n"
    with open(file, 'a') as f:
        f.write(name)


'''''''''''''''''''''
teamStr()

parameters:
    list

returns:
    the list as a 
    string separated
    by commas
'''''''''''''''''''''


def teamStr(team):
    team_list = ""
    team_len = len(team)
    for i in range(team_len):
        team_list += team[i]
        if i < team_len - 1:
            team_list += ", "
    return team_list


'''''''''''''''''''''
chooseCharacter()

parameters:
    number that 
    describes which 
    character in the 
    team

returns:
    chosen character
'''''''''''''''''''''


def chooseCharacter(count):
    print()
    character = ""
    corr = ' '
    while corr[0].lower() != 'y':
        character = validator("Who is character " + str(count + 1) + " on your team?: ")
        corr = validator("Did you choose " + character + "? (Y/N): ", ['y', 'n'])
    return character


'''''''''''''''''''''
startTeam()

parameters:
    read-version of 
    file
    
    write-version of 
    file

creates team then 
adds to file
'''''''''''''''''''''


def addTeam(read):
    next_var = ' '
    team = []
    count = 0
    while count < 3 and next_var[0].lower() != 'n':
        character = chooseCharacter(count)
        team.append(character)
        count += 1
        if count < 3:
            next_var = validator("Do you want to add another character? (Y/N): ", ['y', 'n'])
    team_string = teamStr(team)
    if infile(read, team_string):
        duplicate = validator("Your team: " + team_string + "\nThis team is already in your\
         list. Do you want to duplicate it? (Y/N): ", ['y', 'n'])
        if duplicate == 'y':
            print("\nAdding team now...")
            addtofile(read, team_string)
            print("Your team has been duplicated.")
    else:
        print("\nYour team is: " + team_string)
        print("Adding team now...")
        addtofile(read, team_string)
        print("Your team has been successfully added.")

        

'''''''''''''''''''''
randTeam()

randomly chooses a 
team from the user's 
list of teams
'''''''''''''''''''''


def randTeam(read):
    all_teams = Lister(read)
    if len(all_teams):
        random.shuffle(all_teams)
        return random.choice(all_teams)
    else:
        print(all_teams)


'''''''''''''''''''''
validator()

parameters:
    array of correct
    choices
    
    string of 
    instructions

returns:
    correct inputted 
    value
'''''''''''''''''''''


def validator(string, arr=None):
    name = input(string)
    if arr is not None:
        while not len(name) and name[0].lower() not in arr:
            name = input("Error!!!\n" + string)
    else:
        while not len(name):
            name = input("Error!!!\n" + string)
    return name


if __name__ == '__main__':
    main()