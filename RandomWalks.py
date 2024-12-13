import classes, random
from classes import Walker, Location, Land
import matplotlib.pyplot as plt

def singleWalk(land: Land, walker: Walker, numOfSteps: int):

    # Validate Input
    if numOfSteps < 0:
        raise ValueError('Number of steps must be greater than or equal to zero')
    
    #Record starting position
    startingPosition = land.locate(walker)

    #Simulate the walk itself
    for _ in range(numOfSteps):
        land.moveWalker(walker)

    #Ending position
    endingPosition = land.locate(walker)

    return startingPosition.distance(endingPosition)

def simulatingWalks(numOfSteps: int, numOfTrials: int):

    #Validate input
    if numOfSteps < 0:
        raise ValueError('Number of steps must be greater than or equal to zero')
    if numOfTrials <= 0:
        raise ValueError('Number of trials must be greater than zero')

    #Starting place for all the walkers
    origin = Location(0,0)
    zombie = Walker()

    distances = []

    for _ in range(numOfTrials):

        land = Land()
        land.addWalker(zombie, origin)
        distances.append(round(singleWalk(land, zombie, numOfSteps),1))
    
    return distances

'''def testResults(lengthOfWalks, numOfTrials):

    for numOfSteps in lengthOfWalks:
        distances = simulatingWalks(numOfSteps, numOfTrials)
        print(Walker.__name__, 'random walk of', numOfSteps, 'steps')
        print(' Mean =', round(sum(distances)/len(distances), 4))
        print(' Max =', max(distances), 'Min =', min(distances))

random.seed(0)
testResults((10, 100, 1000, 10000, 100000), 100)'''

def plot(lengthOfWalks, numOfTrials):

    max_values, min_values, means = [],[],[]

    for numOfSteps in lengthOfWalks:
        distances = simulatingWalks(numOfSteps, numOfTrials)
        Mean = round(sum(distances)/len(distances), 4)
        Max = max(distances)
        Min = min(distances)

        max_values.append(Max)
        min_values.append(Min)
        means.append(Mean)

    plt.figure(figsize=(10, 6))
    plt.plot(lengthOfWalks, means, label='Mean Distance', marker='o')
    plt.plot(lengthOfWalks, max_values, label='Max Distance', marker='o')
    plt.plot(lengthOfWalks, min_values, label='Min Distance', marker='o')

    plt.title('Mean, Max, and Min Distances vs Number of Steps')
    plt.xlabel('Number of Steps')
    plt.ylabel('Distance')
    plt.legend()
    plt.grid(True)
    plt.show()

#Setting a seed for testing
random.seed(0)
plot((10, 100, 1000, 10000, 100000), 100)