# Dictionaries

example = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
print(example["key1"])

release_year_dict = {"Thriller": "1982", "Back in Black": "1980",
                     "The Dark Side of the Moon": "1973", "The Bodyguard": "1992",
                     "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976",
                     "Saturday Night Fever": "1977", "Rumours": "1977"}

print(release_year_dict['Thriller'])

print(release_year_dict.keys())
print(release_year_dict.values())

release_year_dict['Graduation'] = '2007'
del (release_year_dict['Rumours'])
print(release_year_dict)

print("The Bodyguard" in release_year_dict)

# Sets
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set1)  # {'soul', 'hard rock', 'R&B', 'rock', 'disco', 'pop'}

album_list = ["Michael Jackson", "Thriller", 1982, "00:42:19",
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)
print(album_set)

a = {"Thriller", "Back in Black", "AC/DC"}
a.add("NSYNC")
a.remove("Back in Black")
print(a)
print("Thriller" in a)

album_set1 = {"Thriller", 'AC/DC', 'Back in Black'}
album_set2 = {"AC/DC", "Back in Black", "The Dark Side of the Moon"}

intersection = album_set1 & album_set2
print(intersection)
print(album_set1.difference(album_set2))

union = album_set1.union(album_set2)
print(union)

superset = album_set1.issuperset(album_set2)
subset = album_set2.issubset(album_set1)
print(superset)
print(subset)


