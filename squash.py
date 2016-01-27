from random import random

def score_point(server, points):
    prob = [0.6, 0.65]
    if random() < prob[server[0]]:
        points[server[0]] += 1
    else:
        if server[0] == 0:
            server[0] = 1
        else:
            server[0] = 0
    return None

def run_trial():
    points = [0,0]
    server = [0]
    while max(points) < 21:
        score_point(server,points)
        #print(points, server)
    return points.index(21)

def run_sim(trials):
    winner = {0:0, 1:0}
    for trial in range(trials):
        trial_win = run_trial()
        print(trial_win)
        winner[trial_win] += 1
    return print(winner)
run_sim(1000)