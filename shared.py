from dataclasses import dataclass
from pathlib import Path
from io import TextIOWrapper
import re
from collections import defaultdict


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

def get_worker_config(files_paths: list[list[str]], kwrds: list[str]):
    return [{"files": files_group, "kwrds": kwrds} for files_group in files_paths]

def search_worker(config: dict):
    result = defaultdict(list)

    for word in config["kwrds"]:
        for path in config["files"]:
            with open(path) as file:
                if search_in_file_conter(word, file):
                    result[f"{word}"].append(path)
                else:
                    result[f"{word}"] = []

    return dict(result)