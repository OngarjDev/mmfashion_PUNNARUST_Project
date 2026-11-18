import json

with open("colab_downloaded_notebook.ipynb", encoding="utf-8") as f:
    nb = json.load(f)

for i, cell in enumerate(nb.get("cells", [])):
    cell_type = cell.get("cell_type")
    src = "".join(cell.get("source", []))
    print(f"==================== CELL {i} ({cell_type}) ====================")
    print(src)
    outputs = cell.get("outputs", [])
    if outputs:
        print("--- Outputs preview ---")
        for out in outputs:
            if "text" in out:
                print("".join(out["text"])[:300])
            elif "data" in out and "text/plain" in out["data"]:
                print("".join(out["data"]["text/plain"])[:300])
