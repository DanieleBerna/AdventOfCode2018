import itertools
import datetime
import collections

# +++++++++++++++ FIRST TRY: ALL DONE USING LISTS... SOOOOOO SLOW!! +++++++++++++++++++++++

def CycleList(index,list,step=1):

    # Used to find the proper insert position and mimic the rotation of the list
    if index+step <= len(list) and index+step >= 0:
        return index+step
    else:
        return (index+step)-(step/abs(step) * len(list))


def PlayMarbleGame(numPlayers, numMarbles):

    # Play the game!
    startTime = datetime.datetime.now()
    pool = range(1, numMarbles + 1)
    playersScores = [0 for i in range(numPlayers)]
    PlayersIterator = itertools.cycle(range(numPlayers))
    marbles = [0]
    currentMarbleIndex = 0

    while len(pool) > 0:
        currentPlayer = PlayersIterator.next()
        if pool[0] % 23 != 0:

            currentMarbleIndex = CycleList(currentMarbleIndex, marbles, step=2)

            marbles.insert(currentMarbleIndex, pool[0])
            pool.pop(0)
        else:
            playersScores[currentPlayer] += pool.pop(0)
            currentMarbleIndex = CycleList(currentMarbleIndex, marbles, step=-7)
            playersScores[currentPlayer] += marbles.pop(currentMarbleIndex)

    playersScores.sort(reverse=True)
    print "Game duration: " + str(datetime.datetime.now() - startTime)
    return playersScores[0]


# +++++++++++++++ SECOND TRY: DEQUE... SOOOOOO FAST!! :-) +++++++++++++++++++++++

def PlayMarbleGameDeque(numPlayers, numMarbles):

    # Play the game!
    startTime = datetime.datetime.now()
    pool = collections.deque(range(1, numMarbles + 1)) # now it's a deque
    playersScores = [0 for i in range(numPlayers)]
    PlayersIterator = itertools.cycle(range(numPlayers))
    marbles = collections.deque([0])  # now it's a deque

    while len(pool) > 0:
        currentPlayer = PlayersIterator.next()
        if pool[0] % 23 != 0:
            marbles.rotate(len(marbles)-1)
            marbles.append(pool.popleft())
        else:
            playersScores[currentPlayer] += pool.popleft()
            marbles.rotate(7)
            playersScores[currentPlayer] += marbles.pop()
            marbles.rotate(-1)

    playersScores.sort(reverse=True)
    print "Game duration: " + str(datetime.datetime.now() - startTime)
    return playersScores[0]


#testString = '10 players; last marble is worth 1618 points'
inputString = open('input_d09.txt').readline()

numPlayers = int(inputString.split(' ')[0])
numMarbles = int(inputString.split(' ')[6])

print "Highscore Part 1 : " + str(PlayMarbleGameDeque(numPlayers, numMarbles))
print "Highscore Part 2 : " + str(PlayMarbleGameDeque(numPlayers, numMarbles*100))