"""
    Canny Edge Detection

    Canny edge detection is one of the most popular edge detection methods in image
    processing. This is a multistep process. It first blurs the image to reduce noise
    and then computes Sobel gradients in the X and Y directions, suppresses the edges
    where nonmaxima is calculated, and finally determines whether a pixel is “edge-like”
    or not by applying hysteresis thresholding.
"""
