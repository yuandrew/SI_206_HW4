def ask_question():
    answer = input('What is your question? ')
    return answer


list1 = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely",
 "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes",
 "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now",
 "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no",
 "My sources say no", "Outlook not so good", "Very doubtful"]



answer = ask_question()
while(answer != 'quit'):
    if answer[-1] == "?":
        print (list1[randrange(len(list1))])
    else:
        print("I\'m sorry, I can only answer questions.")
    answer = ask_question()
