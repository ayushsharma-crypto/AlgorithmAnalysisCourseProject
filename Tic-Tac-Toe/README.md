# Tic-Tac-Toe
1. Tic-tac-toe or Xs and Os, is a game for two players, X and O, who take turns alternately marking the spaces in a 3×3 grid. 

2. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.

3. The game can be played for 3,4 or 5 points which means that, the game finishes after any player scores 3,4 or 5 points. After this you can either quit the game or play again.

4. The player can win, lose or a draw can happen. The winning player gets a point and the losing player gets nothing. At the time of draw, no one gets a point.

## Single player game logic
1. Minimax Algorithm: Minimax is a kind of backtracking algorithm that is used in decision making and game theory to find the optimal move for a player, assuming that your opponent also plays optimally. In Minimax the two players are called maximizer and minimizer. The maximizer tries to get the highest score possible while the minimizer tries to do the opposite and get the lowest score possible. The minimax algorithm performs a depth-first search algorithm for the exploration of the complete game tree.

2. Properties of Minimax algorithm:
    1) Complete- MiniMax algorithm is Complete. It will definitely find a solution (if exist), in the finite search tree.
    2) Optimal- MiniMax algorithm is optimal if both opponents are playing optimally.
    3) Time complexity- As it performs DFS for the game-tree, so the best and worst time complexity of MiniMax algorithm is O(b^m), where b is branching factor of the game-tree, and m is the maximum depth of the tree.
    4) Space Complexity- Space complexity of Minimax algorithm is also similar to DFS which is O(bm).

3. Alpha-Beta pruning: Alpha-Beta pruning isan optimization technique for minimax algorithm. It reduces the computation time by a huge factor. This allows us to search much faster and even go into deeper levels in the game tree. It cuts off branches in the game tree which need not be searched because there already exists a better move available. It is called Alpha-Beta pruning because it passes 2 extra parameters in the minimax function, namely alpha and beta.

4. Single player logic uses Minimax algorithm to play against the user.


## How to play
1. Requirements: For you to run this file, you should have `math`, `random` and `pygame` libraries of python installed or else you can install it by using the command:

        pip3 install <library name>

2. run the command given below on your terminal 

        python3 main.c

3. You will get a new screen in which you can play the game.
4. for marking any box with X or O you can just click on that box.

