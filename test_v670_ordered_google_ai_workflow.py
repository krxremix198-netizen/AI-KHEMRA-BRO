import ast
from pathlib import Path

source_path = Path(__file__).with_name("app.py")
source = source_path.read_text(encoding="utf-8")
tree = ast.parse(source, filename=str(source_path))
functions = {
    node.name: node
    for node in tree.body
    if isinstance(node, ast.FunctionDef)
}

# Google AI Studio fallback must use current stable endpoints while preserving
# whatever model choice the existing UI already sends first.
candidate_source = ast.get_source_segment(source, functions["_candidate_gemini_models"])
for model_id in (
    "gemini-3.7-flash", "gemini-3.6-flash",
    "gemini-3.5-flash", "gemini-3.5-flash-lite",
):
    assert model_id in candidate_source
assert '"gemini-2.5-flash-lite"' not in candidate_source

# Existing visible workflow controls remain intact; this release changes only
# internal quality and fallback behavior.
assert '"🎬 Video → SRT", "📝 AI Subtitle Translator", "📜 SRT → Speech", "🎙️ Text → Speech"' in source
assert '"🎙️ Khmer SRT + MP3 តែម្តង"' in source
assert 'key="generate_srt"' in source

# Execute the ordered-batch coordinator with a deterministic fake model.  It
# must complete every batch before returning, keep all IDs, and return cue order.
nodes = [
    functions["ordered_translation_items"],
    functions["translate_cues_text_only"],
]
namespace = {}
exec(compile(ast.Module(body=nodes, type_ignores=[]), str(source_path), "exec"), namespace)

calls = []
def fake_translate(_client, _model, batch, _context="", _language="Auto-detect"):
    calls.append([cue["id"] for cue in batch])
    return {cue["id"]: {"tag": "M", "text": f"ខ្មែរ {cue['id']}"} for cue in batch}

namespace["_translate_batch_text_only"] = fake_translate
cues = [
    {"id": item, "start": float(item), "end": float(item) + 1.0, "source": f"line {item}"}
    for item in range(1, 66)
]
translated = namespace["translate_cues_text_only"](object(), "gemini-3.7-flash", cues)
assert calls == [list(range(1, 31)), list(range(31, 61)), list(range(61, 66))]
assert list(translated) == list(range(1, 66))
assert len(translated) == 65

repair_source = ast.get_source_segment(source, functions["repair_translation_items"])
assert "contains_non_khmer_script" in repair_source
assert "Never omit, summarize, invent, or weaken any story element" in source

print("v6.7.0 ordered translation, stable Google AI fallback, and unchanged UI checks: OK")
