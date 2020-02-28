import cv2
import math
import numpy as np
import scipy as sp
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
    low2 = cv2.imread("lake-time-10.png")
    low1 = cv2.imread("test.png")
    high1 = cv2.imread("high1.png")
    high2 = cv2.imread("high2.png")

    #initialize the output picture array
    img_write = np.zeros((len(low2), len(low2[0]), 3))

    #convert back to light range
    q_low1 = np.array((len(low1), len(low2[0]), 3), dtype = np.uint32)
    q_low2 = np.array((len(low2), len(low2[0]), 3), dtype = np.uint32)
    q_low1 = np.square(low1, dtype = np.uint16)
    q_low2 = np.square(low2, dtype = np.uint16)

    q_total = np.array((len(low2), len(low2[0]), 3), dtype = np.float)

    q_total = np.add(q_low1, 0.5 * q_low2, dtype = np.float)
    '''
    print("low1")
    print(low1[3357][5537])
    print("q1")
    print(q_low1[3537][5537])

    print("low2")
    print(low2[3357][5537])
    print("q2")
    print(q_low2[3357][5537])

    print("after sum")
    print(q_total[3357][5537])
    '''
    q_total = q_total / 1.5


    q_total = np.ceil(np.sqrt(q_total))
    '''
    print("after sqrt")
    print(q_total[3357][5537])
        
    #print("to write to the file")
    #print(img_write)
    '''
    #output image
    cv2.imwrite("hdr_lake.png", q_total)

process()


