from numpy.random import choice
from fileinput import FileInput
import csv
import random
from datetime import datetime
import shutil
min_prob = .001

#TODO: setup ai moves for X AI to learn from
# try training NEW probabilities with toeBot

class Board:
    
    def draw(self, grid):
        print()
        for i in range(len(grid)):
            if grid[i] == 0:
                temp = i+1
            elif grid[i] == 1:
                temp = 'X'
            else:
                temp = 'O'
            print(temp, end='')  
            print(' ', end='')             
            #print(' ', end='')
            if i % 3 == 2 and i < 8:
                print()
                print("----------")
            elif i < 8:
                print("| ", end='')
        print()
        print()
        print("=======================")
    
    def move(self, grid, player, input, moves):
        if grid[input] == 0:
            grid[input] = player
        else:
            print("error moving player ", end='')
            print(player, end='')
            print(" to ", end='')
            print(input)
            print("moves", end='')
            print(moves)
            print("grid position reads: ", end='')
            print(grid[input])
            exit()  
        moves.append(input)

    def check(self, grid):
        result = 0
        for i in range (3):
            if grid[i] == grid[i+3] == grid[i+6] and grid[i] != 0:
                result = grid[i]
        for i in range(0, 9, 3):
            if grid[i] == grid[i+1] == grid[i+2] and grid[i] != 0:
                result = grid[i]
        if grid[0] == grid[4] == grid[8] and grid[4] != 0:
            result = grid[4]
        if grid[2] == grid[4] == grid[6] and grid[4] != 0:
            result = grid[4]

        full = True
        for i in range(9):
            if grid[i] == 0:
                full = False
                break

        if result == 0 and full == True:
            return 3

        if result != 0:
            print("winner player ", end='')
            print(result)
            return result
        return 0
    
    def train_ai(self, ai, moves):
        # 8/10 times follow best known move, other 2/10 go random (DURING TRAINING ONLY)
        training_decision = random.randint(0,9)
        corners = [0,2,6,8]
        middle = 4
        sides = [1,3,5,7]
        move_num = len(moves)+1
        p1_moves = moves[0::2]
        p2_moves = moves[1::2]
        two_in_a_row = [[0,1],[0,2],[0,4],[0,8],[0,3],[0,6],[1,2],[1,4],[1,7],[1,2],[2,4],[2,6],[2,5],[2,8],[3,4]\
                ,[3,5],[3,6],[5,4],[5,8],[6,7],[6,8],[7,8],[7,4],[6,4],[4,8]]
        winning_3rd = [2,1,8,4,6,3,0,7,4,0,6,4,8,5,5,4,0,3,2,8,7,6,1,2,0]

        # ================= FOR TRAINING O's AI =======================================================
        # if the current ai is p1
        if ai == 1:
            # if its the 20% chance, move randomly
            if training_decision > 8:
                ran = -1
                while ran in moves or ran < 0:
                    ran = random.randint(0,8)
                print("randomly chose " + str(ran))
                return ran
            # if its the 80% make best known move
            else:
                # if you can win
                # check if any of these lists is in p1 moves, if so make a mapped list to the correct output
                for i in range(len(two_in_a_row)):
                    # if the first 2 moves to 3 in a row have been played AND THE 3RD HAS NOT BEEN PLAYED,
                    #  play corresponding 3rd
                    if set(two_in_a_row[i]).issubset(set(p1_moves)) and grid[winning_3rd[i]] == 0:
                        return winning_3rd[i]

                # if you're going to lose
                for i in range(len(two_in_a_row)):
                    if set(two_in_a_row[i]).issubset(set(p2_moves)) and grid[winning_3rd[i]] == 0:
                        return winning_3rd[i]

                # if its your first move
                if move_num == 1:
                    #return middle
                    return random.choice(corners)
                # if its your second move try middle if not corner
                elif middle not in moves:
                    return middle
                # check if corners are available
                elif not set(corners).issubset(moves):
                    ran = -1
                    while ran in moves or ran < 0:
                        ran = random.choice(corners)
                    return ran
                # select a side at random
                else:
                    ran = -1
                    while ran in moves or ran < 0:
                        ran = random.randint(0,8)
                    return ran
        # ======= FOR TRAINING X's AI =======================================
        # if the current ai is player 2
        else:
            # if its the 10% chance, move randomly
            if training_decision > 8:
                ran = -1
                while ran in moves or ran < 0:
                    ran = random.randint(0,8)
                print("randomly chose " + str(ran))
                return ran
            # if its the 90% make best known move
            else:
                # if you can win
                # check if any of these lists is in p1 moves, if so make a mapped list to the correct output
                for i in range(len(two_in_a_row)):
                    # if the first 2 moves to 3 in a row have been played AND THE 3RD HAS NOT BEEN PLAYED,
                    #  play corresponding 3rd
                    if set(two_in_a_row[i]).issubset(set(p2_moves)) and grid[winning_3rd[i]] == 0:
                        #print("returning winning move " + str(winning_3rd[i]))
                        return winning_3rd[i]

                # if you're going to lose
                for i in range(len(two_in_a_row)):
                    if set(two_in_a_row[i]).issubset(set(p1_moves)) and grid[winning_3rd[i]] == 0:
                        #print("preventing lose with move " + str(winning_3rd[i]))
                        return winning_3rd[i]

                # if its your first move try middle if not corner
                if move_num == 2:
                    if middle not in moves:
                        return middle
                    else:
                        return random.choice(corners)
                
                # if he's doing the corners trick choose a side
                if move_num == 4:
                    corner_count = 0
                    for i in corners:
                        if i == 1:
                            corner_count += 1
                    if corner_count == 2:
                        return random.choice(sides)
                    # if he's doing the weird side corner trick do what xkcd says
                    side_count = 0
                    for i in sides:
                        if i == 1:
                            side_count += 1
                    if corner_count == 1 and side_count == 1:
                        if 0 in p1_moves:
                            return 8
                        elif 2 in p1_moves:
                            return 6
                        elif 6 in p1_moves:
                            return 2
                        elif 8 in p1_moves:
                            return 0
                        else:
                            print("mistake in move #4 logic on line 180")
                            exit()
                    else:
                        ran = -1
                        while ran in moves or ran < 0:
                            ran = random.randint(0,8)
                        return ran

                # otherwise choose randomly priorities corner, middle, sides
                else:
                    # check if corners are available
                    if not set(corners).issubset(moves):
                        ran = -1
                        while ran in moves or ran < 0:
                            ran = random.choice(corners)
                        return ran
                    elif middle not in moves:
                        return middle
                    # select a side at random
                    else:
                        ran = -1
                        while ran in moves or ran < 0:
                            ran = random.randint(0,8)
                        return ran
        
    def move_ai(self, grid, ai, weights, moves, z):
        '''
            sum = 0.0

            for i in range(9):
                sum += weights[i]

            if sum < 1.0:
                for i in range(9):
                    if weights[i] != 0.0:
                        weights[i] += (1.0 - sum)
                        break
            elif sum > 1.0:
                for i in range(9):
                    if weights[i] != 0.0:
                        weights[i] -= (sum - 1.0)
                        break  

            for b in range(9):
                if weights[b] < 0:
                    neg_val = weights[b]
                    weights[b] = 0.0
                    max_element = weights.index(max(weights))
                    weights[max_element] += neg_val
                
            for b in range(9):
                if weights[b] > 1.0:
                    excess = weights[b] - 1.0
                    weights[b] = 1.0
                    min_element = weights.index(min(weights))
                    weights[min_element] += excess
        '''

        # if we're training one ai and this is the other, use training algorithm
        if (training == 1 and ai == 2) or (training == 2 and ai == 1):
            decision = self.train_ai(ai, moves) 
            print("training alg returned " + str(decision))
            self.move(grid, ai, decision, moves)
            return
            
        # otherwise use the weights
        else:
            print(weights)
            decision = choice(len(grid), 1, False, weights)
            self.move(grid, ai, decision[0], moves)
            return

    #once working brain can be stored as a tree to avoid linear search
    #result 1 = win 0 = lost

    #also 2 needs training against different first moves, player 1 never tried anything but middle
    def save_weights(self, moves, probs, player, result, incentive):
        if result == 3:
            return 0
        cur_moves = []

        if player < 2:
            start = 0
        else:
            start = 1

        #find first move, update moves prob add next move repeat 
        #also need to account for probs for before any moves have been made (-1)
        for i in range(-1, len(moves)-1):
            #specially assigned for no moves yet
            if i == -1:
                #if start == 0:
                    #line 0 of probs
                    id = 0
                    #index into the line is the first move made +1 to account for id
                    index = moves[0]+1
            else:
                #add another element to cur_moves
                cur_moves.append(moves[i])

                #if its not this players turn, we still want the game id path but don't need to update probs
               # if (start == 0 and i % 2 == 1) or (start == 1 and i % 2 == 0):
               #     continue
                
                #take this portion of the total moves, find it in the file and update the move at that position
                find_id = str(''.join(map(str, cur_moves)))
                id = -1
                for d in range(len(probs)):
                    if probs[d][0] == find_id:
                        id = d
                        break
                if id == -1:
                    print("error in save weights couldnt find probs", end='')
                    print(find_id)
                    exit()

                #switch update prob of NEXT move ie move+1 +1 again because the array starts with the id
                index = int(moves[i+1]+1)

            #probability to switch is the value at to_update +1 because probs[] has id 
            prob_played = probs[id][index]

            #if they won
            if (result == 1 and player < 2) or (result == 2 and player > 1):
               
                new_prob = prob_played * (1+incentive)
                #if the incentive incr prob beyond 1, set it to 1 and diff is whatever that increase was
                if new_prob > 1.0:
                    diff = 1.0 - prob_played
                    new_prob = 1.0
                else:
                    diff = new_prob - prob_played

                #count other probs available to pull from to counter change in prob_played
                other_probs = 0
                for b in range(1,10):
                    #check prob is at least as big as diff/8, if not don't pull from it
                    #added baseline min val for other probs .001
                    if probs[id][b] >= diff/8 and probs[id][b] > min_prob and b != index:
                        other_probs += 1

                #if the values are too small to account for the difference, abandon incentive move on to next move
                if other_probs == 0:
                    print("other probs too small to pull from at", end='')
                    print(probs[id])
                    continue

                #subtract equal portion of the dist lost to the space taken
                for b in range(1,10):
                    #if its bigger than diff/8 and .001 and not index pull from it
                    if probs[id][b] >= diff/8 and probs[id][b] > min_prob and b != index:
                        #subtract an equal portion of the dist lost to taken space   
                        probs[id][b] -= (diff / other_probs) 
                        #now check to see if you pulled too much, if you did, give it back and continue
                        if probs[id][b] < min_prob:
                            #new prob can only take difference between what it was and min_prob
                            new_prob -= (min_prob - probs[id][b])
                            probs[id][b] = min_prob

                #apply new prob to winning move
                probs[id][index] = new_prob

            #if this player lost
            else:        
                new_prob = prob_played * (1-incentive)
                #if the incentive dec prob below 0, set it to 0 and diff is whatever that dec was
                if new_prob < min_prob:
                    diff = prob_played - min_prob
                    new_prob = min_prob
                else:
                    diff = prob_played - new_prob

                #count other probs available to give to, to counter change in prob_played
                other_probs = 0
                for b in range(1,10):
                    #check prob isnt going to be bigger than 1 if given diff/8    V and this element hasn't already been played
                    if probs[id][b] <= 1 - (diff/8) and b != index and b-1 not in cur_moves:
                        other_probs += 1

                #if the values are to close to 1 to account for the difference, abandon incentive move on to next move
                if other_probs == 0 or diff == 0:
                    print("other probs too large to give to or diff = 0", end='')
                    print(probs[id])
                    continue

                #add equal portion of the dist given to the space taken
                for b in range(1,10):
                    # B REFLECTS +1 ADJUSTED ARRAY FOR PROBS WITH ID IN THE FRONT
                    # CUR_MOVES POSITIONS ARE 0 BASED SO NEED TO -1 FROM B HERE AND ABOVE
                    #if its bigger than diff/8 and not index pull from it AND INSTEAD OF 0 JUST MAKE SURE NOT ONE OF PLAYED MOVES
                    if probs[id][b] <= 1 - (diff/8) and b != index and b-1 not in cur_moves:
                        #give an equal portion of the penalty back to the other probs   
                        probs[id][b] += (diff / other_probs) 
                        #now check to see if you gave too much, if you did, give it back and continue
                        if probs[id][b] > 1.0:
                            excess = probs[id][b] - 1.0
                            probs[id][b] = 1.0
                            new_prob += excess
                #apply new prob to winning move
                probs[id][index] = new_prob

            #check that new weights sum to 1.0
            weight_check = probs[id].copy()
            weight_check.pop(0)
            total = sum(weight_check)
            if total < 1.0:
                probs[id][index] += (1.0 - total)
            elif total > 1.0:
                probs[id][index] -= (total - 1.0)

        '''
            if sum(probs[id]) > 1.0:
                biggest = max(probs[id])
                probs[id][biggest] -= sum(probs[id]) - 1.0
            elif sum(probs[id]) < 1.0:
                min_nzero = 0
                for f in range(1,9):
                    if probs[id][f] != 0 and probs[id][f] < probs[id][min_nzero]:
                        min_nzero = f
                probs[id][min_nzero] += 1.0 - sum(probs[id])

            if sum(probs[id]) != 1.0:
                print("what the fuck on line 251")
                exit()
        '''
        #update total games
        total_games_int = int(probs[623530][0])
        total_games_int += 1
        probs[623530][0] = str(total_games_int)
        if player < 2 and result == 1:
            #update wins in probs
            probs[623530][1] += 1
        elif player > 1 and result == 2:
            probs[623530][2] += 1
        return 0

    def load_weights(self, moves, probs, incentive):
        new_weights = []
        #if no moves have been made yet
        if not moves:
            index = 0
        else:
            id = str(''.join(map(str, moves)))
            index = -1
            for i in range(len(probs)):
                if probs[i][0] == id:
                    index = i
                    break
            if index == -1:
                print("error couldn't find/load weights")
                exit()
        new_weights = probs[index].copy()
        new_weights.pop(0)
        
        '''    
            #check that new weights sum to 1.0
            total = sum(new_weights)
            if total < 1.0:
                diff = 1.0 - total
                for e in range(9):
                    if new_weights[e] <= 1.0 - diff and new_weights[e] > 0:
                        new_weights[e] += (diff)
                        probs[index][e+1] += (diff)
                        break
                    elif e == 8:
                        print("couldn't find value to make up diff in load weights check sum of probs")
                        print(probs[index])
                        exit()

            elif total > 1.0:
                diff = total - 1.0
                for e in range(9):
                    if new_weights[e] >= diff and new_weights[e] + diff <= 1.0:
                        new_weights[e] -= (diff)
                        probs[index][e+1] -= (diff)
                        break
                    elif e == 8:
                        print("couldn't find value to make up diff in load weights check sum of probs")
                        print(probs[index])
                        exit()
        '''
        return new_weights
    
    #takes an empty list and player # and fills it with file contents
    def read_file(self, player, probs): 
        if player == 1:
            fp = open("probs1.txt", 'r')
        elif player == 2:
            fp = open("probs2.txt", 'r')
        else:
            print("player not 1 or 2")
            fp.close()
            return -1
        
        i = 0
        for line in fp:
            words = line.split(',')
            newline = ['-1', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            newline[0] = str(words[0])
            for j in range(len(words)-1):
                newline[j+1] = float(words[j+1])
            probs.append(newline)
            i += 1
        fp.close()
        return 0

    #writes probs out to file including last_line #games,p1_w,p2_w also inc graph
    def write_file(self, player, probs, graph):
        if player == 1:
            fp = open("probs1.txt", 'w+')
        elif player == 2:
            fp = open("probs2.txt", 'w+')
        else:
            print("player not 1 or 2")
            fp.close()
            return -1

        for line in probs:
            fp.write(line[0])
            for j in range(len(line)-1):
                fp.write(',' + str(line[j+1]))
            fp.write('\n')

        fp.close()
        return 0

# ============= GLOBAL SETUP ==============================================
board = Board()
incentive = .1
probs1 = []
probs2 = []
p1 = 0
p2 = 0
graph = []
p1_wins = 0
p2_wins = 0
ties = 0
training = 0

#choose players
answer = str(input("Is player 1 human y/n: "))
if answer == 'y':
    p1 = 1
else:
    p1 = 0
answer = str(input("Is player 2 human y/n: "))
if answer == 'y':
    p2 = 3 
else:
    p2 = 2
num_games = int(input("How many games to play: "))

#load probs from file
if p1 == 0:
    if board.read_file(1, probs1) != 0:
        print("error reading prob file 1")
        exit()

if p2 == 2:
    if board.read_file(2, probs2) != 0:
        print("error reading prob file 2")
        exit()

#retrieve last item from graph
with open('graph.txt') as f:
    for line in f:
        values = line.split(',')
        graph.append(int(values[-1]))
        break

# ===================== GAME LOOP =============================

for z in range(num_games):
    #setup every game
    weights = [.111] * 9
    grid = [0] * 9
    moves = []
    result = 0

    board.draw(grid)

    #while no winner
    while(result == 0):
        
        #player 1 move
        if p1 == 1:
            p1_move = -1
            while(p1_move < 1 or p1_move > 9):
                p1_move = int(input("choose move: "))
            board.move(grid, p1, p1_move-1, moves)
        else:
            weights = board.load_weights(moves, probs1, incentive)
            board.move_ai(grid, 1, weights, moves, z)
        board.draw(grid)

        #check for winner
        if (len(moves) >= 5):
            result = board.check(grid)
            if (result != 0):
                break

        #player 2 move
        if p2 == 3:
            p2_move = -1
            while(p2_move < 1 or p2_move > 9):
                p2_move = int(input("choose move: "))
            board.move(grid, 2, p2_move-1, moves)
        else:
            weights = board.load_weights(moves, probs2, incentive)
            board.move_ai(grid, 2, weights, moves, z)
        board.draw(grid)

        #check for winner
        if (len(moves) >= 5):
            result = board.check(grid)
            if (result != 0):
                break
    
    #save weights
    if p1 == 0:
        print("player 1 learning from game ", end='')
        print(moves, end='')
        print("...", end='')
        if board.save_weights(moves, probs1, p1, result, incentive) != 0:
            print("error saving weights ", end='')
            print(moves)
            exit()
        print("done.")
    if p2 == 2:
        print("player 2 learning from game ", end='')
        print(moves, end='')
        print("...", end='')
        if board.save_weights(moves, probs2, p2, result, incentive) != 0:
            print("error saving weights ", end='')
            print(moves)
            exit()
        print("done.")
    
    #append graph
    if result == 1:
        graph.append(graph[-1]+1)
        p1_wins += 1
    elif result == 2:
        graph.append(graph[-1]-1)
        p2_wins += 1
    else:
        graph.append(graph[-1])
        ties += 1

# ============ write probs to file ==========================
print("writing out probabilties to file...", end='')
if p1 == 0:
    if board.write_file(1, probs1, graph) != 0:
        print("error writing to file")
if p2 == 2:
    if board.write_file(2, probs2, graph) != 0:
        print("error writing to file")
print("done.")

#write out graph to file
fp = open("graph.txt", 'a')
for i in range(len(graph)):
    fp.write(',' + str(graph[i]))
fp.close()

fp = open("tally.txt", 'a')
fp.write("p1 wins: " + str(p1_wins) + '\n')
fp.write("p2 wins: " + str(p2_wins) + '\n')
fp.write("ties: " + str(ties) + '\n' + '\n')




