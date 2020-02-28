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

    img_write = np.add(low1, low2)

    img_write = img_write / 510 * 255

    #output image
    cv2.imwrite("hdr_out.png", img_write)

process()


