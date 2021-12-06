class BingoBoardSpot:
    def __init__(self, value):
        self.value = value
        self.marked = False

class BingoBoard:
    def __init__(self, values):
        self.spots = []
        self.bingo = False

        for row in values:
            temp = []

            for value in row:
                temp.append(BingoBoardSpot(value))

            self.spots.append(temp)
    
    def has_bingo(self, draws):
        draw_found = False
        new_draw = draws[-1]

        # Check if latest draw is in board, row by row
        for i in range(len(self.spots)):
            row_values = [spot.value for spot in self.spots[i]]
            if new_draw in row_values:
                row = i
                col = row_values.index(new_draw)
                draw_found = True

        if not draw_found:
            return False

        self.spots[row][col].marked = True

        # Check row of latest draw for bingo
        if all([spot.marked for spot in self.spots[row]]):
            self.bingo = True

        # Check col of latest draw for bingo
        if all([i[col].marked for i in self.spots]):
            self.bingo = True

        return self.bingo

    def print_board(self):
        formatted_board = []
        for row in self.spots:
            formatted_row = []
            for spot in row:
                if spot.marked:
                    formatted_row.append(spot.value + '_')
                else:
                    formatted_row.append(spot.value + ' ')
            formatted_board.append(formatted_row)
        
        for row in formatted_board:
            print(row)
                

def main():
    input_file = open('boards.txt', 'r')
    board_file_lines = input_file.readlines()
    input_file.close()

    input_file = open('numbers.txt', 'r')
    draw_file_lines = input_file.readlines()
    input_file.close()

    values = []

    # Parse board file lines and clean input
    for line in board_file_lines:
        temp = line.strip().split(' ')

        while('' in temp):
            temp.remove('')

        values.append(temp)

    board_dim = len(values[0])

    # Remove empty lists between boards
    while([] in values):
        values.remove([])

    boards = []

    # Create boards from every board_dim set of values
    for i in range(0, len(values), board_dim):
        boards.append(BingoBoard(values[i:i + board_dim]))

    # Parse draw file
    draws = draw_file_lines[0].strip().split(',')
    draws_so_far = []

    # Iterate over draws until bingo found
    for draw in draws:
        draws_so_far.append(draw)
        remove_boards = []

        for board in boards:
            if board.has_bingo(draws_so_far):
                if len(boards) == 1:
                    sum = 0
                    for row in boards[0].spots:
                        for spot in row:
                            if not spot.marked:
                                sum += int(spot.value)
                    
                    print(sum * int(draw))
                    return
                else:
                    remove_boards.append(board)

        # Remove boards that already have bingo until one board is left
        if remove_boards:
            for board in remove_boards:
                boards.remove(board)

main()