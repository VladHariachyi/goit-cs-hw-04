from multiprocessing import Pool
from collections import defaultdict

from shared import SearchConfig, search_in_file_conter, get_worker_files


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


def search_in_files(search_config: SearchConfig):
    files_peer_worker = get_worker_files(search_config.file_paths)
    config = [{"files": files_group, "kwrds": search_config.keywords} for files_group in files_peer_worker]

    with Pool(processes=2) as pool:
        results = list(pool.map(search_worker, config))

        return results

        
