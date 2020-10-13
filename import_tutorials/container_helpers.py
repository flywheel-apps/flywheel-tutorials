"""
The following are helper functions for finding or creating various containers in
Flywheel.
"""
import os
import time

import flywheel


def find_or_create_group(fw_client, group_id, label):
    """
    Find or create Group indictated by "label".

    Args:
        group_id (str): Instance-unique, lower-case alphabetic with "_" as id for Group.
        label (str): The label for the Group. Less restricted than 'id'.

    Returns:
        flywheel.Group: The found or created Group.
    """
    if not label:
        return None

    group = fw_client.groups.find_first(f"label={label}")

    if not group:
        group = flywheel.Group(id=group_id, label=label)
        _group_id = fw_client.add_group(group)
        group = fw_client.get_group(_group_id)

    if group:
        group = group.reload()

    return group


def find_or_create_project(label, group):
    """
    Find or create Flywheel Project with "label" under "group".

    Args:
        label (str): [description]
        group (flywheel.Group): The Flywheel Group object to create this Project under.

    Returns:
        flywheel.Project: The found or created Flywheel Project object.
    """
    if not label:
        return None
    project = group.projects.find_first(f"label={label}")
    return project


def find_or_create_subject(label, sex, project):
    """
    Find or create a Subject with "label" under "project".

    If Subject is found, "sex" is disregarded.

    Args:
        label (str): The label to use for the Subject name.
        sex (str): The sex of the Subject. Can be `None`.
        project (flywheel.Project): The project object to create this Subject under.

    Returns:
        flywheel.Subject: The found or created Flywheel Subject object.
    """
    if not label:
        return None
    subject = project.subjects.find_first(f"label={label}")

    if not subject:
        subject = project.add_subject(code=label, label=label)
        if sex:
            subject.update(sex=sex)

    if subject:
        subject = subject.reload()

    return subject


def find_or_create_session(label, age, subject):
    """
    Find or create a Session with "label" under "subject".

    If Session is found, "age" is disregarded.

    Args:
        label (str): The label to display for this Session.
        age (int): The age of the Subject at the event of this Session.
        subject (flywheel.Subject): The Flywheel Subject to create the Session under.

    Returns:
        flywheel.session: The found or created Flywheel Session.
    """
    if not label:
        return None
    session = subject.sessions.find_first(f"label={label}")

    if not session:
        session = subject.add_session(label=label)
        if age:
            session.update(age=age)

    if session:
        session = session.reload()

    return session


def find_or_create_acquisition(label, info_dict, fp, session, update_info=True):
    """
    Find or create a Acquisition with "label" under "Session".

    If Acquisition exists, upload filepath "fp" and update info if `update_info`==True.

    Args:
        label (str): The label to display for this Acquisition
        info_dict (dict): Dictionary to update or add to instance of Acquisition.
        fp (str): Fullpath to a file to upload into the found/created Acquisition.
        session (flywheel.Session): Session to find or create Acquisition under.
        update_info (bool, optional): Flag to update info of existing Acquisition.
            Defaults to True.

    Returns:
        flywheel.Acquisition: The found or created Flywheel Acquisition object.
    """
    if not label:
        return None
    acq = session.acquisitions.find_first(f"label={label}")

    if not acq:
        acq = session.add_acquisition(label=label)

        if info_dict:
            acq.update(info=info_dict)

    if acq:
        basename = os.path.basename(fp)
        if os.path.isfile(fp) and not acq.get_file(basename):

            acq.upload_file(fp)

            print(f"Uploading {fp} to acquisition {acq.id}")
            while not acq.get_file(basename):
                acq = acq.reload()
                time.sleep(1)

    if update_info:
        f = acq.get_file(basename)
        f.update({"type": "dicom", "modality": "X-ray"})
        f.update_info(info_dict)

    acq = acq.reload()

    return acq
