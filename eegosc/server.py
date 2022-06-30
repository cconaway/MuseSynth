from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client

class EEG_OSCServer():

    def __init__(self, **kwargs):

        self.server_ip = kwargs['server_ip']
        self.server_port = kwargs['server_port']
        self.client_ip = kwargs['client_ip']
        self.client_port = kwargs['client_port']

        self.dispatcher = dispatcher.Dispatcher()
        self.client = udp_client.SimpleUDPClient(self.client_ip, self.client_port)
        
        self.config = kwargs['configuration']
        self.config.run_config(self.dispatcher, self.client)

        self.server = osc_server.ThreadingOSCUDPServer((self.server_ip, self.server_port), self.dispatcher)
        
    def run(self):

        print("Serving on {}".format(self.server.server_address))
        print("Sending to {}:{}".format(self.client_ip, self.client_port))
        
        self.server.serve_forever()
       

        