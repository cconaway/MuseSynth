"""Default Muse 1 Configuration Class"""
from eegosc.processingfunctions.data_handler import Handler
from eegosc.processingfunctions.motion_handler import MotionHandler

class Config(object):
    def __init__(self, record=False):
        self.name = "Muse 1"
        self.handler = Handler('guest_relative_wave')
        self.acc_handler = MotionHandler([-1,-1,-1], 'guest_acc_xyz', window=10)
        self.gyro_handler = MotionHandler([-1,-1,-1], 'guest_gyro_xyz', window=10)

    def run_config(self, dispatch, client):

        dispatch.map("/muse/elements/horseshoe", self.handler.handle_hsi)
        dispatch.map("/muse/acc", self.acc_handler.handle_motion, client)
        dispatch.map("/muse/gyro", self.gyro_handler.handle_motion, client)
        
        wave_names = [('alpha_absolute',0),         
                    ('beta_absolute', 1),
                    ('gamma_absolute', 2),
                    ('delta_absolute', 3),
                    ('theta_absolute', 4)]

        for wave in wave_names:
            dispatch.map(f"/muse/elements/{wave[0]}", self.handler.relative_moving_average, client, wave[1])


    

