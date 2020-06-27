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
    all_alpha = list("ABC")

    def __init__(self):
        self.answer_indexes = [1, 7]
        self.white = (255, 255, 255)
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
        if problem.problemType == "3x3":
            Agent.all_alpha = list("ABCDEFGH")
            return self.solve_3x3(problem)
        if problem.problemType == "2x2":
            Agent.all_alpha = list("ABC")
            return self.solve_2x2(problem)

        print("Error: need to debug if you get here!")
        return -1

    def solve_2x2(self, problem):
        answer = self.all_same_check()
        if answer is not -1:
            print(problem.name, problem.problemType, "all_same_check")
            return answer
        answer = self.is_a_c()
        if answer is not -1:
            print(problem.name, problem.problemType, "is_a_c")
            return answer
        answer = self.a_mirror_b()
        if answer is not -1:
            print(problem.name, problem.problemType, "a_mirror_b")
            return answer
        answer = self.a_rotation_c()
        if answer is not -1:
            print(problem.name, problem.problemType, "a_rotation_c")
            return answer
        answer = self.a_2_b_as_c_2_x()
        if answer is not -1:
            print(problem.name, problem.problemType, "a_2_b_as_c_2_x")
            return answer
        answer = self.a_fill_b()
        if answer is not -1:
            print(problem.name, problem.problemType, "a_fill_b")
            return answer
        answer = self.point_of_intersection()
        if answer is not -1:
            print(problem.name, problem.problemType, "point_of_intersection")
            return answer

        print(problem.name, problem.problemType)
        return -1  # I am changing this from -1. If nothing else if found a shot in the dark is better than a skip

    def solve_3x3(self, problem):
        answer = self.all_same_3x3()
        if answer is not -1:
            print(problem.name, problem.problemType, "all_same_3x3")
            return answer
        answer = self.pixel_growth()
        if answer is not -1:
            print(problem.name, problem.problemType, "pixel_growth")
            return answer
        answer = self.point_of_intersection()
        if answer is not -1:
            print(problem.name, problem.problemType, "point_of_intersection")
            return answer
        answer = self.a_2_b_as_c_2_x(["E", "F", "H"])
        if answer is not -1:
            print(problem.name, problem.problemType, "e_2_f_as_h_2_x")
            return answer
        return -1

    # below are root thinking methods

    def pixel_growth(self):
        """calculate the growth of pixels"""
        a, b, c, d, e, f, g, h = self.open("A", "B", "C", "D", "E", "F", "G", "H")
        # b_sum = Agent.black_pixel_sum(b)
        # c_sum = Agent.black_pixel_sum(c)
        # e_sum = Agent.black_pixel_sum(e)
        # f_sum = Agent.black_pixel_sum(f)
        h_sum = Agent.black_pixel_sum(h)
        g_sum = Agent.black_pixel_sum(g)
        if Agent.margin_of_error(h_sum, g_sum, 10):
            return -1
        # avg = ((c_sum-b_sum) + (f_sum-e_sum))/2
        avg = h_sum - g_sum
        for i in self.answers():
            i_sum_diff = Agent.black_pixel_sum(self.open(i)) - h_sum
            if Agent.margin_of_error(avg, i_sum_diff, 200):
                return i
        return -1


    def euclidean_distance(self):
        """Find the closest using Euclid Dist"""
        g, h = self.open("G", "H")
        dist = np.linalg.norm(g - h)

    def all_same_check(self):
        """If A==B==C then look for A==i"""
        a, b, c = self.open("A", "B", "C")
        if self.is_same(a, b, c):
            best_match = self.check_best_match(a)
            if self.is_same(a, self.open(best_match)):
                return best_match
        return -1

    def all_same_3x3(self):
        """If A==B==C then look for A==i"""
        a, b, c, d, e, f, g, h = self.open("A", "B", "C", "D", "E", "F", "G", "H")
        if self.is_same(a, b, c) and self.is_same(d, e, f) and self.is_same(g, h):
            best_match = self.check_best_match(g)
            if self.is_same(g, self.open(best_match)):
                return best_match
        return -1

    def is_a_c(self):
        """If A==C then look for B==i"""
        a, b, c = self.open("A", "B", "C")
        if self.strict_same(a, c):
            best_match = self.check_best_match(b)
            if self.is_same(b, self.open(best_match)):
                return best_match
        return self.is_a_b()  # try the other way

    def is_a_b(self):
        """If A==B then look for C==i"""
        a, b, c = self.open("A", "B", "C")
        if self.strict_same(a, b):
            best_match = self.check_best_match(c)
            if self.is_same(c, self.open(best_match)):
                return best_match
        return -1

    def a_mirror_b(self):
        """If B is a mirror of A then look for the mirror of C"""
        a, b, c = self.open("A", "B", "C")
        a_mirror = ImageOps.mirror(a)
        if self.is_same(a_mirror, b):
            c_mirror = ImageOps.mirror(c)
            best = self.check_best_match(c_mirror)
            if self.is_same(c_mirror, self.open(best)):
                return best
        return self.a_mirror_c()

    def a_mirror_c(self):
        """If C is a mirror of A then look for the mirror of B"""
        a, b, c = self.open("A", "B", "C")
        a_mirror = ImageOps.mirror(a)
        if self.is_same(a_mirror, c):
            b_mirror = ImageOps.mirror(b)
            best = self.check_best_match(b_mirror)
            if self.is_same(b_mirror, self.open(best)):
                return best
        return -1

    def a_rotation_c(self):
        """If C is a rotation of A then look for the rotation of B"""
        a, b, c = self.open("A", "B", "C")
        degrees = Agent.rotation_check(a, c)
        if degrees != -1:
            b_rotated = Agent.rotate(b, degrees)
            best_match = self.check_best_match(b_rotated)
            if self.is_same(b_rotated, self.open(best_match)):
                return best_match
        return self.a_rotation_b()

    def a_rotation_b(self):
        """If B is a rotation of A then look for the rotation of C"""
        a, b, c = self.open("A", "B", "C")
        degrees = Agent.rotation_check(a, b)
        if degrees != -1:
            c_rotated = Agent.rotate(c, degrees)
            best_match = self.check_best_match(c_rotated)
            if self.is_same(c_rotated, self.open(best_match)):
                return best_match
        return -1

    def a_2_b_as_c_2_x(self, abc=None):
        """A is to B as C is to X"""
        if abc is None:
            abc = ["A", "B", "C"]
        a, b, c = self.open(abc[0], abc[1], abc[2])
        sim_score = math.floor(Agent.similarity_score(a, b) * 100)
        closest_match = self.best_similarity(c, Agent.similarity_score(a, b))
        if Agent.margin_of_error(math.floor(Agent.similarity_score(c, self.open(closest_match)) * 100), sim_score):
            return closest_match
        return self.a_2_c_as_b_2_x(abc)

    def a_2_c_as_b_2_x(self, abc=None):
        """A is to C as B is to X"""
        if abc is None:
            abc = ["A", "B", "C"]
        a, b, c = self.open(abc[0], abc[1], abc[2])
        sim_score = math.floor(Agent.similarity_score(a, c) * 100)
        closest_match = self.best_similarity(b, Agent.similarity_score(a, c))
        if Agent.margin_of_error(math.floor(Agent.similarity_score(b, self.open(closest_match)) * 100), sim_score):
            return closest_match
        return -1

    def a_fill_b(self):
        """
        Note: this can easily create false positives and should go last in the thinking pipeline
        If A Filled solid is the same as B then look for answer that is C filled solid
        """
        a, b, c = self.open("A", "B", "C")
        if self.is_same(Agent.fill_shape(a), b):
            c_filled = Agent.fill_shape(c)
            best_match = self.check_best_match(c_filled)
            if self.is_same(c_filled, self.open(best_match)):
                return best_match
        return self.a_fill_c()

    def a_fill_c(self):
        """
        Note: this can easily create false positives and should go last in the thinking pipeline
        If A Filled solid is the same as C then look for answer that is B filled solid
        """
        a, b, c = self.open("A", "B", "C")
        if self.is_same(Agent.fill_shape(a), c):
            b_filled = Agent.fill_shape(b)
            best_match = self.check_best_match(b_filled)
            if self.is_same(b_filled, self.open(best_match)):
                return best_match
        return -1

    def point_of_intersection(self):
        """
        Draw a line through an image and find the distance between white and black lines for all images. Then look for
        a growth pattern. If a pattern is found use the growth value to find the next image in the patter.
        If an image with the same growth value is found then use that image as the answer other wise return -1
        :return: number
        """
        pattern = Agent.return_pattern(self.all_pattern_shape_spacing())
        is_same = [0]
        for i in self.answers():
            is_same.append(0)  # initialize
            center_spacing = self.find_center_spacing(self.open(i))
            length = min(len(pattern), len(center_spacing))
            for x in range(length):
                if pattern[x] > 1:
                    if self.margin_of_error(center_spacing[x], pattern[x]):
                        if len(is_same) >= i:  # TODO: create else that detects false answers
                            is_same[i] += 1
        pos = int(np.argmax(is_same))
        if is_same[pos] > 0:
            return pos
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

    @staticmethod
    def strict_same(a, b, percent_same=.99):
        if percent_same == 1:
            return False if ImageChops.difference(a, b).getbbox() else True
        if ImageChops.difference(a, b).getbbox():
            if not Agent.close_enough(a, b, percent_same):
                return False
        return True

    def answers(self):
        return range(self.answer_indexes[0], self.answer_indexes[1])

    @staticmethod
    def close_enough(a, b, percent_same=.94):
        return Agent.similarity_score(a, b) >= percent_same

    @staticmethod
    def rotation_check(a, b):
        """"Returns -1 if no match is found otherwise it returns the matching rotation"""
        loop_count = int(360 / 15)
        for i in range(1, loop_count):
            if Agent.close_enough(Agent.rotate(a, 15 * i), b):
                return 15 * i
        return -1

    @staticmethod
    def similarity_score(a, b):
        np_a = np.array(a)
        np_b = np.array(b)
        return np.mean(np_a == np_b)

    @staticmethod
    def fill_shape(a):
        Agent.floodfill(a, xy=(0, 0), value=(255, 0, 255), thresh=200)  # fill around shape with magenta
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

    @staticmethod
    def rotate(a, degrees):
        rot = a.convert('RGBA').rotate(degrees, expand=0)
        fff = Image.new('RGBA', rot.size, (255,) * 4)
        out = Image.composite(rot, fff, rot)
        return out.convert(a.mode)

    def best_similarity(self, a, sim_score, moe=1):
        """This looks for closest match to sim_score of A"""
        low_val = [1, 1]  # [value, index]
        for i in self.answers():
            new_val = abs(sim_score - Agent.similarity_score(a, self.open(i)))
            if new_val < low_val[0]:
                low_val[0] = new_val
                low_val[1] = i
        return low_val[1]

    def check_best_match(self, a):
        """this will compare letter with all numbers and return the one closest to it"""
        high_val = [0, 1]  # [value, index]
        for i in self.answers():
            sim_score = Agent.similarity_score(a, self.open(i))
            if sim_score > high_val[0]:
                high_val[0] = sim_score
                high_val[1] = i
        return high_val[1]

    @staticmethod
    def consecutive_average(a):
        """add all consecutive numbers then divide by how many there are"""
        new_arr = []
        add_all = 0
        count = 1
        for x in range(len(a) - 1):
            if a[x + 1] == a[x] + 1:
                if count == 1:
                    add_all += a[x] + a[x + 1]
                else:
                    add_all += a[x + 1]
                count += 1
            else:
                new_arr.append(add_all / count)
                count = 1
                add_all = 0
        return new_arr

    @staticmethod
    def find_spacing(a, alignment):
        """calculate the distance between white and black pixels and return an array of distances"""
        np_a = np.array(a)
        return Agent.consecutive_average(np.unique(
            np.where((np_a[alignment % np_a.shape[1], :] > -1) * (np_a[alignment % np_a.shape[1], :] < 1))))

    @staticmethod
    def find_center_spacing(a):
        """calculate the distance between white and black pixels and return an array of distances"""
        np_a = np.array(a)
        return Agent.consecutive_average(
            np.unique(
                np.where(
                    (np_a[math.floor(np_a.shape[1] / 2), :] > -1) * (np_a[math.floor(np_a.shape[1] / 2), :] < 1)
                )))

    def all_pattern_shape_spacing(self):
        all_arrays = {}
        for i in Agent.all_alpha:
            all_arrays[i] = (Agent.find_center_spacing(self.open(i)))
        return all_arrays

    @staticmethod
    def black_pixel_sum(a):
        a = np.array(a)
        return ((-1 < a) & (a < 50)).sum()

    @staticmethod
    def return_pattern(obj, size="2x2"):
        """subtract each answer to see if you can use result to guess next img"""
        result = {}
        if size == "3x3":
            result = {
                "AB": [],
                "BC": [],
                "DE": [],
                "EF": [],
                "GH": []
            }
        if size == "2x2":
            result = {
                "AB": [],
                "BC": [],
            }
        total = []
        for x in result:
            length = min(len(obj[x[0]]), len(obj[x[1]]))  # always compare against the smaller of the two arrays
            for i in range(length - 1):
                result[x].append(abs(obj[x[0]][i] - obj[x[1]][
                    i]))  # TODO: go through this and check each value is growing/shrinking at the same rate if not set to 0. Also: let negitive values persist
                if len(total) <= i:
                    total.append(result[x][i])
                else:
                    total[i] += result[x][i]
        # print(result, "result")
        for t in range(len(total)):
            if total[t] > 1:
                total[t] = total[t] / len(result)
        return total

    # Below code is from PIL Library

    @staticmethod
    def _color_diff(color1, color2):
        """
        Uses 1-norm distance to calculate difference between two values.
        """
        if isinstance(color2, tuple):
            return sum([abs(color1[i] - color2[i]) for i in range(0, len(color2))])
        else:
            return abs(color1 - color2)

    @staticmethod
    def floodfill(image, xy, value, border=None, thresh=0):
        """
        (experimental) Fills a bounded region with a given color.
        :param image: Target image.
        :param xy: Seed position (a 2-item coordinate tuple). See
            :ref:`coordinate-system`.
        :param value: Fill color.
        :param border: Optional border value.  If given, the region consists of
            pixels with a color different from the border color.  If not given,
            the region consists of pixels having the same color as the seed
            pixel.
        :param thresh: Optional threshold value which specifies a maximum
            tolerable difference of a pixel value from the 'background' in
            order for it to be replaced. Useful for filling regions of
            non-homogeneous, but similar, colors.
        """
        # based on an implementation by Eric S. Raymond
        # amended by yo1995 @20180806
        pixel = image.load()
        x, y = xy
        try:
            background = pixel[x, y]
            if Agent._color_diff(value, background) <= thresh:
                return  # seed point already has fill color
            pixel[x, y] = value
        except (ValueError, IndexError):
            return  # seed point outside image
        edge = {(x, y)}
        # use a set to keep record of current and previous edge pixels
        # to reduce memory consumption
        full_edge = set()
        while edge:
            new_edge = set()
            for (x, y) in edge:  # 4 adjacent method
                for (s, t) in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    # If already processed, or if a coordinate is negative, skip
                    if (s, t) in full_edge or s < 0 or t < 0:
                        continue
                    try:
                        p = pixel[s, t]
                    except (ValueError, IndexError):
                        pass
                    else:
                        full_edge.add((s, t))
                        if border is None:
                            fill = Agent._color_diff(p, background) <= thresh
                        else:
                            fill = p != value and p != border
                        if fill:
                            pixel[s, t] = value
                            new_edge.add((s, t))
            full_edge = edge  # discard pixels processed
            edge = new_edge
