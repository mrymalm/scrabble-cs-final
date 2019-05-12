import os, random
import time
path=os.getcwd()

CELL_HEIGHT = 64
CELL_WIDTH  = 64
NUM_ROWS = 10
NUM_COLS = 10

numRow=8
numCol=8
dictionary=['jets','jams','gets','zoos','part',
            'alps','band','call','dear','fish',
            'kick','quit','vibe','wind','knit',
            'yeti','xmas','come','owns','dope']
def load_images():
    global img_letters, img_explored
    img_letters=[]
    img_explored=[]
    for num in range(1,27):
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
        self.letter = None
        self.israndom=True
        self.clicked = False
        self.right_words = 0
        self.score = 0
        #k = random.randint(0,25)
        #self.alphabet = chr(k+65)
        
        
class Board:
    def __init__(self, row=8, col=8):
        self.numrow = row
        self.numcol = col
        self.win = False
        # 0 if not end, -1 if u lost, 1 if u win
        self.create_board()
        self.lose = False
        self.score = 0
        
    def create_board(self):
        self.words = []
        self.board = []
        for row in range(self.numrow):
            tmp = []
            for col in range(self.numcol):
                tmp.append(Cell())
            self.board.append(tmp)
        for i in range(4):
            hv= random.randint(0,1)
            word = []
            
            while True:
                x = random.randint(0,self.numrow-4)
                y = random.randint(0,self.numcol-4)
                available=True
                if hv==0:
                    for i in range(4):
                        if self.board[x+i][y].letter != None:
                            available=False
                            break
                    if available:
                        break
                elif hv==1:
                    for i in range(4):
                        if self.board[x][y+i].letter != None:
                            available=False
                            break
                    if available:
                        break
                    
            WordChoice=list(dictionary[x])
            
            if hv==0:
                for i in range(4):
                    self.board[x+i][y].israndom=False
                    self.board[x+i][y].letter = WordChoice[i]
                    word.append([x+i, y])
            elif hv==1:
                for i in range(4):
                    self.board[x][y+i].letter = WordChoice[i]
                    self.board[x][y+i].israndom = False
                    word.append([x, y+i])
            self.words.append(word)
            
                    
        for r in range(self.numrow):
            for c in range(self.numcol):
                if self.board[r][c].letter == None:
                    self.board[r][c].letter = chr(random.randint(0, 25)+97)
                    
        
    def print_board(self):
        for i in range(self.numrow):
            for j in range(self.numcol):
                if self.board[i][j].letter != None:
                    if not self.board[i][j].clicked:
                        image(img_letters[ord(self.board[i][j].letter)-97], i*CELL_WIDTH, j*CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
                    else:
                        image(img_explored[ord(self.board[i][j].letter)-97], i*CELL_WIDTH, j*CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
    def how_many_words(self):
        n = 0
        for i in range(4):
            all_clicked = True
            for j in range(4):
                cor = self.words[i][j]
                if self.board[cor[0]][cor[1]].clicked != True:
                    all_clicked = False
            if all_clicked: n=n+1
        self.score = n*25
        print(self.score)
    
def setup():
    global b, start_time
    start_time = time.time()
    
    load_images()
    b=Board(NUM_ROWS, NUM_COLS)
    size(NUM_ROWS * CELL_HEIGHT, NUM_COLS * CELL_WIDTH)
    '''background(255)'''
    print(b.words)
    
    
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
    b.how_many_words()
    if not b.lose and not b.win:
        b.print_board()
    if time.time() - start_time > 60:
        print("timeout")
        b.lose = True
    if b.score==100:
        b.win = True
        print("you won!")
        noLoop()
    if keyPressed:
        if key==ENTER:
            b.lose = True
            print("You Gave Up")
            print("score= ",b.score)
    if b.lose:
        background(0)
        text("Loser! Haha Your Score: "+ str(b.score), width/2, height/2)
    if b.win:
        background(0)
        text("You Won!", width/2, height/2)
    
def mouseClicked():
    rowid = mouseX // CELL_WIDTH
    colid = mouseY // CELL_HEIGHT
    if b.board[rowid][colid].israndom == False:
        b.board[rowid][colid].clicked = True
    
