#TODO: Create a letter using starting_letter.txt


#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt",'r',newline='') as f2:
    names_l = f2.read()
    names = names_l.split()
    for name in names:
        with open(f"./Output/ReadyToSend/{name}.txt", 'w') as f1:

            with open("./Input/Letters/starting_letter.txt",'r') as f3:
                lines = f3.readlines()
                for line in lines:
                    words = line.split()
                    for word in words:
                        if word == "[name],":
                            # Replace the [name] placeholder with the actual name.
                            line = line.replace("[name]",name)

                    # Save the letters in the folder "ReadyToSend".
                    writer = f1.write(line)



    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp