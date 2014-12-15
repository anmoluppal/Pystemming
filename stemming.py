#The code was written using SUBLIME editor and tested on Python 2.7

import re
from define import VOWELS,STEP_1a_list,STEP_1a_dict,STEP_1b_lsit,STEP_1b_dict,STEP_3_list,STEP_3_dict,STEP_4_list,STEP_4_dict,STEP2_SUFFIX
#******************************************************************************
#******************************************************************************
STEP1B_EXT = 0


def check_vowels(word):
    for dummy_word in word:
        if dummy_word in VOWELS:
            return True
    return False
    
def check_cvc(word):
    # cvc stands for triplet of a consonant , vovel and a consonant at the end.
    consider = word[-3:]
    if re.match("[^aeiouy][aeiouy][^aeiouwxy]",consider):
        return True
    else:
        return False
        

def find_m(word):
    #Eery word is of the form [C] (VC)^m [V], So we are trying to get that value of m
    #For instance if a gien word has only vovels or only consonants then m=0 or if it has vovels and consonants such that no vovel comes after the occurence of consonants then alsp m= 0
    """
        Some examples:
            m=0         TR,   EE,   TREE,   Y,   BY.
            m=1         TROUBLE,   OATS,   TREES,   IVY.
            m=2         TROUBLES,   PRIVATE,   OATEN,   ORRERY. 
    """

    if re.match("[^aeiouy]*?[aeiouy]*?$",word):
        return 0
    elif re.match("[^aeiouy]*?[aeiouy]+[^aeiouy]+[aeiouy]*?$",word):
        return 1
    else:
        return 2

def check_double_word(word):
    #Checks if a given word ends with a double letter , eg' fall
    if len(word)>=2 and word[-1]==word[-2]:
        return True
    else:
        return False
  
#******************************************************************************      
"""
Step 1 Starts Here

Step 1 deals with plurals and past participles

"""
def check_step_1a(word):
    for i in STEP_1a_list:
        if word.endswith(i):
            word = word[:0-(len(i))]+STEP_1a_dict[i]
            break
    return word

#print check_step_1a("caresses")
#print check_step_1a("ponies")
#print check_step_1a("caress")
#print check_step_1a("cats")

def check_step_1b(word):
    global STEP1B_EXT
    if word.endswith("eed") and find_m(word[:-3])>0:
        word = word[:-3]+"ee"
    elif check_vowels(word[:-2]) and word.endswith("ed") and not word.endswith("eed"):
        STEP1B_EXT = 1
        word = word[:-2]
    elif check_vowels(word[:-3]) and word.endswith("ing"):
        STEP1B_EXT = 1
        word = word[:-3]
    return word
"""
The rule to map to a single letter causes the removal of one of the double letter pair. 
The -E is put back on -AT, -BL and -IZ, so that the suffixes -ATE, -BLE and -IZE can be recognised later. 
This E may be removed in step 4. 

"""
#print check_step_1b("feed")
#print check_step_1b("agreed")
#print check_step_1b("plastered")
#print check_step_1b("bled")
#print check_step_1b("motoring")
#print check_step_1b("sing")

def check_step_1b_ext(word):
    if word.endswith("at") or word.endswith("bl") or word.endswith("iz"):
        word+="e"
    if check_double_word(word) and not (word.endswith("l") or word.endswith("s") or word.endswith("z")):
        word = word[:-1]
    elif find_m(word)==1 and check_cvc(word):
        word+="e"
    return word
#print check_step_1b_ext("conflated")
#print check_step_1b_ext("troubled")
#print check_step_1b_ext("sized")
#print check_step_1b_ext("hopping")
#print check_step_1b_ext("tanned")
#print check_step_1b_ext("falling")
#print check_step_1b_ext("hissing")
#print check_step_1b_ext("fizzed")
#print check_step_1b_ext("failing")
#print check_step_1b_ext("filling")

def check_step_1c(word):
    if check_vowels(word[:-1]) and word.endswith("y"):
        word = word[:-1]+"i"
    return word


#print check_step_1c_ext("happy")
#print check_step_1c_ext("sky")
"""
Step 1 Ends Here....

Step 1 deals with plurals and past participles
"""

#******************************************************************************

"""
Step 2 Starts Here
"""

