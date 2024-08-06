




def bender_type():
    # personality = ["passionate","adaptable","peaceful","stubbborn"]
    # conflict = ["head-on","peacefully","adapt","stand-firm"]
    # motivation = ["achieving goals","helping others","exploring","stability"]
    # value_in_others = ["courage","empathy","creativity","reliability"]
    # problem_solving = ["take action","diplomatically","unique solution","logically"]
    print("Thank you for taking our survey lets see what type of bender you are")
    personality = {
        "passionate": "Fire",
        "adaptable": "Water",
        "peaceful": "Air",
        "stubborn": "Earth"
    }
    conflict = {
        "head-on": "Fire",
        "peacefully": "Water",
        "adapt": "Air",
        "stand-firm": "Earth"
    }
    motivation = {
        "achieving goals": "Fire",
        "helping others": "Water",
        "exploring": "Air",
        "stability": "Earth"
    }
    value_in_others = {
        "courage": "Fire",
        "empathy": "Water",
        "creativity": "Air",
        "reliability": "Earth"
    }
    problem_solving = {
        "take action": "Fire",
        "diplomatically": "Water",
        "unique solution": "Air",
        "logically": "Earth"
    }
    while True: 
        # the below ask for the users inpput and uses strip to get rid of whitespace and makes it lower case because the keys to the dictionaries are also lower case
        personality_input = input(" What best describes your  peronality type? passionate,adaptable,peaceful,stubbborn").strip().lower()

        conflict_input = input("What best describes how you handle conflict? head-on,peacefully,adapt,stand-firm").strip().lower()

        motivation_input = input("What best describes what motivates you? achieving goals, helping others,exploring, stability").strip().lower()

        value_input = input("What best describes the quality you value in others? courage,empathy,creativity,reliability").strip().lower()
    
        problem_input = input(" What best decribes how you solve problems? take action,diplomatically,unique solution,logically").strip().lower()
         
        #  The below code checks if the user input is empty
        if not personality_input or not conflict_input or not motivation_input or not value_input or not problem_input:
            print("Please answer all the questions in the survey.")
            continue
        # The below checks if the user input is equal to the keys in the dictionaries above
        if (personality_input in personality and
            conflict_input in conflict and
            motivation_input in motivation and
            value_input in value_in_others and
            problem_input in problem_solving):
                break
        else:
            print("Invalid Input")
            continue

    bender_scores = {"Fire": 0, "Water": 0, "Air": 0, "Earth": 0}
    
    # Brackets are used to refernce the value of a dictionary 
    if personality[personality_input] == "Fire":
        bender_scores["Fire"] += 1
    elif personality[personality_input] == "Water":
        bender_scores["Water"] += 1
    elif personality[personality_input] == "Air":
        bender_scores["Air"] += 1
    elif personality[personality_input] == "Earth":
        bender_scores["Earth"] += 1

    # We're using brcakets here also to add to the values of the dictionaries
    if conflict[conflict_input] == "Fire":
        bender_scores["Fire"] += 1
    elif conflict[conflict_input] == "Water":
        bender_scores["Water"] += 1
    elif conflict[conflict_input] == "Air":
        bender_scores["Air"] += 1
    elif conflict[conflict_input] == "Earth":
        bender_scores["Earth"] += 1


    # Checks for the value from the dictionary motivation
    if motivation[motivation_input] == "Fire":
        bender_scores["Fire"] += 1
    elif motivation[motivation_input] == "Water":
        bender_scores["Water"] += 1
    elif motivation[motivation_input] == "Air":
        bender_scores["Air"] += 1
    elif motivation[motivation_input] == "Earth":
        bender_scores["Earth"] += 1


    # Checks for the value from the dictionary value_in_others 
    if value_in_others[value_input] == "Fire":
        bender_scores["Fire"] += 1
    elif value_in_others[value_input] == "Water":
            bender_scores["Water"] += 1
    elif value_in_others[value_input] == "Air":
        bender_scores["Air"] += 1
    elif value_in_others[value_input] == "Earth":
        bender_scores["Earth"] += 1

    # max when used with a dictionary is used to find the key with the highest value
    # max iterrates through the dictionary and using key=bender_scores.get to get the values and returns the highest value.
    bender_style = max(bender_scores, key=bender_scores.get)
    
    print("Congrajulations You are a " + bender_style + "Bender" )
