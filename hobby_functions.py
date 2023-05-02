hobbies = {'Cuisine': 0, 'Film & Literature': 0, 'Games': 0, 'Tinkering': 0, 'Science': 0, 'Arts & Crafts': 0,
           'Sports': 0, 'Nature': 0, 'Fitness': 0, 'Music & Dance': 0}


# This function calculates OTH based on personality points.
def personality_to_hobby(sim_personality):
    
    # Neat Sims get a small boost to Nature bc Cleaning skill
    # Otherwise Sloppy/Neat doesn't factor in at all
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
        
    # Cuisine hobby is calculated differently
    # For every category in the middle, Sim gets +1 to Cuisine, bc they're giving basic :)
    for key in sim_personality:
        if (sim_personality[key] > 4) and (sim_personality[key] < 7):
            hobbies['Cuisine'] += 1
    
    return hobbies


# This function calculates OTH based on interest points.
# Sims overall get a bigger boost from Interests than Personality
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
