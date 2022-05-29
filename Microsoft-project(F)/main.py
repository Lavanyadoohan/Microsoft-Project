# import all the sub functions
from eye_tracker import *
from head_pose_estimation import *
from Face_age_detection import *
from mouth_opening_detector import *
from gestureVolumeControl_v import *
from ScurityAlarm import *
from brightnessControl import *
from Face_detection_blur import *
from Face_emotion_detection import *
from Face_makeup import *
#from voiceinput import *
from attendance_s import *

# map this to the tkinter buttons

import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import PhotoImage

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def openProject(self):
        exec('brightnessControl.py')

    def __init__(self):
        super().__init__()

        self.title("My Project.py")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Main Features",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Eye Tracker",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.eye_tracker)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Head Pose Estimation",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.head_pose_estimation)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)
        # me
        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Mouth Opening Detector",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.mouth_opening_detector)
        self.button_3.grid(row=4, column=0, pady=10, padx=20)

        self.button_4 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Gesture Volume Control",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.play)
        self.button_4.grid(row=5, column=0, pady=10, padx=20)

        self.button_5 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Gesture Brightness Control",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.brightnessControl)
        self.button_5.grid(row=6, column=0, pady=10, padx=20)

        self.button_6 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Device Scurity Alarm",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.ScurityAlarm)
        self.button_6.grid(row=7, column=0, pady=10, padx=20)

        self.button_7 = customtkinter.CTkButton(master=self.frame_left,
                                               text="Attendance System",
                                               fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                               command=self.attendance_s)
        self.button_7.grid(row=8, column=0, pady=10, padx=20)

        self.switch_1 = customtkinter.CTkSwitch(master=self.frame_left,
                                                text="Dark Mode",
                                                command=self.change_mode)
        self.switch_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)


        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="Microsoft Engage 2022\n" +
                                                        "Final Project\n",
                                                   height=100,
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=45, pady=15)

        # ============ frame_right ============s

        self.radio_var = tkinter.IntVar(value=0)

        self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
                                                        text="Additional Features:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, pady=20, padx=10, sticky="")

        # self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_right,
        #                                                    variable=self.radio_var,
        #                                                    value=0)
        # self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

        # self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_right,
        #                                                    variable=self.radio_var,
        #                                                    value=1)
        # self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

        # self.radio_button_3 = customtkinter.CTkRadioButton(master=self.frame_right,
        #                                                    variable=self.radio_var,
        #                                                    value=2)
        # self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        # self.slider_1 = customtkinter.CTkSlider(master=self.frame_right,
        #                                         from_=0,
        #                                         to=1,
        #                                         number_of_steps=3,
        #                                         command=self.progressbar.set)
        # self.slider_1.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        # self.slider_2 = customtkinter.CTkSlider(master=self.frame_right,
        #                                         command=self.progressbar.set)
        # self.slider_2.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        self.slider_button_1 = customtkinter.CTkButton(master=self.frame_right,
                                                       height=25,
                                                       text="Voice Input",
                                                       command=self.voiceinput)
        self.slider_button_1.grid(row=2, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.slider_button_2 = customtkinter.CTkButton(master=self.frame_right,
                                                       height=25,
                                                       text="Face Makeup",
                                                       command=self.Face_makeup)
        self.slider_button_2.grid(row=3, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        #Face_age_detectionz
        self.slider_button_3 = customtkinter.CTkButton(master=self.frame_right,
                                                       height=25,
                                                       text="Face Blur",
                                                       command=self.Face_detection_blur)
        self.slider_button_3.grid(row=4, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.slider_button_4 = customtkinter.CTkButton(master=self.frame_right,
                                                       height=25,
                                                       text="Face Age Detection",
                                                       command=self.Face_age_detection)
        self.slider_button_4.grid(row=5, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.slider_button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                       height=25,
                                                       text="Face Emotion Detection.",
                                                       command=self.Face_emotion_detection)
        self.slider_button_5.grid(row=6, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Made by: Lavanya Doohan")
        self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")



        # set default values
        # self.radio_button_1.select()
        self.switch_1.select()
        # self.slider_1.set(0.2)
        # self.slider_2.set(0.7)
        # self.progressbar.set(0.5)
        # self.slider_button_1.configure(state=tkinter.DISABLED, text="Disabled Button")
        # self.radio_button_3.configure(state=tkinter.DISABLED)
        # self.check_box_1.configure(state=tkinter.DISABLED, text="CheckBox disabled")
        # self.check_box_2.select()


    def button_event(self):
        print("Button pressed")

    def eye_tracker(self):
        eye_tracker.main()

    def head_pose_estimation(self):
        head_pose_estimation.main()


    def play(self):
        flag = False
        if self.button_4 == "Button pressed":
            flag = True
        return volume()
        # print("Gesture")

    def Face_age_detection(self):
        Face_age_detection.main()

    def Face_makeup(self):
        Face_makeup.main()

    def attendance_s(self):
        attendance_s.main()

    def mouth_opening_detector(self):
        mouth_opening_detector.main()

    def brightnessControl(self):
        brightnessControl.main()

    def ScurityAlarm(self):
        ScurityAlarm.main()
        # print(Scurity)

    def Face_detection_blur(self):
        Face_detection_blur.main()

    def Face_emotion_detection(self):
        Face_emotion_detection.main()

    def voiceinput(self):
        voiceinput.main()

    def change_mode(self):
        if self.switch_1.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()