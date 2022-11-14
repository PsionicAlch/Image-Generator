# Image Generator

This project is based on a wild theory I had. I theorized that if you had infinite time you could generate every image that has ever existed and will ever exist. This is the program to generate those images. I, however, decided to scrap the project for now. I do not have the time nor the patience to run this program. This program will create batch_dump.json files which are like little safe points for incase the program crashed for some reason, you could go back to where you stopped and just keep going from there. The issue is that these files are 500+mb in size for every 100 images generated. This is because the file is just a dictionary of lists, where each list contains 480 000 elements (u8's)... I don't know much about good file compression. In theory this program could be made multithreaded and ran on thousands of divices at the same time, some refactoring would be required.

# If you're brave enough...

I may have an idea as to how we could get around the memory problem. After some googling it seems possible to stream to Youtube using OpenCV. What if we stream the images to Youtube as they get created. This will allow Youtube to worry about saving and stitching the images into a video. We won't have to worry about storage just about keeping the server and the internet connection running. I would not know what we would do if the server accidentally died.

# 14/11/2022

I managed to get a working stream up and running. I found out that you can stream images to a website and the website will just replace the images as they come in. I just have one problem, I don't know if the images will be sync accross websites. I am doubtful. This however serves as a proof of concept that this idea should work.

# I did some math (which might be wrong)

The number of unique frames that could be generated from this program: 

I used to the power of 255 because each individual pixel in the ROW * COLUMN grid can have a value between 0 and 255. 

```python
ROW, COLUMN = 450, 800

image_variations = (ROW * COLUMN) ** 225
fps = 60
video_len_years = (image_variations // fps) // 60 // 60 // 24 // 365
```

If we print video_len_years to the console we get this really big number: 

```python
53395462963808296222774960795450761943521050805004171460356698888149879240346004941338188900240719271986659088174691097448920821149239186714651949396434270517628044536827046661832768266303732119124104854837567793030303529827740067530346327253935985936217897541365592034755165008796588701017216033459264843306764351062632686021434123818775955358114309664151826904420265582596883353493590597170670411252562691273101520158446012644520725935741330643058475316753302412889851007147338067361158942257838224134307797426059443628939635587161368926081369115755391089964213599847552515631411887270201270409584902002410780315776675245586586929339354440402581007048591780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219178082191780821917808219
```

This is the amount of years you'll need to watch this entire video. Not how many years will be needed to make this whole video.

So until further notice, I decided to stop this project. This project would have been perfect for an immortal.