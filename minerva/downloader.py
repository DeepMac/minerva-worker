from pathlib import Path

from minerva.constants import ARIA2C, ARIA2C_SIZE_THRESHOLD
from minerva.downloaders import Downloader, ProgressCallback
from minerva.downloaders.aria2c import Aria2c
from minerva.downloaders.httpx import HTTPX


async def download_file(
    url: str, dest: Path, aria2c_connections: int, known_size: int, pre_allocation: str, on_progress: ProgressCallback
) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)

    downloader: Downloader
    if ARIA2C and known_size >= ARIA2C_SIZE_THRESHOLD:
        downloader = Aria2c()
    else:
        downloader = HTTPX()

    await downloader(
        url=url, dest=dest, connections=aria2c_connections, pre_allocation=pre_allocation, on_progress=on_progress
    )
