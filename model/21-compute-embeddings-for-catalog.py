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

product_embeddings = []

for path in tqdm(catalog_image_paths):
    img = preprocess(Image.open(path).convert("RGB")).unsqueeze(0).to(device)

    with torch.no_grad():
        embedding = clip_model.encode_image(img)
        embedding = embedding / embedding.norm(dim=-1, keepdim=True)

    product_embeddings.append(embedding.cpu().numpy()[0])
