#!/usr/bin/python3
"""There is no module here"""


def generate_invitations(template, attendees):
    """Generates different templates from default one"""
    default_template = template
    for obj in attendees:
        template = default_template
        for key in obj:
            if obj[key] is None:
                template = template.replace(f"{{{key}}}", "N/A")
                continue
            template = template.replace(f"{{{key}}}", obj[key])
        idx = attendees.index(obj)
        new = template
        with open(f"output_{idx}.txt", "w") as f:
            f.write(new)
