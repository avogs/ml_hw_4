import random
import matplotlib.pyplot as plt
import numpy as np

functions = [lambda x: 2*x, lambda x: -2*x]

T = 10**6

all_losses = []
end_losses = []

if_just_this = [0, 0]
options = [0, 1]

etas = []
for i in range(1,10**4, 400):
    etas.append(1/i)

p_i_t = [0.5, 0.5]

#print(len(etas))
#for k in range(len(etas)):
#    eta = etas[k]
#    if_just_this = [0, 0]
#    p_i_t = [0.5, 0.5]
#    print(k)
#    losses = []
#    loss = 0
#    for i in range(T):
#        func = functions[i % 2]
#        if i == 0:
#            func = lambda x: x
#        if_just_this[0] += func(options[0])
#        if_just_this[1] += func(options[1])
#        denominator = (np.exp(-1*eta*if_just_this[0]) + np.exp(-1*eta*if_just_this[1]))
#        p_i_t[0] = np.exp(-1*eta*if_just_this[0]) / denominator
#        p_i_t[1] = np.exp(-1*eta*if_just_this[1]) / denominator
#        choice = random.choices([0, 1], weights = (p_i_t[0], p_i_t[1]), k = 1)[0]
#        loss += func(options[choice])
#        losses.append(loss)
#    end_losses.append(loss)
#    all_losses.append(losses)

etas = [1.0, 0.0024937655860349127, 0.0012484394506866417, 0.0008326394671107411, 0.0006246096189881324, 0.0004997501249375312, 0.00041649312786339027, 0.0003570153516601214, 0.00031240237425804435, 0.00027770063871146905, 0.00024993751562109475, 0.00022722108611679165, 0.00020828993959591752, 0.00019227071716977504, 0.00017853954650955185, 0.00016663889351774705, 0.0001562255897516013, 0.00014703720041170417, 0.00013886960144424384, 0.00013156163662675965, 0.00012498437695288088, 0.00011903344839900012, 0.00011362345188046812, 0.00010868383871318335, 0.00010415581710238516]
end_losses = [-462706, -1736, 857, 114, -99, 457, 348, 979, -125, -810, 382, 68, -700, 959, -901, 1001, 542, 325, -688, -1400, 930, 111, 118, -437, -1009]
print(etas)
print(end_losses)
plt.semilogx(etas[1:], end_losses[1:])
plt.title("Total loss as a function of $\eta$")
plt.xlabel("$\eta$")
plt.ylabel("total loss")
plt.show()