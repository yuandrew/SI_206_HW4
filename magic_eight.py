def ask_question():
    answer = input('What is your question? ')


answer = ask_question()
while(answer != quit):
    if answer[-1] == ‘?’:

    else:
        print(‘I\’m sorry, I can only answer questions.’)
