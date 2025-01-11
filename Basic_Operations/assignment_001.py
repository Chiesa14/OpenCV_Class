import cv2

#change the location according to your folder structure
image = cv2.imread('Basic_Operations/assignment-001-given.jpg')

cv2.rectangle(image, (264, 194), (987, 920), (0, 255, 0), 10)

text = "RAH972U"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 3
thickness = 8
text_color = (0, 255, 0)

(text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, thickness)

text_x, text_y = 835, 155

overlay = image.copy()

cv2.rectangle(overlay, 
              (text_x-2, text_y - text_height-20),  
              (text_x + text_width-6, text_y+baseline),
              (0, 0, 0),-1)

alpha = 0.5  
blended_image = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

cv2.putText(blended_image, text, (text_x, text_y), font, font_scale, text_color, thickness)

cv2.imshow('Image', blended_image)

cv2.waitKey(0)

cv2.imwrite('output/assignment-001-solution.jpg', blended_image)

cv2.destroyAllWindows()