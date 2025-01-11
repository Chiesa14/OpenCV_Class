import cv2  # Import OpenCV library

# Read the image 'lena_small.jpg'
image = cv2.imread('Basic_Operations/lena_small.jpg')

# Flip the image horizontally (1 = horizontal flip)
flipped_image = cv2.flip(image, 1)
flipped_image = cv2.flip(flipped_image, 0)

# Display the flipped image in a window
cv2.imshow('Image before flip', image)
cv2.waitKey(0)
cv2.imshow('Image after flip', flipped_image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the flipped image to a new file
cv2.imwrite('output/lena_flipped.jpg', flipped_image)

# Close all OpenCV windows
cv2.destroyAllWindows()