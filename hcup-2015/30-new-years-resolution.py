import sys
import itertools

def can_reach_goal(goal, foods):
    for order in range(1, len(foods) + 1):
        for subset in itertools.combinations(foods, order):
            if sumlists(subset) == goal:
                return True
    return False
    
def sumlists(ls):
    r = [0 for x in ls[0]]
    for l in ls:
        for i in range(len(r)):
            r[i] += l[i]
    return r

if __name__ == '__main__':
    fname = sys.argv[1]
    with open(fname) as f:
        t = int(f.readline())
        for i in range(1, t + 1):
            goal = [int(x) for x in f.readline().strip().split()]
            n = int(f.readline().strip())

            foods = []
            for x in range(n):
                food = [int(x) for x in f.readline().strip().split()]
                foods.append(food)

            r = can_reach_goal(goal, foods)
            print "Case #%d: %s" % (i, "yes" if r else "no")
