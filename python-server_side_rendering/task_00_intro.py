#!/usr/bin/python3
"""Generate personalized invitation files from a template."""


def generate_invitations(template, attendees):
    """Write one output_X.txt file per attendee, filling the template."""
    # Check input types
    if not isinstance(template, str):
        print("Error: template must be a string, got {}".format(
            type(template).__name__))
        return
    if not isinstance(attendees, list) or \
            not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries, got {}".format(
            type(attendees).__name__))
        return

    # Check empty inputs
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    # Fill the template for each attendee
    for index, attendee in enumerate(attendees, start=1):
        text = template
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            text = text.replace("{" + key + "}", str(value))

        try:
            with open("output_{}.txt".format(index), "w") as file:
                file.write(text)
        except Exception as e:
            print("Error writing output_{}.txt: {}".format(index, e))