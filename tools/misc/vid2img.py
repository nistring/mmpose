import cv2
import argparse
import os

'''
Convert video in to snapshots
Usage: python tools/misc/vid2img.py "path-to-video"
'''

parser = argparse.ArgumentParser()
parser.add_argument('input', help='input video filename')
args = parser.parse_args()

save_dir = os.path.join(os.path.dirname(args.input), (os.path.basename(args.input).split('.')[0] +'_imgs'))
os.makedirs(save_dir, exist_ok=True)
cap = cv2.VideoCapture(args.input)

frame_idx = 0
while cap.isOpened():
    success, frame = cap.read()
    mask = frame.sum(2) > 230 * 3
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)
    frame[:, :, 3][mask] = 0
    cv2.imwrite(os.path.join(save_dir, str(frame_idx).zfill(5) + '.png'), frame)
    frame_idx += 1
