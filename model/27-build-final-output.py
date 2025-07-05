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

final_output = []

for det in detections:
    video_id = det["frame"].split("_frame")[0]

    output_entry = {
        "video_id": video_id,
        "vibes": vibe_results.get(video_id, []),
        "products": []
    }

    prod_entry = {
        "type": "fashion_item",
        "match_type": det["match_type"],
        "matched_product_id": det["matched_product_id"],
        "confidence": round(det["similarity"], 3),
        "bbox": det["bbox"]
    }

    output_entry["products"].append(prod_entry)
    final_output.append(output_entry)
