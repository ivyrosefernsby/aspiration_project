# define libraries
zodiac = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn',
          'Aquarius', 'Pisces']
interests = {'Politics': 5, 'Food': 5, 'Crime': 5, 'Sports': 5, 'Work': 5, 'School': 5, 'Money': 5, 'Entertainment':
             5, 'Health': 5, 'Paranormal': 5, 'Weather': 5, 'Toys': 5, 'Environment': 5, 'Culture': 5, 'Fashion': 5,
             'Travel': 5, 'Animals': 5, 'Sci Fi': 5}
personality = {'Sloppy': 5, 'Shy': 5, 'Lazy': 5, 'Serious': 5, 'Grouchy': 5}
hobbies = {'Cuisine': 0, 'Film & Literature': 0, 'Games': 0, 'Tinkering': 0, 'Science': 0, 'Arts & Crafts': 0,
           'Sports': 0, 'Nature': 0, 'Fitness': 0, 'Music & Dance': 0}
aspirations = {'Family': 0, 'Fortune': 0, 'Knowledge': 0, 'Pleasure': 0, 'Popularity': 0, 'Romance': 0}

# define variables needed


# program introduces itself, asks user for input
# define introduction and inputs as function
def input_zodiac():
    sim_zodiac = ''
    while sim_zodiac not in zodiac:
        zodiac_input = input("What is your Sim's Zodiac sign? ")
        sim_zodiac = zodiac_input.title()
        if sim_zodiac not in zodiac:
            print("That's not a Zodiac sign I'm familiar with. Let's try again!")
    return sim_zodiac
    
    
def input_personality():
    score = -1
    for key in personality:
        score = int(input("What is your Sim's {score} score? ".format(score=key)))
        
        
# one zodiac sign (string)
# 5 integers for personality points
# 18 integers for interests (could pare down to 6 integers for 3 high 3 low)

# program compares info with libraries
# program calculates answers based on input

# program outputs answers
# two aspirations (for primary and secondary)
# one hobby

print("Welcome! Let's figure out who your Sim is going to be. :)")
print("First, I need to know some things about your Sim.")
