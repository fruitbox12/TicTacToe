# TicTacToe
Console TicTacToe App

AI player class holds strategies, referencing the different methods of winning in a nested loop with certain conditions
`    1 4 
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
`
