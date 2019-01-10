# Virtual_Look_Project

This purpose of this project is to able a user upload his/ her image with plain background and upload a image of hat/ cap with plain background to check how the hat/ cap looks on the user.

This is a very basic version with lot of improvements to do.

Mainly with properly calculating the aspect ratio of the cap/ hat with respect to the face of the user and properly process the image to make it properly overlap over the head withou having any gaps.

This project was for a competition wherein the timeline for coding was just 2 days. Hence, image processing is used.
However, future scope would be to use machine learning to improve the quality of the application.

The project uses, PIL, tkinter for image processing and UI and haarcascade library from OpenCV(already trained .xml files) for frontal face detection.

The code is in python.

Instructions:
Run the UI.py file from terminal/ command prompt. GUI opens up. USing Browse button upload the image of user, here you can load girl2.png.
Using the Add button, you can load the cap/hat image, here you can load hat_black.png. Press Go button and check how the hat looks on the user. There is no refresh functionality added. To check for other images, yu will have to upload again the picture of user using browse button and picture of hat/cap using the add button.

