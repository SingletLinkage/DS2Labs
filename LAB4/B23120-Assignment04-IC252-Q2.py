import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

probab_defective = {'incandescent': 0.1, 'LED': 0.05}
probab_light = {'incandescent': 0.4, 'LED': 0.6}

def joint_probab_table(replacement):
    # pick two light bulbs at random without replacement
    # Random Variable : Y = {0, 1, 2} -> total number of defective light bulbs
    # Random Variable : X = {0, 1, 2} -> total number of incandescent light bulbs
    print('Defining Random Variable Used: ')
    print('X = {0, 1, 2} -> total number of incandescent light bulbs')
    print('Y = {0, 1, 2} -> total number of defective light bulbs')
    # =============== SIMULATING ==================
    joint_probab = np.zeros((3, 3))
    simulation = 100000
    for _ in range(simulation):
        bulbs = np.random.choice(['incandescent', 'incandescent', 'LED', 'LED', 'LED'], size=2, replace=replacement)
        c_incandescent = bulbs.tolist().count('incandescent')
        c_defective = 0
        for b in bulbs:
            c_defective += np.random.choice([0,1], p=[1-probab_defective[b], probab_defective[b]])
        joint_probab[c_defective][c_incandescent] += 1
    joint_probab = joint_probab / simulation

    print('Joint Probability by Simulation: \n', pd.DataFrame(joint_probab, columns=['0', '1', '2'], index=['0', '1', '2']))

    # =============== CALCULATING ==================
    print('Joint Probability by Calculation: ')
    joint_probab_calc = np.zeros((3, 3))

    if not replacement:
        light_p = np.array([0.3, 0.6, 0.1])  # probabilities calculated theoretically
    else:
        light_p = np.array([0.36, 0.48, 0.16])  # probabilities calculated theoretically

    # looping through number of incandescent light bulbs:
    for i in range(3):        
        # Case: 0 defective light bulbs
        joint_probab_calc[0][i] = light_p[i] * (1-probab_defective['incandescent'])**i * (1-probab_defective['LED'])**(2-i)

        # Case: 2 defective light bulbs
        joint_probab_calc[2][i] = light_p[i] * probab_defective['incandescent']**i * probab_defective['LED']**(2-i)

    # 1 defective separate cases:
    joint_probab_calc[1][0] = light_p[0] * 2 * probab_defective['LED'] * (1-probab_defective['LED'])
    joint_probab_calc[1][1] = light_p[1] * (probab_defective['incandescent'] * (1-probab_defective['LED']) + probab_defective['LED'] * (1-probab_defective['incandescent']))
    joint_probab_calc[1][2] = light_p[2] * 2 * probab_defective['incandescent'] * (1-probab_defective['incandescent'])
        
    
    df = pd.DataFrame(joint_probab_calc, columns=['0', '1', '2'], index=['0', '1', '2'])
    print(df.to_string())
    plot_joint(df)
    return df

def plot_joint(df):
    x = np.arange(3)
    y = np.arange(3)
    z = df.to_numpy()
    X, Y = np.meshgrid(x, y)

    # Create figure and axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Flatten X and Y, and convert Z to 1D array
    x_data = X.flatten()
    y_data = Y.flatten()
    z_data = z.flatten()

    # Define bar dimensions
    dx = dy = 0.5  # Width and depth of bars
    dz = z_data  # Height of bars

    # Plot 3D bar graph
    ax.bar3d(x_data, y_data, np.zeros_like(z_data), dx, dy, dz)

    # Set labels and title
    ax.set_xlabel('Number of Incandescest Light Bulbs')
    ax.set_ylabel('Total Number of Defective Light bulbs')
    ax.set_xticks([0, 1, 2])
    ax.set_yticks([0, 1, 2])
    ax.set_zlabel('Probability Density')
    ax.set_title('3D Bar Graph of Joint PDF')

    ax.view_init(azim=120, elev=30)  # azim: azimuth angle, elev: elevation angle

    plt.show()

def marginal_probability(df):
    marginal_probab_incandes = df.sum(axis=0)
    marginal_probab_defective = df.sum(axis=1)
    return marginal_probab_incandes, marginal_probab_defective

def generic_jointpdf(replacement):
    string = 'with replacement' if replacement else 'without replacement'
    df = joint_probab_table(replacement)
    res = marginal_probability(df)
    print('Marginal Probability Tables')
    print('Number of Incandescent Light Bulbs')
    print(res[0].to_string())
    print('Defective Light Bulbs')
    print(res[1].to_string())

    # Plotting Marginals
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    ax[0].bar(res[0].index, res[0].values)
    ax[0].set_title('Marginal Probability of Incandescent Light Bulbs '+string)
    ax[0].set_xlabel('Number of Incandescent Light Bulbs')
    ax[0].set_ylabel('Probability Density')

    ax[1].bar(res[1].index, res[1].values)
    ax[1].set_title('Marginal Probability of Defective Light Bulbs '+string)
    ax[1].set_xlabel('Number of Defective Light Bulbs')
    ax[1].set_ylabel('Probability Density')

    plt.show()

def part_a_b():
    print('Joint PMF WITH Replacement')
    generic_jointpdf(False)


def part_d():
    # P(one defective | first incandescent) = ?
    # P(one defective | first incandescent) = P(one defective, first incandescent) / P(first incandescent)
    # P(first incandescent) = 2/5 = 0.4
    # first incandescent --> ii(0.1) + il(0.3) --> without replaceement
    # P(one defective, ii) = P(ii) * P(defective | i) * (1 - P(defective | i)) * 2
    #                      = 0.1 * 0.1 * 0.9 * 2
    #                      = 0.018
    # P(one defective, il) = P(il) * [P(defective | i) * (1 - P(defective | l)) + P(defective | l) * (1 - P(defective | i))]
    #                      = 0.3 * [0.1 * 0.95 + 0.05 * 0.9]
    #                      = 0.042
    # P(one defective) = P(one defective, ii) + P(one defective, il)
    #                  = 0.018 + 0.042
    #                  = 0.06
    # P(one defective | first incandescent) = 0.06 / 0.4
    #                                        = 0.15
    print('Conditional probability of getting one defective bulb given the first chosen is incandescent', 0.15)

def part_e():
    # No, the events are not independent
    # The choice of type of lightbulbs influence the probability of getting a defective light bulb since the probabilities are different for each type of light bulb
    # For example, the probability of getting a defective incandescent light bulb is 0.1 while the probability of getting a defective LED light bulb is 0.05
    # So, the probability of getting a defective light bulb is dependent on the type of light bulb chosen

    # Explaining using Joint Probability Table
    # P(1 defective, 1 incandescent) = 0.042
    # P(1 defective) = 0.18
    # P(1 incandescent) = 0.4
    # P(1 defective, 1 incandescent) != P(1 defective) * P(1 incandescent)
    ...

def part_f():
    print('Joint PMF WITH Replacement')
    generic_jointpdf(True)

def part_g():
    # Yes, the PMF of X will change upon sampling with replacement
    # The probabilities of getting incandescent light bulbs will change since the probabilities are calculated based on the number of incandescent light bulbs in the sample
    # Initially, for 5 light bulbs, the probabilities are 0.4, 0.6 for incandescent and led respectively
    # But, after sampling with replacement, the probabilities will change depending on the first light bulb chosen
    # For example, if the first light bulb chosen is led, the probability of getting another led light bulb will be 0.5
    ...

part_a_b()
part_f()