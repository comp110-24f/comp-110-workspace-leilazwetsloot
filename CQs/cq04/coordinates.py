"""Part of Challenge Question 04 - Importing and Scope"""

__author__ = "730776566"


def get_coords(xs: str, ys: str) -> None:
    """finding the ordered pairs of the two strings"""
    xsindex: int = 0
    ysindex: int = 0
    while xsindex < len(xs):
        while ysindex < len(ys):  # nested while loop, clarified from ed stem
            print("(" + xs[xsindex] + "," + ys[ysindex] + ")")
            ysindex += 1
        xsindex += 1
        ysindex = 0  # must reset or inside y while loop wont run
