import ast
import asyncio
import re
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import edge_tts

root = Path(__file__).parent
source_path = root / "app.py"
source = source_path.read_text(encoding="utf-8")
tree = ast.parse(source, filename=str(source_path))

# The translation policy must protect story meaning while keeping every source
# timestamp locked for speech generation.
for required in (
    "STORY, MEANING, AND EMOTIONAL DEPTH",
    "Never summarize, weaken, invent, or replace",
    "LOCKED SRT TIMING",
    "starts exactly at each cue start",
    "must finish at or before the cue end",
):
    assert required in source, required
assert "total = max(0.35, final_end_ms / 1000.0)" in source
assert "final_end_ms + 350" not in source
assert "App មិនកាត់សំឡេង" in source
assert "artificial milliseconds are added" in source

assignments = {
    "PISITH", "SREYMOM", "VOICE_PROFILES", "VOICE_FADE_IN_SECONDS",
    "VOICE_FADE_OUT_SECONDS", "MIN_VOICE_GAP_MS", "MAX_TEMPO_SPEED",
    "FINAL_LEVELER_FILTER", "TAG_ALIASES", "NON_KHMER_SCRIPT_RE", "DUCKING_DEFAULTS",
}
functions = {
    "normalize_voice_tag", "contains_non_khmer_script", "normalize_dialogue",
    "prepare_tts_text", "synthesize", "run_async", "character_voice_filters",
    "voice_tone_filters", "normalized_ducking_config", "append_audio_master_filters",
    "probe_audio_duration", "atempo_chain", "parse_srt", "create_mp3",
}
nodes = []
for node in tree.body:
    if isinstance(node, ast.Assign):
        names = [target.id for target in node.targets if isinstance(target, ast.Name)]
        if any(name in assignments for name in names):
            nodes.append(node)
    elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in functions:
        nodes.append(node)

namespace = {
    "re": re, "asyncio": asyncio, "edge_tts": edge_tts, "subprocess": subprocess,
    "tempfile": tempfile, "Path": Path, "ThreadPoolExecutor": ThreadPoolExecutor,
    "as_completed": as_completed,
}
exec(compile(ast.Module(body=nodes, type_ignores=[]), str(source_path), "exec"), namespace)

srt = """1
00:00:00,000 --> 00:00:04,000
[M] អូនកុំបារម្ភអីណា បងនៅទីនេះ。

2
00:00:04,200 --> 00:00:08,000
[F] ខ្ញុំយល់ហើយ យើងទៅជាមួយគ្នា។
"""

with tempfile.TemporaryDirectory() as temp_dir:
    output = Path(temp_dir) / "strict-timing.mp3"
    output.write_bytes(namespace["create_mp3"](srt))
    duration = namespace["probe_audio_duration"](output)
    # MP3 encoding can add a few milliseconds of codec padding, but rendered
    # speech must not grow into a visible extra tail after the locked SRT end.
    assert duration <= 8.06, duration

print("v6.6.2 story-preservation and strict-SRT-timing checks: OK")
