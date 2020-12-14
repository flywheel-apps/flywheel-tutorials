"""
The following are helper functions for finding or creating various containers in
Flywheel.
"""
import logging
import os
import time

import flywheel

log = logging.getLogger(__name__)


def find_or_create_group(fw_client, group_id, label):
    """
    Find or create Group indictated by "label".

    Args:
        fw_client (flywheel.Client): An active client to a Flywheel for an account with
            site-admin privileges.
        group_id (str): Instance-unique, lower-case alphabetic with "_" as id for Group.
        label (str): The Group label to find or create. Less restricted than 'id'.

    Returns:
        flywheel.Group: The found or created Group.
    """
    if not label:
        return None

    group = fw_client.groups.find_first(f"label={label}")

    if not group:
        log.info(f'Group with label "{label}" not found, creating.')
        group = flywheel.Group(id=group_id, label=label)
        _group_id = fw_client.add_group(group)
        group = fw_client.get_group(_group_id)
    else:
        log.info(f'Group with label "{label}" found.')
    if group:
        group = group.reload()

    return group


def find_or_create_project(label, group, update=True, **kwargs):
    """
    Find or create Flywheel Project with "label" under "group".

    Args:
        label (str): The Project label to find or create.
        group (flywheel.Group): The Flywheel Group object to create this Project under.
        update (bool, optional): Flag to update metadata of new or existing Project.
            Defaults to True.
        kwargs (dict): Any key/value properties of the Project you would like to update.
            Included `info` key is handled separately.
    Returns:
        flywheel.Project: The found or created Flywheel Project object.
    """
    if not label:
        return None
    project = group.projects.find_first(f"label={label}")

    if not project:
        log.info(f'Project with label "{label}" not found, creating.')
        project = group.add_project(label=label)
    else:
        log.info(f'Project with label "{label}" found.')

    if project:
        if update and kwargs:
            # Check for info, separate update process
            if "info" in kwargs:
                info = kwargs.pop("info")
                project.update_info(info)
            # Check for empty dictionary
            if kwargs:
                project.update(**kwargs)

        project = project.reload()

    return project


def find_or_create_subject(label, project, update=True, **kwargs):
    """
    Find or create a Subject with "label" under "project".

    If Subject is found, "sex" is disregarded.

    Args:
        label (str): The Subject label to find or create.
        sex (str): The sex of the Subject. Can be `None`.
        project (flywheel.Project): The project object to create this Subject under.
        update (bool, optional): Flag to update metadata of new or existing Subject.
            Defaults to True.
        kwargs (dict): Any key/value properties of the Subject you would like to update.
            Included `info` key is handled separately.
    Returns:
        flywheel.Subject: The found or created Flywheel Subject object.
    """
    if not label:
        return None
    subject = project.subjects.find_first(f"label={label}")

    if not subject:
        log.info(f'Subject with label "{label}" not found, creating.')
        subject = project.add_subject(code=label, label=label)
    else:
        log.info(f'Subject with label "{label}" found.')

    if update and kwargs:
        subject.update(**kwargs)

    if subject:
        if update and kwargs:
            # Check for info, separate update process
            if "info" in kwargs:
                info = kwargs.pop("info")
                subject.update_info(info)
            # Check for empty dictionary
            if kwargs:
                subject.update(**kwargs)
        subject = subject.reload()

    return subject


def find_or_create_session(label, subject, update=True, **kwargs):
    """
    Find or create a Session with "label" under "subject".

    If Session is found, "age" is disregarded.

    Args:
        label (str): The Session label to find or create.
        subject (flywheel.Subject): The Flywheel Subject to create the Session under.
        update (bool, optional): Flag to update metadata of new or existing Session.
            Defaults to True.
        kwargs (dict): Any key/value properties of the Session you would like to update.
            Included `info` key is handled separately.
    Returns:
        flywheel.Session: The found or created Flywheel Session.
    """
    if not label:
        return None
    session = subject.sessions.find_first(f"label={label}")

    if not session:
        log.info(f'Session with label "{label}" not found, creating.')
        session = subject.add_session(label=label)
    else:
        log.info(f'Session with label "{label}" found.')

    if session:
        if update and kwargs:
            # Check for info, separate update process
            if "info" in kwargs:
                info = kwargs.pop("info")
                session.update_info(info)
            # Check for empty dictionary
            if kwargs:
                session.update(**kwargs)

        session = session.reload()

    return session


def find_or_create_acquisition(label, session, update=True, **kwargs):
    """
    Find or create a Acquisition with "label" under "Session".

    If Acquisition exists, upload filepath "fp" and update info if `update_info`==True.

    Args:
        label (str): The Acquisition label to search or create.
        session (flywheel.Session): Session to find or create Acquisition under.
        update (bool, optional): Flag to update metadata of new or existing Acquisition.
            Defaults to True.
        kwargs (dict): Any key/value properties of the Acquisition subject you would
            like to update. Included `info` key is handled separately.

    Returns:
        flywheel.Acquisition: The found or created Flywheel Acquisition object.
    """
    if not label:
        return None

    acq = session.acquisitions.find_first(f"label={label}")

    if not acq:
        log.info(f'Acquisition with label "{label}" not found, creating.')
        acq = session.add_acquisition(label=label)

    else:
        log.info(f'Acquisition with label "{label}" found.')

    if acq:
        if update and kwargs:
            # Check for info, separate update process
            if "info" in kwargs:
                info = kwargs.pop("info")
                acq.update_info(info)
            # Check for empty dictionary
            if kwargs:
                acq.update(**kwargs)

        acq = acq.reload()

    return acq


def upload_file_to_acquisition(acquisition, fp, update=True, **kwargs):
    """Upload file to Acquisition container and update info if `update=True`.

    Args:
        acquisition (flywheel.Acquisition): A Flywheel Acquisition
        fp (Path-like): Path to file to upload
        update (bool): If true, update file metadata with key/value passed as kwargs.
        kwargs (dict): Any key/value properties of the Acquisition file you would like
            to update. Included `info` key is handled separately.
    """
    basename = os.path.basename(fp)
    if not os.path.isfile(fp):
        raise ValueError(f"{fp} is not file.")

    if acquisition.get_file(basename):
        log.info(f"File {basename} already exists in container. Skipping.")
        return
    else:
        log.info(f"Uploading {fp} to acquisition {acquisition.id}")
        acquisition.upload_file(fp)
        # to make sure the file is available before performing an update
        while not acquisition.get_file(basename):
            acquisition = acquisition.reload()
            time.sleep(1)

    if update and kwargs:
        f = acquisition.get_file(basename)
        # Check for info, separate process
        if "info" in kwargs:
            info = kwargs.pop("info")
            f.update_info(info)
        # Check for empty dictionary
        if kwargs:
            f.update(**kwargs)
