from canvas import Canvas
import sys
# create an instance of canvas and pass the file to its constructor
try:
    c = Canvas(sys.argv[1])
    c.executeCommands()
except:
    print "Please provide the input file as an arguement."
    sys.exit()


#####################################################################################
# Instuctions to run the program
# This program has been written in python 2.7
# On command line within the folder type: python main.py input.txt
# executeCommands method will run all the commands in the file and print output after each command


# Tests
#######################################################################################
# Tests are written in test_canvas.py
# There is a separate test_input.txt file which is specific to the written tests. Please don't change
# In order to run and see all the tests pass run python test_canvas.py
