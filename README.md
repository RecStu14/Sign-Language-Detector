# Sign-Language-Recognition
The Dataset used in this project is the **American Sign Language Letters Dataset** which is publicly accessed from Roboflow. (https://public.roboflow.com/object-detection/american-sign-language-letters/1)

In this branch an **image classification** approach was used to classify the hand gestures, however, this resulted in the model largely overfitting due to the presence of many background details that were memorised by the model. Hence, this proves that a better appraoch would be the **object detection** appraoch where the area of the image to be learned by the model is clearly marked by bounding boxes as well as labels.
