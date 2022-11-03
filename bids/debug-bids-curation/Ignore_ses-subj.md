# Debug BIDS Curation

## Add a new acquisition type from the BIDS Specification

Here is an example showing how to ignore entire subjects and sessions by putting "_ignore-BIDS" in the session or subject label:

```json
        {
            "id": "bids_session",
            "template": "session",
            "where": {
                "container_type": "session"
            },
            "initialize": {
                "ignore": {
                    "$switch": {
                        "$on": "session.label",
                        "$cases": [
                            {
                                "$regex": "(^|.*_)ignore(-(BIDS|bids)).*$",
                                "$value": true
                            },
                            {
                                "$default": true,
                                "$value": false
                            }
                        ]
                    }
                },
                "ignore": {
                    "$switch": {
                        "$on": "subject.label",
                        "$cases": [
                            {
                                "$regex": "(^|.*_)ignore(-(BIDS|bids)).*$",
                                "$value": true
                            },
                            {
                                "$default": true,
                                "$value": false
                            }
                        ]
                    }
                }
            }
        },
```
