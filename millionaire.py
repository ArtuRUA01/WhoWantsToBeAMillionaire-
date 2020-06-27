
import random
import time
import json

MONEY_TREE = [0, 100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]

############### TIMER

class WWTBAMPlayer():
    def __init__(self, name):
        self.name = name
        self.money = 0
        self.prize = 0

    def right_answer(self, money_per_round):
        self.money = money_per_round

    def wrong_answer(self):
        self.money = 0

    def __str__(self):
        return "{} - {}$\nPrize money: {}$".format(self.name, self.money, self.prize)

def read_question(number_question):
    with open('wwtbam_json_file.json', 'r') as f:
        all_data = json.loads(f.read())
        random_number = random.randint(1, 547)
        question = all_data[random_number]['question']
        a = all_data[random_number]['A']
        b = all_data[random_number]['B']
        c = all_data[random_number]['C']
        d = all_data[random_number]['D']
        answer = all_data[random_number]['answer']
        view_question(number_question, question, a, b, c, d)
        return answer

def view_question(number_question,question, a, b, c, d):
    print('Question # {}: {}'.format(number_question, question))
    print('A: {}'.format(a))
    print('B: {}'.format(b))
    print('C: {}'.format(c))
    print('D: {}'.format(d))

def get_player_name():
    # add try except
    player_name = input("Enter your name: ")
    return player_name

def beautiful_table(player):
    ind = MONEY_TREE[MONEY_TREE.index(player.money) + 1]
    print('\n\tMONEY TREE\n')
    for i in MONEY_TREE[::-1]:
        if i in [1000, 32000, 1000000]:
            print('{} XxXxXxX'.format(i))
            continue
        if i == ind:
            print('{}<------'.format(i))
        else:
            if i == 0:
                continue
            print('{}\t'.format(i))
    print()

def fifty_by_fifty(correct_answer):
    print('\nYou enter tip fifty by fifty (50%/50%)')
    letter = ['A', 'B', 'C', 'D']
    if correct_answer[0] == letter[0]:
        print('A or {}'.format(random.choice(['B', 'C', 'D'])))
    elif correct_answer[0] == letter[1]:
        print('{} or B'.format(random.choice(['A', 'C', 'D'])))
    elif correct_answer[0] == letter[2]:
        print('C or {}'.format(random.choice(['B', 'A', 'D'])))
    elif correct_answer[0] == letter[3]:
        print('{} or D'.format(random.choice(['B', 'C', 'A'])))

def tip_call():
    print('You choose tip "Call to ..."')
    print('So You call to ...')
    time.sleep(1)
    print('Google.com')
    print('You can find the answer to this question on the Internet')

def tip_hall(correct_answer):
    print('You choose tip "Hall help"')
    random_flip = random.randint(1, 6)
    print('random_flip', random_flip)
    answer = []
    percentage = 100
    if random_flip == 1:
        for _ in range(3):
            version = random.randint(0, percentage-1)
            answer.append(version)
            percentage -= version
        answer.append(100 - sum(answer))
    else:
        correct_version = random.randint(40, percentage-40)
        answer.append(correct_version)
        percentage -= correct_version
        for i in range(2):
            version = random.randint(0, percentage-1)
            answer.append(version)
            percentage -= version
        answer.append(100 - sum(answer))

    letter = ['A', 'B', 'C', 'D']
    if correct_answer[0] == letter[0]:
        print('A: {}%'.format(answer[0]))
        print('B: {}%'.format(answer[1]))
        print('C: {}%'.format(answer[2]))
        print('D: {}%'.format(answer[3]))
    elif correct_answer[0] == letter[1]:
        print('A: {}%'.format(answer[1]))
        print('B: {}%'.format(answer[0]))
        print('C: {}%'.format(answer[2]))
        print('D: {}%'.format(answer[3]))
    elif correct_answer[0] == letter[2]:
        print('A: {}%'.format(answer[2]))
        print('B: {}%'.format(answer[1]))
        print('C: {}%'.format(answer[0]))
        print('D: {}%'.format(answer[3]))
    elif correct_answer[0] == letter[3]:
        print('A: {}%'.format(answer[3]))
        print('B: {}%'.format(answer[1]))
        print('C: {}%'.format(answer[2]))
        print('D: {}%'.format(answer[0]))


def game():
    print('=' * 55)
    print("Welcome to the game 'Who wants to be a Millionaire?'")
    print('=' * 55)
    player_name = get_player_name()
    player = WWTBAMPlayer(player_name)
    print(player)
    tips = []
    for question in range(15):
        time.sleep(3)
        beautiful_table(player)
        correct_answer = read_question(question+1)
        print('Tips: 1. "Call to ..." 2. "Hall help" 3. "Fifty by fifty"')
        time.sleep(0.5)
        print('correct_answer: {}'.format(correct_answer))
        # add try except
        player_answer = input('Enter your answer: ').upper()
        time.sleep(0.5)
        while player_answer in ['1', '2', '3']:
            if player_answer == '1' and player_answer not in tips:
                print()
                tip_call()
                print()
                tips.append('1')
            elif player_answer == '2' and player_answer not in tips:
                print()
                tip_hall(correct_answer)
                print()
                tips.append('2')
            elif player_answer == '3' and player_answer not in tips:
                print()
                fifty_by_fifty(correct_answer)
                print()
                tips.append('3')
            else:
                print('You use this tip.')
            player_answer = input('Enter your answer: ').upper()
            if player_answer in ['A', 'B', 'C', 'D']:
                break

        if correct_answer == player_answer:
            money_per_round = MONEY_TREE[question+1]
            print("Congratulation! You earn {}$".format(money_per_round))
            player.right_answer(money_per_round)
            if money_per_round == MONEY_TREE[5]:
                player.prize = money_per_round
            elif money_per_round == MONEY_TREE[10]:
                player.prize = money_per_round
            elif money_per_round == MONEY_TREE[15]:
                player.prize = money_per_round
            print()
            print('-'*25)
            print(player)
            print('-'*25)
        else:
            print('Wrong answer! Correct answer: {}\nGoodbye'.format(correct_answer))
            player.wrong_answer()
            print()
            print('-'*25)
            print(player)
            print('-'*25)
            exit()

game()


