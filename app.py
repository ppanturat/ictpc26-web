import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSudT3DGFue2LrgIApc93JtG4LVBvjsGtajuasn7coYEfUdQN4Vh1D-mRq0Lt3sN4501NFkRP2AtrEW/pub?output=csv"

# route for homepage
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/rules')
def rules():
    return render_template('rules.html')

@app.route('/teams')
def teams():
    try:
        df = pd.read_csv(SHEET_URL)
        
        # Fill empty cells with empty strings to avoid errors
        df = df.fillna('')
        
        teams_data = []
        
        for index, row in df.iterrows():
            members_list = []
            if str(row['Member 1 ID']).strip(): members_list.append(str(row['Member 1 ID']))
            if str(row['Member 2 ID']).strip(): members_list.append(str(row['Member 2 ID']))
            if str(row['Member 3 ID']).strip(): members_list.append(str(row['Member 3 ID']))

            programs_found = set()
            
            if str(row['Member 1 Program']).strip(): programs_found.add(str(row['Member 1 Program']).strip())
            if str(row['Member 2 Program']).strip(): programs_found.add(str(row['Member 2 Program']).strip())
            if str(row['Member 3 Program']).strip(): programs_found.add(str(row['Member 3 Program']).strip())
            
            program_display = ", ".join(sorted(programs_found))

            teams_data.append({
                "name": row['Team Name'], 
                "program": program_display,  
                "members": members_list
            })
            
        return render_template('teams.html', teams=teams_data)
        
    except Exception as e:
        return f"Error reading sheet. Check column names in Sheet vs Code! <br>Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
