"""
utils/time_logger.py
This module provides a decorator to log the execution time of functions."""

import os
import sys
import time
from discord_notify import send_message

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
api_path = os.path.join(project_root, "API")
if api_path not in sys.path:
    sys.path.append(api_path)

try:
    from api_key_loader import APIKeyLoader

    APIKeyLoader = APIKeyLoader()
except ImportError as e:
    print(
        "Could not import 'api_key_loader'. Please check that '../API/api_key_loader.py' exists."
    )
    raise e


def time_logger(original_function):
    """Decorator to log the execution time of a function."""

    def wrapper(*args, **kwargs):
        process_start_time = time.process_time()
        performance_start_time = time.perf_counter()

        result = original_function(*args, **kwargs)

        process_end_time = time.process_time()
        performance_end_time = time.perf_counter()
        execution_time = process_end_time - process_start_time
        performance_time = performance_end_time - performance_start_time
        print(f"Execution time: {execution_time:.6f} seconds", end=", ")
        print(f"Performance time: {performance_time:.6f} seconds")
        send_message(
            f"Execution time: {execution_time:.6f} seconds, Performance time: {performance_time:.6f} seconds"
        )
        return result

    return wrapper
