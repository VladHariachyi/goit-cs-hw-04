from concurrent.futures import ThreadPoolExecutor

from shared import SearchConfig, search_worker, get_worker_files, get_worker_config


def search_in_files(search_config: SearchConfig):
    files_peer_worker = get_worker_files(search_config.file_paths)
    config = get_worker_config(files_peer_worker, search_config.keywords)

    with ThreadPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(search_worker, config))

        return results
