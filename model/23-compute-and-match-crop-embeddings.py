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

for det in detections:
    img = preprocess(Image.open(det["crop_path"]).convert("RGB")).unsqueeze(0).to(device)

    with torch.no_grad():
        emb = clip_model.encode_image(img)
        emb = emb / emb.norm(dim=-1, keepdim=True)

    emb = emb.cpu().numpy().astype("float32")
    D, I = index.search(emb, 1)

    similarity = D[0][0]
    matched_idx = I[0][0]
    matched_product_id = catalog_product_ids[matched_idx]

    if similarity > 0.9:
        match_type = "Exact Match"
    elif similarity > 0.75:
        match_type = "Similar Match"
    else:
        match_type = "No Match"

    det.update({
        "matched_product_id": matched_product_id,
        "match_type": match_type,
        "similarity": float(similarity)
    })
