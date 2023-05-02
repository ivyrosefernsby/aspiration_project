aspirations = {'Family': 0, 'Fortune': 0, 'Knowledge': 0, 'Pleasure': 0, 'Popularity': 0, 'Romance': 0}


# This function checks a Sim's Zodiac and gives +1 to the corresponding aspirations
# Based on Maxis code, PleasantSims variation and my own taste
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


# This function calculates aspiration based on personality points
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
        
    if sim_personality['Lazy'] > 6:
        aspirations['Romance'] += 1
        aspirations['Popularity'] += 1
        
    if sim_personality['Serious'] < 5:
        aspirations['Fortune'] += 1
        
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


# This function calculates aspiration based on interest points
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
