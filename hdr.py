import cv2
import math
import numpy as np
import sympy as sp
from decimal import *

def weight_calc(number):
    order = 6 * (number / 255) - 3
    weight = math.exp(-(order ** 2))
    return weight

def hdr_comp(val1, val2, val3, val4):
    w1 = weight_calc(val1)
    w2 = weight_calc(val2)
    w3 = weight_calc(val3)
    w4 = weight_calc(val4)
    
    final_val = math.sqrt((50 / 3 * w1 * val1 + w2 * val2 + 1 / 7.5 * w3 * val3 + 320 / 3 * w4 * val4) / (50 / 3 * w1 + w2 + 1 / 7.5 * w3 + 320 / 3 * w4))
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
            img_write[y][x][0] = int(hdr_comp((50 / 3 * low2[y][x][0]) ** 2,
                                                        low1[y][x][0] ** 2,
                                                        (1 / 7.5 * high1[y][x][0]) ** 2,
                                                        (320 / 3 * high2[y][x][0]) ** 2))
            img_write[y][x][1] = int(hdr_comp((50 / 3 * low2[y][x][1]) ** 2,
                                                        low1[y][x][1] ** 2,
                                                        (1 / 7.5 * high1[y][x][1]) ** 2,
                                                        (320 / 3 * high2[y][x][1]) ** 2))
            img_write[y][x][2] = int(hdr_comp((50 / 3 * low2[y][x][2]) ** 2,
                                                        low1[y][x][2] ** 2,
                                                        (1 / 7.5 * high1[y][x][2]) ** 2,
                                                        (320 / 3 * high2[y][x][2]) ** 2))

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


