from scipy.signal import find_peaks, butter, filtfilt
from utils import interpolate_01
from car_camera import RESOLUTION

# resolution is 640 x 480
HORIZONTAL_LINE = 240  # horizontal line at y=HORIZONTAL_LINE
CENTER_X = RESOLUTION[0] / 2

ANGLE_EXAGGERATION = 1.25  # linear, 25% exaggeration

STRAIGHT_SPEED = .25
TURN_SPEED = .1


class Processor:
    # To filter the noise in the image we use a 3rd order Butterworth filter

    def __init__(self):
        # Wn = 0.02, the cut-off frequency, acceptable values are from 0 to 1
        b, a = butter(3, 0.02)
        self.a = a
        self.b = b

        self.current_speed = 0
        self.current_angle = 0

    def process(self, frame):
        """
        `frame` should be in YUV format
        returns the speed and angle for this frame
        """
        guide_x = self.find_guide_pos(frame)
        if guide_x is None:  # can't see the track guideline
            angle = self.current_angle
        else:
            angle = (guide_x - CENTER_X) / CENTER_X
            angle *= ANGLE_EXAGGERATION  # force steeper wheel angles

        # slow down on steeper turns
        # when the angle is zero, then go full straight speed
        # when the angle is one (either full left or full right), then go at the lower turn speed
        speed = interpolate_01(STRAIGHT_SPEED, TURN_SPEED, 1-abs(angle))

        self.current_speed = speed
        self.current_angle = angle
        return speed, angle

    def find_guide_pos(self, frame):
        """ Returns the x-coordinate of the center of the track line (if in line of sight) """
        # Get the intensity component of the image (a trick to get black and white images)
        bw_img = frame.array[:, :, 0]

        # Select a horizontal line in the middle of the image
        line = bw_img[HORIZONTAL_LINE, :]

        # Smoothen the transitions so we can detect the peaks
        smooth_line = filtfilt(self.b, self.a, line)

        # Find peaks of black (the guide)
        peaks, _ = find_peaks(smooth_line, height=128)
        if len(peaks) == 0:
            return None

        # Return the average of the peaks
        return peaks.mean()
