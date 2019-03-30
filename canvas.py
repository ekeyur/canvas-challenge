import sys


class Canvas:
    def __init__(self, file):
        self.file = file
        self.instructions = []
        self.canvas = []
        self.BORDER_GIVE = 2  # Canvas border pixels

    def transferInputToInstructions(self):
        with open(self.file) as fp:
            for line in fp:
                line = line.replace('\n', '')
                self.instructions.append(line.split(' '))

    def createCanvas(self, h, w):
        for i in range(0, h):
            for j in range(0, w):
                if i == 0 or i == h-1:
                    self.canvas[i][j] = '-'
                elif j == 0 or j == w-1:
                    self.canvas[i][j] = '|'
                else:
                    self.canvas[i][j] = ' '

    def drawLine(self, x1, y1, x2, y2):
        for h in range(y1, y2+1):
            for w in range(x1, x2+1):
                self.canvas[h][w] = 'x'

    def bucketFill(self, x, y, newColor, oldColor):
        height = len(self.canvas)
        width = len(self.canvas[0])
        if self.canvas[x][y] != oldColor:
            return
        if self.canvas[x][y] == oldColor:
            self.canvas[x][y] = newColor
            if x > 1:
                self.bucketFill(x-1, y, newColor, oldColor)
            if y > 1:
                self.bucketFill(x, y-1, newColor, oldColor)
            if x < height-1:
                self.bucketFill(x+1, y, newColor, oldColor)
            if y < width-1:
                self.bucketFill(x, y+1, newColor, oldColor)

    def initializeCanvasSize(self, width, height):
        self.canvas = [[' ' for h in range(height)]
                       for w in range(width)]

    def executeLine(self, index, line):
        if index == 0 and (len(line) != 3 or line[0] != 'C'):
            print 'Please define canvas dimensions in the correct format'
            sys.exit()
        if index == 0 and len(line) == 3 and line[0] == 'C':
            height = int(line[1])+self.BORDER_GIVE
            width = int(line[2])+self.BORDER_GIVE
            self.initializeCanvasSize(width, height)
            self.createCanvas(width, height)
        if line[0] == 'L':
            x1 = int(line[1])
            y1 = int(line[2])
            x2 = int(line[3])
            y2 = int(line[4])
            self.drawLine(x1, y1, x2, y2)
        if line[0] == 'R':
            element, x1s, y1s, x2s, y2s = line
            x1 = int(x1s)
            x2 = int(x2s)
            y1 = int(y1s)
            y2 = int(y2s)
            self.drawLine(x1, y1, x2, y1)
            self.drawLine(x1, y1, x1, y2)
            self.drawLine(x1, y2, x2, y2)
            self.drawLine(x2, y1, x2, y2)
        if line[0] == 'B':
            element, x, y, color = line
            oldColor = self.canvas[int(y)][int(x)]
            self.bucketFill(int(y), int(x), color, oldColor)
        self.printCanvas()

    def printCanvas(self):
        str = ''
        for idx, line in enumerate(self.canvas):
            print str.join(line)

    def executeCommands(self):
        self.transferInputToInstructions()
        for idx, line in enumerate(self.instructions):
            self.executeLine(idx, line)
