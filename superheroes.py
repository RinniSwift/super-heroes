import random

class Ability:

	def __init__(self, name, attack_strength):
		self.name = name
		self.attack_strength = attack_strength

	def attack(self):
		lowest_attack = self.attack_strength // 2
		attack = random.randint(lowest_attack, self.attack_strength)
		return attack



	def update_attack(self, attack_strength):
		self.attack_strength = attack_strength


class Weapon(Ability):
	def attack(self):
		attac = random.randint(0, self.attack_strength)
		return attac


class Armor:

	def __init__(self, name, defense):
		self.name = name
		self.defense = defense

	def defend(self):
		random_value = random.randint(0, self.defense)
		return random_value
		

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
		total_defense = 0

		if len(self.armors) == 0:
			return 0

		for i in self.armors:
			total_defense += i.defend()

		if self.health == 0:
			total_defense = 0
			return total_defense
		else:
			return total_defense

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


		

	def __str__(self):
		return self.name

	def add_ability(self, ability):
		self.abilities.append(ability)

	def attack(self):
		total_attacks = 0
		for i in self.abilities:
			total_attacks += i.attack()
		return total_attacks


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

		for i in self.heroes:
			print(i.name)
			if i.name == name:
				self.heroes.remove(i)
			else:
				return 0

	def find_hero(self, name):
		if len(self.heroes) == 0:
			return 0

		for i in self.heroes:
			if i.name == name:
				return i
			else:
				return 0

	def view_all_heroes(self):
		for hero in self.heroes:
			print(hero)


	def attack(self, other_team):
		total_attack_strength = 0
		for hero in self.heroes:
			total_attack_strength += hero.attack()
			killed_heroes = other_team.defend(total_attack_strength)



		for hero in self.heroes:
			hero.add_kill(killed_heroes)

	def defend(self, damage_amt):
		total_defense = 0
		for hero in self.heroes:
			total_defense += hero.defend()

		if damage_amt > total_defense:
			excess_damage = damage_amt - total_defense
			num_kills = self.deal_damage(excess_damage)
		return num_kills


	def deal_damage(self, damage):

		if len(self.heroes) != 0:
			individual_damage = damage // len(self.heroes)
		else:
			return 0

		dead_heroes = 0
		for hero in self.heroes:
			if hero.health > individual_damage:
				hero.take_damage(individual_damage)
			else:
				hero.take_damage(individual_damage)
				dead_heroes += 1
		return dead_heroes





	def revive_heroes(self, health=100):
		for hero in self.heroes:
			hero.health = hero.start_health


	def stats(self):
		# for hero in self.heroes:
		# 	kills = hero.killed 
		# 	deaths = hero.deaths
		# 	print("ratio of kills to deaths is {}:{}".format(kills, deaths))

		print("ratio of kills to deaths is {}:{}".format(self.kills, self.deaths))

	def update_kills(self):
		for hero in self.heroes:
			hero.kills += 1


class Arena:

	def __init__(self):
		self.team_one = None
		self.team_two = None

	def build_team_one(self):
		self.team_one = Team(input("Input team one name: "))


	def build_team_two(self):
		self.team_two = Team(input("Input team two name: "))

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
		for hero in self.team_one:
			print("{} kill to death ratio is {}:{}".format(self.name, self.kills, self.deaths))

		for hero in self.team_two:
			print("{} kill to death ratio is {}:{}".format(self.name, self.kills, self.deaths))





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






