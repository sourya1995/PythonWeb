import cv2
import numpy as np
import glob

frameSize = (1000, 1000)
frameRate = 10

out = cv2.VideoWriter('output/output_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), frameRate, frameSize)

for i in range(0, 11):
    filename = 'data/astr/' + str(i) + '.png'
    img = cv2.imread(filename)
    out.write(img)

out.release()