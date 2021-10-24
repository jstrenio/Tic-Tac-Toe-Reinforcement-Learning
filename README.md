# tictactoe

This is one of the first python programs I ever wrote in an attempt to come up with a reinforcement learning algorithm before I began taking classes on RL
or ML. While I originally thought I was writing something similar to Q-Learning, I realized that this implementation samples from a distribution to update the
policy directly and so is actually something of a policy gradient algorithm though the reward function doesn't discount moves over time. Thankfully with 
a low learning rate, Tic Tac Toe doesn't last very long and so convergence was still possible. I have not revisited this much since studying ML but thought I 
would put this up as an early experiment.
