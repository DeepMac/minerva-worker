import os
import shutil
import tempfile
from pathlib import Path

# servers
SERVER_URL = os.environ.get("MINERVA_SERVER", "https://api.minerva-archive.org")
UPLOAD_SERVER_URL = os.environ.get("MINERVA_UPLOAD_SERVER", "https://gate.minerva-archive.org")

# auth
TOKEN_FILE = Path(os.environ.get("MINERVA_TOKEN_FILE", Path.home() / ".minerva-dpn" / "token"))

# downloader
ARIA2C = shutil.which("aria2c")
TEMP_DIR = Path(os.environ.get("MINERVA_TEMP_DIR", Path(tempfile.gettempdir()) / ".minerva-dpn"))
MAX_RETRIES = int(os.environ.get("MINERVA_MAX_RETRIES", 3))
RETRY_DELAY = int(os.environ.get("MINERVA_RETRY_DELAY", 5))
ARIA2C_SIZE_THRESHOLD = int(
    os.environ.get("MINERVA_ARIA2C_SIZE_THRESHOLD", 1 * 1024 * 1024)
)  # skip aria2c for files < 1 MB
HAS_ARIA2C = ARIA2C is not None

# uploader
UPLOAD_CHUNK_SIZE = (
    8 * 1024 * 1024
)  # Cloudflare limit is 50 MB, but using 8 MB to reduce total chunks and speed up uploads
UPLOAD_START_RETRIES = 12
UPLOAD_CHUNK_RETRIES = 30
UPLOAD_FINISH_RETRIES = 12

# error handling
RETRIABLE_STATUS_CODES = {408, 425, 429, 500, 502, 503, 504, 520, 521, 522, 523, 524}

# jobs
REPORT_RETRIES = 20

# worker loop
QUEUE_PREFETCH = int(os.environ.get("MINERVA_QUEUE_PREFETCH", 2))  # queue depth = concurrency * this

# console/logs
HISTORY_LINES = int(os.environ.get("MINERVA_HISTORY_LINES", 5))  # completed jobs shown above active table
