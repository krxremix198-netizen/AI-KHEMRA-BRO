import ast
import re
from pathlib import Path

source_path = Path(__file__).with_name("app.py")
source = source_path.read_text(encoding="utf-8")
tree = ast.parse(source, filename=str(source_path))

assert 'APP_VERSION = "6.7.0"' in source
assert "0719067125" not in source
assert 'os.getenv("AI_KHEMRA_BRO_DATA_DIR", "")' in source
assert "PERSISTENT_LICENSE_STORAGE_CONFIGURED" in source
assert "LICENSE_DB_PATH.parent.mkdir(parents=True, exist_ok=True)" in source
assert "def admin_credentials_configured" in source
assert "if not admin_credentials_configured():" in source

functions = {
    node.name: node
    for node in tree.body
    if isinstance(node, ast.FunctionDef)
}
normalize_node = functions["normalize_access_code"]
namespace = {"re": re}
exec(
    compile(ast.Module(body=[normalize_node], type_ignores=[]), str(source_path), "exec"),
    namespace,
)
normalize = namespace["normalize_access_code"]
assert normalize("khbr_01-AB") == "KHBR_01-AB"
assert normalize("x" * 70) == "X" * 64

validate_source = ast.get_source_segment(source, functions["validate_customer_login"])
assert "No device lock and no single-session lock" in validate_source
assert "_hash_session" not in validate_source
assert "active_session_hash=NULL" in validate_source

save_upload_source = ast.get_source_segment(source, functions["save_upload"])
assert "size > 150 * 1024 * 1024" in save_upload_source
assert "size <= 0" in save_upload_source

single_voice_source = ast.get_source_segment(source, functions["create_single_voice_mp3"])
assert "subprocess.TimeoutExpired" in single_voice_source
assert "FileNotFoundError" in single_voice_source

mp3_source = ast.get_source_segment(source, functions["create_mp3"])
assert "'-nostdin'" in mp3_source
assert "subprocess.TimeoutExpired" in mp3_source

print("v6.6.1 deployment persistence, admin secret, and multi-device access checks: OK")
