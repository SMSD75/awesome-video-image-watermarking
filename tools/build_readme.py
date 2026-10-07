"""Builds README.md from papers.json. Run: python tools/build_readme.py"""
import json, re
from collections import OrderedDict, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
papers = json.loads((ROOT / "papers.json").read_text())

REPO = "SMSD75/awesome-watermarking"
TOP_TIER = ["CVPR", "ICCV", "ECCV", "NeurIPS", "ICLR", "ICML", "AAAI", "ACM MM",
            "IEEE S&P", "CCS", "NDSS", "USENIX Security", "AISTATS", "WACV", "ICASSP", "Interspeech", "EMNLP",
            "IEEE TIP", "IEEE TIFS", "JMLR", "ACM CSUR"]

# Section tree: (anchor id, number, heading, [(sub id, number, heading, key)]) ; key = (sec, sub)
SECTIONS = [
    ("foundations", "2.1", "Foundations", [], ("Foundations", None)),
    ("image-post-hoc", "2.2", "Image — Post-hoc Watermarking", [], ("Image — Post-hoc (Encoder/Decoder) Watermarking", None)),
    ("image-in-generation", "2.3", "Image — In-Generation Watermarking", [
        ("fine-tuning--weight-based", "2.3.1", "Fine-tuning / Weight-based", ("Image — In-Generation Watermarking for Generative Models", "Fine-tuning / weight-based")),
        ("initial-noise--semantic", "2.3.2", "Initial-noise / Semantic (Training-free)", ("Image — In-Generation Watermarking for Generative Models", "Initial-noise / semantic (training-free)")),
        ("autoregressive--other-generators", "2.3.3", "Autoregressive & Other Generators", ("Image — In-Generation Watermarking for Generative Models", "Autoregressive & other generators")),
    ], None),
    ("video", "2.4", "Video Watermarking", [
        ("post-hoc-video", "2.4.1", "Post-hoc Video", ("Video Watermarking", "Post-hoc video")),
        ("in-generation-video-diffusion", "2.4.2", "In-generation (Video Diffusion)", ("Video Watermarking", "In-generation (video diffusion)")),
    ], None),
    ("audio", "2.5", "Audio Watermarking", [], ("Audio Watermarking", None)),
    ("attacks", "2.6", "Attacks: Removal, Forgery & Spoofing", [], ("Attacks: Removal, Forgery, Spoofing", None)),
    ("benchmarks", "2.7", "Benchmarks, Surveys & Toolkits", [], ("Benchmarks, Surveys & Toolkits", None)),
]
TOPIC = {
    "Foundations": "Foundations", "Image — Post-hoc (Encoder/Decoder) Watermarking": "Image · Post-hoc",
    "Image — In-Generation Watermarking for Generative Models": "Image · In-gen",
    "Video Watermarking": "Video", "Audio Watermarking": "Audio",
    "Attacks: Removal, Forgery, Spoofing": "Attack", "Benchmarks, Surveys & Toolkits": "Benchmark",
}


def year(p):
    m = re.search(r"(19|20)\d{2}", p["venue"])
    return int(m.group(0)) if m else 0


def venue_group(p):
    """'NeurIPS 2024 (D&B)' -> 'NeurIPS 2024'; returns None for non-top-tier or workshops."""
    v = p["venue"]
    if "Workshop" in v:
        return None
    for t in TOP_TIER:
        if v.startswith(t + " "):
            return f"{t} {year(p)}"
    return None


def stars(code):
    m = re.match(r"https://github\.com/([^/]+/[^/#?]+)", code or "")
    if not m:
        return ""
    r = m.group(1)
    return f"![GitHub stars](https://img.shields.io/github/stars/{r}?style=social)"


def entry(p):
    L = p["links"]
    s = "⭐ " if p["star"] else ""
    parts = [f"+ {s}**{p['title']}**", f"[[{p['venue']}]({L['paper']})]"]
    if "code" in L:
        parts.append(f"[[Code]({L['code']})]")
    if "project" in L:
        parts.append(f"[[Project]({L['project']})]")
    b = stars(L.get("code"))
    if b:
        parts.append(b)
    return " ".join(parts)


