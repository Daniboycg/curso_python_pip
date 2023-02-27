import random

round=1
user_wins=0
computer_wins=0

def choose_options():
  options = ('Piedra', 'Papel', 'Tijera')
  z = input("Escriba piedra, papel o tijera: ")
  z1= z.capitalize()
  comp = random.choice(options)
  return z1, comp
  if not z1 in options:
    print('Input invalido')
    return None
   # continue

def rules(z1, comp, user_wins, computer_wins):
  
  if z1 == comp:
    print('Empate!')
  elif z1 == 'Piedra' and comp == 'Tijera':
    print('Ganaste!')
    user_wins += 1
  elif z1 == 'Piedra' and comp == 'Papel':
    print('Perdiste tonto!')
    computer_wins += 1
  elif z1 == 'Tijera' and comp == 'Papel':
    print('Ganaste!')
    user_wins += 1
  elif z1 == 'Tijera' and comp == 'Piedra':
    print('Perdiste tonto!')
    computer_wins += 1
  elif z1 == 'Papel' and comp == 'Piedra':
    print('Ganaste!')
    user_wins += 1
  elif z1 == 'Papel' and comp == 'Tijera':
    print('Perdiste tonto!')
    computer_wins += 1  
  return user_wins, computer_wins  
    
def winner(user_wins, computer_wins):
    
    print(f'''
    🙋 User wins: {user_wins}
    🤖 Computer wins: {computer_wins}
                ''')
    
    if user_wins == 3:
        print('🎖️ El ganador es User 🎖️')
        exit()
        
    if computer_wins == 3:
        print('🎖️ El ganador es Computer 🎖️')
        exit()  
    
while 1>0:
  z1, comp = choose_options()
  
  print("\n")
  print('*-'*20)
  print('               ROUND: ', round,'          ')
  print('*-'*20)
  round = round+1
  print('Usuario escogió: ', z1)
  print('La compu eligió: '+comp)
  
  user_wins, computer_wins = rules(z1,comp, user_wins, computer_wins)

  winner(user_wins, computer_wins)
  
