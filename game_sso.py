from random import randint

game_running = True
game_results = []

def calculate_monster_attack():
   return randint(monster['Attack_min'], monster['Attack_max'])

def Game_ends(winner_name):
    print(f'{winner_name} WON')


while game_running == True:

    counter = 0

    new_round = True
    
    player ={'Name':'Shadow','Attack':14,'Heal':16,'Health':100}
    monster ={'Name':'Lynx','Attack_min':10, 'Attack_max':18, 'Health':100}

    print('---' * 10)
    print('Enter Player Name')
    player['Name'] = input()

    print('---' * 10)
    print(player['Name'] + ' Has ' + str(player['Health']) + ' Health ')
    print(monster['Name'] + ' Has ' + str(monster['Health']) + ' Health ')

    while new_round == True:

        counter = counter + 1

        player_won = False
        monster_won = False

        print('---' * 10)
        print('Please select action')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit game')
        print('4) Show Results')

        player_choice = input()

        if player_choice == '1':
            monster['Health'] = monster['Health'] - player['Attack']
            if monster['Health'] <= 0:
                player_won = True

            else:
                #monster_attack = randint(monster['Attack_min'], monster['Attack_max'])
                player['Health'] = player['Health'] - calculate_monster_attack()
                #print(calculate_monster_attack())  
                if player['Health'] <= 0:
                    monster_won = True
            
            
          #print(monster['Name']+ 'Health is',monster['Health'])
          #print(player['Name']+'Health is',player['Health'])

        elif player_choice == '2':
            player['Health'] = player['Health'] + player['Heal']

            player['Health'] = player['Health'] - calculate_monster_attack()
            if player['Health'] <= 0:
                monster_won = True
            

        elif player_choice == '3':
            new_round = False
            game_running = False
            

        elif player_choice == '4':
            for i in game_results:
                print(i)


        else:
            print('Invalid Input')    


        if player_won ==False and monster_won == False:
            print(player['Name'] + ' Has ' + str(player['Health']) + ' Left ')
            print(monster['Name'] + ' Has ' + str(monster['Health']) + ' Left ')
            #print(calculate_monster_attack())



        elif player_won:
            Game_ends(player['Name'])
            round_result = {'Name':player['Name'], 'Health':player['Health'], 'rounds': counter}
            game_results.append(round_result)
            print(game_results)
            new_round = False
        
        elif monster_won:
            Game_ends(monster['Name'])
            round_result = {'Name':player['Name'], 'Health':player['Health'],  'rounds': counter}
            game_results.append(round_result)
            print(game_results)
            new_round = False

        