def section_items(key, chronological=False):
    xs = [p for p in papers if (p["sec"], p["sub"]) == key]
    return sorted(xs, key=lambda p: year(p), reverse=not chronological)


unique = OrderedDict((p["title"], p) for p in papers)
n_papers = len(unique)
n_code = sum(1 for p in unique.values() if "code" in p["links"])

out = []
w = out.append

# ---------- Header ----------
w('<div align="center">\n')
w('<h1>Awesome Watermarking</h1>\n')
w('<p><b>A curated list of watermarking research for images, video and audio — from classic deep watermarking to watermarks for diffusion and autoregressive generators, plus the attacks and benchmarks that test them.</b></p>\n')
w(f'<a href="https://github.com/{REPO}/pulls"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome"></a>')
w(f'<img src="https://img.shields.io/badge/papers-{n_papers}-blue.svg?style=flat-square" alt="Papers">')
w(f'<img src="https://img.shields.io/badge/with%20code-{n_code}-orange.svg?style=flat-square" alt="With code">')
w(f'<a href="https://github.com/{REPO}/commits/main"><img src="https://img.shields.io/github/last-commit/{REPO}?style=flat-square" alt="Last commit"></a>')
w('<a href="LICENSE"><img src="https://img.shields.io/badge/license-CC0--1.0-lightgrey.svg?style=flat-square" alt="License: CC0-1.0"></a>')
w(f'<a href="https://github.com/{REPO}/stargazers"><img src="https://img.shields.io/github/stars/{REPO}?style=flat-square" alt="Stars"></a>\n')
w('<br>\n')
w('<img src="assets/overview.svg" alt="Overview of the watermarking pipeline and what this list covers" width="92%">\n')
w('<p><b>Keywords:</b> <i>invisible watermarking · generative AI provenance · diffusion watermarking · video watermarking · audio watermarking · watermark removal · content authenticity</i></p>\n')
w('<p><a href="#1-must-read-papers">Must-Read</a> · <a href="#2-paper-list">Paper List</a> · '
  '<a href="#3-papers-by-venue">By Venue</a> · <a href="#4-contributing">Contributing</a> · '
  '<a href="#5-citation">Citation</a></p>\n')
w('</div>\n')

# ---------- News ----------
w('## 🔥 News\n')
w(f'- **[2026-10]** ✅ Full citation audit: every entry checked against arXiv / proceedings for title, venue, year and official code; '
  f'list expanded to **{n_papers} papers** with new top-tier work (CVPR/ICCV/ECCV, NeurIPS/ICLR/ICML, USENIX Security, CCS, S&P, AAAI, ACM MM).')
w('- **[2026-10]** 🚀 Launched with image, video and audio watermarking, including the latest **CVPR 2026**, **ICLR 2026** and **ICML 2026** papers.')
w('- **[2026-10]** 🔊 Audio coverage: AudioSeal, WavMark, Timbre, AudioMarkNet (USENIX Sec), XAttnMark, GROOT, RAW-Bench and more.\n')
w('> [!TIP]\n> ⭐ marks foundational or highly influential work. Within each section, papers are ordered newest first. '
  'Contributions are welcome — see [Contributing](#4-contributing).\n')

# ---------- TOC ----------
w('## 📑 Contents\n')
w('- [1. Must-Read Papers](#1-must-read-papers)')
w('- [2. Paper List](#2-paper-list)')
for sid, num, head, subs, _ in SECTIONS:
    w(f'  - [{num} {head}](#{sid})')
    for ssid, snum, shead, _k in subs:
        w(f'    - [{snum} {shead}](#{ssid})')
w('- [3. Papers by Venue](#3-papers-by-venue)')
w('- [4. Contributing](#4-contributing)')
w('- [5. Citation](#5-citation)')
w('- [Star History](#star-history)\n')

