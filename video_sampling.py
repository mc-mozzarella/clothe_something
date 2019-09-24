import  numpy as np
import cv2
import sys
import argparse

def extractFrames(PathIn, PathOut):
    cap=cv2.VideoCapture(PathIn)
    success, img = cap.read()
    count = 0
    success = True
    while(success):
        cap.set(cv2.CAP_PROP_POS_MSEC,(count*100))
        success , img = cap.read()
        cv2.imwrite( PathOut + "frame%d.jpg"% count, img)
        count += 1


if __name__=="__main__":
    a=argparse.ArgumentParser()
    a.add_argument("--PathIn", help="path to video")
    a.add_argument("--PathOut", help = "path to frames")
    args = a.parse_args()
    print()
    extractFrames(args.PathIn, args.PathOut)
