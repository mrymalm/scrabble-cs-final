import os, random
path=os.getcwd()

CELL_HEIGHT = 64
CELL_WIDTH  = 64
NUM_ROWS = 10
NUM_COLS = 10

numRow=8
numCol=8
board=[]
dictionary=['jets','jams','gets','zoos','part',
            'alps','band','call','dear','fish',
            'kick','quit','vibe','wind','knit',
            'yeti','xmas','come','owns','dope']
def load_images():
    global img_letter, img_explored
    img_letters=[]
    img_explored=[]
    for num in range(1,26):
        location1=path + "/" +str(num) + ".jpg"
        location2=path + "/" + str(num) +".explored"+ ".jpg"
        print("Loading image from: " + location1)
        print("Loading image from: " + location2)
        img1 = loadImage(location1)
        img2 = loadImage(location2)
        assert img1 != None
        assert img2 != None
        img_letters.append(img1)
        img_explored.append(img2)

class Cell:
    def __init__(self):
        self.explored = False
        #k = random.randint(0,25)
        #self.alphabet = chr(k+65)
        
        
class Board:
    def __init__(self):
        self.numrow = row
        self.numcol = col
        self.end_game = False
        # 0 if not end, -1 if u lost, 1 if u win
        self.create_board()
    def create_board(self):
        self.board = []
        for row in range(self.row):
            tmp = []
            for col in range(self.col):
                tmp.append(Cell(False))
            self.board.append(tmp)
        for i in range(4):
            x = random.randint(0,20)
            y = random.randint(0,20)
            hv= random.randint(0,1)
            wordChoice=list(dictionary[x])
            if hv==0:
                count = 0
                for i in range(4):
                    yy=y+i
                    if yy<4:
                        count=count+1
                if count==4:
                    for i in range(4):
                        yy=y+i
                        board[x][yy]=wordChoice[i]
                    break
            elif hv==1:
                count=0
                for i in range(4):
                    xx=x+i
                    if xx<10:
                        count=count+1
                if count==4:
                    for i in range(4):
                        xx=x+i
                        board[xx][y]=wordChoice3 and wordChoice4
                    break
            board.append(WordChoice1)
            board.append(WordChoice2)
            board.append(WordChoice3)
            board.append(WordChoice4)
            
        
        








def setup():
    global b
    load_images()
    b=Board(numRow, numCol)
    b.create_board()
    size(NUM_ROWS * CELL_HEIGHT, NUM_COLS * CELL_WIDTH)
    background(255)
def drawLetter(rowid, colid):
    xcoord = colid * CELL_WIDTH
    ycoord = rowid * CELL_HEIGHT
    image(img_letter, xcoord, ycoord)
def drawExplored(rowid, colid):
    xcoord = colid * CELL_WIDTH
    ycoord = rowid * CELL_HEIGHT
    image(img_explored, xcoord, ycoord)


def draw():
    background(255)
    b.print_board()
    
def mouseClicked():
    colid = mouseX // CELL_WIDTH
    rowid = mouseY // CELL_HEIGHT
    
    
