#!/usr/bin/python3
"""N queens on a chess board without killing each other?
"""
import sys


def main(N):
    """Main fucntion returning the combinations
    """
    combs = []
    for i in range(N):
        for j in range(N):
            combs.append([i, j])
    valids = []
    current = []
    invalids = []
    j = 1
    trials = 0
    while j < N-1:  # start [0,1], then [0,2], etc ..
        valid = [[0, j]]
        i = 0
        rounds = 0
        while len(valid) < N and i < len(combs) and rounds < N * 2:
            curr = combs[i]
            validity = True
            for queen in valid:
                # Not mirror image
                cond1 = not(queen[1] == curr[0] and queen[0] == curr[1])
                # Not on same diagonal
                cond2 = not(abs(queen[1] - curr[1]) == abs(queen[0] - curr[0]))
                # Not on main diagonal
                cond3 = not((queen[1] == queen[0]))
                cond3 = True
                # Not on same row with any element in valid
                cond4 = not (queen[1] == curr[1])
                # Not on same column as any element in valid
                cond5 = not (queen[0] == curr[0])
                # adhoc (*if [0,1] starts no even [2,0], [4,0], but [3,0] ,etc
                cond6 = not(queen[1] == 0 and (queen[0] % 2) == (j % 2))
                cond6 = True
                if cond1 and cond2 and cond3 and cond4 and cond5 and cond6:
                    pass
                else:
                    validity = False
            if validity:
                valid.append(curr)
            i = i + 1
            if i == len(combs) and rounds < N*2:
                i = 0
                rounds += 1
        if len(valid) == N:
            valids.append(valid)
            j = j + 1
        # reinitiliaze initials (invalids tracking would replace backtracking?)
            invalids = []
        else:
            if valid:
                value = valid.pop()
                if not(value in invalids):
                    invalids.append(value)
            trials += 1

            if trials == 3:
                trials = 0
                j += 1
            print("i, j ", i, j)
            print("invalids ", invalids)
            print("valids ", valids)

        valid = []
    return valids


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
        if N >= 4:
            queenset = main(N)
            if queenset:
                for a in queenset:
                    print(a)
        else:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
