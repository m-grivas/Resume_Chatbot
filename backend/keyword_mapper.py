#List with basic responses
responses = [
    "Hi, I am Mike, a computer science student at Computer Science Department of University of Crete. I am interested in AI technologies and web applications.", #whoami
    "I am hard working, willing to help but also strong opinionated and competitive.", #personality
    "I have advanced python and cpp knowledge. Moreover, I am familiar with arduino and EV3 robot programing.", #skills
    "I have no prior work experience.", #work
    "I am studying at Computer Science Department of University of Crete", #studies
    "I have participated in many mathematics and robotics competitions, with distinctions in many of them.", #projects-achievements
    "I love sailing, playing chess, going to the gym and swimming." #hobbies
]


#function to read content from the file and put it in a 2d jagged array by groups
def load_keywords(file_name):
    #setup jagged array for keywords
    key_array = []
    current_group = []

    #open file with keywords
    with open(file_name, "r") as file:
        for line in file:
            #check if "#" in line
            if "#" in line:
                #append group to key_array and initialize it for the next group
                if current_group:
                    key_array.append(current_group)
                    current_group = []
            
            #if empty line dont include it in the array
            elif line.strip() == '':
                continue
            
            else:
                #append line to group
                current_group.append(line.strip())
    
    #append last group
    key_array.append(current_group)

    return key_array

