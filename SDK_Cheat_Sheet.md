
# Flywheel SDK Cheat Sheet

## Flywheel CLI Login

Logging in with your Flywheel API-Key will make the indicated instance default.

``` bash
$ fw login $API_KEY
```

## Flywheel Client

The Flywheel SDK Client is the default interface to Flywheel objects.

Providing an API-Key overrides the system default, if initialized.

``` python
import flywheel

API_KEY = ""

fw_client = flywheel.Client()
fw_client = flywheel.Client(API_KEY)
```

## Get Container by ID

Every container (Group, Projects, Sessions, and Acquisitions) can be referred to by its unique `bson` id.

``` python
ID = "bson id"
container = fw_client.get(ID)
container = container.reload()
```

## Finders

Finders can be used from the client on any container class (Groups, Projects, Subjects, Sessions, Acquisitions, Jobs)

`fw_client.container_class` (e.g. `fw_client.projects()`)

Or from an immediate child of a valid container

`parent_container.container_class` (e.g. `project.sessions()`)

The finder syntax is the same for both forms.  Some container-specific search strings may apply.

* **[\*.container_class()](https://flywheel-io.gitlab.io/product/backend/sdk/branches/master/python/flywheel.html?highlight=find_first#flywheel.finder.Finder)**:

    Returns a complete listing of the indicated container without populating files, analyses, or custom information.

    ``` python
    for session in fw_client.sessions():
        for acquisition in session.acquisitions():
            print(f"{session.label}: {acquisition.label}")
    ```

* **[\*.container_class.find()](https://flywheel-io.gitlab.io/product/backend/sdk/branches/master/python/flywheel.html?highlight=find_first#flywheel.finder.Finder)**:

    Find all items in the collection that match the provided filter. Lists of files, analyses, or custom information are not included without a `container.reload` on each container in list.

    Search strings are comma-separated conditionals acting as an `AND` statement.

    ``` python
    search = 'modified>=2019-08-07,modified<=2020-08-07'
    for session in fw_client.sessions.find(search):
        for acquisition in session.acquisitions.find(search):
            print(f"{session.label}: {acquisition.label}")
    ```

* **[\*.container_class.find_first()](https://flywheel-io.gitlab.io/product/backend/sdk/branches/master/python/flywheel.html?highlight=find_first#flywheel.finder.Finder.find_first)**:

    Find the first item matching the provided filter. Returns None if no items matched.

    ``` python
    search = 'modified>=2019-08-07,modified<=2020-08-07'
    session = fw_client.sessions.find_first(search)
    acquisition = session.acquisitions.find_first(search)
    print(f"{session.label}: {acquisition.label}")
    ```

* **[\*.container_class.find_one()](https://flywheel-io.gitlab.io/product/backend/sdk/branches/master/python/flywheel.html?highlight=find_first#flywheel.finder.Finder.find_one)**:

    Find exactly one item matching the provided filter. Raises a ValueError if 0 or 2+ items matched.

    ``` python
    session = fw_client.sessions.find_one()
    acquisition = session.acquisitions.find_one()
    print(f"{session.label}: {acquisition.label}")
    ```

* **[\*.container_class.iter()](https://flywheel-io.gitlab.io/product/backend/sdk/branches/master/python/flywheel.html?highlight=find_first#flywheel.finder.Finder.iter)**:

    Iterate over all items in the collection, without limit.

    ``` python
    for session in fw_client.sessions.iter():
        for acquisition in session.acquisitions.iter():
            print(f"{session.label}: {acquisition.label}")
    ```

* **[\*.container_class.iter_find()](https://flywheel-io.gitlab.io/product/backend/sdk/branches/master/python/flywheel.html?highlight=find_first#flywheel.finder.Finder.iter_find)**:

    Iterate over all items in the collection that match the provided filter, without limit.

    ``` python
    search = 'modified>=2019-08-07,modified<=2020-08-07'
    for session in fw_client.sessions.iter_find(search):
        for acquisition in session.acquisitions.iter_find(search):
            print(f"{session.label}: {acquisition.label}")
    ```
