# single_motion_detection_django
A minimal example on how to implement a video feed for single motion detection with Django.

Most of the code presented here has been taken from a blog post written by Adrian Rosebrock which you can find [here](https://www.pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/). That blog describes how to implement a single motion detection with Flask. The purpose of this mini-project was to learn some basics of [Django](https://www.djangoproject.com/).

If you would like to download and test this on your own, please ensure that you have the right packages installed. For this purpose, you can use the conda environment attached as computer_vision.yml. To create a new environment on your machine using an .yml configuration file please run the below command on your conda terminal:

$ conda-env create -n new_env -f=\path\to\computer_vision.yml

Once you have the environment installed, you can open the PyCharm project and from the local terminal run:

$ py manage.py runserver

Please note that the above command should be run on the directory where manage.py has been saved.

If everything went well, you should see the below message:

Django version 2.2.5, using settings 'mysite.settings'
<br> Starting development server at http://127.0.0.1:8000/
<br> Quit the server with CTRL-BREAK.

In order to access the test web page that will display the video feed with a single motion detection you should type the below url on your browser:
http://127.0.0.1:8000/motion_dection/motion

Please note that the port (8000) might be different on your own machine.

The end result should look something like the below image.

![alt text](https://github.com/monti-nicolas/single_motion_detection_django/blob/main/SingleMotionDetection_Django/images_example/result.png)
