import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

weathers = ['sunny', 'rainy', 'cloudy']
clothes = ['t-shirt', 'sweater', 'jacket']

weather_probability = {'sunny': 0.4, 'rainy': 0.28, 'cloudy': 0.32}
clothes_probability = {
    'sunny' : {'t-shirt': 0.8, 'sweater': 0.08, 'jacket': 0.12},
    'rainy' : {'t-shirt': 0.15, 'sweater': 0.25, 'jacket': 0.6},
    'cloudy': {'t-shirt': 0.2, 'sweater': 0.4, 'jacket': 0.4}
}


def joint_probab_table():
    joint_probab = np.zeros((3, 3))
    simulation_days = 100000
    # simulating a large number of days
    for _ in range(simulation_days):
        weather = np.random.choice(weathers, p=[weather_probability[w] for w in weathers])
        cloth = np.random.choice(clothes, p=[clothes_probability[weather][c] for c in clothes])
        joint_probab[weathers.index(weather)][clothes.index(cloth)] += 1
    joint_probab = joint_probab / simulation_days
    return joint_probab

def marginal_probab_table(df):
    marginal_probab_cloth = df.sum(axis=0)
    marginal_probab_weather = df.sum(axis=1)
    return marginal_probab_weather, marginal_probab_cloth

def marginal_plot(weather, cloth):
    # Plotting the marginal probability of weather
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    ax[0].bar(weathers, weather)
    ax[0].set_xlabel('Weather')
    ax[0].set_ylabel('Probability')
    ax[0].set_title('Marginal Probability of Weather')

    # Plotting the marginal probability of clothes
    ax[1].bar(clothes, cloth)
    ax[1].set_xlabel('Clothes')
    ax[1].set_ylabel('Probability')
    ax[1].set_title('Marginal Probability of Clothes')
    plt.show()

def conditional_probab(df : pd.DataFrame, mar_weather : pd.Series):
    # P(cloth|weather) = P(cloth, weather) / P(weather)
    for w in weathers:
        df.loc[w] = df.loc[w] / mar_weather.loc[w]
    return df

if __name__ == '__main__':
    df = pd.DataFrame(joint_probab_table(), columns=clothes, index=weathers)
    res = marginal_probab_table(df)

    # ============== Part A =================
    print('Joint Probability Table')
    print(df.to_string())
    # ============== Part B =================
    print('Marginal Probability Tables')
    print('Weather')
    print(res[0].to_string())
    print('Clothes')
    print(res[1].to_string())

    marginal_plot(res[0], res[1])

    # ============== Part C =================
    print('Conditional Probability Table')
    print(conditional_probab(df, res[0]).to_string())