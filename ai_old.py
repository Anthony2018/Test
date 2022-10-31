import time
import random 
import io

class key:
    def key(self):
        return "10jifn2eonvgp1o2ornfdlf-1230"

class ai:
    def __init__(self):
        pass
        # self.f = open('time.txt', 'a')
        # self.f.truncate()
        # self.f.close()

    class state:
        def __init__(self, a, b, a_fin, b_fin):
            self.a = a
            self.b = b
            self.a_fin = a_fin
            self.b_fin = b_fin

        '''
        This is the function to get the next state after we/the opponent take the next move.
        It is the same as the updateLocalState function in main.py
        :param: move - int, the next move we/ the opponent will take; opposite - bool, True if the opponent takes the
                move, False if we take the move.
        :returns: cagain - bool, if the player can move again; new_state - state, the next state after that move
        '''
        def nextState(self, move, opposite):
            a = self.a
            b = self.b
            a_fin = self.a_fin
            b_fin = self.b_fin
            if opposite:
                # swap
                a = self.b
                b = self.a
                a_fin = self.b_fin
                b_fin = self.a_fin
            ao = a[:]
            all = a[move:] + [a_fin] + b + a[:move]
            count = a[move]
            all[0] = 0
            p = 1
            while count > 0:
                all[p] += 1
                p = (p + 1) % 13
                count -= 1
            a_fin = all[6 - move]
            b = all[7 - move:13 - move]
            a = all[13 - move:] + all[:6 - move]
            cagain = bool()
            ceat = False
            p = (p - 1) % 13
            if p == 6 - move:
                cagain = True
            if p <= 5 - move and ao[move] < 14:
                id = p + move
                if (ao[id] == 0 or p % 13 == 0) and b[5 - id] > 0:
                    ceat = True
            elif p >= 14 - move and ao[move] < 14:
                id = p + move - 13
                if (ao[id] == 0 or p % 13 == 0) and b[5 - id] > 0:
                    ceat = True
            if ceat:
                a_fin += a[id] + b[5 - id]
                b[5 - id] = 0
                a[id] = 0
            if sum(a) == 0:
                b_fin += sum(b)
            if sum(b) == 0:
                a_fin += sum(a)
            new_state = ai.state(a, b, a_fin, b_fin)
            if opposite:
                # reverse a and b
                new_state = ai.state(b, a, b_fin, a_fin)

            return cagain, new_state

        '''
        This is the heuristic function
        :param: self
        :returns: float, the examine scores of the current state.
        '''
        def heuristic(self):
            # h1 is the current score of a - score of b, and the current stones held by a - the current stones held by b
            h1 = self.a_fin - self.b_fin + sum(self.a) * 0.5 - sum(self.b) * 0.5
            # h2 is the stones a can eat
            h2 = 0
            for i in range(6):
                if self.a[i] % 13 + i <= 5:
                    if self.a[self.a[i] % 13 + i] == 0 or self.a[i] % 13 == 0:
                        h2 += 1 + self.b[5 - (self.a[i] % 13 + i)]
                elif 0 <= self.a[i] % 13 - (13 - i) <= 5:
                    if self.a[self.a[i] % 13 - (13 - i)] == 0:
                        h2 += 1 + self.b[5 - (self.a[i] % 13 - (13 - i))]
                # if self.b[i] % 13 + i <= 5:
                #     if self.b[self.b[i] % 13 + i] == 0 or self.b[i] % 13 == 0:
                #         h2 -= 1 + self.a[5 - (self.b[i] % 13 + i)]
                # elif 0 <= self.b[i] % 13 - (13 - i) <= 5:
                #     if self.b[self.b[i] % 13 - (13 - i)] == 0:
                #         h2 -= 1 + self.a[5 - (self.b[i] % 13 - (13 - i))]
            # 37 is the winning score, if a wins, the heuristic should be very large, verse visa.
            if self.a_fin >= 37:
                return 1000 + h1
            if self.b_fin >= 37:
                return -1000 + h1
            return 0.8*h1 + 0.2*h2


    # Kalah:
    #         b[5]  b[4]  b[3]  b[2]  b[1]  b[0]
    # b_fin                                         a_fin
    #         a[0]  a[1]  a[2]  a[3]  a[4]  a[5]
    # Main function call:
    # Input:
    # a: a[5] array storing the stones in your holes
    # b: b[5] array storing the stones in opponent's holes
    # a_fin: Your scoring hole (Kalah)
    # b_fin: Opponent's scoring hole (Kalah)
    # t: search time limit (ms)
    # a always moves first
    #
    # Return:
    # You should return a value 0-5 number indicating your move, with search time limitation given as parameter
    # If you are eligible for a second move, just neglect. The framework will call this function again
    # You need to design your heuristics.
    # You must use minimax search with alpha-beta pruning as the basic algorithm
    # use timer to limit search, for example:
    # start = time.time()
    # end = time.time()
    # elapsed_time = end - start
    # if elapsed_time * 1000 >= t:
    #    return result immediately 
    def move(self, a, b, a_fin, b_fin, t):
        # #For test only: return a random move
        # self.f = open('time.txt', 'a')
        # r = []
        # for i in range(6):
        #     if a[i] != 0:
        #         r.append(i)
        # # To test the execution time, use time and file modules
        # # In your experiments, you can try different depth, for example:
        # # f = open('time.txt', 'a') #append to time.txt so that you can see running time for all moves.
        # # Make sure to clean the file before each of your experiment
        # for d in [3, 5, 7]: #You should try more
        #     self.f.write('depth = '+str(d)+'\n')
        #     t_start = time.time()
        #     self.minimax(depth = d)
        #     self.f.write(str(time.time()-t_start)+'\n')
        # self.f.close()
        # return r[random.randint(0, len(r)-1)]
        # #But remember in your final version you should choose only one depth according to your CPU speed (TA's is 2.0GHz)
        # #and remove timing code.

        #Comment all the code above and start your code hereS
        state = ai.state(a, b, a_fin, b_fin)
        # self.f = open('time.txt', 'a')
        depth = 6
        # self.f.write('depth = ' + str(depth) + '\n')
        # t_start = time.time()
        r = self.minimax(state, depth=depth)
        # self.f.write(str(time.time()-t_start)+'\n')
        # self.f.close()
        return r

    # calling function
    '''
    Doing the minimax search, find the optimized choice
    :param state - the original state; depth - int, the maximum depth of our search
    :returns move - int, the optimized move we should make
    '''
    def minimax(self, state, depth):
        # example: doing nothing but wait 0.1*depth sec
        # time.sleep(0.1*depth)
        move, v = self.max_value(state, float('-inf'), float('inf'), depth)
        return move

    '''
    This is our turn
    :param state - the current state; alpha - the max value along the previous path; beta: the min value along the 
           previous path; depth - current depth
    :returns move - int, the optimized move to make the max value; v - float, the max value
    '''
    def max_value(self, state, alpha, beta, depth):
        move = None
        # if the depth is 0 or we can no longer move.
        if not depth or self.is_terminal(state):
            return move, state.heuristic()
        v = float('-inf')
        for m in range(6):
            if not state.a[m]:
                continue
            cagain, new_state = state.nextState(m, False)
            if not cagain:
                # To the opponent's turn, depth - 1
                t, next_v = self.min_value(new_state, alpha, beta, depth-1)
                if next_v > v:
                    v = next_v
                    move = m
            else:
                # Get another bonus turn, depth keeps the same
                t, next_v = self.max_value(new_state, alpha, beta, depth)
                if next_v > v:
                    v = next_v
                    move = m
            # beta cutoff
            if v >= beta:
                return move, v
            # update alpha
            alpha = max(alpha, v)
        return move, v

    '''
    This is the opponent's turn
    :param state - the current state; alpha - the max value along the previous path; beta: the min value along the 
           previous path; depth - current depth
    :returns move - int, the optimized move to make the min value; v - float, the min value
    '''
    def min_value(self, state, alpha, beta, depth):
        move = None
        if not depth or self.is_terminal(state):
            return move, state.heuristic()
        v = float('inf')
        for m in range(6):
            if not state.a[m]:
                continue
            cagain, new_state = state.nextState(m, True)
            if not cagain:
                # To our turn, depth - 1
                t, next_v = self.max_value(new_state, alpha, beta, depth-1)
                if next_v < v:
                    v = next_v
                    move = m
            else:
                # Opponent gets bonus turn, depth keeps unchanged
                t, next_v = self.min_value(new_state, alpha, beta, depth)
                if next_v < v:
                    v = next_v
                    move = m
            # alpha cut off
            if v <= alpha:
                return move, v
            # update beta
            beta = min(beta, v)
        return move, v

    '''
    To check if the state is the terminal
    :param state - the current state
    :returns True if it's terminal
    '''
    def is_terminal(self, state):
        if (not sum(state.b)) or (not sum(state.a)) or state.a_fin >= 37 or state.b_fin >= 37:
            # if no stones are in a's hole or b's hole or someone already wins
            return True
        return False
if __name__ == "__main__":
    test = ai()
    ## test 1: player
    a = [6,6,6,6,6,6]
    b = [6,6,6,6,6,6]
    a_fin = 0
    b_fin = 0
    ## test 2: op
    a = [6,6,6,6,6,6]
    b = [6,6,6,6,6,6]
    a_fin = 0
    b_fin = 0
    ## test 3: eat
    a = [0,0,11,0,7,0]
    b = [6,6,6,6,6,6]
    a_fin = 0
    b_fin = 0
    s0 = test.state(a, b, a_fin, b_fin)
    bouns, s = s0.nextState(2, False)
    # print(bouns,s.a,s.b,s.a_fin,s.b_fin)
    # s0 = test.state(a, b, a_fin, b_fin)
    # print(s0.heuristic())
    s0 = test.state(a, b, a_fin, b_fin)
    print(test.minimax(s0,0))



