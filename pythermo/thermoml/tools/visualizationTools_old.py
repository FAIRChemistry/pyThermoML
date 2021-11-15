from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

def plotArrheniusOld(tempdict, viscdict, title=None):

    if title is None:
        title = "Arrhenius"
    
    for key in tempdict.keys():

        x = np.array(tempdict[key])
        x = x.reshape(-1, 1)
        y = np.array(viscdict[key])

        model = LinearRegression()
        model.fit(x, y)

        print("R2: ", round(model.score(x, y), 2))

        t = (min(x), max(x))

        plt.scatter(x, y, alpha=0.5)
        plt.plot(t, model.predict(t), label=key)

    plt.grid()
    plt.title(title)
    plt.xlabel("1/RT in [mol/KJ]")
    plt.ylabel("ln(eta) in [cP]")
    plt.legend()
    plt.show()