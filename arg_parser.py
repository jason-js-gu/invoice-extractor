import argparse


def get_arg_parser(module: str, description: str) -> argparse.ArgumentParser:
    """
    Create and configure an argument parser for a command-line interface.

    Args:
        module (str): The name of the module or script (used as the program name in help).
        description (str): A short description of what the script does.

    Returns:
        argparse.ArgumentParser: The configured argument parser.
    """
    # Initialize the argument parser with a program name and description
    parser = argparse.ArgumentParser(prog=module, description=description)

    # Add an optional argument for a single image file to process
    parser.add_argument(
        "-f",
        "--image-file",
        help="Path to the image file to be processed",
        type=str,
    )

    # Add an optional argument for the folder to save processed images
    parser.add_argument(
        "-p",
        "--folder-path",
        help="Directory path where processed images will be saved",
        type=str,
    )

    return parser
