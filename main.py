from drone_controller import DroneController
from card_detector import CardDetector
from action_handler import ActionHandler
from video_stream import VideoStream

import threading


def main():
    drone = DroneController()
    detector = CardDetector()
    action_handler = ActionHandler(drone)

    def frame_processor(frame):
        detected_cards = detector.detect_cards(frame)
        for card in detected_cards:
            action_handler.perform_action(card)

    drone.connect()
    drone.takeoff()
    drone.enable_video_stream()

    # Initialize and start video stream with frame processor
    tello_video = VideoStream()
    video_thread = threading.Thread(target=tello_video.recv, args=(frame_processor,))
    video_thread.start()

    try:
        while True:
            # Main loop for other drone operations if needed
            pass

    except KeyboardInterrupt:
        print("Program interrupted by user, landing the drone...")
    finally:
        drone.land()
        drone.disable_video_stream()
        tello_video.terminate()
        video_thread.join()


if __name__ == "__main__":
    main()
