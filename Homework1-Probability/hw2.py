import sys
import math
import numpy as np

def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the 26-dimensional multinomial
    parameter vector (character probabilities of English and Spanish) as
    described in section 1.2 of the writeup.

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e = [0] * 26
    s = [0] * 26

    with open('e.txt', encoding='utf-8') as f:
        for line in f:
               #strip: removes the newline character
            #split: split the string on space character

            char, prob = line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.

            e[ord(char) - ord('A')] = float(prob)
    f.close()

    with open('s.txt', encoding='utf-8') as f:
        for line in f:
            char, prob = line.strip().split(" ")
            s[ord(char) - ord('A')] = float(prob)

    return e, s

def shred(filename):
    '''
    Reads a text file and counts the occurrences of each letter A-Z (ignoring case),
    returning a dictionary of character counts.
    '''
     #Using a dictionary here. You may change this to any data structure of
    #your choice such as lists (X=[]) etc. for the assignment

    X = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}  # Initialize dictionary

    with open(filename, encoding='utf-8') as f:
         # TODO: add your code here
         
         #read the file and convert the text to uppercase
         text = f.read().upper()
         for char in text:
             #check if the character is an alphabet A-Z afer case-floding 
                if 'A' <= char <= 'Z':  # Only count A-Z
                    X[char] += 1 #increment the count of the character by 1

    return X 

# TODO: add your code here for the assignment
# You are free to implement it as you wish!
# Happy Coding!



def output():
    # Check for correct command-line arguments
    if len(sys.argv) != 4:
        print("Usage: python hw2.py <input_file> <prior_english> <prior_spanish>")
        sys.exit(1)

    input_file = sys.argv[1]
    prior_english = float(sys.argv[2])
    prior_spanish = float(sys.argv[3])
        
    # Compute character counts
    letter_counts = shred(input_file)
    print("Q1")
    for char_code in range(ord('A'), ord('Z') + 1):
        char = chr(char_code)
        print(f"{char} {letter_counts[char]}")

    # Language identification 
    english_vector, spanish_vector = get_parameter_vectors()

    #probabilities for the first character 
    count_A = letter_counts['A']
    log_prob_A_english = count_A * math.log(english_vector[0]) if english_vector[0] > 0 else 0.0
    log_prob_A_spanish = count_A * math.log(spanish_vector[0]) if spanish_vector[0] > 0 else 0.0

    print("Q2")
    print(f"{log_prob_A_english:.4f}")
    print(f"{log_prob_A_spanish:.4f}")

    # Compute F_english and F_spanish log joint probabilities
    F_english = math.log(prior_english)  # log(P(Y=English))
    F_spanish = math.log(prior_spanish) # log(P(Y=Spanish))

    for i in range(26):
        letter = chr(ord('A') + i)
        count = letter_counts[letter]
        # Add log(p_i^X_i) = X_i * log(p_i) for English
        if english_vector[i] > 0:
            F_english += count * math.log(english_vector[i])
        # Add log(p_i^X_i) = X_i * log(p_i) for Spanish
        if spanish_vector[i] > 0:
            F_spanish += count * math.log(spanish_vector[i])

    print("Q3")
    print(f"{F_english:.4f}")
    print(f"{F_spanish:.4f}")

    # Compute posterior probability P(Y=English|X)
    # Use log-sum-exp trick to avoid underflow
    diff = F_spanish - F_english  # log(P(X|Spanish)P(Spanish)) - log(P(X|English)P(English))
    
    if diff > 100:  # P(English|X) ≈ 0
       probability_english = 0.0  # English is extremely unlikely
    elif diff < -100:  # P(English|X) ≈ 1
         probability_english = 1.0 # English is almost certain
    else:
        probability_english = 1 / (1 + math.exp(diff))  # Sigmoid of -diff

    print("Q4")
    print(f"{probability_english:.4f}")

if __name__ == "__main__":
    output()   

