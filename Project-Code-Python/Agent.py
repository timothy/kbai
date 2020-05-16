# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
from PIL import Image, ImageChops
import numpy


class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints 
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def Solve(self, problem):
        self.problem = problem
        print(problem)
        return self.all_same_check(problem)

    def all_same_check(self, problem):
        a = Image.open(problem.figures['A'].visualFilename).convert('RGB')
        b = Image.open(problem.figures['B'].visualFilename).convert('RGB')
        c = Image.open(problem.figures['C'].visualFilename).convert('RGB')
        diff = ImageChops.difference(a, b)
        diff2 = ImageChops.difference(a, c)
        if not diff.getbbox() and not diff2.getbbox():
            for i in range(1, 6):
                if not ImageChops.difference(a, self.open(i)).getbbox():
                    print("the images are the same!")
                    print(problem.name, i)
                    return i
        return -1

    def open(self, attr):
        return Image.open(self.problem.figures[str(attr)].visualFilename).convert('RGB')
