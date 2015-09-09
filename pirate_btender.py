import random #just giving us access to the random libarary for the random. choice function

""" lines 4 and 12 and 19 and 20 are all dictionaries- they use curly braces {}. 
a dictionary is a collection of name:value pairs. line 20 is our empty glass
the dictionary has what are commonly called "keys". in this example the keys are the "salty, fruity, etc."""


questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"], 
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

answers = {} #variable that calls  
my_Drink = [] #these are calling back to the list in the ingredient dictionary. square brackets are lists. they are mutable (changeable)

def ask_questions(): # a function that asks all our questions from "questions" dictionary. also stores our answers from our answers dictionary
    for key in questions: #for loop. this loops through all the questions in the the questions dictionary.
        print questions[key]
        answers[key] = raw_input(">") #built in function. a way to read something in from the user 
        #and spit it back out. think turning the key in your car. you don't know what happens under the hood but the car still runs

def mixed_drink(): # a function that actually fills our drink based on answers
    for key in answers: #for loop
        if answers[key] == "y":
            my_Drink.append(random.choice(ingredients[key])) #append is another built in function-just adds something to a list
  

if __name__ == '__main__': #this is our main fuction. where all programs begin and end- start using these moving forward
    ask_questions()
    mixed_drink()
    print my_Drink
