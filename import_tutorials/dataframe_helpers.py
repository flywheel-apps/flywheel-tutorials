"""
    Various functions to facilitate the cleaning and formating of pandas dataframes.

    This may be expanded as the need arises.
"""
import copy
import datetime
import logging

import numpy as np

log = logging.getLogger(__name__)


def convert_time_to_seconds(time_span, scale):
    """
    Convert arbitrary time span to seconds.

    On failure, returns 0 seconds.

    Args:
        time_span (str): The length of time specified by units "scale".
        scale (str): The units of the length of time specified in "time_span".
            Valid Entries: 'Y', 'M', 'W', 'D'
    Returns:
        int: Total seconds in time_span.
    """

    conversion = {
        "Y": 365.25,
        "M": 30,
        "W": 7,
        "D": 1,
    }
    try:
        seconds = datetime.timedelta(
            int(time_span) * conversion.get(scale)
        ).total_seconds()
    except ValueError:
        log.warning("Error, returning 0.")
        seconds = 0
    return seconds


def format_sex_string(sex_str):
    """
    Converts 'M', 'F', or else to 'male', 'female', or empty string (e.g. '').

    Args:
        sex_str (str): String consisting of 'M', 'F', '', or None.

    Returns:
        str: 'M', 'F', or ''
    """
    if sex_str == "M":
        sex = "male"
    elif sex_str == "F":
        sex = "female"
    else:
        sex = ""
    return sex


def create_session_label(offset, default_session_label):
    """
    Format Session label

    Args:
        offset (str): Number of days since the start of symptoms or hospitalization.
            See SCHEMA.md.

    Returns:
        str: Label of Session
    """
    if not offset:
        label = default_session_label
    elif np.isnan(offset):
        label = default_session_label
    else:
        label = f"offset_{str(int(offset)).zfill(3)}"
    return label


def cleanup_row_dict(row_dict):
    """
    Cleanup session age, clinical notes, other notes, and empty values.

    Args:
        row_dict (dict): Raw dictionary representation of dataframe row.

    Returns:
        dict: Cleaned version of row_dict.
    """
    # fix session age
    row_dict["session_age"] = int(row_dict["session_age"])
    # fix notes
    if row_dict.get("Unnamed: 16"):
        row_dict["clinical notes"] = "\s".join(
            [row_dict["clinical notes"], row_dict["other notes"]]
        )
        row_dict["other notes"] = row_dict["Unnamed: 16"]
        row_dict["Unnamed: 16"] = ""

    # Copy row_dict
    return_dict = copy.deepcopy(row_dict)

    # To remove empty values
    for key, value in row_dict.items():
        if value in ["", None]:
            return_dict.pop(key)

    return return_dict
