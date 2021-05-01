"""
    Noise reduction using smoothing and blurring

    Bilateral blurring:
        The previous three blurring techniques yield blurred images with the side effect that we
        lose the edges in the image. To blur an image while preserving the edges, we use bilateral
        blurring, which is an enhancement over Gaussian blurring. Bilateral blurring takes two
        Gaussian distributions to perform the computation. The first Gaussian function considers
        the spatial neighbors (pixels in x and y space that are close together). The second Gaussian
        function considers the pixel intensity of the neighboring pixels. This makes sure that only
        those pixels that are of similar intensity to the central pixel are considered for blurring,
        leaving the edges intact as the edges tend to have higher intensity compared to other pixels.
"""

from cv2 import imread, imshow, waitKey, bilateralFilter
