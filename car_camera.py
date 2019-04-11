from picamera.array import PiYUVArray
from picamera import PiCamera


RESOLUTION = (640, 480)  # TODO can we do lower resolution?


class Camera:
    def __init__(self):
        self.camera = PiCamera()

        # Check the link below for the combinations between mode and resolution
        # https://picamera.readthedocs.io/en/release-1.13/fov.html#sensor-modes
        self.camera.sensor_mode = 7
        self.camera.resolution = RESOLUTION
        self.camera.framerate = 120  # TODO why so many frames per second?

    def frames(self):
        raw_capture = PiYUVArray(self.camera, size=RESOLUTION)
        stream = self.camera.capture_continuous(raw_capture, format="yuv", use_video_port=True)

        try:
            for frame in stream:
                raw_capture.truncate(0)  # Reset the buffer for the next image
                yield frame
        except KeyboardInterrupt:
            raw_capture.close()
            stream.close()
            print('Closed streams')
        # TODO check that it closes (reaches here) upon break
        # TODO do I also need to close the camera? (self.camera.close())
