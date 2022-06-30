import time
import csv

path = './data/'
filename = 'eeg_data_1'

with open('{}{}.csv'.format(path, filename), 'w', newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['address', 'args'])

f = open('{}{}.csv'.format(path, filename), 'w', newline="")
csvwriter = csv.writer(f)

def send_to_client(client, address, *args):
    client.send_message(address, args[0])
    time.sleep(1)

    #csvwriter.writerow([address]+list(*args))
    #time.sleep(1)

def close_file():
    f.close()