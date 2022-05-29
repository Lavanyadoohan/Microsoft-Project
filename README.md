# Microsoft-Project(Project_1)
A python GUI integrated attendance system using face recognition to take attendance.

In this python project, I have made an attendance system which takes attendance by using face recognition technique. I have also intergrated it with GUI (Graphical user interface) so it can be easy to use by anyone. GUI for this project is also made on python using tkinter.

TECHNOLOGY USED:

tkinter for whole GUI
OpenCV for taking images and face recognition (cv2.face.LBPHFaceRecognizer_create())
CSV, Numpy, Pandas, datetime etc. for other purposes.
FEATURES:

Easy to use with interactive GUI support.
Password protection for new person registration.
Creates/Updates CSV file for deatils of students on registration.
Creates a new CSV file everyday for attendance and marks attendance with proper date and time.
Displays live attendance updates for the day on the main screen in tabular format with Id, name, date and time.

# Microsoft-Project(Project_2)
Prerequisites
For vision:

Tensorflow>2
OpenCV
sklearn=0.19.1 # for face spoofing. 
The model used was trained with this version and does not support recent ones.

Vision
It has six vision based functionalities right now:

Track eyeballs and report if candidate is looking left, right or up.
Find if the candidate opens his mouth by recording the distance between lips at starting.
Instance segmentation to count number of people and report if no one or more than one person detected.
Find and report any instances of mobile phones.
Head pose estimation to find where the person is looking.
Face spoofing detection
Face detection
Earlier, Dlib's frontal face HOG detector was used to find faces. However, it did not give very good results. In face_detection different face detection models are compared and OpenCV's DNN module provides best result and the results are present in this article.

It is implemented in face_detector.py and is used for tracking eyes, mouth opening detection, head pose estimation, and face spoofing.

An additional quantized model is also added for face detector as described in Issue 14. This can be used by setting the parameter quantized as True when calling the get_face_detector(). On quick testing of face detector on my laptop the normal version gave ~17.5 FPS while the quantized version gave ~19.5 FPS. This would be especially useful when deploying on edge devices due to it being uint8 quantized.

Facial Landmarks
Earlier, Dlib's facial landmarks model was used but it did not give good results when face was at an angle. Now, a model provided in this repository is used. A comparison between them and the reason for choosing the new Tensorflow based model is shown in this article.

It is implemented in face_landmarks.py and is used for tracking eyes, mouth opening detection, and head pose estimation.

Note
If you want to use dlib models then checkout the old-master branch.

Eye tracking
eye_tracker.py is to track eyes. A detailed explanation is provided in this article. However, it was written using dlib.!
![image](https://user-images.githubusercontent.com/98827445/170885709-d8fbed08-afb1-4958-99b8-8ad2667d9d12.png)

