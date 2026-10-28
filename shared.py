from dataclasses import dataclass
from pathlib import Path
from io import TextIOWrapper
import re


MAX_FILES_AMOUNT_FOR_WORKER = 2

@dataclass
class SearchConfig:
    keywords: list[str]
    file_paths: list[Path]

def get_worker_files(file_paths: list[str]) -> list[list[str]]:
    return [file_paths[i:i + MAX_FILES_AMOUNT_FOR_WORKER] for i in range(0, len(file_paths), MAX_FILES_AMOUNT_FOR_WORKER)]

def search_in_file_conter(
    search_criteria: str,
    file: TextIOWrapper
) -> int:
    count = 0
    
    for line in file:
        count += len(re.findall(search_criteria, line, re.IGNORECASE))

    return count