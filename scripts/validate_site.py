"""Validate the static site's links and media before publishing to GitHub Pages."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json

ROOT = Path(__file__).resolve().parents[1] / "docs"


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.references = []
        self.ids = set()
        self.media = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a" and "href" in attrs:
            self.references.append(attrs["href"])
        if tag in ("img", "video", "source", "script", "link"):
            reference = attrs.get("src") or attrs.get("href")
            if reference:
                self.references.append(reference)
        if tag in ("img", "video", "source") and attrs.get("src"):
            self.media.append(attrs["src"])


pages = {path.resolve(): Page(path.read_text()) for path in ROOT.rglob("*.html")}
errors = []
root = ROOT.resolve()
media = set()
for path, page in pages.items():
    text = path.read_text()
    if "/Users/" in text or "file://" in text:
        errors.append(f"Workstation path in {path.relative_to(root)}")
    for reference in page.references:
        url = urlsplit(reference)
        if url.scheme or url.netloc:
            continue
        if url.path.startswith("/"):
            errors.append(f"Root-relative URL in {path.relative_to(root)}: {reference}")
            continue
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        if not target.is_relative_to(root):
            errors.append(f"Link outside website: {reference}")
            continue
        if target.is_dir():
            target /= "index.html"
        if not target.is_file():
            errors.append(f"Missing {reference} in {path.relative_to(root)}")
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            errors.append(f"Missing anchor {reference} in {path.relative_to(root)}")
    for reference in page.media:
        url = urlsplit(reference)
        if not url.scheme and not url.netloc:
            media.add((path.parent / unquote(url.path)).resolve())

if errors:
    raise SystemExit("\n".join(errors))
if not (root / "index.html").is_file():
    raise SystemExit("Missing homepage")
print(json.dumps({
    "pages": len(pages),
    "images": sum(path.suffix == ".webp" for path in media),
    "videos": sum(path.suffix == ".mp4" for path in media),
    "links_and_anchors": "passed",
    "paths": "portable",
}, ensure_ascii=False))
