from timeit import timeit

from file_managing_via_multiprocessing import search_in_files as sif_multiprocessing
from file_managing_via_threading import search_in_files as sif_threading
from shared import SearchConfig


search_config = SearchConfig(
    keywords=["software", "power", "cities"],
    file_paths=[
        "documents/doc_1.txt",
        "documents/doc_2.txt",
        "documents/doc_3.txt",
        "documents/doc_4.txt"
    ]
)

if __name__ == "__main__":
    sif_threading_res = None
    sif_multiprocessing_res = None

    def sif_threading_wrapper(search_config):
        global sif_threading_res
        sif_threading_res = sif_threading(search_config)

    def sif_multiprocessing_wrapper(search_config):
        global sif_multiprocessing_res
        sif_multiprocessing_res = sif_multiprocessing(search_config)

    sif_threading_execution_time = timeit(
        stmt=lambda: sif_threading_wrapper(search_config),
        number=1
    )
    sif_multiprocessing_execution_time = timeit(
        stmt=lambda: sif_multiprocessing_wrapper(search_config),
        number=1
    )

    print(f"\nThreading search time: {sif_threading_execution_time:.4f} s \n Search res: {sif_threading_res}")
    print(f"\nMultiprocessing search time: {sif_multiprocessing_execution_time:.4f} s \n Search res: {sif_multiprocessing_res}")