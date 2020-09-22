import random 


# random.random() generates random # between 0-1, not including 1
print('-- random.random() --')
print(f'random_1: {random.random()}')
print(f'random_2: {random.random()}')

# random.randrange(#stop) generates random # between 0-#stop
print('-- random.randrange(#stop) --')
print(f'randrange(10)_1: {random.randrange(10)}')
print(f'randrange(10)_2: {random.randrange(10)}')

# random.randint(#start,#stop) generates random # between #start-#stop
print('-- random.randint(#start,#stop) --')
print(f'randint(3,9)_1: {random.randint(3,9)}')
print(f'randint(3,9)_2: {random.randint(3,9)}')

# random.randrange(#start,#stop,#step) generates random # between #start-#stop increment by #step
print('-- random.randrange(#start,#stop,#step) --')
print(f'randrange(5,15,2)_1: {random.randrange(5,15,2)}')
print(f'randrange(5,15,2)_2: {random.randrange(5,15,2)}')

# random.choice(list) generates random selection from the given list
print('-- random.choice(list) --')
list1 = ['a', 'b', 'c', 'd']
print("list1 = ['a', 'b', 'c', 'd']")
print(f'choice(list1)_1: {random.choice(list1)}')
print(f'choice(list1)_2: {random.choice(list1)}')

# random.choice(range(#stop)) generates random # between 0-#stop, similar to randrange(#stop), exectued differently
print('-- random.choice(range(#stop)) --')
print(f'choice(range(10))_1: {random.choice(range(10))}')
print(f'choice(range(10))_2: {random.choice(range(10))}')

# random.shuffle(list) generates random shuffle of the given list contents
print('-- random.shuffle(list) --')
list2 = ['a', 'b', 'c', 'd']
print("list2 = ['a', 'b', 'c', 'd']")
random.shuffle(list2)
print(f'shuffle(list2)_1: {list2}')
random.shuffle(list2)
print(f'shuffle(list2)_2: {list2}')

### Distributions ###
# pseudo-random #s, technically not random
# random.uniform(#start,#stop) generates random float # between #start-#stop
print('-- random.uniform(#start,#stop) --')
print(f'uniform(2,9)_1: {random.uniform(2,9)}')
print(f'uniform(2,9)_2: {random.uniform(2,9)}')

# random.gauss(mu(mean),sigma(standard deviation)) generates random # with gaussian distribution, bell shaped curve 
print('-- random.gauss(#mu,#sigma) --')
print(f'gauss(3.4,25))_1: {random.gauss(3.4,25)}')
print(f'gauss(3.4,25)_2: {random.gauss(3.4,25)}')

# random.expovariate(#lambd) generates pseudo-random # with exponential distribution, non 0 - infinity
print('-- random.expovariate(#lambd) --')
print(f'expovariate(1.5)_1: {random.expovariate(1.5)}')
print(f'expovariate(1.5)_2: {random.expovariate(1.5)}')

# random.gammavariate(#alpha(shape),#beta) generates pseudo-random # with exponential distribution, > 0, not acutally random, techinically could be determined
print('-- random.gammavariate(#alpha, #beta) --')
print(f'gammavariate(3.4,25)_1: {random.gammavariate(3.4,25)}')
print(f'gammavariate(3.4,25)_2: {random.gammavariate(3.4,25)}')

# random.lognormvariate(#mu(mean),#sigma(standard deviation) generates pseudo-random # with log-normal distribution
# log-normal (or lognormal) distribution is a continuous probability distribution of a random variable whose logarithm is normally distributed. Thus, if the random 
# variable X is log-normally distributed, then Y = ln(X) has a normal distribution.[1][2][3] Equivalently, if Y has a normal distribution, then the exponential 
# function of Y, X = exp(Y), has a log-normal distribution
print('-- random.lognormvariate(#mu, #sigma) --')
print(f'lognormvariate(3.4,25)_1: {random.lognormvariate(3.4,25)}')
print(f'lognormvariate(3.4,25)_2: {random.lognormvariate(3.4,25)}')

# random.vonmisesvariate(#mu(mean),#kappa) generates pseudo-random # with von Mises distribution or circular normal distribution
# von Mises distribution (also known as the circular normal distribution or Tikhonov distribution) is a continuous probability distribution on the circle. It is a close 
# approximation to the wrapped normal distribution, which is the circular analogue of the normal distribution
print('-- random.vonmisesvariate(#mu, #kappa) --')
print(f'vonmisesvariate(3.4,25)_1: {random.vonmisesvariate(3.4,25)}')
print(f'vonmisesvariate(3.4,25)_2: {random.vonmisesvariate(3.4,25)}')

# random.paretovariate(#alpha(shape)) generates pseudo-random # with Pareto distribution
# Pareto distribution is a power-law probability distribution that is used in description of social, scientific, geophysical, actuarial, and many other types of observable phenomena
print('-- random.paretovariate(#alpha) --')
print(f'paretovariate(3.7)_1: {random.paretovariate(3.7)}')
print(f'paretovariate(3.7)_2: {random.paretovariate(3.7)}')

# random.weibullvariate(#alpha(scale),#beta(shape)) generates pseudo-random # with Weibull distribution
# Weibull distribution is a continuous probability distribution
print('-- random.weibullvariate(#alpha, #beta) --')
print(f'weibullvariate(3.4,25)_1: {random.weibullvariate(3.4,25)}')
print(f'weibullvariate(3.4,25)_2: {random.weibullvariate(3.4,25)}')
