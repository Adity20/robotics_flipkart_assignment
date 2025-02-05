## This is the Image_Detection part of the project that allows you to be able to pass an image and get the detection on it.

#WARNING: It would be save a lot of time,and generally be more convenient if it is ran all at once in the main RPF.ipynb.
# This is due to RFD module having reloading the 'detection_model1' object just for a single use.

from RFD import run_inference_for_single_image
# from RFD import RBF
from RFD import Boxes
from RFD import detection_model1
import cv2




# image = "download(1).jpg"
image = cv2.imread("tes(1).jpg")
image = cv2.resize(image, (800, 600))


# shape = list(image.shape)
# im_height = int(shape[0])
# im_width =int(shape[1])


def RBF(detection_model, image):
    output_dict = run_inference_for_single_image(detection_model, image)
    box0 = Boxes(0, image)
    box1 = Boxes(1, image)
    box2 = Boxes(2, image)
    #     if (output_dict['detection_classes'][0]==1) & (output_dict['detection_scores'][0]>= 0.5):
    #         if output_dict['detection_scores'][0]>= 0.5:

    image = cv2.rectangle(image, (box0.xmin, box0.ymin), (box0.xmax, box0.ymax), box0.colour, 2)
    image = cv2.rectangle(image, (box0.xmin, box0.ymin - 60), (box0.xmax, box0.ymin), box0.colour, -1)
    image = cv2.putText(image, box0.label, (box0.xmin, box0.ymin - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255),
                        2)
    image = cv2.putText(image, box0.ripeness, (box0.xmin, box0.ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                        (255, 255, 255), 2)

    #             if output_dict['detection_scores'][1]>= 0.5:

    image = cv2.rectangle(image, (box1.xmin, box1.ymin), (box1.xmax, box1.ymax), box1.colour, 2)
    image = cv2.rectangle(image, (box1.xmin, box1.ymin - 60), (box1.xmax, box1.ymin), box1.colour, -1)
    image = cv2.putText(image, box1.label, (box1.xmin, box1.ymin - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255),
                        2)
    image = cv2.putText(image, box1.ripeness, (box1.xmin, box1.ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                        (255, 255, 255), 2)

    #             if output_dict['detection_scores'][2]>= 0.5:

    image = cv2.rectangle(image, (box2.xmin, box2.ymin), (box2.xmax, box2.ymax), box2.colour, 2)
    image = cv2.rectangle(image, (box2.xmin, box2.ymin - 60), (box2.xmax, box2.ymin), box2.colour, -1)
    image = cv2.putText(image, box2.label, (box2.xmin, box2.ymin - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255),
                        2)
    image = cv2.putText(image, box2.ripeness, (box2.xmin, box2.ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                        (255, 255, 255), 2)
    #     image = cv2.resize(image, (800, 600))
    return image


# In[63]:


cv2.imshow('image', RBF(detection_model1, image))

cv2.waitKey(0)
cv2.destroyAllWindows()
