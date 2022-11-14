#-------------------------------------------------------------------------------
# Name:        Negative Filter, Blemish removal and hough tranform circle  
# Purpose:  Assignment Deployment using Streamlit
#
# Author:      Aditya B.
#
# Created:     10-11-2022
# Copyright:   (c) Aditya 2022
#-------------------------------------------------------------------------------

import cv2
import streamlit as st
import numpy as np
import cv2
from PIL import Image, ImageFilter



def main():
    st.title("Assignment 3")
    html_temp = """
    <div style="background-color:cyan;padding:10px">
    <h4 style="color:black;text-align:center;">Filter, Blemish removal and Hough Transform for circles</h4>
    <h5 style="color:black;text-align:right;">Author: Aditya B.</h5>
    </div><br>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    image_file = st.file_uploader("Choose a image file", type="jpg")
    if image_file is not None:
        file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)

        if st.button('Negative Filter'):
            inv = cv2.bitwise_not(img)
            st.image(inv, channels="BGR")
        if st.button('Blemish Removal'):
            image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # convert to HSV
            figure_size = 11 # the dimension of the x and y axis of the kernal.
            new_image = cv2.medianBlur(image, figure_size)
            image=cv2.cvtColor(image, cv2.COLOR_HSV2RGB)

            st.image(img, channels="BGR", caption="Original Image")
            st.image(image, channels="RGB", caption="Bleshish Removed Image")

        if st.button('Hough Transform for circles'):
            img_copy = img.copy()
            img = cv2.medianBlur(img,3)
            # Convert to greyscale
            img_gray = cv2.cvtColor(img_copy,cv2.COLOR_BGR2GRAY)
            # Apply Hough transform to greyscale image
            circles = cv2.HoughCircles(img_gray,cv2.HOUGH_GRADIENT,1,20,
                                 param1=60,param2=40,minRadius=0,maxRadius=0)
            circles = np.uint16(np.around(circles))
            # Draw the circles
            for i in circles[0,:]:
                # draw the outer circle
                cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
                # draw the center of the circle
                cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
            st.image(img, caption="Hough Transform for circles")



if __name__ == '__main__':
    main()
