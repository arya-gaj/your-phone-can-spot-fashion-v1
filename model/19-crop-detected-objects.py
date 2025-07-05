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

cropped_dir = "detected_crops"
os.makedirs(cropped_dir, exist_ok=True)

crop_index = 0

for det in detections:
    img = Image.open(det["frame"]).convert("RGB")
    x1, y1, x2, y2 = map(int, det["bbox"])
    crop = img.crop((x1, y1, x2, y2))

    crop_path = os.path.join(cropped_dir, f"crop_{crop_index:04}.jpg")
    crop.save(crop_path)

    det["crop_path"] = crop_path
    crop_index += 1
