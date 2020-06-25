
import random
import time
import json

MONEY_TREE = [0, 100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]

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

#####################################################
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
#####################################################

def get_player_name():
    # add try except
    player_name = input("Enter your name: ")
    return player_name

def beautiful_table(player):
    ind = MONEY_TREE[MONEY_TREE.index(player.money) + 1]
    print('\tMONEY TREE\n')
    for i in MONEY_TREE[::-1]:
        if i == ind:
            print('--->{}<---'.format(i))
        else:
            print('\t{}\t'.format(i))
    print()

def game():
    print('=' * 55)
    print("Welcome to the game 'Who wants to be a Millionaire?'")
    print('=' * 55)
    time.sleep(3)
    player_name = get_player_name()
    player = WWTBAMPlayer(player_name)
    print(player)
    print()
    for question in range(15):
        time.sleep(2)
        print()
        beautiful_table(player)
        print()
        correct_answer = read_question(question+1)
        print('correct_answer: {}'.format(correct_answer))
        # add try except
        player_answer = input('Enter your answer: ').upper()
        time.sleep(2)
        if correct_answer == player_answer:
            money_per_round = MONEY_TREE[question+1]
            print("Congratulation! You earn {}$".format(money_per_round))
            player.right_answer(money_per_round)
            print('-'*25)
            print(player)
            print('-'*25)
        else:
            print('Wrong answer! Goodbye')
            player.wrong_answer()
            print('-'*25)
            print(player)
            print('-'*25)
            exit()
    time.sleep(5)

game()


