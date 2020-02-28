import cv2
import math
import numpy as np
import sympy as sp
from decimal import *

def weight_calc(number):
    order = 6 * (number / 255) - 3
    weight = math.exp(-(order ** 2))
    return weight

def hdr_comp(val1, val2):
    w1 = weight_calc(val1)
    w2 = weight_calc(val2)
    
    final_val = math.sqrt(w1 * val1 + w2 * val2)
    return final_val

def process():
    low2 = cv2.imread("low2.png")
    low1 = cv2.imread("low1.png")
    high1 = cv2.imread("high1.png")
    high2 = cv2.imread("high2.png")
    
    #initialize the output picture array
    img_write = np.zeros((len(low2), len(low2[0]), 3))

    for y in range(len(low2)):
        for x in range(len(low2[0])):
            print("y is", y , "x is", x)
            img_write[y][x][0] = int(hdr_comp((low2[y][x][0]) ** 2,
                                                        low1[y][x][0] ** 2))
            img_write[y][x][1] = int(hdr_comp((low2[y][x][1]) ** 2,
                                                        low1[y][x][1] ** 2))
            img_write[y][x][2] = int(hdr_comp((low2[y][x][2]) ** 2,
                                                        low1[y][x][2] ** 2))

            #handle the overflow cases(8bit = 255)
            if img_write[y][x][0] > 255:
                img_write[y][x][0] = 255;

            if img_write[y][x][1] > 255:
                img_write[y][x][1] = 255;

            if img_write[y][x][2] > 255:
                img_write[y][x][2] = 255;

    #output image
    cv2.imwrite("hdr_out.png", img_write)

process()


