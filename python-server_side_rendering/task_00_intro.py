#!/usr/bin/python3
"""There is no module here"""


def generate_invitations(default_template, attendees):
    """Generates different templates from default one"""
    try:
        isinstance(default_template, str) or isinstance(attendees, list)
        try:
            for obj in attendees:
                try:
                    template = default_template
                except Exception:
                    return "Template is empty, no output files generated."
                for key in obj:
                    if obj[key] is None:
                        template = template.replace(f"{{{key}}}", "N/A")
                        continue
                    template = template.replace(f"{{{key}}}", obj[key])
                idx = attendees.index(obj)
                new = template
                with open(f"output_{idx}.txt", "w") as f:
                    f.write(new)
        except IndexError:
            return "No data provided, no output files generated."
    except Exception:
        return "Invalid input"
