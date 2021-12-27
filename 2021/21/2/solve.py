import numpy as np

def main():

    # dimensions: position of player one, score of player one, position of player two, score of player two
    # value: how many universes are there in that state
    state = np.zeros((11,11,21,21), dtype=int)

    #starting state: p1 is at 2, p2 is at 1, both have zero score
    state[2][1][0][0] = 1

    wins = [0,0]

    while np.any(state):
        for player_in_turn in 1, 2:
            new_state = np.zeros(state.shape, dtype=int)
            for p1_pos, p2_positions in enumerate(state):
                for p2_pos, p1_scores in enumerate(p2_positions):
                    for p1_score, p2_scores in enumerate(p1_scores):
                        for p2_score, universes in enumerate(p2_scores):
                            if universes != 0:
                                for roll1 in 1, 2, 3:
                                    for roll2 in 1, 2, 3:
                                        for roll3 in 1, 2, 3:
                                            roll = roll1 + roll2 + roll3
                                            if (player_in_turn == 1):
                                                new_pos = p1_pos + roll
                                                while new_pos > 10:
                                                    new_pos = new_pos - 10
                                                new_score = p1_score + new_pos
                                                if new_score < 21:
                                                    new_state[new_pos][p2_pos][new_score][p2_score] += universes
                                                else:
                                                    wins[0] += universes
                                            else:
                                                new_pos = p2_pos + roll
                                                while new_pos > 10:
                                                    new_pos = new_pos - 10
                                                new_score = p2_score + new_pos
                                                if new_score < 21:
                                                    new_state[p1_pos][new_pos][p1_score][new_score] += universes
                                                else:
                                                    wins[1] += universes
            print(wins)
            state = new_state

    print(f"WINNER WINS IN {max(wins)} universes")

if __name__ == "__main__":
    main()