# ---------- Must-read table ----------
w('## 1. Must-Read Papers\n')
w('A starting point: the papers that defined each line of work.\n')
w('| Title | Venue | Year | Code | Topic |')
w('|:------|:-----:|:----:|:----:|:-----:|')
must = [p for p in unique.values() if p["star"]]
order = list(TOPIC)
must.sort(key=lambda p: (order.index(p["sec"]), year(p)))
for p in must:
    L = p["links"]
    v = re.sub(r"\s*(19|20)\d{2}", "", p["venue"]).strip()
    b = stars(L.get("code"))
    title = (b + " <br> " if b else "") + f"[**{p['title']}**]({L['paper']})"
    code = f"[GitHub]({L['code']})" if "code" in L else "—"
    w(f"| {title} | {v} | {year(p)} | {code} | {TOPIC[p['sec']]} |")
w('')

# ---------- Paper list ----------
w('## 2. Paper List\n')
for sid, num, head, subs, key in SECTIONS:
    w(f'<a id="{sid}"></a>\n')
    w(f'### {num} {head}\n')
    if key:
        for p in section_items(key, chronological=(sid == "foundations")):
            w(entry(p))
        w('')
    for ssid, snum, shead, skey in subs:
        w(f'<a id="{ssid}"></a>\n')
        w(f'#### {snum} {shead}\n')
        for p in section_items(skey):
            w(entry(p))
        w('')
    w('<p align="right"><a href="#-contents">⬆ back to top</a></p>\n')

# ---------- By venue ----------
w('## 3. Papers by Venue\n')
w('Top-tier conference and journal papers from 2024 onward, grouped by venue. Click to expand.\n')
groups = defaultdict(list)
for p in unique.values():
    g = venue_group(p)
    if g and year(p) >= 2024:
        groups[g].append(p)
def gkey(g):
    name, y = g.rsplit(" ", 1)
    return (-int(y), TOP_TIER.index(name))
for g in sorted(groups, key=gkey):
    ps = groups[g]
    w(f'<details>\n<summary><b>{g}</b> ({len(ps)})</summary>\n')
    for p in ps:
        L = p["links"]
        line = f"+ [{p['title']}]({L['paper']})"
        if "code" in L:
            line += f" [[Code]({L['code']})]"
        w(line + f" — *{TOPIC[p['sec']]}*")
    w('\n</details>\n')

# ---------- Contributing ----------
w('## 4. Contributing\n')
w('Contributions are very welcome. To add a paper, open a pull request or an issue with:\n')
w('```markdown\n+ **Paper Title** [[Venue Year](paper_link)] [[Code](code_link)]\n```\n')
w('The README is generated from [`papers.json`](papers.json): add an entry there and run '
  '`python tools/build_readme.py`. Please keep to image, video and audio watermarking, prefer '
  'peer-reviewed versions, and link the arXiv or official proceedings page.\n')

# ---------- Citation ----------
w('## 5. Citation\n')
w('If you find this list useful, please consider starring ⭐ the repo and citing it:\n')
w('```bibtex\n@misc{salehi2026awesomewatermarking,\n  title        = {Awesome Watermarking: A Curated List of Image, Video and Audio Watermarking Research},\n'
  '  author       = {Salehi, Mohammadreza},\n  year         = {2026},\n'
  f'  howpublished = {{\\url{{https://github.com/{REPO}}}}}\n}}\n```\n')

# ---------- Star history ----------
w('## Star History\n')
w(f'<a href="https://star-history.com/#{REPO}&Date">\n'
  f'  <img src="https://api.star-history.com/svg?repos={REPO}&type=Date" alt="Star History Chart" width="600">\n</a>\n')
w('<p align="right"><a href="#-contents">⬆ back to top</a></p>')

(ROOT / "README.md").write_text("\n".join(out) + "\n")
print(f"README.md written: {n_papers} unique papers, {n_code} with code, {sum(len(v) for v in groups.values())} in by-venue")
