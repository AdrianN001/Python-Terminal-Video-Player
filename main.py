import threading
import io
import cv2
import time
from class_queue import Queue
import sys

# CHARACTERS = r".,-~`*^)&%$#@0"
#CHARACTERS = "".join(reversed(CHARACTERS))
CHARACTERS = r"""$@B%8&WM*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. """
CHARACTERS = "".join(reversed(CHARACTERS))
MAX_BRIGHTNESS = 255

FRAME_TIME = (1/60)

WIDTH = 220
HEIGHT = 100


CACHE = {}
def write_frame_to_console( frame ) -> None:
    
    time.sleep(FRAME_TIME)

    buffer = io.StringIO()

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (pixel_brightness := frame[y][x]) not in CACHE:
                brightness = pixel_brightness / MAX_BRIGHTNESS
                ascii_repr = int(brightness * (len(CHARACTERS)-1))
                CACHE[pixel_brightness] = CHARACTERS[ ascii_repr ]
                 
            buffer.write(CACHE[pixel_brightness])
        buffer.write("\n")

    print( buffer.getvalue())

def print_frame(queue: Queue) -> None:

    while True:
        res, good = queue.get()
        if not good:
            time.sleep(0.5)
            continue
        
            
        write_frame_to_console(res)



def main(video_path: str) -> None:

    queue = Queue()
    working_thread = threading.Thread(target=print_frame, args=(queue,))
    working_thread.start()

    video = cv2.VideoCapture(video_path)
    while True:
        succ, frame = video.read()
        if not succ: 
            break
        print(queue.length())
        downscaled_frame = cv2.resize(frame, (WIDTH, HEIGHT), interpolation=cv2.INTER_AREA)
        gray_downscaled_frame = cv2.cvtColor(downscaled_frame, cv2.COLOR_BGR2GRAY)

        queue.push(gray_downscaled_frame)

        write_frame_to_console(gray_downscaled_frame)
    working_thread.join()

if __name__ == "__main__": 

    try:
        main(sys.argv[1])
    except IndexError:
        raise Exception("No was video given.")
