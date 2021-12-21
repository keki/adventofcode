def main():
    score = [0,0]
    pos = [2,1]
    rolls = [0,0]
    player = 0

    state = {'last_roll': 0}
    def roll():
        state['last_roll'] += 1
        if state['last_roll'] > 100:
            state['last_roll'] = state['last_roll'] - 100
        return state['last_roll']

    while score[0] < 1000 and score[1] < 1000:
        pos[player] = (pos[player] + roll() + roll() + roll() -1 ) % 10 + 1
        score[player] += pos[player]
        rolls[player] += 3
        player = 1 - player

    print("POSITIONS", pos)
    print("SCORES", score)
    print("ROLLS", rolls)
    print("RESULT:", min(score) * sum(rolls))

if __name__ == "__main__":
    main()

