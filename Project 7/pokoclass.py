class Pokemon:
    def __init__(self, number, name, type_1, type_2, total, hp, attack, defense, sp_attack, sp_defense, speed, gen, legendary):
        self.number = number
        self.name = name
        self.type_1 = type_1
        self.type_2 = type_2
        self.total = total
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense =sp_defense
        self.speed = speed
        self.gen = gen
        self.legendary = legendary

    
    def __eq__(self, other):
        if self.hp == other.hp:
            return( self.name + ' and ' + other.name + ' have equal hp' )
        else:
            return( self.name + ' and ' + other.name + ' do not have equal hp' )

    def __gt__(self, other):
        if self.hp > other.hp:
            return( self.name + ' has greater hp than ' + other.name )
        else:
            return( self.name + ' does not have greater hp than ' + other.name )

    def __lt__(self, other):
        if self.hp < other.hp:
            return( self.name + ' has lesser hp than ' + other.name )
        else:
            return( self.name + ' does not have lesser hp than ' + other.name )
