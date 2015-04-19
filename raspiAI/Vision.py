#Possible video solution http://stackoverflow.com/questions/16493008/using-opencv-detectmultiscale-to-find-my-face
#good site http://docs.opencv.org/modules/contrib/doc/facerec/facerec_tutorial.html
import os
import sys
import numpy as np
import cv2
import cv2.cv as cv

__version__ = '0.1.20150419'
__author__ = "JPSIII and sjs_20012001"
__url__ = 'https://github.com/joesox/raspiAI'
__doc__ = "Twitter Class to work with TwitterAPI."

class Vision(object):
    """description of Vision class"""
    def __repr__(self):
        if not self:  
            return 'Attrs()'  
        return '<%s>' % (self.__class__.__name__)

    def detect(self, img, cascade):
        rects = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=3, minSize=(10, 10), flags = cv.CV_HAAR_SCALE_IMAGE)
        if(len(rects) == 0):
            return []
        rects[:,2:] += rects[:,:2]
        return rects

    def draw_rects(self, img, rects, color):
        for x1, y1, x2, y2 in rects:
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

    def FollowFaceVideo(self, cascade):
        """ Capture video feed frame-by-frame; Draw a rectangle around the faces; Display the resulting frame  """
        try:
            cascPath = cascade
            faceCascade = cv2.CascadeClassifier(cascPath)
            video_capture = cv2.VideoCapture(0)
            while True:
                # Capture frame-by-frame
                ret, frame = video_capture.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30),
                    flags=cv2.cv.CV_HAAR_SCALE_IMAGE
                )

                # Draw a rectangle around the faces
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                # Display the resulting frame
                cv2.imshow('Video', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            # When everything is done, release the capture
            video_capture.release()
            cv2.destroyAllWindows()
        except NameError, x:
            print 'Exception: ', x

def demo():
    v = Vision()
    img = cv2.imread('image.jpg',cv2.CV_LOAD_IMAGE_COLOR)  ## Read image file
    if (img == None):                                      ## Check for invalid input
        print "Could not open or find the image"
    else:
        cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        gray = cv2.equalizeHist(gray)

        rects = v.detect(gray, cascade)

        ## Extract face coordinates
        x1 = rects[0][1]
        y1 = rects[0][0]
        x2 = rects[0][3]
        y2 = rects[0][2]

        ## Extract face ROI
        faceROI = gray[x1:x2, y1:y2]

        ## Show face ROI
        cv2.imshow('Display face ROI', faceROI)

        vis = img.copy()
        v.draw_rects(vis, rects, (0, 255, 0))
    cv2.namedWindow('Display image')          ## create window for display
    cv2.imshow('Display image', vis)          ## Show image in the window

    print "size of image: ", img.shape        ## print size of image
    cv2.waitKey(0)                            ## Wait for keystroke
    cv2.destroyAllWindows()                   ## Destroy all windows
    print "Finished Vision demo!"

def demo2():
    v = Vision()
    v.FollowFaceVideo("haarcascade_frontalface_alt.xml")

if __name__ == '__main__':
    demo()