def check_step2(word):
    if word[-1] in STEP2_SUFFIX and len(word)>=2 and:
        if word[-2]=="a":
            if word.endswith("ational") and find_m(word[:-7])>0:
                word = word[:-7]+"ate"
            elif word.endswith("tional") and find_m(word[:-6])>0:
                word = word[:-6]+"tion"
        elif word[-2]=="c":
            if word.endswith("enci") and find_m(word[:-4])>0:
                word = word[:-4]+"ence"
            elif word.endswith("anci") and find_m(word[:-4])>0:
                word = word[:-4]+"ance"
        elif word[-2]=="e":
            if word.endswith("izer") and find_m(word[:-4])>0:
                word = word[:-4]+"ize"
        elif word[-2]=="l":
            if word.endswith("abli") and find_m(word[:-4])>0:
                word = word[:-4]+"able"
            elif word.endswith("alli") and find_m(word[:-4])>0:
                word = word[:-4]+"al"
            elif word.endswith("entli") and find_m(word[:-5])>0:
                word = word[:-5]+"ent"
            elif word.endswith("eli") and find_m(word[:-3])>0:
                word = word[:-3]+"e"
            elif word.endswith("ousli") and find_m(word[:-5])>0:
                word = word[:-5]+"ous"
        elif word[-2] == "o":
            if word.endswith("ization") and find_m(word[:-7])>0:
                word = word[:-7]+"ize"
            elif word.endswith("ation") and find_m(word[:-5])>0:
                word = word[:-5]+"ate"
            elif word.endswith("ator") and find_m(word[:-4])>0:
                word = word[:-4]+"ate"
        elif word[-2] == "s":
            if word.endswith("iveness") and find_m(word[:-7])>0:
                word = word[:-7]+"ive"
            elif word.endswith("fulness") and find_m(word[:-7])>0:
                word = word[:-7]+"ful"
            elif word.endswith("ousness") and find_m(word[:-7])>0:
                word = word[:-7]+"ous"
        elif word[-2] == "t":
            if word.endswith("aliti") and find_m(word[:-5])>0:
                word = word[:-5]+"al"
            elif word.endswith("iviti") and find_m(word[:-5])>0:
                word = word[:-5]+"ive"
            elif word.endswith("biliti") and find_m(word[:-6])>0:
                word = word[:-6]+"ble"
    return word
    

"""
print check_step2("conditional")
print check_step2("rational")
print check_step2("valenci")
print check_step2("hesitanci")
print check_step2("digitizer")
print check_step2("conformabli")
print check_step2("radicalli")
print check_step2("differentli")
print check_step2("vileli")
print check_step2("analogousli")
print check_step2("vietnamization")
print check_step2("predication")
print check_step2("operator")
print check_step2("feudalism")
print check_step2("decisiveness")
print check_step2("hopefulness")
print check_step2("callousness")
print check_step2("formaliti")
print check_step2("sensitiviti")
print check_step2("sensibiliti")
"""

#******************************************************************************

"""
Step 3 Starts Here
"""
def check_step3(word):
    if word[-1] in "eils":      # Checks if the word ends with any one of possible characters
        for dummy_key in STEP_3_list:
            if word.endswith(dummy_key) and find_m(word[:0-len(dummy_key)])>0:
                word = word[:0-(len(dummy_key))]+STEP_3_dict[dummy_key]
                break
    return word


"""
print check_step3("triplicate")
print check_step3("formative")
print check_step3("formalize")
print check_step3("hopeful")
print check_step3("goodness")
print check_step3("electrical")
print check_step3("electriciti")
"""


"""
STEP 3 Ends here 
"""
#******************************************************************************

"""
STEP 4 Reoves the suffixes

"""      
def check_step4(word):
    if word[-1] in "lerctnumis":      # Checks if the word ends with any one of possible characters
        for dummy_key in STEP_4_list:
            if word.endswith(dummy_key) and find_m(word[:0-len(dummy_key)])>1:
                if dummy_key == "ion" and word[-4] in "st":
                    word = word[:-3]
                else:
                    word = word[:0-(len(dummy_key))]+STEP_4_dict[dummy_key]
                    break
    return word
""" 
print check_step4("revival")
print check_step4("allowance")
print check_step4("inference")
print check_step4("airliner")
print check_step4("gyroscopic")
print check_step4("adjustable")
print check_step4("defensible")
print check_step4("irritant")
print check_step4("replacement")
print check_step4("adjustment")
print check_step4("dependent")
print check_step4("adoption")
print check_step4("homologou")
print check_step4("communism")
print check_step4("activate")
print check_step4("angulariti")
print check_step4("homologous")
print check_step4("effective")
print check_step4("bowdlerize")
"""
#******************************************************************************

def check_step_5a(word):
    if find_m(word[:-1])>1 and word.endswith("e"):
        word = word[:-1]
    elif find_m(word[:-1])==1 and not check_cvc(word[:-1]) and word.endswith("e"):
        word = word[:-1]
    return word
    
def check_step_5b(word):
    if find_m(word)>1 and check_double_word(word) and word.endswith("l"):
        word = word[:-1]
    return word
    
"""
print check_step_5a("cease")
print check_step_5b("controll")
print check_step_5b("roll")

"""

#******************************************************************************
