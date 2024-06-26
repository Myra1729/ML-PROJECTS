import cv2
import numpy as np

def get_limits(color):
    c=np.uint8([[color]])
    hsvc=cv2.cvtColor(c,cv2.COLOR_BGR2HSV)
    lower=hsvc[0][0][0]-10,50,50
    upper=hsvc[0][0][0]+10,255,255
    lower=np.array(lower,dtype=np.uint8)
    upper=np.array(upper,dtype=np.uint8)
    return lower,upper


# Define the lower and upper bounds for the HSV color range
yellow=[0,255,255]
lower,upper=get_limits(yellow)

# Capture video from the default camera (index 0)
vid=cv2.VideoCapture(0)

while True:
    # Read a frame from the video stream
    success, video = vid.read()
    
    # Convert the frame from RGB to HSV color space
    img=cv2.cvtColor(video, cv2.COLOR_BGR2HSV)
    
    # Apply a mask to the HSV image based on the defined color range
    mask=cv2.inRange(img, lower, upper)
    
    # Find contours in the masked image
    contours, hier = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through the contours
    if len(contours) != 0:
        for contour in contours:
            # Check if the contour area is greater than or equal to 400
            if cv2.contourArea(contour) >= 400:
                # Get the bounding rectangle coordinates
                x0, y0, w, h = cv2.boundingRect(contour)
                # Draw a rectangle around the contour on the original video frame
                cv2.rectangle(video, (x0, y0), (x0+w, y0+h), (255, 0, 0), 5)

    # Display the original video and the masked video
    cv2.imshow("Original", video)
    cv2.imshow("Black mask", mask)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

vid.release()
# Release video capture and close windows
cv2.destroyAllWindows()
