# define libraries
zodiac_list = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn',
               'Aquarius', 'Pisces']
interests = {'Politics': 5, 'Food': 5, 'Crime': 5, 'Sports': 5, 'Work': 5, 'School': 5, 'Money': 5, 'Entertainment':
             5, 'Health': 5, 'Paranormal': 5, 'Weather': 5, 'Toys': 5, 'Environment': 5, 'Culture': 5, 'Fashion': 5,
             'Travel': 5, 'Animals': 5, 'Sci Fi': 5}
personality = {'Sloppy': 5, 'Shy': 5, 'Lazy': 5, 'Serious': 5, 'Grouchy': 5}
hobbies = {'Cuisine': 0, 'Film & Literature': 0, 'Games': 0, 'Tinkering': 0, 'Science': 0, 'Arts & Crafts': 0,
           'Sports': 0, 'Nature': 0, 'Fitness': 0, 'Music & Dance': 0}
aspirations = {'Family': 0, 'Fortune': 0, 'Knowledge': 0, 'Pleasure': 0, 'Popularity': 0, 'Romance': 0}


def input_zodiac():
    sim_zodiac = ''
    while sim_zodiac not in zodiac_list:
        zodiac_input = input("What is your Sim's Zodiac sign? ")
        sim_zodiac = zodiac_input.title()
        if sim_zodiac not in zodiac_list:
            print("That's not a Zodiac sign I'm familiar with. Let's try again!")
    print("Your Sim's Zodiac sign as been set to: {sign}.".format(sign=sim_zodiac))
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
    print("Your Sim's personality points have been set to:")
    print(personality)
    return personality
    
    
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


def aspiration_chooser(sim_zodiac, sim_personality):
    zodiac_to_asp(sim_zodiac)
    personality_to_asp(sim_personality)
    print("Now calculating your score... retrieving highest aspiration...")
    asp_score = max(aspirations)
    print("Your Sim's highest scoring aspiration is {asp}!".format(asp=asp_score))
    return asp_score


print("Welcome! Let's figure out who your Sim is going to be. :)")
print("First, I need to know some things about your Sim.")
zodiac_sign = input_zodiac()
p_points = input_personality()
# print(zodiac_sign)
# print(p_points)
aspiration_chooser(zodiac_sign, p_points)
