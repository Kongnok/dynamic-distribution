import numpy as np

class DynamicDistributor:
    def __init__(self, n_options):
        self.n_options = n_options
        self.alphas = np.ones(n_options)
        self.betas = np.ones(n_options)
        
    def select_option(self):
        samples = [np.random.beta(self.alphas[i], self.betas[i]) for i in range(self.n_options)]
        return np.argmax(samples)
        
    def update_distribution(self, chosen_option, reward):
        if reward == 1:
            self.alphas[chosen_option] += 1
        else:
            self.betas[chosen_option] += 1

if __name__ == "__main__":
    true_probabilities = [0.10, 0.65, 0.25]
    n_ads = len(true_probabilities)
    
    distributor = DynamicDistributor(n_ads)
    total_trials = 1000
    choices_history = {0: 0, 1: 0, 2: 0}
    
    print("Starting dynamic distribution simulation...\n")
    
    for trial in range(total_trials):
        chosen_ad = distributor.select_option()
        choices_history[chosen_ad] += 1
        
        user_clicked = np.random.rand() < true_probabilities[chosen_ad]
        
        distributor.update_distribution(chosen_ad, int(user_clicked))

    print("### Final Traffic Distribution ###")
    for ad, count in choices_history.items():
        print(f"Ad {ad} shown {count} times (Expected CTR: {true_probabilities[ad]*100}%)")