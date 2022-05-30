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

SCREENSHOTS
MAIN SCREEN:
![00](https://user-images.githubusercontent.com/98827445/171038189-32f0cd52-0af2-4b33-8b4a-2f06972f2cfc.png)

ENTERING OF ID AND PASSWORD
![01](https://user-images.githubusercontent.com/98827445/171038301-56405847-d5f1-445e-9123-60b4190eb2b3.png)

THEN CLICK ON TAKE IMAGE 
![image](https://user-images.githubusercontent.com/98827445/171038852-eec6eb8d-b29b-49d7-9337-b06049abb511.png)

THEN SAVE YOUR PROFILE BY ENTERING YOUR PASSWORD 
![03](https://user-images.githubusercontent.com/98827445/171038962-13884498-e86a-427c-970e-bddabd306be9.png)
After saving your profile the total registration will change to 1, now as you have registred yourself you can finally take your attendance.

TAKING ATTENDANCE:
![image](https://user-images.githubusercontent.com/98827445/171039341-025ff978-b62d-44c1-8df4-2e93cc87db0f.png)
press Q for recording your attendance 

walla! we are finally done with attendance part now.

SHOWING ATTENDANCE TAKEN:
![image](https://user-images.githubusercontent.com/98827445/171039711-df5bf298-e8b1-4af8-84e4-061b7f15747f.png)

ADDITIONAL HELP OPTION IN MENUBAR:
![04](https://user-images.githubusercontent.com/98827445/171039810-f2183a03-c8fa-4537-a8b3-51c0c29e2d49.png)

CHANGE PASSWORD OPTION:
![05](https://user-images.githubusercontent.com/98827445/171039925-5886437a-5b0a-4ebb-adf5-aa7be73534e7.png)


# Microsoft-Project(Project_2)
Prerequisites
For vision:

Tensorflow>2
OpenCV
sklearn=0.19.1 # for face spoofing. 
The model used was trained with this version and does not support recent ones.

Vision
It has six vision based functionalities right now:

Track eyeballs and report if the candidate is looking left, right, or up.
Find if the candidate opens his mouth by recording the distance between lips at starting.
Head pose estimation to find where the person is looking.
Security alarm to help in detecting the movement 
Face spoofing detection


One’s body movement-based functionality:
Security alarm

Lastly, 2 gesture-based
Brightness control 
volume control

With the help of all these features cheating in online exams will become almost impossible as your eye, lips, head posture, etc will all get monitored.

Apart from that, a student might want to fix the volume or brightness of his or her pc during either duration of the exam. For both these purposes, he/she can use his or her hand gestures. 
Implementation of all these techniques will leave no reason for a student to sit near his or her device and hence proctoring in online exams will become more efficient and easier with time.

Eye tracking
eye_tracker.py is to track eyes
![image](https://user-images.githubusercontent.com/98827445/171060382-3f52f584-0782-45a0-bb24-76a985be3fa2.png)

Mouth Opening Detection
mouth_opening_detector.py is used to check if the candidate opens his/her mouth during the exam after recording it initially. 
![image](https://user-images.githubusercontent.com/98827445/171060439-d58435cf-ae02-46d0-8574-61c5fc982069.png)
![image](https://user-images.githubusercontent.com/98827445/171060529-adb9eae0-cd0d-42c3-83fd-6956f43c9685.png)
![image](https://user-images.githubusercontent.com/98827445/171060612-ef4c515b-e477-4326-a87f-2f797bf938c2.png)


Head pose estimation
head_pose_estimation.py is used for finding where the head is facing.
![image](https://user-images.githubusercontent.com/98827445/171060822-7ada0f68-7299-4e49-8f08-9332e7a20831.png)
![image](https://user-images.githubusercontent.com/98827445/171060747-ab84ec85-d0d2-4e72-856a-ccd594b30ff4.png)




Face spoofing
face_spoofing.py is used for finding whether the face is real or a photograph or image

Even thought i have not included it in my gui. the code for it is available on my github.

Security alarm
![image](https://user-images.githubusercontent.com/98827445/171061246-d98b253a-ce6d-49a4-b8e8-6297b783a3f2.png)
![image](https://user-images.githubusercontent.com/98827445/171061300-5b19087e-ae48-4b13-a24f-29e62a04c8ad.png)


Brightness control 
![image](https://user-images.githubusercontent.com/98827445/171061153-217900e5-f652-4cc1-9cb5-0c4d399e0eb8.png)


Volume control
![image](https://user-images.githubusercontent.com/98827445/171061041-2e290cf9-5b0b-4ca6-b7ca-1d6713226733.png)

Attendance system
![image](https://user-images.githubusercontent.com/98827445/171061384-a10f5e65-4c5d-427b-b5da-8ca884d59d4c.png)


Final GUI in dark mode
![image](https://user-images.githubusercontent.com/98827445/171060127-e041b5bc-3992-4125-99b7-35e83a21418c.png)

Final GUI in light mode
![image](https://user-images.githubusercontent.com/98827445/171060202-c20c7e59-183e-4e33-9ac2-6498dcdeda17.png)

Additional features of my project include
1. Voice input
2. Face makeup
3. Face blur
4. Face age detection
5. Face emotion detection 

Future Scope
1. Room for improving accuracy
2. Multithreading implementataion, etc.

Additional document
[Microsoft Engage Project 2022_Documentation.docx](https://github.com/Lavanyadoohan/Microsoft-Project/files/8800809/Microsoft.Engage.Project.2022_Documentation.docx)



