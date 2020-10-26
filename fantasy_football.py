class Player:
    def __init__(self, first_name, last_name, position, weekly_projection):
        self.first_name = first_name.title()
        self.last_name = last_name.title()

        self.position = position.upper()
        self.weekly_projection = weekly_projection

    # def lineup(self, position, weekly_projection):
    #     i = 0
    #     while i < len()


       

    # def full_name(self):
    #     full = f'{self.first_name} {self.last_name}'
    #     return full

    # def all_players(self, name, position, weekly_projection):
    #     i = 0
    #     while i < len(all_players[position] == 'QB'):
    #         if all_players[position][i] == 'QB' > 15:







# class QB(Player):
#     def __init__(self, first_name, last_name, position, team, weekly_projection, bye_week):
#         super().__init__(first_name, last_name, position, team, starter, weekly_projection, bye_week)  
#     def full_name(self):
#         full = f'{self.first_name} {self.last_name}'
#         return full    

# class RB(Player):
#     def __init__(self, first_name, last_name, position, team, weekly_projection, bye_week):
#         super() .__init__(first_name, last_name, position, team, weekly_projection, bye_week) 

# class WR(Player):
#     def __init__(self, first_name, last_name, position, team, weekly_projection, bye_week):
#         super().__init__(first_name, last_name, position, team, weekly_projection, bye_week) 

# class TE(Player):
#     def __init__(self, first_name, last_name, position, team, weekly_projection, bye_week):
#         super().__init__(first_name, last_name, position, team, weekly_projection, bye_week)
 

# wilson = QB('Russell', 'wilson', 'qb','seattle seahawks', True, 27, 6)
# bridgewater = QB('teddy', 'bridgewater', 'qb', 'carolina panther', True, 16, 13)

# mixon = RB('joe', 'mixon', 'rb', 'cincinatti bengals', True, 22, 9)
# gaskins = RB('myles', 'gaskins', 'rb', 'miami dolphins', True, 0, 7)
# scott = RB('boston', 'scott', 'rb', 'philadelphia eagles', True, 15, 9)
# johnson = RB('d\'ernest', 'johnson', 'rb', 'cleveland browns', True, 5, 9)



# woods = WR('robert', 'woods', 'wr', 'los angeles rams', True, 16, 9)
# golladay = WR('kenny', 'golladay', 'wr', 'detroit lions', True, 20, 5)
# boyd = WR('tyler', 'boyd', 'wr', 'cincinatti bengals', True, 16, 9)
# kirk = WR('christian', 'kirk', 'wr', 'arizona cardinals', True, 13, 8)
# samuel = WR('curtis', 'samuel', 'rb', 'carolina panthers', True, 9, 13)
# pascal = WR('zach', 'pascal', 'wr', 'indianapolis cults', True, 0, 7)
# moore = WR('david', 'moore', 'wr', 'seattle seahawks', True, 6, 6)
# isabella = WR('andy', 'isabella', 'wr', 'arizona cardinals', True, 5, 8)

# engram = TE('evan', 'engram', 'te', 'new york giants', True, 10, 11)
# hockenson = TE('TJ', 'hockenson', 'te', 'detroit lions', True, 11, 5)

quarterbacks = {
    'wilson': Player('Russell', 'wilson', 'qb', 27),
    'bridgewater': Player('teddy', 'bridgewater', 'qb',16)
}

runningbacks = {
    'mixon': Player('joe', 'mixon', 'rb', 22),
    'gaskins': Player('myles', 'gaskins', 'rb', 0),
    'scott': Player('boston', 'scott', 'rb', 15),
    'johnson': Player('d\'ernest', 'johnson', 'rb', 5)
}

widerecievers = {
    'woods': Player('robert', 'woods', 'wr', 16),
    'golladay': Player('kenny', 'golladay', 'wr', 20),
    'boyd': Player('tyler', 'boyd', 'wr', 16),
    'kirk': Player('christian', 'kirk', 'wr', 13),
    'samuel': Player('curtis', 'samuel', 'rb', 9),
    'pascal': Player('zach', 'pascal', 'wr', 0),
    'moore': Player('david', 'moore', 'wr', 6),
    'isabella': Player('andy', 'isabella', 'wr', 5)
}

tightends = {
    'engram': Player('evan', 'engram', 'te', 10),
    'hockenson': Player('TJ', 'hockenson', 'te', 11)
}


# for position, player in quarterbacks.items():
#     fullName = f'{player.first_name} {player.last_name}'
#     projectPoints = player.weekly_projection
#     playerPostion = player.positon.upper()
#     print(fullName)
#     print(projectPoints)
#     print(playerPostion)

weeklyStarts = []

def startLineup(obj):
    for player in obj:
        russ = obj[0]
        # fullName = f'{obj[player].first_name} {obj[player].last_name}'
        # position = obj[player].position
        # projections = obj[player].weekly_projection
        # starter = None
        print(russ)

startLineup(quarterbacks)        





