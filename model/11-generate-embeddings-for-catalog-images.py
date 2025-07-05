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

image_embeddings = []
image_ids = []

catalog_path = "catalog_images"

for product_id in tqdm(os.listdir(catalog_path)):
    product_dir = os.path.join(catalog_path, product_id)

    if not os.path.isdir(product_dir):
        continue

    for image_name in os.listdir(product_dir):
        image_path = os.path.join(product_dir, image_name)

        try:
            image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)

            with torch.no_grad():
                embedding = model.encode_image(image).cpu().numpy().flatten()

            image_embeddings.append(embedding)
            image_ids.append((product_id, image_name))

        except Exception as e:
            print(f"Error with {image_path}: {e}")
