                                   
class Char:
    def __init__(self, name, weapon, health, power):
        self.name = name
        self.weapon = weapon
        self.health = health
        self.power = power

    def description(self):
        print(f"\nYou've chosen {self.name} with {self.weapon} as his weapon.")

    def attacked(self, num):
        self.health = self.health - num
        print(f'\nI {self.name}, got hit for {num} points and now have {self.health}. But I\'ve won the battle. Onward!')

    def attack(self, enemy):
        enemy.attacked(self.power)            


class GoodGuy(Char):
    def __init__(self, name, weapon, health=10, power=3):
        super().__init__(name, weapon, health=15, power=7)
    def battle_cry(self):
        print('Waaaaaar!')    

class BadBoy(Char):
    def __init__(self, name, weapon, health= 15, power=7):
        super().__init__(name, weapon, health, power)

class Guards(Char):  
    def __init__(self, name, weapon, health= 15, power=10):
        super().__init__(name, weapon, health, power)
    def guard_id(self):
        print('ID please.')
    def guard_attack(self, enemy):
        enemy.attacked(self.power)





hero = GoodGuy('Mr. Nice Guy', 'Sword of Destiny')
the_villian =  BadBoy('Mr. Trouble', 'Fist of Fury')  
large_guards = Guards('Big Boys', 'These hands' )   



def good_guy_story_4():
    print('****************************************')
    while True:
        message = f"\nAs you Naruto run towards the 2 large guards with your {hero.weapon}, "
        message +=f"\n1 of the guards says, 'Whoa, whoa, whoa, you can't bring that into the party. Sorry.'"
        message +=f'\nThe other prompts: '
        print(message)

        large_guards.guard_id()
        print('****************************************')

        prompt = f'\nThis is odd. A party? You ask the guard. Is it possible you\'ve been bamboozled by the Princess? '
        prompt += f'\nDo you investigate further? '
        choice_4 = input(prompt).title()

        if choice_4 == 'Yes':
            story = f"\n\nYou hand over the {hero.weapon} to the guards and proceed through the double doors."
            story += f'\n\nYou wander the room looking for the Princess. There\'s no sign of evil doing, just good vibes. '
            story +=f"\n\nThe feeling of being bamboozled grows stronger and hits a fever pitch when you hear The Princess' giggle from a dark corner. "
            story += f"\n\nYou look over to see The Princess getting cozy with Luigi and they're enjoying a few laughs with Kirby and Mario"
            story += f"\n\nYou've been fooled by the Princess and proceed cause a scene. {the_villian.name} ask you to leave, but you refuse."
            story += f"\n\nThe 2 large guards enter the room and proceed to beat you up and kick you out. The End."

            print(story)
            print('****************************************')
            break
        else:
            print("No judgements here, something's not right about this situation.")    
            break

def good_guy_story_3():
    print('****************************************')
    while True:
        prompt = f'\n\nYou\'ve made it upstairs. The commotion is getting louder, the walls are shaking and you\'re starting to hear house music.'   
        prompt += f'\n\nYou\'re getting suspcious now. You\'ve fought a Tiger and have {hero.health} health left over but, '  
        prompt += f'\n\nin the distance you see flashing lights flickering in the small opening of large wooden double doors, guarded 2 very large men.'  
        prompt += f'\n\nDo you confront the men? Yes or No.'

        choice_3 = input(prompt).title()
        print('\n****************************************')
        if choice_3 == 'Yes':
            print(f"You let out a battle cry and pull your {hero.weapon}.")
            hero.battle_cry()
            print('\n****************************************')
            good_guy_story_4()

        elif choice_3 == 'No':
            print('No judgments here, trust your gut.')
            break
        elif choice_3 == 'Quit':
            break
        else:
            print('Answer Yes or No')         


def good_guy_story_2():
    print('\n****************************************')
    while True:

        prompt = f"\nYou have illegally broken into the {the_villian.name}'s castle."
        prompt += '\nUpon illegal entry you hear commotion coming from levels above but there\'s a Tiger blocking the door way.'
        prompt += f"\nYou're equipped with {hero.weapon}, do you take on the Tiger to proceed upstairs: Yes or No? "
        choice_2 = input(prompt).title()
        print('\n****************************************')

        if choice_2 == 'Yes':
            print('\nYou really want to fight a Tiger?!')
            hero.attacked(4)
            print('\n****************************************')
            good_guy_story_3()

        elif choice_2 == 'No':
            print('No judgements here, I wouldn\'t fight a Tiger either.')
            break    
        elif choice_2 == 'Quit':
            break
        else:
            print('Please answer Yes or No. ')                  


def good_guy_story():
    while True:
        print(f"\n*** You've recieved a text saying that {the_villian.name} has kidnapped The Princess and you must save her. ***")
        hero_prompt = f"\nYou've tracked down the {the_villian.name} and the princess."
        hero_prompt += f"\n{the_villian.name} has the princess locked in the dungeon in his castle. Is she worth the trouble: Yes or No? "
        
        choice_1 = input(hero_prompt).title()
        
        if choice_1 == 'Yes':
            print('\nOnward!')
            good_guy_story_2()
        elif choice_1 == 'No':
            print('No judgements here.')
            break
        elif choice_1 == 'Quit':
            break
        else:
            print('Answer either Yes or No!')

def bad_guy_story_3():
    while True:
        prompt = """As you're pondering whether to investigate you hear a loud roar then whimpering. Obviously, the tiger has been injured.
        this must be the doing of only 1 person, {hero.name}! You start to make your way to the guards, but it's already too late, he's
        already infiltrated your party. You politely ask {hero.name} to leave but he refuses, asserting the he must save The Princess from your evil grasp.
        Do you inform {hero.name} that's been played?"""
        choice_3 = input(prompt)
        if choice_3 == 'Yes' or choice_3 == 'No':
            break
                       
def bad_guy_story_2():
    while True:
        prompt = '''
        You're preparing for your drama free party. For added measure, you rent a guard Tiger
        for added security.

        It's party time and the mood is merry. You've even invited Mario and Luigi. The Princess is there
        but you can't recall inviting her. You think to have her removed, but then you're distracted by your 
        castle alarm going off. You have a guard tiger, but do you investigate further? Yes or No.
        '''
        choice_2 = input(prompt).title()
        if choice_2 == 'Yes' or choice_2 == 'No':
            print('The Tiger should be able to handle any minor disturbances.')
            bad_guy_story_3()
        elif choice_2 == 'Quit':
            break    
        else:
            print('Answer Yes or No.')    


def bad_guy_story():
        print(f"*** You've recieved a text from The Princess asking about the party you're hosting. ***") 
        prompt = f"\nYou didn't invite The Princess because she's action packed with drama."  
        prompt += f"\nNot only that, her friend, {hero.name} is a sword waving lunatic, "   
        prompt += f"\nDo you respond to her text? Yes or No."       

        choice_1 = input(prompt).title()
        if choice_1 == 'Yes' or choice_1 == 'No':
            bad_guy_story_2()
        else:
            print('Choose Yes or No')    


def start():
    while True:
        prompt = "\nChoose your character: The Hero or The Villian"
        prompt += "\nEnter 'quit' to end the program. "
        character = input(prompt).title()
        if character == 'quit' or character == 'Quit':
            break
        elif character == 'The Hero':
            character = hero
            print('\n****************************************')
            hero.description()
            good_guy_story()
        elif character == 'The Villian':
            character = the_villian
            print('\n****************************************')
            the_villian.description()
            bad_guy_story()

        else:
            print('Enter: The Hero or The Villian.')             
start()        



















    






