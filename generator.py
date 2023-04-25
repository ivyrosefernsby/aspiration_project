import csv

zodiac_list = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn',
               'Aquarius', 'Pisces']
interests = {'Politics': 5, 'Food': 5, 'Crime': 5, 'Sports': 5, 'Work': 5, 'School': 5, 'Money': 5, 'Entertainment':
             5, 'Health': 5, 'Paranormal': 5, 'Weather': 5, 'Toys': 5, 'Environment': 5, 'Culture': 5, 'Fashion': 5,
             'Travel': 5, 'Animals': 5, 'Sci Fi': 5}
personality = {'Sloppy': 5, 'Shy': 5, 'Lazy': 5, 'Serious': 5, 'Grouchy': 5}
hobbies = {'Cuisine': 0, 'Film & Literature': 0, 'Games': 0, 'Tinkering': 0, 'Science': 0, 'Arts & Crafts': 0,
           'Sports': 0, 'Nature': 0, 'Fitness': 0, 'Music & Dance': 0}
aspirations = {'Family': 0, 'Fortune': 0, 'Knowledge': 0, 'Pleasure': 0, 'Popularity': 0, 'Romance': 0}


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
        self.header = ['name', 'zodiac', 'aspiration', 'hobby', 'personality']
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
            with open('sim.csv', 'w', newline='') as file:
                self.writer = csv.writer(file)
                self.writer.writerow(self.header)
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
    print("Now I need to know your Sim's personality points. Please enter a number between 1 and 10 for each question.")
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


def zodiac_to_asp(sim_zodiac):
    if sim_zodiac == 'Aries' or 'Taurus' or 'Cancer' or 'Sagittarius' or 'Aquarius' or 'Pisces':
        aspirations['Family'] += 1
    if sim_zodiac == 'Taurus' or 'Gemini' or 'Leo' or 'Scorpio' or 'Sagittarius' or 'Capricorn':
        aspirations['Fortune'] += 1
    if sim_zodiac == 'Cancer' or 'Virgo' or 'Scorpio' or 'Capricorn' or 'Aquarius' or 'Pisces':
        aspirations['Knowledge'] += 1
    if sim_zodiac == 'Taurus' or 'Gemini' or 'Virgo' or 'Libra' or 'Capricorn' or 'Aquarius':
        aspirations['Pleasure'] += 1
    if sim_zodiac == 'Aries' or 'Gemini' or 'Leo' or 'Libra' or 'Sagittarius' or 'Pisces':
        aspirations['Popularity'] += 1
    if sim_zodiac == 'Aries' or 'Cancer' or 'Leo' or 'Virgo' or 'Libra' or 'Scorpio':
        aspirations['Romance'] += 1
    return aspirations


def personality_to_asp(sim_personality):
    if sim_personality['Sloppy'] < 5:
        aspirations['Pleasure'] += 1
        aspirations['Romance'] += 1
    if sim_personality['Sloppy'] > 6:
        aspirations['Knowledge'] += 1
        aspirations['Fortune'] += 1
    if sim_personality['Shy'] < 5:
        aspirations['Knowledge'] += 1
        aspirations['Family'] += 1
    if sim_personality['Shy'] > 6:
        aspirations['Popularity'] += 1
        aspirations['Fortune'] += 1
    if sim_personality['Lazy'] < 5:
        aspirations['Pleasure'] += 1
        aspirations['Family'] += 1
    if sim_personality['Lazy'] > 6:
        aspirations['Romance'] += 1
        aspirations['Popularity'] += 1
    if sim_personality['Serious'] < 5:
        aspirations['Fortune'] += 1
        aspirations['Knowledge'] += 1
    if sim_personality['Serious'] > 6:
        aspirations['Pleasure'] += 1
        aspirations['Family'] += 1
    if sim_personality['Grouchy'] < 5:
        aspirations['Romance'] += 1
        aspirations['Knowledge'] += 1
    if sim_personality['Grouchy'] > 6:
        aspirations['Family'] += 1
        aspirations['Popularity'] += 1
    return aspirations


