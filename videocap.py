import cv2
import time

def capture_image():
    cpt = cv2.VideoCapture(0)  

    if not cpt.isOpened():
        print("Error: Could not open webcam")
        return
    
    while True:
        ret, frame = cpt.read()
        if not ret:
            print("Error: Could not read frame")
            break
        
        cv2.imshow("Camera Preview - Press Enter to Capture", frame)

        # Wait for user input
        key = cv2.waitKey(1)
        if key == 13:  # Enter key (ASCII 13)
            break
        elif key == 27:  # Escape key (ASCII 27) - Cancel
            print("Photo capture cancelled.")
            cpt.release()
            cv2.destroyAllWindows()
            status = "stopped"
            return  status# Exit the function
    
    timestamp = time.strftime("%Y%m%d_%H%M%S")  
    image_path = f"images/captured_image_{timestamp}.jpg"
    cv2.imwrite(image_path, frame)
    
    print(f"Image saved as {image_path}")

    # Release resources
    cpt.release()
    cv2.destroyAllWindows()

    # Show the captured image
    img = cv2.imread(image_path)
    cv2.imshow("Captured Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return image_path
