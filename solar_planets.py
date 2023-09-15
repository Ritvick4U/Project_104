import cv2

loadimage = cv2.imread("solar-system.jpg")

cv2.putText(loadimage,"Sun",(20,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(loadimage,"Mercury",(110,180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(loadimage,"Venus",(190,270), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(loadimage,"Earth",(300,270), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(loadimage,"Mars",(400,270), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(loadimage,"Jupiter",(500,90), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(loadimage,"Saturn",(720,110), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(loadimage,"Uranus",(950,130), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(loadimage,"Neptune",(1080,130), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))


cv2.imwrite("Solar_Image_With_Text.jpg", loadimage)

cv2.imshow("output", loadimage)
cv2.waitKey(0)



