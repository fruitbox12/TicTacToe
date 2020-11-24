import player

class AIPlayer(player.Player):
    def __init__(self, type, number, name, board):
        player.Player.__init__(self, type, number, name, board)
    # Pseudo-constants
        self.__ME = True
        self.__OTHER = False
    # The Override abstract method
    # The AI CANNOT USE THIS METHOD,NO ROW, COL PARMS POSSIBLE
    # One option (the OOP "purist" way) is to declare two abstract methods in the parent class.
    # Another option (unorthodos way) is to use the default values and then ignore these unused parameters.
    def play(self, row = -1, col = -1):
        # NEED THE OTHER PLAYER NUMBER(S)!
        # Check for possible AI win
        win, play_row, play_col = self.possible_horizontal_win(self.__ME)

        if not win:
            win, play_row, play_col = self.possible_vertical_win(self.__ME)

            if not win:
                win, play_row, play_col = self.possible_diagonal_win(self.__ME)

                if not win:
                    # Run thru tic tac toe strategies
                    block, play_row, play_col = self.possible_horizontal_win(self.__OTHER)

                    if not block:

                        block, play_row, play_col = self.possible_vertical_win(self.__OTHER)

                        if not block:
                            win, play_row, play_col = self.possible_diagonal_win(self.__OTHER)

                            if not block:
                               # block, play_row, play_col = self.square_strategy(self.__ME)
                               
                                if not block:
                                    block, play_row, play_col = self.three_corner_strategy(self.__ME)

                                    if not block:
                                        block, play_row, play_col = self.v_strategy(self.__ME)

                                        if not block:
                                            play_row, play_col = self.no_strategy()

        self.move(play_row, play_col)

        return play_row, play_col

    # Offen  sive strategy/Defensive Strategy
    def possible_horizontal_win(self, occupied_by_me = True):
        win = False

        # Get the current player's piece
        number_of_positions = 0
     
        empty_position = False

        player_number = self.get_number()
        rows = self.get_rows()
        cols = self.get_cols()
        board = self.get_board()
        empty = board.get_empty()
        win_row = empty
        win_col = empty
        invalid = board.get_invalid()

        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                position = board.get_board_position(row, col)
                if occupied_by_me:
                    if position == player_number:
                        number_of_positions += 1
                else:
                    if position != player_number and position != empty:
                        number_of_positions += 1
                if position == empty:
                    win_row = row
                    win_col = col
                    empty_position = True

            if number_of_positions == cols - 1 and empty_position:
                win = True
                break;
            else:
                    number_of_positions = 0;
                    win_row = invalid
                    win_col = invalid
                    empty_position = False

        return win, win_row, win_col

    # Offensive strategy
    def possible_vertical_win(self, occupied_by_me = True):
        win = False

        # Get the current player's piece
        number_of_positions = 0

        rows = self.get_rows()
        cols = self.get_cols()
        board = self.get_board()
        empty = board.get_empty()
        win_row = empty
        win_col = empty
        invalid = board.get_invalid()

        empty_position = False

        player_number = self.get_number()

        for col in range(1, cols + 1):
            for row in range(1, rows + 1):
                position = board.get_board_position(row, col)

                if occupied_by_me:
                    if position == player_number:
                        number_of_positions += 1
                elif position != player_number and position != empty:
                        number_of_positions += 1
                elif position == empty:
                    win_row = row
                    win_col = col
                    empty_position = True

            if number_of_positions == rows - 1 and empty_position:
                win = True
                break;
            else:
                number_of_positions = 0;
                win_row = invalid
                win_col = invalid
                empty_position = False

        return win, win_row, win_col

    # Offensive strategy
    def possible_diagonal_win(self, occupied_by_me = True):
        win = False

        # Get the current player's move

        number_of_positions = 0

        rows = self.get_rows()
        cols = self.get_cols()
        board = self.get_board()
        empty = board.get_empty()
        win_row = empty
        win_col = empty
        invalid = board.get_invalid()

        empty_position = False
        player_number = self.get_number()
        other_player_number = 0

        # Check for the left diagonal top left to bottom right
        for row in range(1, rows + 1):
            for col in range(row, row + 1):
                position = board.get_board_position(row, col)
                if occupied_by_me:
                    if position == player_number:
                        number_of_positions += 1
                elif position != player_number:
                    if other_player_number  != empty:
                        other_player_number = position
                        number_of_positions += 1
                    else:
                        other_player_number = position
                        number_of_positions = 1
                else:
                        win_row = row
                        win_col = col
                        empty_position = True


            if number_of_positions == cols - 1and empty_position:
                win = True
                break;
            else:
                number_of_positions = 0;
                win_row = invalid
                win_col = invalid
                empty_position = False
        else:
            number_of_positions = 0
            win_row = empty
            win_col = empty
            empty_position = False

            # Check for the right diagonal top right to bottom left
            for row in range(1, rows + 1):
                for col in range(cols - row + 1, cols - row + 2):
                    position = self.get_position()
                    if occupied_by_me:
                        if position == player_number:
                            number_of_positions += 1
                    elif position != player_number:
                        if other_player_number  != empty:
                            other_player_number = position
                            number_of_positions += 1
                        else:
                            other_player_number = position
                            number_of_positions = 1
                    else:
                            win_row = row
                            win_col = col
                            empty_position = True
                    if number_of_positions == cols - 1 and empty_position:
                        win = True
                        break;
                    else:
                        number_of_positions = 0;   
                        empty_position = False

        return win, win_row, win_col

        """
         4 
        2 = 16 combinations (4 possible squares taken two sides at a time)

         1 | 2 | 3      1 2     2 3     8 combinations
	     ---------	    4 5     5 6
	     4 | 5 | 6
	     ---------      4 5     5 6     8 combinations
	     7 | 8 | 9      7 8     8 9

        8 combinations

        1-2-5   2-3-6
        2-5-4   3-6-5
        5-4-1   6-5-2
        4-1-2   5-2-3

        8 combinations

        4-5-8   5-6-9
        5-8-7   6-9-8
        8-7-4   9-8-5
        7-4-5   8-5-6

         1 | 2 | 3      1 2     2 3     8 combinations
	     ---------	    4 5     5 6
	     4 | 5 | 6
	     ---------      4 5     5 6     8 combinations
	     7 | 8 | 9      7 8     8 9

        [1] X | X |      [2]   | X |     [3]  X |   |    [4] X | X | 
	        ---------	     ---------	      ---------	     ----------
	          | X |		     X | X |		  X | X |   	 X |   | 
	        ---------	     ---------	      ---------	     ----------
	          |   |  	       |   |  	        |   |  	       |   | 

        [5]   | X | X    [6]   |   | X   [7]    | X |    [8]   | X | X
	        ---------	     ---------	      ---------	     ----------
	          |   |	X	       | X | X		    | X | X  	   | X | 
	        ---------	     ---------	      ---------	     ----------
	          |   |  	       |   |  	        |   |  	       |   | 

        [9]   |   |      [10]  |   |     [11]   |   |    [12]  |   | 
	        ---------	     ---------	      ---------	     ----------
	        X | X |		       | X | 		  X |   |   	 X | X | 
	        ---------	     ---------	      ---------	     ----------
	          | X |  	     X | X |  	      X | X |  	     X |   | 

        [13]  |   |      [14]  |   |     [15]   |   |    [16]  |   | 
	        ---------	     ---------	      ---------	     ----------
	          | X |	X	       |   | X		    | X |   	   | X | X
	        ---------	     ---------	      ---------	     ----------
	          |   | X 	       | X | X 	        | X | X	       | X | 
     
        """
