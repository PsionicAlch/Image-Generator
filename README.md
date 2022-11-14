# Image Generator

This project is based on a wild theory I had. I theorized that if you had infinite time you could generate every image that has ever existed and will ever exist. This is the program to generate those images. I, however, decided to scrap the project for now. I do not have the time nor the patience to run this program. This program will create batch_dump.json files which are like little safe points for incase the program crashed for some reason, you could go back to where you stopped and just keep going from there. The issue is that these files are 500+mb in size for every 100 images generated. This is because the file is just a dictionary of lists, where each list contains 480 000 elements (u8's)... I don't know much about good file compression. In theory this program could be made multithreaded and ran on thousands of divices at the same time, some refactoring would be required.

# If you're brave enough...

I may have an idea as to how we could get around the memory problem. After some googling it seems possible to stream to Youtube using OpenCV. What if we stream the images to Youtube as they get created. This will allow Youtube to worry about saving and stitching the images into a video. We won't have to worry about storage just about keeping the server and the internet connection running. I would not know what we would do if the server accidentally died.

# 14/11/2022

I managed to get a working stream up and running. I found out that you can stream images to a website and the website will just replace the images as they come in. I just have one problem, I don't know if the images will be sync accross websites. I am doubtful. This however serves as a proof of concept that this idea should work.