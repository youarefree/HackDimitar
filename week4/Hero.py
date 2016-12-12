class Hero:

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.name = kwargs['name']
        self.title = kwargs['title']
        self.health = kwargs['health']
        self.mana = kwargs['mana']
        self.mana_regeneration_rate = kwargs['mana_regeneration_rate']
        self.weapon = None
        self.spell = None

    def known_as(self):
        return "{0} the {1}".format(self.name, self.title)

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        return self.get_health() > 0

    def can_cast(self):
        return self.get_mana() > 0

    def take_damage(self, damage_points):
        if damage_points > self.health:
            self.health = 0
        else:
            self.health -= damage_points

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        else:
            self.health += healing_points
            if self.health > self.kwargs['health']:
                self.heath = self.kwargs['health']
            return True

    def take_mana(self, mana_points):
        if map.move_hero():
            self.mana += self.mana_regeneration_rate
        else:
            self.mana += mana_points

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

    def attack(self, by):
        if by == "weapon" and self.weapon is not None:
            return self.weapon.get_damage()
        else:
            return 0
        if by == "magic" and self.spell is not None:
            if self.spell.get_mana_cost() > self.mana:
                print("Insufficient mana")
                return 0
            else:
                self.mana -= self.spell.get_mana_cost()
        else:
            return 0
