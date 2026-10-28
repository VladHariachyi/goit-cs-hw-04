from multiprocessing import Pool

from shared import SearchConfig, search_worker, get_worker_files, get_worker_config


def search_in_files(search_config: SearchConfig):
    files_peer_worker = get_worker_files(search_config.file_paths)
    config = get_worker_config(files_peer_worker, search_config.keywords)

    with Pool(processes=2) as pool:
        results = list(pool.map(search_worker, config))

        return results

        
