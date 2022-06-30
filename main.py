"""
Helper Script for running python OSC server
"""

import argparse
import sys

from eegosc.server import EEG_OSCServer
import eegosc.default_constants as default_constants
import eegosc.configurations as configurations

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--SERVER_IP', type=str, required=False, help="Server To Recieve On")
    parser.add_argument('--SERVER_PORT', type=int, required=False, help="Server Port to Recieve On")
    parser.add_argument('--CLIENT_IP', type=str, required=False, help="Client to send to")
    parser.add_argument('--CLIENT_PORT', type=str, required=False, help="Client Port")

    parser.add_argument('--config', type=str, required=False)

    args = parser.parse_args()

    if args.SERVER_IP == None:
        SERVER_IP = default_constants.SERVER_IP
    else:
        SERVER_IP = args.SERVER_IP

    if args.SERVER_PORT == None:
        SERVER_PORT = default_constants.SERVER_PORT
    else:
        SERVER_PORT = args.SERVER_PORT

    if args.CLIENT_IP == None:
        CLIENT_IP = default_constants.CLIENT_IP
    else:
        CLIENT_IP = args.CLIENT_IP

    if args.CLIENT_PORT == None:
        CLIENT_PORT = default_constants.CLIENT_PORT
    else:
        CLIENT_PORT = args.CLIENT_PORT

    if args.config == 'guest':
        config = configurations.guest_muse.Config(record=True)
    else: 
        config = configurations.default_muse1.Config(record=True) #make a way to choose what configs

    server = EEG_OSCServer(configuration=config,
                            server_ip=SERVER_IP,
                            server_port=SERVER_PORT,
                            client_ip=CLIENT_IP,
                            client_port=CLIENT_PORT)
    server.run()

def cleanup():
    from eegosc.processingfunctions.server_utility import close_file
    close_file()
    sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        cleanup()