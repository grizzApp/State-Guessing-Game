import turtle
import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)
PATH_CSV = os.path.join(BASE_DIR, '50_states.csv')
IMG = os.path.join(BASE_DIR, 'blank_states_img.gif')
FONT = ('Brass Mono Regular', 10, 'normal')

df = pd.read_csv(PATH_CSV)
all_state = df['state']

screen = turtle.Screen()
screen.title('US State Guessing Game')
screen.tracer(0)
screen.addshape(IMG)

turtle.shape(IMG)

text = turtle.Turtle()
text.hideturtle()
text.penup()

def check_user_guess(guess) -> bool:
    return guess in df['state'].values

def get_coor(guess) -> tuple[int, int]:
    if check_user_guess(guess):
        state = df[df['state'] == guess]
        x_cor = int(state['x'].iloc[0])
        y_cor = int(state['y'].iloc[0])
        return ((x_cor, y_cor))

guessed_states = []
total_state = len(df)
guess_count = 0

while guess_count < total_state:
    screen.update()
    user_guess = turtle.textinput(title=f'There is {guess_count}/{total_state} states to guess', prompt="What's another state name?").title()

    if user_guess is None:
        continue

    if user_guess == 'Exit':
        break

    if check_user_guess(user_guess):
        coordinate = get_coor(user_guess)
        text.goto(coordinate)
        text.write(arg=user_guess, move=True, font=FONT)
        guess_count += 1
        guessed_states.append(user_guess)


for guessed in guessed_states:
    df = df[df['state'] != guessed][['state']]

df.to_csv('state_to_learn.csv', index=False)