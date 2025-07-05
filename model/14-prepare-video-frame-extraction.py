"""
Your Phone Can Spot Fashion – A lightweight yet powerful system that analyzes short-form videos in real time to identify fashion products by combining computer vision and natural language processing, all processed locally.

Copyright (C) 2025 Aryaman Gajrani

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

Contact: arya-gaj@proton.me
"""

import cv2
import os

video_dir = "videos"
frame_output_dir = "video_frames"
os.makedirs(frame_output_dir, exist_ok=True)

def extract_frames(video_path, output_path, frame_rate=1):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    interval = int(fps // frame_rate)
    count, saved = 0, 0

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        if count % interval == 0:
            frame_name = f"{os.path.splitext(os.path.basename(video_path))[0]}_frame_{saved:04}.jpg"
            cv2.imwrite(os.path.join(output_path, frame_name), frame)
            saved += 1

        count += 1

    cap.release()
