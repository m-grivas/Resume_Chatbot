import re
import numpy as np


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


def find_best_response(file_name, question):
    key_array = load_keywords(file_name)
    
    #create an zero array which contains the times a relative word is found for each answer
    finds = [0] * 7

    #for each category store the times a relative word appears in the question
    for i in range(7):
        for word in key_array[i]:
            pattern = fr"\w*{word}\w*"

            if re.search(pattern, question, re.IGNORECASE):
                finds[i] += 1


    #apply weighs to answers
    finds = np.array(finds)
    weights = np.array([0.8, 1, 1, 0.9, 0.9, 1, 1])
    finds = finds*weights

    #find max argument's index and return it
    max_index = np.argmax(finds)

    return responses[max_index]


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

