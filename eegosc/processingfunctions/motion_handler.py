from eegosc.processingfunctions.moving_average import MovingAverage
from eegosc.processingfunctions import server_utility

class MotionHandler(object):

    def __init__(self, data_struct, send_address, window=10):
        self.window = window
        self.data_struct = data_struct
        self.send_address = send_address
        self.mv = [MovingAverage(size=self.window) for i in range(len(self.data_struct))]


    def handle_motion(self, address: str, client, *args):
        for d in [0,1,2]:
            self.data_struct[d] = self.mv[d].next(args[d])

        server_utility.send_to_client(client[0],'{}'.format(self.send_address), self.data_struct)
        