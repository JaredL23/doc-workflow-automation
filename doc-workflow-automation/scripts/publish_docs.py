
import json, time, pathlib

def publish():
    meta_path = pathlib.Path("data/metadata.json")
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    major, minor, patch = map(int, meta["version"].split("."))
    patch += 1
    meta["version"] = f"{major}.{minor}.{patch}"
    meta["last_published"] = time.strftime("%Y-%m-%d")
    pathlib.Path("dist").mkdir(exist_ok=True)
    (pathlib.Path("dist") / "artifact.txt").write_text(
        f"TITLE: {meta['title']}\nVERSION: {meta['version']}\nPUBLISHED: {meta['last_published']}\nREVISION: {meta['revision_summary']}\n",
        encoding="utf-8"
    )
    meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print("Published:", meta["version"])

if __name__ == "__main__":
    publish()
