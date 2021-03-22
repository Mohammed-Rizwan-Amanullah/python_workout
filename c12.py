favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
}

special_friends = ["sarah", "phil"]

for name in favorite_languages.keys():
    print(f"\nhey {name} welcome")

    if name in special_friends:
        language = favorite_languages[name].title()
        print(f"happy to see you here {name}")
        print(f"you love {language} isn it?")
