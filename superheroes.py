import random

class Ability:

	def __init__(self, name, attack_strength):
		self.name = name
		self.attack_strength = attack_strength

	def attack(self):
		lowest_attack_value = int(self.attack_strength) // 2
		attack_value = random.randint(lowest_attack_value, int(self.attack_strength))
		return attack_value


	def update_attack(self, attack_strength):
		self.attack_strength = attack_strength


class Weapon(Ability):
	def attack(self):
		return random.randint(0, self.attack_strength)


class Armor:

	def __init__(self, name, defense):
		self.name = name
		self.defense = defense

	def defend(self):
		random_defend_value = random.randint(0, int(self.defense))
		return random_defend_value
		

class Hero:

	def __init__(self, name, health=100):
		self.abilities = list()
		self.name = name
		self.armors = list()
		self.start_health = health
		self.health = health
		self.deaths = 0
		self.kills = 0

	def __str__(self):
		return self.name

	def defend(self):

		defenses = 0
		if len(self.armors) == 0:
			return 0

		for armor in self.armors:
			defenses += armor.defend()

		if self.health == 0:
			defenses = 0
			return defenses
		else:
			return defenses


	def add_armor(self, name):
		self.armors.append(name)

	def take_damage(self, damage_amt):
		self.health = self.health - damage_amt

		if self.health <= 0:
			self.deaths += 1
		else:
			return 0

	def add_kill(self, num_kills):
		self.kills += num_kills

	def add_ability(self, ability):
		self.abilities.append(ability)

	def attack(self):
		total = 0
		for x in self.abilities:
			total += x.attack()
		return total


class Team():

	def __init__(self, team_name):
		self.team_name = team_name
		self.heroes = list()

	def add_hero(self, Hero):
		self.heroes.append(Hero)

	def remove_hero(self, name):
		print("removeeeeed")
		if len(self.heroes) == 0:
			return 0

		for hero in self.heroes:
			if hero.name == name:
				self.heroes.remove(hero)
				return True
			else:
				return 0



	def find_hero(self, name):
		if len(self.heroes) == 0:
			return 0
		for i in self.heroes:
			if i.name == name:
				return hero
		return 0

	def view_all_heroes(self):

		viewed_heroes = []
		if len(self.heroes) == 0:
			print("No heroes in this team!")
		for hero in self.heroes:
			viewed_heroes.append(hero.name)
		print(viewed_heroes)



	def attack(self, other_team):
		tot_attack_strength = 0
		for hero in self.heroes:
			tot_attack_strength += hero.attack()
		killed_heroes = other_team.defend(tot_attack_strength)

		for hero in self.heroes:
			hero.add_kill(killed_heroes)

	def defend(self, total_attack_strength):
		tot_defence = 0
		for hero in self.heroes:
			tot_defence += hero.defend()
		excess_damage = total_attack_strength - tot_defence
		if excess_damage > 0:
			return self.deal_damage(excess_damage)
		else:
			return 0


	def deal_damage(self, damage):

		if len(self.heroes) != 0:
			damage_per_hero = damage // len(self.heroes)
		else:
			return 0
		count = 0
		for hero in self.heroes:
			if hero.health > damage_per_hero:
				hero.take_damage(damage_per_hero)
			else:
				hero.take_damage(damage_per_hero)
				count += 1
		return count





	def revive_heroes(self, health=100):
		for hero in self.heroes:
			hero.health = 100


	def stats(self):
		for hero in self.heroes:
			print("{}'s ratio of kills to deaths is {}:{}".format(hero.name, hero.kills, hero.deaths))

	def update_kills(self):
		for hero in self.heroes:
			hero.kills += 1


class Arena:

	def __init__(self):
		self.team_one = None
		self.team_two = None

	def build_team_one(self):
		self.team_one = Team(input("Input team one name: "))
		print("Go {}!!!".format(self.team_one.team_name))
		print("\n")
		hero1 = Hero(input("input a hero's name: "))
		self.team_one.add_hero(hero1)
		print("You have added {} to {}".format(hero1.name, self.team_one.team_name))
		
		print("\n")
		ability1 = Ability(input("input name of ability: "), input("input ability's attack strength: "))
		hero1.add_ability(ability1)
		print("You have added the ability {} to {}".format(ability1.name, hero1.name))
		
		print("\n\n")
		hero2 = Hero(input("input a second hero's name: "))
		self.team_one.add_hero(hero2)
		print("You have added {} to {}".format(hero2.name, self.team_one.team_name))

		print("\n")
		ability2 = Ability(input("input name of ability: "), input("input ability's attack strength: "))
		hero2.add_ability(ability2)
		print("You have added the ability {} to {}".format(ability2.name, hero2.name))


	def build_team_two(self):
		self.team_two = Team(input("Input team two name: "))
		print("Go {}!!!".format(self.team_two.team_name))
        # add the hero
		print("\n")
		hero1 = Hero(input("input a hero's name: "))
		self.team_two.add_hero(hero1)
		print("You have added {} to {}".format(hero1.name, self.team_two.team_name))
        # add the ability
		print("\n")
		ability1 = Ability(input("input name of ability: "), input("input ability's attack strength: "))
		hero1.add_ability(ability1)
		print("You have added the ability {} to {}".format(ability1.name, hero1.name))
        # add armor
		print("\n")
		armor = Armor(input("input name of armor: "), input("input armors attack strenght: "))
		hero1.add_armor(armor)
		print("You have added {} to {}".format(armor.name, hero1.name))

        # add hero 2
		print("\n\n")
		hero2 = Hero(input("input a second hero's name: "))
		self.team_two.add_hero(hero2)
		print("You have added {} to {}".format(hero2.name, self.team_two.team_name))
        # add ability to hero 2
		print("\n")
		ability2 = Ability(input("input name of ability: "), input("input ability's attack strength: "))
		hero2.add_ability(ability2)
		print("You have added the ability {} to {}".format(ability2.name, hero2.name))
        # add armor to hero 2
		print("\n")
		armor2 = Armor(input("input name of armor: "), input("input armors attack strenght: "))
		hero2.add_armor(armor2)
		print("You have added {} to {}".format(armor2.name, hero2.name))

	def team_battle(self):
		running = True
		while running:
			deaths_team_one = 0
			for hero in self.team_one.heroes:
				if hero.health <= 0:
					deaths_team_one += 1
			self.team_one.attack(self.team_two)
			if deaths_team_one == len(self.team_one.heroes):
				running = False

			deaths_team_two = 0
			for hero in self.team_two.heroes:
				if hero.health <= 0:
					deaths_team_two += 1
			self.team_two.attack(self.team_one)
			if deaths_team_two == len(self.team_two.heroes):
				running = False

	def show_stats(self):
		print("\n")
		print("Team 1 stats:")
		self.team_one.stats()

		print("\n")
		print("Team 2 stats:")
		self.team_two.stats()




if __name__ == "__main__":
	# hero = Hero("wonder woman")
	# print(hero.attack())
	# ability = Ability("Divine Speed", 6)
	# hero.add_ability(ability)
	# print(hero.attack())


	# new_ability = Ability("super human strength", 5)
	# hero.add_ability(new_ability)
	# print(hero.attack())

	game_is_running = True

	arena = Arena()

	arena.build_team_one()
	arena.build_team_two()

	while game_is_running:
		arena.team_battle()
		arena.show_stats()
		play_again = input("Play again? Y or N: ")

		if play_again.lower() == "n":
			game_is_running = False

		else:
			# revive heroes to play again
			arena.team_one.revive_heroes()
			arena.team_two.revive_heroes()






