
def game():
    letters=['a','b','e','g','d','o','c','t','u']
    words=['at','bat','egg','go','dog','out','cat','tab']
    print('You Need to gess 3 word from below alphabets')
    print(letters)
    score=0
    for j in range(3):
        word=input('Enter the gess Word :- ')
        for i in words:
            if word==i:
                words.remove(word)
                score+=1
        print('You Earn ',score,'point')
    if score==3:
            print('')
            print("""
                  you Win This Game
                  """)
            print("""
                🎉 Congratulations! 🎉  
                """)
    else:
        print('')
        print('Lost')    


print('Hello')
start=input('Do you want to start the game\nif yes press "Y" :- ')

if start=='Y' or start=='y':
    game()

else:
    print('THANK YOU')
