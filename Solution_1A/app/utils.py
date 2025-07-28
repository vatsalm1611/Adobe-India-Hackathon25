def extract_outline(doc):
    blocks = []
    font_sizes = {}
    for page_num, page in enumerate(doc, start=1):
        blocks += [{"text": s['text'].strip(), "size": s['size'], "page": page_num}
                   for b in page.get_text("dict")["blocks"]
                   if b.get("type") == 0
                   for l in b.get("lines", [])
                   for s in l.get("spans", []) if s['text'].strip()]
        for b in page.get_text("dict")["blocks"]:
            if b.get("type") == 0:
                for l in b.get("lines", []):
                    for s in l.get("spans", []):
                        font_sizes[s['size']] = font_sizes.get(s['size'], 0) + 1

    common_sizes = sorted(font_sizes.items(), key=lambda x: -x[1])
    size_to_level = {}
    for i, (size, _) in enumerate(common_sizes[:3]):
        size_to_level[size] = f"H{i+1}"

    title = blocks[0]["text"] if blocks else "Untitled"
    outline = []
    for b in blocks:
        level = size_to_level.get(b["size"])
        if level:
            outline.append({"level": level, "text": b["text"], "page": b["page"]})
    return {"title": title, "outline": outline}
