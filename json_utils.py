import json
import logging
import os

logger = logging.getLogger(__name__)


def read_json(file_path):
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        return None

    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        logger.error(f"Successfully read the file: {file_path}")
        return data
    except json.JSONDecodeError:
        logger.error(f"Failed to decode JSON from the file: {file_path}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error while reading the file: {e}")
        return None


def write_json(file_path, data):
    if data is None:
        logging.error("No data to write.")
        return

    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
        logging.info(f"Successfully wrote the transformed data to {file_path}")
    except Exception as e:
        logging.error(f"Failed to write data to {file_path}: {e}")


def modify_json(data, updates):
    logger.info("Modifying JSON data")
    data.update(updates)
    return data


def transform_data(data):
    try:
        # Example transformation: Add a new key-value pair to the JSON
        if isinstance(data, dict):
            data["transformed"] = True
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    item["transformed"] = True
        logging.info("Data transformation completed successfully.")
        return data
    except Exception as e:
        logging.error(f"Error during data transformation: {e}")
        return None
