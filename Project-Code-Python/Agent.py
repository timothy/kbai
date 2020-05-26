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
from PIL import Image, ImageChops, ImageOps, ImageDraw
import numpy as np
import math


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
        answer = self.a_rotation_c()
        if answer is not -1:
            return answer
        answer = self.a_2_b_as_c_2_x()
        if answer is not -1:
            return answer
        answer = self.a_fill_b()
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
        """If B is a mirror of A then look for the mirror of C"""
        a, b, c = self.open("A", "B", "C")
        a_mirror = ImageOps.mirror(a)
        if self.is_same(a_mirror, b):
            c_mirror = ImageOps.mirror(c)
            for i in self.answers():
                if self.is_same(c_mirror, self.open(i)):
                    return i
        return self.a_mirror_c()

    def a_mirror_c(self):
        """If C is a mirror of A then look for the mirror of B"""
        a, b, c = self.open("A", "B", "C")
        a_mirror = ImageOps.mirror(a)
        if self.is_same(a_mirror, c):
            b_mirror = ImageOps.mirror(b)
            for i in self.answers():
                if self.is_same(b_mirror, self.open(i)):
                    return i
        return -1

    def a_rotation_c(self):
        """If C is a rotation of A then look for the rotation of B"""
        a, b, c = self.open("A", "B", "C")
        degrees = Agent.rotation_check(a, c)
        if degrees != -1:
            b_rotated = b.rotate(degrees)
            for i in self.answers():
                if self.is_same(b_rotated, self.open(i)):
                    return i
        return self.a_rotation_b()

    def a_rotation_b(self):
        """If B is a rotation of A then look for the rotation of C"""
        a, b, c = self.open("A", "B", "C")
        degrees = Agent.rotation_check(a, b)
        if degrees != -1:
            c_rotated = c.rotate(degrees)
            for i in self.answers():
                if self.is_same(c_rotated, self.open(i)):
                    return i
        return -1

    def a_2_b_as_c_2_x(self):
        """A is to B as C is to X"""
        a, b, c = self.open("A", "B", "C")
        sim_score = math.floor(Agent.similarity_score(a, b) * 100)
        for i in self.answers():
            if Agent.margin_of_error(math.floor(Agent.similarity_score(c, self.open(i)) * 100), sim_score):
                return i
        return self.a_2_c_as_b_2_x()

    def a_2_c_as_b_2_x(self):
        """A is to C as B is to X"""
        a, b, c = self.open("A", "B", "C")
        sim_score = math.floor(Agent.similarity_score(a, c) * 100)
        for i in self.answers():
            if Agent.margin_of_error(math.floor(Agent.similarity_score(b, self.open(i)) * 100), sim_score):
                return i
        return -1

    def a_fill_b(self):
        """
        Note: this can easily create false positives and should go last in the thinking pipeline
        If A Filled solid is the same as B then look for answer that is C filled solid
        """
        a, b, c = self.open("A", "B", "C")
        if self.is_same(Agent.fill_shape(a), b):
            for i in self.answers():
                if self.is_same(Agent.fill_shape(c), self.open(i)):
                    return i
        return self.a_fill_c()

    def a_fill_c(self):
        """
        Note: this can easily create false positives and should go last in the thinking pipeline
        If A Filled solid is the same as C then look for answer that is B filled solid
        """
        a, b, c = self.open("A", "B", "C")
        if self.is_same(Agent.fill_shape(a), c):
            for i in self.answers():
                if self.is_same(Agent.fill_shape(b), self.open(i)):
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
        return Agent.similarity_score(a, b) >= .95

    @staticmethod
    def rotation_check(a, b):
        """"Returns -1 if no match is found otherwise it returns the matching rotation"""
        if Agent.close_enough(a.rotate(90), b):
            return 90
        if Agent.close_enough(a.rotate(180), b):
            return 180
        if Agent.close_enough(a.rotate(270), b):
            return 270
        return -1

    @staticmethod
    def similarity_score(a, b):
        np_a = np.array(a)
        np_b = np.array(b)
        return np.mean(np_a == np_b)

    @staticmethod
    def fill_shape(a):
        ImageDraw.floodfill(a, xy=(0, 0), value=(255, 0, 255), thresh=200)  # fill around shape with magenta
        a = np.array(a)
        a[(a[:, :, 0:3] != [255, 0, 255]).any(2)] = [0, 0, 0]  # fill remaining white pixes with black
        a[(a[:, :, 0:3] == [255, 0, 255]).all(2)] = [255, 255, 255]  # Revert magenta pixels to white
        return Image.fromarray(a)

    @staticmethod
    def margin_of_error(a, b, moe=1):
        """
        This will check if the values are within the margin of error
        3 give or take
        """
        if a - moe <= b <= a + moe:
            return True
        return False
