import matplotlib.pyplot as plt
from math import log
x_vals = [(10000, 19.22),(20100,25.64),(20200,37),(40200,36.94),(80000, 58.81),(120000,95.57),(130000,99.6),(140000,99.63)]
o_vals = [(100000,16.23),(100100,17),(110100, 20.56),(130100,22.25),(150100,24.54),(170100,29.82),(190100,38.15),(210100,56.06),(230100,81.28),(250100,88.92),(270100,90.31),(290100,91.16),(340100,92.25)]
not_per_o = [(20000,16),(40000,18.48),(80000,20.39),(120000,20.39),(170000,24.93)]
ai_vs_ai = [(20000,1853/200),(40000,5745/400),(80000,8634/400),(120000,9278/400),(160000,10010/400),(200000,11261/400),(240000,12668/400),(280000,13245/400),(360000,26563/800)]

x, y = zip(*x_vals)
a, b = zip(*o_vals)
c, d = zip(*not_per_o)
e, f = zip(*ai_vs_ai)

plt.plot(x,y, label="X's")
plt.plot(a,b, label="O's")
plt.plot(c,d, label="O's (X plays middle 1st)")
plt.plot(e,f, label="AI vs AI ties")
plt.legend()
plt.grid()
plt.xlabel('number of games')
plt.ylabel('win or tie %')
plt.title('Tic Tac Toe Reinforcement \nLearning Accuracy VS "Perfect Game" ')
plt.show()