import numpy as np
import pickle

def main():

    partner_type = "pspecs_action_outsource"
    nof_repeat = 10
    # A, B, C refers to Partner A, B, and C
    a_sum, b_sum, c_sum = 0, 0, 0
    reward_sum, terminal_sum = 0, 0

    for i in range(nof_repeat):
        partner_specifity_mat_exfinal = pickle.load(open(partner_type + '/' + str(i) + '_' + partner_type + '_partner_specifity_mat_exfinal.pkl', 'rb'), encoding="latin1")
        run_stats = pickle.load(open(partner_type + '/' + str(i) + '_' + partner_type + '_run_stats.pkl', 'rb'), encoding="latin1")
        cumulative_reward, nof_terminal_episodes = run_stats[0], run_stats[1]
        partner_sum = np.sum(partner_specifity_mat_exfinal, axis=0)

        print(i, partner_sum, nof_terminal_episodes, cumulative_reward)
        a_sum += partner_sum[0]
        b_sum += partner_sum[1]
        c_sum += partner_sum[2]

        reward_sum += cumulative_reward
        terminal_sum += nof_terminal_episodes
    print("=================================")
    print("Partner sum: ", a_sum, b_sum, c_sum, terminal_sum, reward_sum)
    print("Partner avg: ", a_sum/nof_repeat, b_sum/nof_repeat, c_sum/nof_repeat, terminal_sum/nof_repeat, reward_sum/nof_repeat)


if __name__ == '__main__':
    main()
