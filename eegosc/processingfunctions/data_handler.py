import math
from eegosc.processingfunctions.moving_average import MovingAverage
from eegosc.processingfunctions import server_utility

class Handler(object):

    def __init__(self, send_address, window=10):
        self.window = window
        self.send_address = send_address

        self.hsi = [4,4,4,4]
        self.abs_waves = [-1,-1,-1,-1,-1]
        self.rel_waves = [-1,-1,-1,-1,-1]
        self.output_mv_rel_wave = [-1,-1,-1,-1,-1]

        self.mv_rel_waves = [MovingAverage(size=self.window) for i in range(5)]

    def handle_hsi(self, address: str, *args):
        self.hsi = args

    def relative_moving_average(self, address: str, fixed_arg, *args):
        """Applies a moving average to each stream of data based on hsi signals."""
        hsi = self.hsi
        client = fixed_arg[0]

        #print(address, client[0], args)

        if (hsi[0]==1 or hsi[1]==1 or hsi[2]==1 or hsi[3]==1): #if any sensor has a good read
            sumVals = 0
            countVals = 0
            wave = fixed_arg[1] # 0 or 1 or 2 or 3

            for i in [0,1,2,3]: #For wave id
                if hsi[i]==1: #Check the sensor, if good then...
                    countVals+=1    #add to count
                    sumVals+=args[i] #add the value to the sum value

            #Compute Absolute Average and Relative to other signals
            self.abs_waves[wave] = sumVals/countVals #gives absolute average.
            self.rel_waves[wave] = math.pow(10, self.abs_waves[wave]) / (math.pow(10,self.abs_waves[0]) + math.pow(10,self.abs_waves[1]) + math.pow(10,self.abs_waves[2]) + math.pow(10,self.abs_waves[3]) + math.pow(10,self.abs_waves[4]))

            #Apply Moving Average
            self.output_mv_rel_wave[wave] = float(self.mv_rel_waves[wave].next(self.rel_waves[wave]))
            server_utility.send_to_client(client, '{}'.format(self.send_address), self.output_mv_rel_wave)