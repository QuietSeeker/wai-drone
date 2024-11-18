import cv2


class VideoStream:
    def __init__(self):
        self._running = True
        self.video = cv2.VideoCapture("udp://@0.0.0.0:11111")

    def terminate(self):
        self._running = False
        self.video.release()
        cv2.destroyAllWindows()

    def recv(self, frame_processor):
        while self._running:
            try:
                ret, frame = self.video.read()
                if ret:
                    # Resize frame
                    height, width, _ = frame.shape
                    new_h = int(height / 2)
                    new_w = int(width / 2)

                    # Resize for improved performance
                    new_frame = cv2.resize(frame, (new_w, new_h))

                    # Display the resulting frame
                    cv2.imshow("Tello", new_frame)

                    # Process frame using the passed frame_processor function
                    frame_processor(new_frame)

                cv2.waitKey(1)
            except Exception as err:
                print(f"Error in video stream: {err}")
