#sudoku solver, not the best one in the world but it does some stuff
#so far implemented:
# rules of sudoku
# hidden singles (a number only has one possible position in a row, column, or box)
# naked pairs / triples (two cells (that see each other) only have the same two numbers as possibilities, 
# so those possibilities can be removed from other cells in their row/column/box, or three cells and three numbers for triples)
# bifurcation (which is disabled by default) (basically just guess and check)
#goal: solve all of the sudokus on the project euler questions without bifurcation 
# i should prettify this so i can toss it into my resume or something
from os import remove
import functions as f
import math as m
import itertools as it
def init_args():
    return [None, False, 0, [], [], []]
DEBUG = False
args = init_args()
def show_board(board):
    print("-" * 30)
    for row in board:
        print(row)
    print("-" * 30)

def basic_update_poss_board(board, poss_board):
    '''returns new poss_board, set old poss_board = to this function'''
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for possibility in poss_board[i][j]:
                    board[i][j] = int(possibility)
                    if check_broken(board):
                        poss_board[i][j] = poss_board[i][j].replace(possibility,'')
                    board[i][j] = 0
            else:
                poss_board[i][j] = ""
    return poss_board

def box_row_reduction(poss_board):
    for num in range(1,10):
        #iterate over each box
        for big_row in range(3):
            for big_col in range(3):
                box_coords = []
                for small_row in range(3):
                    for small_col in range(3):
                        new_coord = (big_row * 3 + small_row, big_col * 3 + small_col)
                        box_coords.append(new_coord)
                possible_locations_of_num = []
                for coord in box_coords:
                    i,j = coord
                    if str(num) in poss_board[i][j]:
                        possible_locations_of_num.append(coord)
                #check possible locations to see if they are all in same row or same column
                if len(possible_locations_of_num) > 0:
                    row_check = possible_locations_of_num[0][0]
                    col_check = possible_locations_of_num[0][1]
                    if all([coord[0] == row_check for coord in possible_locations_of_num]):
                        #all same row (row_check)
                        if DEBUG: #bad practice, fix later
                            print(f"box row reduce number {num} on row {row_check} by box {big_row * 3 + big_col}")
                        for j in [x for x in range(9) if x // 3 != big_row]:
                            poss_board[row_check][j] = poss_board[row_check][j].replace(str(num), '')

                    elif all([coord[1] == col_check for coord in possible_locations_of_num]):
                        #all same col (col_check)
                        if DEBUG: #bad practice, fix later
                            print(f"box column reduce number {num} on column {col_check} by box {big_row * 3 + big_col}")
                        for i in [x for x in range(9) if x//3 != big_col]:
                            poss_board[i][col_check] = poss_board[i][col_check].replace(str(num), '')
    return poss_board

def copy_board(board):
    out = []
    for row in board:
        new_row = []
        for cell in row:
            new_row.append(cell)
        out.append(new_row)
    return out

def check_dupes(nine_nums):
    non_emptys = []
    for num in nine_nums:
        if num in non_emptys:
            return True
        if num != 0:
            non_emptys.append(num)
    return False

def check_broken(board):
    #checking if rows share the same digit
    for row in board:
        if check_dupes(row):
            return True
    #checking if columns share the same digit
    for i in range(9):
        col = []
        for j in range(9):
            col.append(board[j][i])
        if check_dupes(col):
            return True
    #checking if boxes share the same digit
    for i in range(9):
        box = []
        big_row = i // 3
        big_col = i % 3
        for j in range(9):
            small_row = j // 3
            small_col = j % 3
            sudoku_row = big_row * 3 + small_row
            sudoku_col = big_col * 3 + small_col
            box.append(board[sudoku_row][sudoku_col])
        if check_dupes(box):
            return True

def is_naked_possibility_subset_of(small_string,big_string):
    for c in small_string:
        if c not in big_string:
            return False
    return True

#this will operate on naked pairs and triples to start
#naked pairs and triples are simply locked sets of size 2 and 3 respectively
#a locked set is N cells *that all see each other* with N possible values
def naked_locked_set_finder(poss_board, coords, set_size, already_found_locked_set_coords):
    '''This will return all naked locked sets of size (set_size) in the nine_coords.
    This means it will return a list containing all the strings of length (set_size)
    which are the possible values of a locked set.
    It will NOT edit either the board or the poss_board.
    coords is a list of 2-tuples of coordinates in the sudoku board.'''
    locked_sets = []
    nine_list = []
    for coord_pair in coords:
        if coord_pair not in already_found_locked_set_coords:
            i,j = coord_pair
            poss_string = poss_board[i][j]
            if poss_string != "":
                nine_list.append(coord_pair)
    for combo in it.combinations("123456789",set_size):
        subset_counter = 0
        for coord_pair in nine_list:
            i,j = coord_pair
            if is_naked_possibility_subset_of(poss_board[i][j], combo):
                subset_counter += 1
        if subset_counter == set_size:
            locked_sets.append(combo)
    return locked_sets

def hidden_locked_set_finder(poss_board, coords, set_size, already_found_locked_set_coords):
    locked_sets = []
    nine_coord_list = []
    poss_space = [] # do not get fucked over by off-by-ones, you will hate yourself and the world and everything
    for i in range(9):
        poss_space.append("")
    for coord_pair in coords:
        if coord_pair not in already_found_locked_set_coords:
            i,j = coord_pair
            poss_string = poss_board[i][j]
        if len(poss_string) != 0:
            nine_coord_list.append(coord_pair)
            for num in range(1,10):
                if str(num) in poss_string:
                    poss_space[num - 1] += len(nine_coord_list) - 1
    #so... now things are just like finding naked triples, but i have to remember to use list indices as nums and list entries as coords
    for combo in it.combinations("123456789",set_size):
        subset_counter = 0


def remove_possibilities_based_on_naked_locked_sets(poss_board,coords,cell):
    '''returns the new poss_board, set old poss_board = to this function'''
    locked_set_coords = []
    for coord_pair in coords:
        i,j = coord_pair 
        if is_naked_possibility_subset_of(poss_board[i][j],cell):
            locked_set_coords.append(coord_pair)
    #cells are located, now we remove these two numbers from all others in row/col/box
    invalid_nums = [x for x in cell]
    for coord_pair in locked_set_coords:
        coords.remove(coord_pair)
    for coord_pair in coords:
        i,j = coord_pair
        poss_board[i][j] = "".join([x for x in poss_board[i][j] if x not in invalid_nums]) #what the actual fuck is this line lmao
    return poss_board, locked_set_coords

def modify_args(index, data, mode = "replace"):
    global args
    #index table: 
    # 0 = poss_board / the board containing all of the possibilities for each cell
    # 1 = allow_bifurcation / should the computer solve by bifurcation, or "guess and check"
    # 2 = steps_taken / how many times has the program iterated through already
    # 3 = row_locked_set_coords / a list containing the coordinates of all locked sets (in rows only)
    # 4 = col_locked_set_coords / see (3), but for columns
    # 5 = box_locked_set_coords / see (3), but for boxes
    if mode == "replace":
        args[index] = data
    #DO NOT USE THIS MODE WITH NON-LIST ARGUMENTS/DATA
    if mode == "add":
        arg_to_modify = args[index]
        for element in data:
            arg_to_modify.append(element)
        args[index] = arg_to_modify


def solve_board(board):
    global args
    debug = DEBUG
    if debug:
        show_board(board)
    poss_board = args[0]
    allow_bifurcation = args[1]
    steps_taken = args[2]
    row_locked_set_coords = args[3]
    col_locked_set_coords = args[4]
    box_locked_set_coords = args[5]
    PERMITTED_STEPS = 10000
    if steps_taken >= PERMITTED_STEPS:
        print("too many steps")
        return None
    if board == None:
        return None
    # returns the solved board if all cells are filled in
    # the plan is to otherwise recurse through by making one edit to the board at a time
    complete = not check_broken(board)
    if check_broken(board):
        if debug:
            print("board is broken")
        return board

    for row in board:
        if not complete:
            break
        for number in row:
            if number == 0:
                complete = False
                break
    if complete:
        if debug:
            print("board is complete")
        return board
    #generate possibility board:
    #i.e. a 9x9 board, which has strings containing digits 1-9
    #if the number can go there on the sudoku board (no number of the same sees it)
    #then it's added to the possiblity board
    #it's not too slow, don't worry
    if poss_board == None:
        poss_board = []
        for i in range(9):
            init_row = []
            for j in range(9):
                init_row.append("")
            poss_board.append(init_row)
        for num in range(1, 10):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == 0:
                        board[i][j] = num
                        if not check_broken(board):
                            poss_board[i][j] += str(num)
                        board[i][j] = 0
    else:
        poss_board = basic_update_poss_board(board,poss_board)
    modify_args(0, poss_board)
    #RULES OF SUDOKU
    #(Naked Single), if there's only one possibility for a square then obviously that's what the square is
    #next, check if any of them are length 1, and if they are, set the number to that number and return solve_board on that
    for i in range(9):
        for j in range(9):
            possibilities = poss_board[i][j]
            if len(possibilities) == 1:
                board[i][j] = int(possibilities)
                modify_args(2, steps_taken + 1)
                if debug:
                    print("rules of sudoku")
                    print(possibilities + " found at cell (" + str(i) + "," + str(j) + ")")
                return solve_board(board)
    #HIDDEN SINGLES
    #ok, now we want to see if there's only one possible occurrence of a number in a row, col, or box
    #like, if 1 has only one spot it can go in a column, then it has to be there, 
    #because all rows, cols, and boxes contain the numbers 1-9
    for num in range(1,10):
        #rows first
        for i in range(9):
            finds = 0
            j_coord = -1
            for j in range(9):
                if str(num) in poss_board[i][j]:
                    finds += 1
                    j_coord = j
            if finds == 1:
                board[i][j_coord] = num
                modify_args(2, steps_taken + 1)
                if debug:
                    print("hidden singles: row")
                    print(str(num) + " found at cell (" + str(i) + "," + str(j_coord) + ")")
                return solve_board(board)
        for i in range(9):
            finds = 0 
            j_coord = -1
            for j in range(9):
                if str(num) in poss_board[j][i]:
                    finds += 1
                    j_coord = j
            if finds == 1:
                board[j_coord][i] = num
                modify_args(2, steps_taken + 1)
                if debug:
                    print("hidden singles: column")
                    print(str(num) + " found at cell (" + str(j_coord) + "," + str(i) + ")")
                return solve_board(board)
        #boxes third
        for i in range(9):
            box = []
            big_row = i // 3
            big_col = i % 3
            for j in range(9):
                small_row = j // 3
                small_col = j % 3
                sudoku_row = big_row * 3 + small_row
                sudoku_col = big_col * 3 + small_col
                box.append([sudoku_row,sudoku_col])
            finds = 0
            edit_coords = [-1,-1]
            for coords in box:
                i = coords[0]
                j = coords[1]
                if str(num) in poss_board[i][j]:
                    finds += 1
                    edit_coords = coords
            if finds == 1:
                board[edit_coords[0]][edit_coords[1]] = num
                modify_args(2, steps_taken + 1)
                if debug:
                    print("hidden singles: box")
                    print(str(num) + " found at cell (" + str(edit_coords[0]) + "," + str(edit_coords[1]) + ")")
                return solve_board(board)

    #NAKED PAIRS (works) AND TRIPLES (works) AND QUADS (works) 
    #next, we want to notice pairs/triples in rows/cols/boxes
    #imagine a row where there are two boxes that can both only be 2 or 5. 
    #then it's no longer possible for any other cell in that row to be 2 or 5, because then the sudoku would break
    #if we can spot those it'll help a lot i think 
    #ideally the code will spot this generally (if there are three cells that can only be 2,3,5, etc.) THIS WORKED
    #maybe it will even be integrated with the 1 possibility case(although i don't want to break that for now)
    #also, it doesn't fit in as the same sudoku technique so i'll keep it separate (like andrew's solver)
    #this should really be put into a function to clean up the code, there's a lot of duplicated effort
    #PROBLEM: even if a locked set is found, it will simply be found over and over again until the recursion limit is reached
    #possible solutions: we could keep a list of all coordinates of locked sets. This has some issues (if a locked set has an effect on a box and a row/col, 
    #the LS will not act on the box, because it won't get a chance to iterate on it)
    #we could keep track within rows, columns, and boxes separately, but that seems lame
    #it will also snowball the more techniques that i add, requiring more and more lists for each technique to stop it
    #i could create an (args) list for solve_board, and create a function that can edit that more simply
    #that would probably be best practice
    #rows first
    for i in range(9):
        poss_row = []
        for j in range(9):
            poss_row.append((i,j))
        for size in range(2,5):
            for cell in naked_locked_set_finder(poss_board,poss_row,size,args[3]):
                poss_board, new_locked_set_coords = remove_possibilities_based_on_naked_locked_sets(poss_board,poss_row,cell)
                modify_args(0,poss_board)
                modify_args(2, steps_taken + 1)
                modify_args(3,new_locked_set_coords,"add")
                if debug: 
                    print("locked set: row " + str(i) + ", nums = " + str(cell) + ", size = " + str(size))
                return solve_board(board)
    #cols second
    for i in range(9):
        poss_col = []
        for j in range(9):
            poss_col.append((j,i))
        for size in range(2,5):
            for cell in naked_locked_set_finder(poss_board,poss_col,size,args[4]):
                poss_board, new_locked_set_coords = remove_possibilities_based_on_naked_locked_sets(poss_board,poss_col,cell)
                modify_args(0,poss_board)
                modify_args(2, steps_taken + 1)
                modify_args(4,new_locked_set_coords,"add")
                if debug: 
                    print("locked set: column " + str(i) + ", nums = " + str(cell) + ", size = " + str(size))
                return solve_board(board)
    #boxes third
    for i in range(9):
        poss_box = []
        big_row = i // 3
        big_col = i % 3
        for j in range(9):
            small_row = j // 3
            small_col = j % 3
            sudoku_row = big_row * 3 + small_row
            sudoku_col = big_col * 3 + small_col
            poss_box.append((sudoku_row,sudoku_col))
        for size in range(2,5):
            for cell in naked_locked_set_finder(poss_board,poss_box,size,args[5]):
                poss_board, new_locked_set_coords = remove_possibilities_based_on_naked_locked_sets(poss_board,poss_box,cell)
                modify_args(0,poss_board)
                modify_args(2, steps_taken + 1)
                modify_args(5,new_locked_set_coords,"add")
                if debug: 
                    print("locked set: box (" + str(big_row) + "," + str(big_col) + "), nums = " + str(cell) + ", size = " + str(size))
                return solve_board(board)
    #HIDDEN PAIRS AND TRIPLES
    #this is similar to naked pairs and triples, but slightly different.
    #imagine a row, where there are two boxes which are the only two places in the row that 2 and 5 can go in
    #that means those two squares are another locked set, where 2 and 5 are the only numbers that can go there.
    #this causes eliminations of possiblities in the same way that naked pairs/triples do
    #detecting these is harder, but once i find them i can use mostly the same code from the remove_possibilities_based_on_naked_locked_sets function
    #the plan is most likely to find all the coordinates for each possibility (1 can go in positions 0, 1, 4, 5) for example
    #then run the naked locked set finder on the coordinates, and use that output as the coords in the row/col/box
    #this works p well, but i'd also need to keep track of the index in the naked locked set finder
    #will probably need to write a new function???
    #as standard, rows first
    for i in range(9):
        poss_coords_row = []
        poss_row = []
        for j in range(9):
            poss_row.append((i,j))
    
    #BOX ROW REDUCTION
    #sometimes, there are only two places a digit can go in a specific box, which happen to be along the same row or column.
    #in this case, we know that the digit cannot appear anywhere else in the row/column
    #otherwise the digit would not be placeable in that box
    #have to iterate over each box, and check each individual row column pair i suppose
    poss_board = box_row_reduction(poss_board)
    #------------------------------------------------------------------------------------
    #then we'll see how far this gets us i guess
    #i want to get the solver to be able to solve all of them without needing bifurcation
    #so i'm adding a variable that can turn it on or off
    #BIFURCATION
    #so this is the technique that computers are good at, but is incredibly boring
    #essentially, the computer picks a cell that has not yet been filled
    #it then guesses a possible number for that cell and sees what new cells it can fill in
    #if this leads to a broken puzzle state, then the puzzle resets and guesses the next possible number
    #it does this until one of those numbers gives the correct solution
    #there's no logic required, however you can't solve a puzzle with only bifurcation because it's too intensive on memory(too many paths)
    #so some basic sudoku logic is also required, but just naked singles and basic sudoku rules are enough to remedy this problem
    if allow_bifurcation:
        for i in range(9):
            for j in range(9):
                poss_string = poss_board[i][j]
                if debug:
                    print("bifurcating on " + str(i) + str(j))
                saved_board = copy_board(board)
                for c in poss_string:
                    if debug:
                        print("guessing " + c)
                    args = init_args()
                    args[2] = steps_taken
                    attempt = int(c)
                    board[i][j] = attempt
                    modify_args(2,steps_taken + 1)
                    x = solve_board(board)
                    if x != None and not check_broken(x):
                        print("the one below was bifurcated")
                        return x
                    else:
                        if debug:
                            print("guess " + c + " didn't work")
                        board = copy_board(saved_board)
                        args = init_args()
    if debug:
        print("no technique worked")
    return None #technically i don't need to do this but i'm just making sure i remember
    
def main():
    global args
    test_file = open("p096_test.txt")
    test_board = []
    for j in range(10):
        test_line = test_file.readline()
        if j != 0:
            test_row = [int(c) for c in test_line[:9]]
            test_board.append(test_row)
    sudoku_file = open("p096_sudoku.txt")
    boards = []
    for i in range(50):
        new_board = []
        for j in range(10):
            sudoku_line = sudoku_file.readline()
            if j != 0:
                new_row = [int(c) for c in sudoku_line[:9]]
                new_board.append(new_row)
        boards.append(new_board)
    total = 0
    i = 0
    solved = 0
    for board in boards:
    # board = boards[5]
    # if True:
        args = init_args()
        # uncomment the following line to enable bifurcation
        # args[1] = True
        i+=1
        x = solve_board(board)
        if x != None:
            if not check_broken(x):
                solved += 1
                show_board(x)
                three_digit_string = ""
                three_digit_string += str(x[0][0]) + str(x[0][1]) + str(x[0][2])
                print(three_digit_string)
                print(i)
                total += int(three_digit_string)
        else:
            print("-" * 30)
            print("can't figure this one out")
            print(i)
            print("-" * 30)
    print("solved: " + str(solved) + "/" + str(i))
    print(total)
        
if __name__ == "__main__":
    main()