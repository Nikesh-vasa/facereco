import cv2

cam_port = 0
cam = cv2.VideoCapture(cam_port)

inp = input("Enter the person Name: ")

while True:
    result, image = cam.read()
    cv2.imshow(inp, image)
    
    key = cv2.waitKey(1)
    if key == ord('q'):  # Press 'q' to quit
        print("Exiting...")
        break
    elif key == ord('s'):  # Press 's' to save the image
        cv2.imwrite(inp + ".png", image)
        print("Image Saved.")
        break

cam.release()
cv2.destroyAllWindows()
