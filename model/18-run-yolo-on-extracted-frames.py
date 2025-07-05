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

frame_files = [os.path.join(frame_output_dir, f) for f in os.listdir(frame_output_dir) if f.endswith(".jpg")]

detections = []

for frame_path in frame_files:
    results = model(frame_path)[0]

    for box in results.boxes:
        cls = int(box.cls.item())
        conf = float(box.conf.item())
        xyxy = box.xyxy[0].tolist()
        detections.append({
            "frame": frame_path,
            "class": model.names[cls],
            "confidence": conf,
            "bbox": xyxy
        })
