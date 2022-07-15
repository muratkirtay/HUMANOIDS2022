import numpy as np
import matplotlib.pyplot as plt

def main():

    plt.style.use('seaborn')
    X_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '11', '12', '13', '14']

    # the lists below can be created by using table_data.py
    partner_A = [52.542374, 49.593494, 38.617886, 36.580883, 33.704975, 28.107075, 26., 25.663717, 36.363636,
                 31.177446, 29.206348, 32.236843, 26.785715]
    partner_B = [27.118645, 21.95122, 28.455284, 26.470589, 30.874786, 39.57935, 34.8, 42.477875, 40.909092,
                 28.689884, 31.11111,  28.947369, 21.428572]
    partner_C = [20.338984, 28.455284, 32.92683, 36.94853, 35.42024, 32.313576, 39.2, 31.858408, 22.727272,
                 40.13267, 39.68254, 38.81579, 51.785713]

    X_axis, width = np.arange(len(X_labels)), 0.28

    plt.bar(X_axis - width, partner_A, width, label='Partner A')
    plt.bar(X_axis, partner_B, width, label='Partner B')
    plt.bar(X_axis + width, partner_C, width, label='Partner C')
    plt.ylim([0, 70])
    plt.xticks(X_axis, X_labels)
    plt.xlabel("States")
    plt.ylabel("Partner specificity (%)")
    plt.legend()
    plt.savefig("state_specs.png")
    plt.show()

if __name__ == '__main__':
    main()