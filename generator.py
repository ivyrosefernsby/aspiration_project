import csv

import asp_functions
import hobby_functions
from hobby_functions import *
from asp_functions import *

zodiac_list = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn',
               'Aquarius', 'Pisces']
interests = {'Politics': 5, 'Food': 5, 'Crime': 5, 'Sports': 5, 'Work': 5, 'School': 5, 'Money': 5, 'Entertainment':
             5, 'Health': 5, 'Paranormal': 5, 'Weather': 5, 'Toys': 5, 'Environment': 5, 'Culture': 5, 'Fashion': 5,
             'Travel': 5, 'Animals': 5, 'Sci Fi': 5}
personality = {'Sloppy': 5, 'Shy': 5, 'Lazy': 5, 'Serious': 5, 'Grouchy': 5}


class Sim:
    def __init__(self, name, zodiac, hobby, aspiration, person, interest):
        self.writer = None
        self.name = name
        self.zodiac = zodiac
        self.hobby = hobby
        self.aspiration = aspiration
        self.personality = person
        self.interests = interest
        self.points = list(person.values())
        self.list = []
    
    def __repr__(self):
        return "{name} is a {zodiac}. A good aspiration for {name} is {asp}, and a good hobby is {hobby}.".format(
            name=self.name, zodiac=self.zodiac, asp=self.aspiration, hobby=self.hobby)
    
    def show_personality(self):
        print(self.personality)
        
    def show_interests(self):
        print(self.interests)
        
    def write_sim(self):
        self.list.append(self.name)
        self.list.append(self.zodiac)
        self.list.append(self.aspiration)
        self.list.append(self.hobby)
        self.list.append(self.points)
        confirm = input("Would you like to save {name}'s data? [y/n] ".format(name=self.name))
        if confirm == 'y':
            with open('sim.csv', 'a', newline='') as file:
                self.writer = csv.writer(file)
                self.writer.writerow(self.list)
            print("{name}'s data has been stored in sim.csv!".format(name=self.name))
        else:
            print("Understood. {name} has not been saved.".format(name=self.name))
        
        
def input_zodiac():
    sim_zodiac = ''
    while sim_zodiac not in zodiac_list:
        zodiac_input = input("What is your Sim's Zodiac sign? ")
        sim_zodiac = zodiac_input.title()
        if sim_zodiac not in zodiac_list:
            print("That's not a Zodiac sign I'm familiar with. Let's try again!")
    print("Your Sim's Zodiac sign has been set to: {sign}.".format(sign=sim_zodiac))
    return sim_zodiac
    
    
def input_personality():
    score = -1
    print("Now I need to know your Sim's personality points. Please enter a number from 0 to 10 for each question.")
    for key in personality:
        while (score < 0) or (score > 10):
            score = int(input("What is your Sim's {key} score? ".format(key=key)))
            if (score < 0) or (score > 10):
                print("That score seems to be out of range, let's ask that one again.")
        personality[key] = score
        score = -1
    print("Thank you! Let's move on.")
    return personality
    

def input_interests():
    score = -1
    print("Last part, I need your Sim's interest points.")
    print("There are 18 total interests, so this may be tedious. Hang in there!")
    for key in interests:
        while (score < 0) or (score > 10):
            score = int(input("What is your Sim's {key} score? ".format(key=key)))
            if (score < 0) or (score > 10):
                print("That score seems to be out of range, let's ask that one again.")
        interests[key] = score
        score = -1
    print("Very good!")
    return interests


def aspiration_chooser(sim_zodiac, sim_personality, sim_interests):
    asp_list = asp_functions.aspirations
    zodiac_to_asp(sim_zodiac)
    personality_to_asp(sim_personality)
    interests_to_asp(sim_interests)
    print("Now calculating your Sim's aspiration... retrieving highest score...")
    asp_score = max(asp_list, key=asp_list.get)
    print("Your Sim's highest scoring aspiration is {asp}!".format(asp=asp_score))
    print(asp_list)
    return asp_score


def hobby_chooser(sim_personality, sim_interests):
    hobby_list = hobby_functions.hobbies
    personality_to_hobby(sim_personality)
    interests_to_hobby(sim_interests)
    print("Now calculating your Sim's one true hobby... retrieving highest score...")
    hobby_score = max(hobby_list, key=hobby_list.get)
    print("Your Sim's highest scoring hobby is {hobby}!".format(hobby=hobby_score))
    print(hobby_list)
    return hobby_score


print("Welcome! Let's figure out who your Sim is going to be. :)")
print("First, I need to know some things about your Sim.")
zodiac_sign = input_zodiac()
p_points = input_personality()
i_points = input_interests()
asp = aspiration_chooser(zodiac_sign, p_points, i_points)
oth = hobby_chooser(p_points, i_points)
sim_name = input("Finally, please name your Sim: ")
new_sim = Sim(sim_name, zodiac_sign, oth, asp, p_points, i_points)
print(new_sim)
new_sim.show_personality()
new_sim.show_interests()
new_sim.write_sim()
input("Press any key to exit: ")
