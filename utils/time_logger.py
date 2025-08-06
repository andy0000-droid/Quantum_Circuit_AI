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


# pylint: disable=too-few-public-methods
class TimeLogger:
    """Class to log the execution time of methods."""

    def __init__(self, org_func):
        self.org_func = org_func
        self.execution_time = None
        self.performance_time = None

    def __call__(self, *args, **kwargs):
        process_start_time = time.process_time_ns()
        performance_start_time = time.perf_counter_ns()

        result = self.org_func(*args, **kwargs)

        process_end_time = time.process_time_ns()
        performance_end_time = time.perf_counter_ns()
        execution_time = process_end_time - process_start_time
        performance_time = performance_end_time - performance_start_time
        print(f"Execution time: {execution_time} nano seconds", end=", ")
        print(f"Performance time: {performance_time} nano seconds")
        send_message(
            f"Execution time: {execution_time} nano seconds, Performance time: {performance_time} nano seconds"
        )
        self.execution_time = execution_time
        self.performance_time = performance_time
        return result

    @property
    def get_perf_time(self):
        """Get the performance time."""
        return self.execution_time, self.performance_time


if __name__ == "__main__":
    # Example usage
    @TimeLogger
    def example_function():
        """An example function to demonstrate the TimeLogger decorator."""
        time.sleep(1)  # Simulate a function that takes some time to execute

    example_function()