def interests_to_asp(sim_interests):
    if sim_interests['Politics'] > 6:
        aspirations['Fortune'] += 1
        aspirations['Popularity'] += 1
    if sim_interests['Food'] > 6:
        aspirations['Family'] += 1
        aspirations['Pleasure'] += 1
    if sim_interests['Crime'] > 6:
        aspirations['Knowledge'] += 1
        aspirations['Fortune'] += 1
    if sim_interests['Sports'] < 4:
        aspirations['Knowledge'] += 1
    if sim_interests['Work'] > 6:
        aspirations['Fortune'] += 1
        aspirations['Knowledge'] += 1
    if sim_interests['School'] > 6:
        aspirations['Family'] += 2
        aspirations['Knowledge'] += 1
    if sim_interests['Money'] > 6:
        aspirations['Fortune'] += 2
        aspirations['Romance'] += 1
    if sim_interests['Entertainment'] > 6:
        aspirations['Pleasure'] += 2
    if sim_interests['Health'] > 6:
        aspirations['Romance'] += 2
        aspirations['Popularity'] += 1
    if sim_interests['Paranormal'] > 6:
        aspirations['Knowledge'] += 1
    if sim_interests['Weather'] < 5:
        aspirations['Pleasure'] += 1
        aspirations['Popularity'] += 1
        aspirations['Romance'] += 1
    if sim_interests['Toys'] > 6:
        aspirations['Family'] += 1
        aspirations['Knowledge'] += 1
    if sim_interests['Environment'] > 6:
        aspirations['Family'] += 1
    if sim_interests['Culture'] > 6:
        aspirations['Fortune'] += 1
        aspirations['Romance'] += 1
    if sim_interests['Fashion'] > 6:
        aspirations['Popularity'] += 1
        aspirations['Fortune'] += 1
    if sim_interests['Travel'] > 6:
        aspirations['Pleasure'] += 1
        aspirations['Popularity'] += 2
        aspirations['Romance'] += 1
    if sim_interests['Animals'] > 6:
        aspirations['Family'] += 1
        aspirations['Pleasure'] += 1
    if sim_interests['Sci Fi'] > 6:
        aspirations['Knowledge'] += 1
    return aspirations


def personality_to_hobby(sim_personality):
    if sim_personality['Sloppy'] > 6:
        hobbies['Nature'] += 2
    if sim_personality['Shy'] < 5:
        hobbies['Tinkering'] += 1
        hobbies['Arts & Crafts'] += 3
    if sim_personality['Shy'] > 6:
        hobbies['Sports'] += 1
    if sim_personality['Lazy'] < 5:
        hobbies['Film & Literature'] += 2
    if sim_personality['Lazy'] > 6:
        hobbies['Sports'] += 2
        hobbies['Fitness'] += 2
        hobbies['Music & Dance'] += 1
    if sim_personality['Serious'] < 5:
        hobbies['Tinkering'] += 2
        hobbies['Science'] += 3
        hobbies['Fitness'] += 1
    if sim_personality['Serious'] > 6:
        hobbies['Film & Literature'] += 1
        hobbies['Games'] += 3
        hobbies['Music & Dance'] += 2
    for key in sim_personality:
        if (sim_personality[key] > 4) and (sim_personality[key] < 7):
            hobbies['Cuisine'] += 1
    return hobbies


def interests_to_hobby(sim_interests):
    if sim_interests['Food'] > 6:
        hobbies['Cuisine'] += 2
    if sim_interests['Entertainment'] > 6:
        hobbies['Film & Literature'] += 2
        hobbies['Games'] += 2
        hobbies['Music & Dance'] += 2
    if sim_interests['Culture'] > 6:
        hobbies['Film & Literature'] += 2
        hobbies['Arts & Crafts'] += 2
        hobbies['Music & Dance'] += 2
    if sim_interests['School'] > 6:
        hobbies['Science'] += 2
    if sim_interests['Toys'] > 6:
        hobbies['Games'] += 2
        hobbies['Tinkering'] += 4
    if sim_interests['Sci Fi'] > 6:
        hobbies['Science'] += 2
    if sim_interests['Fashion'] > 6:
        hobbies['Arts & Crafts'] += 2
    if sim_interests['Sports'] > 6:
        hobbies['Sports'] += 4
    if sim_interests['Health'] > 6:
        hobbies['Fitness'] += 4
    if sim_interests['Environment'] > 6:
        hobbies['Nature'] += 2
    if sim_interests['Animals'] > 6:
        hobbies['Nature'] += 2
    if sim_interests['Weather'] > 6:
        hobbies['Nature'] += 1
    return hobbies


def aspiration_chooser(sim_zodiac, sim_personality, sim_interests):
    zodiac_to_asp(sim_zodiac)
    personality_to_asp(sim_personality)
    interests_to_asp(sim_interests)
    print("Now calculating your Sim's aspiration... retrieving highest score...")
    asp_score = max(aspirations, key=aspirations.get)
    print("Your Sim's highest scoring aspiration is {asp}!".format(asp=asp_score))
    print(aspirations)
    return asp_score


def hobby_chooser(sim_personality, sim_interests):
    personality_to_hobby(sim_personality)
    interests_to_hobby(sim_interests)
    print("Now calculating your Sim's one true hobby... retrieving highest score...")
    hobby_score = max(hobbies, key=hobbies.get)
    print("Your Sim's highest scoring hobby is {hobby}!".format(hobby=hobby_score))
    print(hobbies)
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
