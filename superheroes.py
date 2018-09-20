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
		defend = random.randint(0, self.defense)
		return defend
		

class Hero:

	def __init__(self, name, health=100):
		self.abilities = list()
		self.name = name

		self.armors = list()
		self.health = health
		self.start_health = health
		self.deaths = 0
		self.killed = 0

	def defend(self):
		total_defense = 0
		for i in self.armors:
			total_defense += i.defend()
		if self.health == 0:
			return 0

	def take_damage(self, damage_amt):
		self.health -= damage_amt
		if self.health == 0:
			self.deaths += 1

	def add_kill(self, num_kills):
		self.killed += num_kills

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
		for i in self.heroes:
			total_attack_strength += i.attack()

		total_kills = other_team.defend(total_attack_strength)

		for hero in self.heroes:
			hero.add_kill(total_kills)

	def defend(self, damage_amt):
		total_defense = 0
		for hero in self.heroes:
			total_defense += hero.defend()
			if damage_amt > total_defense:
				excess_damage = damage_amt - total_defense
				num_kills = self.deal_damage(excess_damage)
		return num_kills


	def deal_damage(self, damage):

		individual_damage = damage // len(self.heroes)
		dead_heroes = 0
		for hero in self.heroes:
			if individual_damage > hero.health:
				dead_heroes += 1
			else:
				hero.health -= individual_damage





	def revive_heroes(self, health=100):
		for hero in self.heroes:
			hero.health = self.health

	def stats(self):
		for hero in self.heroes:
			kills = hero.killed 
			deaths = hero.deaths
			print("ratio of kills to deaths is " + kills + ":" + deaths)

	def update_kills(self):
		for hero in self.heroes:
			hero.killed += 1














if __name__ == "__main__":
	hero = Hero("wonder woman")
	print(hero.attack())
	ability = Ability("Divine Speed", 6)
	hero.add_ability(ability)
	print(hero.attack())


	new_ability = Ability("super human strength", 5)
	hero.add_ability(new_ability)
	print(hero.attack())



