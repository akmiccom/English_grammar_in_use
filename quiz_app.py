from random import sample
from time import sleep
import re


def question_English(QUESTION_NUM, SLEEP_TIME):

    with open('English.md', mode='r', encoding='utf-8') as f:
        sentenses = f.read()

    questions = []
    for s in sentenses.split('\n'):
        if '   ' in s:
            tmp_s = re.sub(r'\d{,2}|', '', s)
            text = re.sub(r' \.', '', tmp_s)
            questions.append(text.strip())

    for i, s in enumerate(sample(questions, QUESTION_NUM)):
        print(f'Q{i+1} : ', s)
        sleep(SLEEP_TIME)


def question_Japanese(QUESTION_NUM, SLEEP_TIME):

    with open('Japanese.md', mode='r', encoding='utf-8') as f:
        sentenses = f.read()

    questions = []
    for s in sentenses.split('\n'):
        if '   ' in s:
            tmp_s = re.sub(r'\d{,2}|', '', s)
            text = re.sub(r' \.', '', tmp_s)
            questions.append(text.strip())

    for i, s in enumerate(sample(questions, QUESTION_NUM)):
        print(f'Q{i+1} : ', s)
        sleep(SLEEP_TIME)


if __name__ == '__main__':

    question_Japanese(QUESTION_NUM=9, SLEEP_TIME=0.3)

    question_English(QUESTION_NUM=9, SLEEP_TIME=0.3)
