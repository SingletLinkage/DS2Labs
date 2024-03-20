# full house - 3 cards of one rank and 2 cards of another rank
import numpy as np
import math

# ----------------- Part A -----------------
def part_a():
    # probability of full house
    # 13C1 * 4C3 * 12C1 * 4C2 / 52C5
    probability_full_house = math.comb(13, 1) * math.comb(4, 3) * math.comb(12, 1) * math.comb(4, 2) / math.comb(52, 5)
    print(f"Theoretical: \tProbability of full house: \t{probability_full_house:.5f}")

# ----------------- Part B -----------------
def part_b():
    expts = 100000
    valid = expts
    full = 0
    for _ in range(expts):
        # generate 5 cards
        ranks = [i for i in range(1, 53)]
        np.random.shuffle(ranks)
        ranks = [i%13 for i in ranks[:5]]
        # check for wrong deck
        if len(set(ranks)) < 2:
            valid -= 1
            continue
        # check if full house
        if ranks.count(max(ranks)) * ranks.count(min(ranks)) == 6 and len(set(ranks)) == 2:
            # print(ranks)
            full += 1

    print(f"Simulated: \tProbability of full house: \t{full/valid:.5f}")


# ----------------- Part C -----------------
def part_c():
    expts = 1000
    trials = 1000
    fh_count = 0
    fulls = []
    # calculation of probability of atleast 2 full houses

    for i in range(expts):
        full = 0
        valid = trials
        for i in range(trials):
            # generate 5 cards
            ranks = [i for i in range(1, 53)]
            np.random.shuffle(ranks)
            ranks = [i%13 for i in ranks[:5]]

            # check for wrong deck
            if len(set(ranks)) < 2:
                valid -= 1
                continue

            # check if full house
            if ranks.count(max(ranks)) * ranks.count(min(ranks)) == 6 and len(set(ranks)) == 2:
                # print(ranks)
                full += 1

        fulls.append(full)
        if full >= 2:
            fh_count += 1

    # print(fulls)
    print("Simulated: \tP(getting more than 2 full houses): \t", fh_count/expts)
    probability_full_house = math.comb(13, 1) * math.comb(4, 3) * math.comb(12, 1) * math.comb(4, 2) / math.comb(52, 5)    
    # mean = 1 - (zero full house probab) - (1 full house probab)

    mean_th = 1 - (1 - probability_full_house)**trials - (trials * probability_full_house * (1 - probability_full_house)**(trials-1))
    
    print('Theoretical: \tP(getting more than 2 full houses): \t', round(mean_th,2))



    print('Full house: \t', end='')
    print(f"Mean: {np.mean(fulls)}\t", end ='')
    print(f"Variance: {np.var(fulls):.2f}")


if __name__ == "__main__":
    part_a()
    part_b()
    part_c()