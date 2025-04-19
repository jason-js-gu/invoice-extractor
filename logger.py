import pathlib
from datetime import datetime as dt
from typing import List


def logger(module: str, log_name_suffix: str) -> pathlib.Path:
    """
    Generate a timestamped log file path in a 'logs' directory relative to the given module.

    Args:
        module (str): The file path of the module that is generating the log.
        log_name_suffix (str): A descriptive suffix to append to the log file name.

    Returns:
        pathlib.Path: The full path to the generated log file.
    """
    # Determine the directory where the log file should be stored
    log_path = pathlib.Path(module).parent / "logs"

    # Create the 'logs' directory if it doesn't exist
    if not log_path.is_dir():
        log_path.mkdir(parents=True, exist_ok=True)

    # Generate a timestamp string in the format YYYYMMDDHHMMSS
    time_stamp = dt.now()
    formatter = "%Y%m%d%H%M%S"
    str_now = time_stamp.strftime(formatter)

    # Construct the log filename using the module name, timestamp, and suffix
    log_filename = f"{pathlib.Path(module).stem}-{str_now}-{log_name_suffix}.log"

    # Return the full path to the log file
    return log_path / log_filename


def log_it(log_path: pathlib.Path, msgs: List[str], img_name: str) -> str:
    """
    Append a timestamped log entry to the given log file, including a header for the processed image
    and a list of messages.

    Args:
        log_path (pathlib.Path): The path to the log file where messages should be written.
        msgs (List[str]): A list of message strings to log.
        img_name (str): The name of the image being processed.

    Returns:
        str: The absolute path to the log file as a string.
    """
    # Open the log file in append mode with UTF-8 encoding
    with log_path.open("a", encoding="utf-8") as lp:
        # Get current timestamp with millisecond precision
        timestamp = dt.now()
        # Prepare the caption for this image processing entry
        caption = (
            f"{timestamp.isoformat(timespec='milliseconds')}: "
            f"Processing image {img_name}\n"
        )
        # Write the caption followed by each log message
        lp.write(caption)
        for msg in msgs:
            lp.write(f"{msg}\n")

    # Return the absolute path to the log file
    return str(log_path.absolute())
