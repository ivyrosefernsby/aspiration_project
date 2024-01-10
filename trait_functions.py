traits = {'Absent-Minded': 0, 'Adventurous': 0, 'Ambitious': 0, 'Angler': 0, 'Animal Lover': 0, 'Artistic': 0,
          'Athletic': 0, 'Avant Garde': 0, 'Bookworm': 0, 'Born Salesperson': 0, 'Bot Fan': 0, 'Brave': 0,
          'Brooding': 0, "Can't Stand Art": 0, 'Cat Person': 0, 'Charismatic': 0, 'Childish': 0, 'Clumsy': 0,
          'Commitment Issues': 0, 'Computer Whiz': 0, 'Couch Potato': 0, 'Coward': 0, 'Daredevil': 0, "Disciplined":
              0, 'Dislikes Children': 0, 'Diva': 0, 'Dog Person': 0, 'Dramatic': 0, 'Easily Impressed': 0,
          'Eccentric': 0, 'Eco-Friendly': 0, "Equestrian": 0, 'Evil': 0, 'Excitable': 0, 'Family-Oriented': 0,
          'Flirty': 0, 'Friendly': 0, 'Frugal': 0, 'Gatherer': 0, 'Genius': 0, 'Good': 0, 'Good Sense of Humor': 0,
          'Great Kisser': 0, 'Green Thumb': 0, 'Grumpy': 0, 'Handy': 0, 'Hates the Outdoors': 0, 'Heavy Sleeper': 0,
          'Hopeless Romantic': 0, 'Hot-Headed': 0, 'Hydrophobic': 0, 'Insane': 0, 'Irresistible': 0, 'Kleptomaniac': 0,
          'Light Sleeper': 0, 'Loner': 0, 'Loser': 0, 'Loves the Cold': 0, 'Loves the Heat': 0, 'Loves the Outdoors':
              0, 'Loves to Swim': 0, 'Lucky': 0, 'Mean-Spirited': 0, 'Mooch': 0, 'Natural Born Performer': 0,
          'Natural Cook': 0, 'Neat': 0, 'Neurotic': 0, 'Never Nude': 0, 'Night Owl': 0, 'No Sense of Humor': 0,
          'Nurturing': 0, 'Over-Emotional': 0, 'Party Animal': 0, 'Perceptive': 0, 'Perfectionist': 0,
          "Photographer's Eye": 0, 'Proper': 0, 'Rebellious': 0, 'Sailor': 0, 'Savvy Sculptor': 0, 'Schmoozer': 0,
          'Shy': 0, 'Slob': 0, 'Snob': 0, 'Social Butterfly': 0, 'Socially Awkward': 0, 'Star Quality': 0,
          'Supernatural Fan': 0, 'Supernatural Skeptic': 0, 'Technophobe': 0, 'Unflirty': 0, 'Unlucky': 0,
          'Unstable': 0, 'Vegetarian': 0, 'Vehicle Enthusiast': 0, 'Virtuoso': 0, 'Workaholic': 0}

def personality_to_traits(sim_personality):
    
    if sim_personality['Sloppy'] < 4:
        traits['Slob'] += 1
    if sim_personality['Sloppy'] > 7:
        traits['Neat'] += 1
        
    if sim_personality['Shy'] < 4:
        traits['Shy'] += 1
    if sim_personality['Shy'] > 7:
        traits['Social Butterfly'] += 1
        
    if sim_personality['Lazy'] < 4:
        traits['Couch Potato'] += 1
    if sim_personality['Lazy'] > 7:
        traits['Athletic'] += 1
        
    if sim_personality['Serious'] < 4:
        traits['No Sense of Humor'] += 1
    if sim_personality['Serious'] > 7:
        traits['Good Sense of Humor'] += 1
        
    if sim_personality['Grouchy'] < 4:
        traits['Grumpy'] += 1
    if sim_personality['Grouchy'] > 7:
        traits['Friendly'] += 1
        
    if sim_personality['Grouchy'] > 6 and sim_personality['Shy'] > 4:
        traits['Charismatic'] += 1
        
    if sim_personality['Grouchy'] < 4 and sim_personality['Serious'] < 4:
        traits['Dislikes Children'] += 1
    
    return traits
        
def interests_to_traits(sim_interests):
    if sim_interests['Work'] > 7:
        traits['Workaholic'] += 1
    
    if sim_interests['Politics'] > 7:
        traits['Schmoozer'] += 1
        
    if sim_interests['Toys'] > 6 and sim_interests['School'] > 6:
        traits['Childish'] += 1
        
def personality_interests_to_traits(sim_personality, sim_interests):
    if sim_personality['Grouchy'] < 4 and sim_personality['Serious'] < 4 and sim_interests['Toys'] < 5:
        traits['Dislikes Children'] += 3