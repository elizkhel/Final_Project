import random

class Character: # character class agweriloba (features)
    def __init__(self, name, health, attack_power, special_ability):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.special_ability = special_ability
        self.special_ability_used = False
        self.attack_history = []

    def is_alive(self):  # mogebulis gansasazgvrad tu health < 0 waago
        return self.health > 0

    def take_damage(self, damage):  # ramdenit shemouties da ramdeni darcha sicocxle
        self.health -= damage
        self.attack_history.append(f"{self.name} took {damage} damage (Health: {self.health})") # sheinaxos dictionaryshi 
        print(f"{self.name} takes {damage} damage and has {self.health} health left.")

    def attack(self, other): #ramdenit sheutia da ramdeni darcha sicocxle
        damage = random.randint(1, self.attack_power)
        if random.random() < 0.2: # 20% shansit did damage miayenebs
            damage *= 2
            print("Critical hit!")
        
        self.attack_history.append(f"{self.name} attacked {other.name} for {damage} damage")
        print(f"{self.name} attacks {other.name} for {damage} damage.")
        other.take_damage(damage)

# mxolod 1 gamoiyenos special_ability
    def use_special_ability(self, other):
        if self.special_ability_used:
            print(f"{self.name} has already used their special ability!")
            return
        if self.special_ability == "heal":
            heal_amount = random.randint(10, 30)
            self.health += heal_amount
            self.attack_history.append(f"{self.name} used special ability and healed for {heal_amount} (Health: {self.health})")
            print(f"{self.name} heals for {heal_amount} health points.")
        elif self.special_ability == "double_damage":
            damage = random.randint(1, self.attack_power) * 2
            self.attack_history.append(f"{self.name} used special ability and dealt {damage} damage to {other.name}")
            print(f"{self.name} uses special ability to deal {damage} damage to {other.name}.")
            other.take_damage(damage)
        self.special_ability_used = True  # gamoiyena special_ability

# aq inheritance gamoviyeneb oop principe-dan

class Jinx(Character):
    def __init__(self):
        super().__init__("Jinx", 100, 15, "double_damage")

class Kayn(Character):
    def __init__(self):
        super().__init__("Kayn", 30, 5, "heal")

class Akali(Character):
    def __init__(self):
        super().__init__("Akali", 50, 10, "double_damage")

class MissFortune(Character):
    def __init__(self):
        super().__init__("Miss Fortune", 100, 20, "heal")


class Aatrox(Character):
    def __init__(self):
        super().__init__("Aatrox", 80, 12, "heal")


class Zeri(Character):
    def __init__(self):
        super().__init__("Zeri", 60, 18, "double_damage")


# saxelis archevisas gamovidzaxeb shesabamis class-is characters
class CharacterPicker:
    def __init__(self):
        self.char_map = {
            "Jinx": Jinx,
            "Kayn": Kayn,
            "Akali": Akali,
            "Miss Fortune": MissFortune,
            "Aatrox": Aatrox,
            "Zeri": Zeri,
        }
    
    def get_character(self, character_name: str):
        return self.char_map[character_name]()


