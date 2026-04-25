def generate_invitations(template, attendees):
    # ---- Input validation ----
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # ---- Empty checks ----
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # ---- Process attendees ----
    for i, attendee in enumerate(attendees, start=1):
        # Extract values with fallback to "N/A"
        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        # Replace placeholders
        output_content = template
        output_content = output_content.replace("{name}", str(name))
        output_content = output_content.replace("{event_title}", str(event_title))
        output_content = output_content.replace("{event_date}", str(event_date))
        output_content = output_content.replace("{event_location}", str(event_location))

        # ---- Write file ----
        filename = f"output_{i}.txt"
        try:
            with open(filename, "w") as f:
                f.write(output_content)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
