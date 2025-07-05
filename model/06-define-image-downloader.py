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

def download_image(row):
    product_id = row["id"]
    image_url = row["image_url"]
    product_dir = os.path.join(base_dir, str(product_id))
    os.makedirs(product_dir, exist_ok=True)

    try:
        response = requests.get(image_url, timeout=5)

        if response.status_code == 200:
            img = Image.open(BytesIO(response.content)).convert("RGB")
            image_name = os.path.basename(image_url).split("?")[0]
            image_path = os.path.join(product_dir, image_name)
            img.save(image_path)
            return f"{product_id}"

        else:
            return f"{product_id} - HTTP {response.status_code}"

    except Exception as e:
        return f"{product_id} - {e}"
