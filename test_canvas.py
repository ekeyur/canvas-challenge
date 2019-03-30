import unittest
from canvas import Canvas


class TestSum(unittest.TestCase):

    def setUp(self):
        self.c = Canvas("test_input.txt")

    def test_file(self):
        self.assertEqual(self.c.file, "test_input.txt",
                         "Should be the given filename")

    def test_transferInputToInstructions(self):
        self.c.transferInputToInstructions()
        self.assertEqual(len(self.c.instructions[0]), 3)
        self.assertEqual(self.c.instructions[0], ['C', '10', '5'])

    def test_initializeCanvasSize(self):
        self.c.transferInputToInstructions()
        element, w, h = self.c.instructions[0]
        self.c.initializeCanvasSize(int(w)+2, int(h)+2)
        self.assertEqual(int(w)+2, len(self.c.canvas),
                         "Should be the width of Canvas command given")
        self.assertEqual(int(h)+2, len(self.c.canvas[0]),
                         "Should be the height of Canvas command given")

    def test_createCanvas(self):
        self.c.transferInputToInstructions()
        element, width, height = self.c.instructions[0]
        h = int(height)
        w = int(width)
        self.c.initializeCanvasSize(w+2, h+2)
        self.c.createCanvas(w+2, h+2)
        self.assertEqual(self.c.canvas[0][w-4], '-')
        self.assertEqual(self.c.canvas[h][0], '|')
        self.assertEqual(self.c.canvas[0][h], '-')
        self.assertEqual(self.c.canvas[4][w-4], '|')
        self.assertEqual(self.c.canvas[h/2][w/2], ' ')

    def test_drawLine(self):
        self.c.transferInputToInstructions()
        element, width, height = self.c.instructions[0]
        h = int(height)
        w = int(width)
        self.c.initializeCanvasSize(w+2, h+2)
        self.c.createCanvas(w+2, h+2)
        self.c.drawLine(2, 3, 2, 6)
        self.assertEqual(self.c.canvas[3][2], 'x')
        self.assertEqual(self.c.canvas[4][2], 'x')
        self.assertEqual(self.c.canvas[5][2], 'x')
        self.assertEqual(self.c.canvas[6][2], 'x')

    def test_executeLineToDrawLine(self):
        self.c.executeLine(0, ['C', '10', '5'])
        self.c.executeLine(1, ['L', '3', '2', '6', '2'])
        self.assertEqual(self.c.canvas[2][3], 'x')
        self.assertEqual(self.c.canvas[2][4], 'x')
        self.assertEqual(self.c.canvas[2][5], 'x')
        self.assertEqual(self.c.canvas[2][6], 'x')

    def test_executeLineToDrawRectangle(self):
        self.c.executeLine(0, ['C', '10', '5'])
        self.c.executeLine(1, ['R', '3', '2', '6', '5'])
        self.assertEqual(self.c.canvas[2][3], 'x')
        self.assertEqual(self.c.canvas[5][6], 'x')
        self.assertEqual(self.c.canvas[2][6], 'x')
        self.assertEqual(self.c.canvas[5][3], 'x')

    def test_executeLineToFillBucket(self):
        self.c.executeLine(0, ['C', '10', '5'])
        self.c.executeLine(1, ['R', '3', '2', '6', '5'])
        self.c.executeLine(2, ['B', '4', '4', 'v'])
        self.assertEqual(self.c.canvas[2][3], 'x')
        self.assertEqual(self.c.canvas[5][6], 'x')
        self.assertEqual(self.c.canvas[2][6], 'x')
        self.assertEqual(self.c.canvas[5][3], 'x')
        self.assertEqual(self.c.canvas[3][4], 'v')
        self.assertEqual(self.c.canvas[3][5], 'v')
        self.assertEqual(self.c.canvas[4][4], 'v')
        self.assertEqual(self.c.canvas[4][5], 'v')

    def test_executeLineToExitIfCanvasNotDefined(self):
        self.assertRaises(SystemExit, self.c.executeLine, 0, ['K', '3', '4'])


if __name__ == '__main__':
    unittest.main()
