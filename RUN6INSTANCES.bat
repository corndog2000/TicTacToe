set game_count=30000000

start "" python TicTacToe.py --games %game_count% --count --winners --random --model_name num1
start "" python TicTacToe.py --games %game_count% --count --winners --random --model_name num2
start "" python TicTacToe.py --games %game_count% --count --winners --random --model_name num3
start "" python TicTacToe.py --games %game_count% --count --winners --random --model_name num4
start "" python TicTacToe.py --games %game_count% --count --winners --random --model_name num5
start "" python TicTacToe.py --games %game_count% --count --winners --random --model_name num6

pause