#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 13:14:22 2022

@author: micahross
"""


infile = open("/Users/micahross/Documents/Work 2022/Python Code/gps.txt", "r")
lines = infile.readlines()
#print (lines)

outfile = open('/Users/micahross/Documents/Work 2022/Python Code/gps_pix4d_format.txt', 'w')

with open('/Users/micahross/Documents/Work 2022/Python Code/gps.txt', 'r') as f:
        my_list = [line.rstrip('/n') for line in f]

#print (my_list)

for i in my_list[:]:
    #print (i)
    imgnum, long, lat, alt, o,p,k, time =i.split(",")
    #print (imgnum)
    out_imgnum = imgnum.rstrip('.img') + '.TIF'
    #print (out_imgname)	
    outfile.write(out_imgnum+","+lat+","+long+","+alt +"\n")

infile.close()
outfile.close()


    

