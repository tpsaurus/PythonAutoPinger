import pathlib
import os
import sys
import requests
import time
from playsound import playsound
# Import prepend
def get_parent():
    file_path = os.path.realpath(__file__)
    me = pathlib.Path(file_path)
    return me.parent

def main():
    print("\n"*20)
    sound_effect = get_parent().parent/'resources'/'alarm.mp3'
    url = input("Url to attempt to ping: ")
    wait_in = input("Time in mins between pings(default 15): ")
    timeout_in = input("Time in seconds before timeout(default 30): ")
    if wait_in:
        wait = int(wait_in)
    else:
        wait = 15
    if timeout_in:
        timeout = int(timeout_in)
    else:
        timeout = 30
    
    lastiteration = time.time()-wait*60
    
    while (True):
        try:
            time.sleep(1)
            if time.time()-lastiteration > wait*60:
                # test
                try:
                    result = requests.get(url,timeout=timeout)
                except requests.Timeout as error:
                    print(error)
                else:
                    print(result)
                    print(f"Website {url} loaded")
                    while True:
                        playsound(sound_effect)
                finally:
                    lastiteration = time.time()
        except KeyboardInterrupt:
            print("Closing program...")
            return 0

            
if __name__ == "__main__":
    sys.exit(main())