import csv

# shua tamashi tu moindoma istoriis naxva motamashem 
def display_attack_history(characters):
    print("\nAttack History:")
    for character in characters:
        for entry in character.attack_history:
            print(entry)


# tamashis istoriis shenaxvis punqcia csv-shi
def save_attack_history(characters, file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Character", "Action"])
        for character in characters:
            for entry in character.attack_history:
                writer.writerow([entry])
