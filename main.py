import cv2
import sys

CHARACTERS = r".,-~`*^)&%$#@0"
#CHARACTERS = "".join(reversed(CHARACTERS))
#CHARACTERS = r"""$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. """
#CHARACTERS = "".join(reversed(CHARACTERS))
MAX_BRIGHTNESS = 255

WIDTH = 450
HEIGHT = 150

CACHE = {}
def write_frame_to_console( frame ) -> None:
    
    pixels_row = [[]]

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (pixel := frame[y][x]) in CACHE:
                pixels_row[-1].append(CACHE[pixel])
            else:
                CACHE[pixel] = CHARACTERS[ pixel //  (MAX_BRIGHTNESS // CHARACTERS.__len__()) -1 ]
                pixels_row[-1].append(CACHE[pixel])
        pixels_row.append([])

    
    
    for row in pixels_row:
        print( "".join(row))



def main(video_path: str) -> None:

    video = cv2.VideoCapture(video_path)
    while True:
        succ, frame = video.read()
        if not succ: 
            break
        downscaled_frame = cv2.resize(frame, (WIDTH, HEIGHT), interpolation=cv2.INTER_AREA)
        gray_downscaled_frame = cv2.cvtColor(downscaled_frame, cv2.COLOR_BGR2GRAY)

        write_frame_to_console(gray_downscaled_frame)


if __name__ == "__main__": 

    try:
        main(sys.argv[1])
    except IndexError:
        raise Exception("No was video given.")
