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
from PIL import Image, ImageChops, ImageOps
import numpy as np


class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        self.answer_indexes = [1, 7]
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
        answer = self.all_same_check()
        if answer is not -1:
            return answer
        answer = self.is_a_c()
        if answer is not -1:
            return answer
        answer = self.a_mirror_b()
        if answer is not -1:
            return answer

        print(problem.name, problem.problemType)
        return -1

    # below are root thinking methods

    def all_same_check(self):
        """If A==B==C then look for A==i"""
        a, b, c = self.open("A", "B", "C")
        if self.is_same(a, b, c):
            for i in self.answers():
                if not ImageChops.difference(a, self.open(i)).getbbox():
                    print("the images are the same!")
                    print(self.problem.name, i)
                    return i
        return -1

    def is_a_c(self):
        """If A==C then look for B==i"""
        a, b, c = self.open("A", "B", "C")
        if self.is_same(a, c):
            for i in self.answers():
                if self.is_same(b, self.open(i)):
                    return i
        return self.is_a_b()  # try the other way

    def is_a_b(self):
        """If A==B then look for C==i"""
        a, b, c = self.open("A", "B", "C")
        if self.is_same(a, b):
            for i in self.answers():
                if self.is_same(c, self.open(i)):
                    return i
        return -1

    def a_mirror_b(self):
        """If B is a mirror if A the look for the mirror of C"""
        a, b, c = self.open("A", "B", "C")
        a_mirror = ImageOps.mirror(a)
        if self.is_same(a_mirror, b):
            c_mirror = ImageOps.mirror(c)
            for i in self.answers():
                if self.is_same(c_mirror, self.open(i)):
                    return i
        return self.a_mirror_c()

    def a_mirror_c(self):
        """If C is a mirror if A the look for the mirror of B"""
        a, b, c = self.open("A", "B", "C")
        a_mirror = ImageOps.mirror(a)
        if self.is_same(a_mirror, c):
            b_mirror = ImageOps.mirror(b)
            for i in self.answers():
                if self.is_same(b_mirror, self.open(i)):
                    return i
        return -1

    # below are helper methods

    def open(self, *attr):
        if len(attr) is 1:
            return Image.open(self.problem.figures[str(attr[0])].visualFilename).convert('RGB')
        final = []
        for i in attr:
            final.append(Image.open(self.problem.figures[str(i)].visualFilename).convert('RGB'))
        return final

    @staticmethod
    def is_same(*args):
        if len(args) <= 1:
            return True
        last = args[0]
        for i in range(1, len(args)):
            if ImageChops.difference(last, args[i]).getbbox():
                if not Agent.close_enough(last, args[i]):
                    return False
            last = args[i]
        return True

    def answers(self):
        return range(self.answer_indexes[0], self.answer_indexes[1])

    @staticmethod
    def close_enough(a, b):
        np_a = np.array(a)
        np_b = np.array(b)
        test = np.mean(np_a == np_b)
        return test >= .95
