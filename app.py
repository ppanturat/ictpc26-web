import csv
import requests
import io
from flask import Flask, render_template

app = Flask(__name__)

SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSudT3DGFue2LrgIApc93JtG4LVBvjsGtajuasn7coYEfUdQN4Vh1D-mRq0Lt3sN4501NFkRP2AtrEW/pub?output=csv"


# route for homepage
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/rules")
def rules():
    return render_template("rules.html")


@app.route("/schedule")
def schedule():
    return render_template("schedule.html")


@app.route("/scores")
def scores():
    return render_template("scores.html")


@app.route("/teams")
def teams():
    try:
        # Download the CSV text using requests (Lighter than Pandas)
        response = requests.get(SHEET_URL)
        response.raise_for_status()  # Check for download errors

        # Force Python to read the file as UTF-8 (supports Thai, Emoji, etc.)
        response.encoding = "utf-8"

        # Parse CSV data
        csv_file = io.StringIO(response.text)
        reader = csv.DictReader(csv_file)

        teams_data = []

        for row in reader:
            # --- Collect Members ---
            members_list = []
            if row.get("Member 1 ID", "").strip():
                members_list.append(row["Member 1 ID"].strip())
            if row.get("Member 2 ID", "").strip():
                members_list.append(row["Member 2 ID"].strip())
            if row.get("Member 3 ID", "").strip():
                members_list.append(row["Member 3 ID"].strip())

            # --- Calculate Program ---
            programs_found = set()
            if row.get("Member 1 Program", "").strip():
                programs_found.add(row["Member 1 Program"].strip())
            if row.get("Member 2 Program", "").strip():
                programs_found.add(row["Member 2 Program"].strip())
            if row.get("Member 3 Program", "").strip():
                programs_found.add(row["Member 3 Program"].strip())

            program_display = ", ".join(sorted(programs_found))

            teams_data.append(
                {
                    "name": row.get("Team Name", "Unknown"),
                    "program": program_display,
                    "members": members_list,
                }
            )

        # Sort the teams (A-Z)
        teams_data = sorted(teams_data, key=lambda x: x['name'].lower())

        return render_template("teams.html", teams=teams_data)

    except Exception as e:
        return f"Error reading sheet: {e}"


if __name__ == "__main__":
    app.run(debug=True)
