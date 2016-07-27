import clipboard
import os
import subprocess
from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor, Future
from time import sleep
pool = ThreadPoolExecutor(max_workers=2)
os.chdir('C:/Downloads')
links = []
response = -1
def enlist():
    global links
    link = ''
    prev = ''
    while(True):
        try:
            link = clipboard.paste()
            
            if prev == link:
                pass
            else:
                print(prev)
                prev = link
                if 'youtube' in prev:
                    links.append(prev)
                    sleep(5)
        except:
            print("damned")

def download():
    global links
    global response
    done = []
    i = 0
    try:
        while(True):
            if i+1 <= len(links):
                to_download = links[i]
                com = 'youtube-dl ' + to_download
                response = subprocess.call(com)
                if response == 0:
                    done.append(to_download)
                    i += 1
                    sleep(5)
    except:
        print("damned")

'''p1 = Process(target = enlist())
p1.start()
p2 = Process(target = download())
p2.start()'''
pool.submit(enlist)
pool.submit(download)
