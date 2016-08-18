# OpenCV Learning Path

## OpenCV and Python

### Set up an OpenCV and Python 3 development environment

This will get you up and running with OpenCV and Python 3 on a development laptop. You should be relatively comfortable with running commands and changing directories, setting permissions for files and folders from the command line.

#### Tasks

1. Launch the terminal and change directory to you home directory.
2. Create a work directory if one doesn't already exist.
3. Change directory to your work directory and launch the Atom editor: `atom .`
4. Create `show_img.py` and write a program to open and display an image file you supply as an argument to the script.

  ```python
  #!/usr/bin/env python3
  import cv2
  import os.path
  import sys

  imgPath = sys.argv[1]
  if not os.path.isfile(imgPath):
      print("usage: show_img.py <file>")
      sys.exit()

  img = cv2.imread(imgPath)
  cv2.imshow('image', img)
  cv2.waitKey(0)
  ```

5. Back in the terminal, run you new script in Python 3.

  ```sh
  ~/exercises $ python3 show_img.py
  ```

6. Make the script executable and run it directly from the command line.

  ```sh
  ~/exercises $ chmod +x show_img.py
  ~/exercises $ ./show_img.py
  ```

#### Example

- [`show_img.py`](python/show_img.py)

#### References

- [Python](https://www.python.org)
- [Atom editor](https://atom.io)
- [Shebang (Unix)](https://en.wikipedia.org/wiki/Shebang_(Unix))
- [`cv2.imread()`](http://docs.opencv.org/3.0-last-rst/modules/imgcodecs/doc/reading_and_writing_images.html#cv2.imread)
- [`cv2.imshow()`](http://docs.opencv.org/3.0-last-rst/modules/highgui/doc/user_interface.html#cv2.imshow)
- [`cv2.waitKey()`](http://docs.opencv.org/3.0-last-rst/modules/highgui/doc/user_interface.html#cv2.waitKey)

## OpenCV and C++

### Set up an OpenCV and C++ development environment

This will get you up and running with OpenCV and C++ on a development laptop. You should be relatively comfortable with running commands and changing directories, setting permissions for files and folders from the command line.

#### Tasks

1. Launch the terminal and change directory to you home directory.
2. Create a work directory if one doesn't already exist.
3. Change directory to your work directory and launch the Atom editor: `atom .`
4. Create `show_img.cpp`.

  ```cpp
  #include <opencv2/highgui/highgui.hpp>

  int main() {
    cv::Mat img = cv::imread("trex.png");

    cv::imshow("Tyrannosaurus Rex", img);
    cv::waitKey();
  }

  ```

5. Back in the terminal, compile and run your program. In this example we use `make`.

  ```sh
  $ make
  $ ./show_img
  ```

#### Example

- [`show_img`](cpp/show_img)

#### References

- [OpenCV C++ API](http://docs.opencv.org/3.1.0/#gsc.tab=0)
- [`cv::Mat`](http://docs.opencv.org/3.1.0/d3/d63/classcv_1_1Mat.html#gsc.tab=0)
- [`cv::imread()`](http://docs.opencv.org/3.1.0/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56)
- [`cv::imshow()`](http://docs.opencv.org/3.1.0/d7/dfc/group__highgui.html#ga453d42fe4cb60e5723281a89973ee563)
- [`cv::waitKey()`](http://docs.opencv.org/3.1.0/d7/dfc/group__highgui.html#ga5628525ad33f52eab17feebcfba38bd7)
