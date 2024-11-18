import socket


class DroneController:
    """
    @brief  Tello IP address. Use local IP address since
            host computer/device is a WiFi client to Tello.
    """

    tello_ip = "192.168.10.1"

    """
    Tello port to send command message.
    """
    command_port = 8889

    """
    @brief  Host IP address. 0.0.0.0 referring to current 
            host/computer IP address.
    """
    host_ip = "0.0.0.0"

    """
    @brief  UDP port to receive response msg from Tello.
            Tello command response will send to this port.
    """
    response_port = 9000

    def __init__(self):
        self.tello_address = (DroneController.tello_ip, DroneController.command_port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((DroneController.host_ip, DroneController.response_port))

    def send_command(self, command):
        self.socket.sendto(command.encode(), self.tello_address)
        response, _ = self.socket.recvfrom(1024)  # Read 1024-bytes from UDP socket
        return response.decode()

    def connect(self):
        return self.send_command("command")

    def takeoff(self):
        return self.send_command("takeoff")

    def land(self):
        return self.send_command("land")

    def get_battery(self):
        return self.send_command("battery?")

    def enable_video_stream(self):
        return self.send_command("streamon")

    def disable_video_stream(self):
        return self.send_command("streamoff")
