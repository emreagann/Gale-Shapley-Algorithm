def stable_marriage(men_preferences, women_preferences):

    matches = {}
    unmatched_men = list(men_preferences.keys())
    
    while unmatched_men:
        man = unmatched_men.pop(0)
        preferences = men_preferences[man]
        for woman in preferences:
            if woman not in matches:
                matches[woman] = man
                break
            else:
                current = matches[woman]
                woman_preferences_list = women_preferences[woman]
                if woman_preferences_list.index(man) <= woman_preferences_list.index(current):
                    matches[woman] = man
                    unmatched_men.append(current)
                    break
                
    return matches

men_preferences = {
    'Bob': ['Lea', 'Ann', 'Sue'],
    'Jim': ['Ann', 'Lea', 'Sue'],
    'Tom': ['Sue', 'Lea', 'Ann']
}

women_preferences = {
    'Ann': ['Tom', 'Jim', 'Bob'],
    'Lea': ['Bob', 'Tom', 'Jim'],
    'Sue': ['Jim', 'Bob', 'Tom']
}

matches = stable_marriage(men_preferences, women_preferences)
for woman, man in matches.items():
    print(f"{man} and {woman} are matched")

