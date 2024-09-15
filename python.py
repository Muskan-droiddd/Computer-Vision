# images.py
import cv2

def load_image(image_path):
    # Load an image from the specified file
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Could not load image.")
        return None

    # Return the loaded image
    return image

if __name__ == "__main__":
    # Use relative path to the image in the same directory
    image_path = "image.jpg"  # Replace this with the name of your image
    image = load_image(image_path)

    if image is not None:
        # Display the image in a window
        cv2.imshow("Loaded Image", image)

        # Wait for a key press and close the window
        cv2.waitKey(0)
        cv2.destroyAllWindows()
