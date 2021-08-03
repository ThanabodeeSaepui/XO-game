"""Member
ธนาบดี แซ่ปุ่ย 6301012620138
ปรินทร สมภู 6301012610060
เสฏฐภูมิ ตุลยสุข 6301012630192
"""
class XO(object):
    def __init__(self) -> None:
        self.board_array = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.player = ["X","O"]
        self.turn_count = 0
        
    def add_position(self, pos):
        x = (pos-1)%3
        y = (pos-1)//3
        if self.board_array[y][x] == ' ':
            self.board_array[y][x] = self.player[0]
            self.turn_count += 1
            self.change_player()
        else:
            print("Can not put mark on same position")

    def change_player(self):
        self.player[0],self.player[1] = self.player[1],self.player[0]


    def check_winner(self):
        check_list_2 = list()
        check_list_3 = list()
        for i in range(len(self.board_array)):
            check_list = list()
            check_list_2.append(self.board_array[i][i])
            check_list_3.append(self.board_array[i][len(self.board_array)-1-i])
            for j in range(len(self.board_array[i])):
                if self.board_array[j] == [self.player[1]]*len(self.board_array[i]):
                    return(True,False)
                check_list.append(self.board_array[j][i])
            if check_list == [self.player[1]]*len(check_list):
                return(True,False)
        if check_list_2 == [self.player[1]]*len(self.board_array) or check_list_3 == [self.player[1]]*len(self.board_array):
            return (True,False)
        if self.turn_count == 9:
            return (True,True)
        return(False,False)
    def display_board(self):
        for i in self.board_array:
            row_i = str()
            for j in i:
                row_i += f"({j})"
            print(f"{row_i}")
    
game_xo = XO()
game_xo.display_board()
while(not game_xo.check_winner()[0]):
    INPUT = input(f"{game_xo.player[0]}'s turn : ")
    try:
        game_xo.add_position(int(INPUT))
        game_xo.display_board()
    except:
        print("please enter 1-9")
        game_xo.display_board()
if game_xo.check_winner()[1]:
    print("Draw.")
else:
    print(f"{game_xo.player[1]} is the winner.")