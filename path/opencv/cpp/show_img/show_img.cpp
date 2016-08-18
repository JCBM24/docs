#include <iostream>
#include <opencv2/highgui/highgui.hpp>

int main() {
  cv::Mat img = cv::imread("trex.png");

  if (!img.empty()) {
    std::cout << "Image loaded" << std::endl;
  } else {
    std::cout << "Error : Image cannot be loaded" << std::endl;
    return -1;
  }
  cv::imshow("Tyrannosaurus Rex", img);
  cv::waitKey();
}