# no need to code #2 bc its too avi
    def square_strategy (self, occupied_by_me = True):
        # Get the current player's move
        player_number = self.get_number()
        number_of_positions = 0
        board = self.get_board()
        rows = self.get_rows()
        cols = self.get_cols()
        empty = board.get_empty()
        invalid = board.get_invalid()
        block_row = invalid
        block_col = invalid
        blocked = False


        empty_position = False
        # Case [1]
        # Row 1 Col 1, Col 2
        # Row 2 Col 2
        for row in range(1, rows):
           for col in range(row, rows):
               position = board.get_board_position(row, col)
               if position == player_number:
                   number_of_positions+=1

               elif position == empty:
                   block_row = row
                   block_col = col
                   blocked = True
        return blocked, block_row, block_col
    """
	    // Strategy 3: if the human player is attempting to execute the "three corner strategy":
	    // 
	    // Models [1] through [4]:
	    //
	    // [1] X |   | X   [2]   |   | X   [3] X |   |   [4] X |   | X
	    //     ---------	   ----------	   --------		 ----------
	    //		 |   |		     |   |		     |   |		   |   |
	    //	   ---------	   ---------	   ---------	 ----------
	    //       |   | X	   X |   | X	   X |   | X	 X |   | 
	    //
	    // block it by attacking horizontally along the middle, thus forcing the human player
	    // to break off the attack and go on the defensive:
	    // 
	    // [1] X |   | X   [2]   |   | X
	    //	   ---------	   ---------
	    //	   O | O |	         | O | O
	    //	   ---------	   ---------
	    //	     |   | X	   X |   | X
	    //
	    // If we get to this strategy, the O should already be in the middle, blocking a human win
	    // along either diagonal line.
	"""
    def three_corner_strategy(self, occupied_by_me = True):

        player_number = self.get_number()
        this_player_positions = 0
        other_player_positions = 0
        board = self.get_board()
        rows = self.get_rows()
        cols = self.get_cols()
        empty = board.get_empty()
        invalid = board.get_invalid()
        block_row = invalid
        block_col = invalid
        blocked = False

        for row in range(1, rows + 1, 2):
            for col in range(1, cols + 1, 2):
                position = board.get_board_position(row, col)
                if position == player_number:
                    this_player_positions+=1
                elif position != empty:
                    other_player_positions+=1

        if other_player_positions == 1:
            position = board.get_board_position(rows - 1, cols - 1)
            if position == empty:
                block_row = rows - 1
                block_col = cols - 1
                blocked = True

        elif other_player_positions == 2:
            for col in range(cols-1, cols):
                for row in range(1, rows + 1, 2):

                    position = board.get_board_position(row, col)
                    if position == empty:

                        block_row = row
                        block_col = col
                        blocked = True
                        break;

        return blocked, block_row, block_col

    def no_strategy(self, occupied_by_me = True): 
        board = self.get_board()
        rows = self.get_rows()
        cols = self.get_cols()
        empty = board.get_empty()
        invalid = board.get_invalid()
        empty_row = invalid
        empty_col = invalid
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                position = board.get_board_position(row, col)

                if position == empty:
                     empty_row = row
                     empty_col = col
                     empty_position = True
        
        if not empty_position:
            raise Exception("ai_player.no_strategy(): No position left to paly, Board is full")

        return empty_row, empty_col
    """//----------------------------------------------------------------------------------------
	// Strategy 4: if the human player is attempting to execute the "V strategy":
	// 
	// Models [1] through [4]:
	//
	// [1] X |   | X   [2]   |   | X   [3]   |   |   [4] X |   | 
	//     ---------	   ----------	   --------		 ----------
	//		 | X |		     | X |		     | X |		   | X |
	//	   ---------	   ---------	   ---------	 ----------
	//       |   |  	     |   | X	   X |   | X	 X |   | 
	// 
	// block it placing an O on the third peg of the offensive:
	// 
	// [2] O |   | O <--- block the attack here  
	//	   ---------
	//	     | X |	
	//	   ---------
	//	     |   | X
	//
	// The O at the top left corner we get from strategy #7 (any blank cell starting at that 
	// position). Placing an O at the top right corner forces the human player into a defensive
	// position and breaks off the attack.
	//
	// The human player can only put this strategy into effect by holding the middle cell.
	// We will attempt to preempt this strateby by taking the middle cell in strategy #6.
	//
	// Models [1] and [4] are taken care of by strategy #7 (no strategy) but the code
	// is included here anyway just in case...
	//
	// Begin by detecting an X in the middle.
	//-----------------------------------------------------------------------------------------
    """
    def v_strategy(self, occupied_by_me = True):
        this_player_positions = 0
        other_player_positions = 0
        number_of_positions = 0
        player_number = self.get_number()        
        board = self.get_board()
        rows = self.get_rows()
        cols = self.get_cols()
        empty = board.get_empty() 
        blocked = False     
        empty_position = False
        invalid = board.get_invalid()
        play_row = invalid
        play_col = invalid
        empty_row = invalid
        empty_col = invalid 
        number_of_corners = 0
        center = round(rows / 2.0)

        position = board.get_board_position(center, center)
        if position == empty:
            empty_center = True
            play_row = center
            play_col = center
            blocked = True
        # If middle position is already occupied by this player, do nothing
        elif position != player_number:
            other_player_positions = 1
            for row in range(1, rows + 1, 2):
                for col in range(1, cols + 1, 2):
                    position = board.get_board_position(row, col)

                    if position == player_number: 
                        this_player_positions += 1
                    elif  position == empty:
                         empty_row = row
                         empty_col = col 
                         empty_position = True

                    else:
                        other_player_positions += 1

                if other_player_positions == 2:
                    # Check if the third position is available
                    if empty_position:
                        play_row = empty_row
                        play_col = empty_col
                        blocked = True
                        break
                # Possibilities:
                # 1. Other player occupis 3 positions (game over!). Do nothing
                # 2. Other player occupies only the middle position (1). do nothing
                else:
                    this_player_positions = 0
                    other_player_positions = 1

            # check the other vertical positions
            for col in range(1, cols + 1, 2):
                for row in range(1, rows + 1, 2):
                    position = board.get_board_position(row, col)

                    if position == player_number: 
                        this_player_positions += 1
                    elif  position == empty:
                         empty_row = row
                         empty_col = col 
                         empty_position = True

                    else:
                        other_player_positions += 1

                if other_player_positions == 2:
                    # Check if the third position is available
                    if empty_position:
                        play_row = empty_row
                        play_col = empty_col
                        blocked = True
                        break
                # Possibilities:
                # 1. Other player occupis 3 positions (game over!). Do nothing
                # 2. Other player occupies only the middle position (1). do nothing
                else:
                    this_player_positions = 0
                    other_player_positions = 1
        return blocked, empty_row, empty_col


    def center_strategy (self, occupied_by_me = True):       
        player_number = self.get_number()        
        board = self.get_board()
        rows = self.get_rows()
        cols = self.get_cols()
        empty = board.get_empty() 
        blocked = False     

        if board.get_board_position(rows - 1, cols - 1) == empty:
            empty_row = row
            empty_col = col
            blocked = True

        return blocked, empty_row, empty_col

    