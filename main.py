import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Sample Data: Structure of MITRE ATT&CK (Replace with actual dataset)
data = {
    'Technique': ['Phishing', 'Spearphishing', 'Brute Force', 'SQL Injection', 'Malware', 'PowerShell', 'Credential Dumping'],
    'Tactic': ['Initial Access', 'Initial Access', 'Credential Access', 'Execution', 'Persistence', 'Execution', 'Credential Access'],
    'Mitigation': ['User training', 'User training', 'Account lockout policies', 'Input validation', 'Anti-malware software', 'Script blocking', 'Monitor logs'],
    'Category': ['Social Engineering', 'Social Engineering', 'Password Cracking', 'Injection', 'Malware', 'Scripting', 'Password Cracking']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Circular Dendrogram (Sunburst chart with filters)
fig = px.sunburst(df, path=['Tactic', 'Category', 'Technique'], values=None, 
                  title='MITRE ATT&CK Circular Dendrogram')

# Question 1: Most common techniques (formatted vertically)
technique_counts = df['Category'].value_counts().reset_index()
technique_counts.columns = ['Category', 'Count']
technique_str = "<br>".join([f"{row['Category']}: {row['Count']}" for _, row in technique_counts.iterrows()])

# Question 2: Top 3 Tactics (formatted vertically)
top_tactics = df['Tactic'].value_counts().nlargest(3).reset_index()
top_tactics.columns = ['Tactic', 'Count']
tactics_str = "<br>".join([f"{row['Tactic']}: {row['Count']}" for _, row in top_tactics.iterrows()])

# Question 3: Mitigation Suggestions (formatted vertically)
mitigations_list = [f"{technique}: {mitigation}" for technique, mitigation in df.groupby('Technique')['Mitigation'].first().items()]
mitigations_str = "<br>".join(mitigations_list)

# Create annotations to display text next to the figure with proper wrapping and vertical alignment
annotations = [
    go.layout.Annotation(
        x=1.05,  # Move it to the right
        y=0.85,
        xref="paper",
        yref="paper",
        showarrow=False,
        text=f"<b>Most Common Techniques:</b><br>{technique_str}",
        align="left",
        font=dict(size=12),
        width=250,  # Set a fixed width to allow wrapping
    ),
    go.layout.Annotation(
        x=1.05,  # Align all at same x
        y=0.55,
        xref="paper",
        yref="paper",
        showarrow=False,
        text=f"<b>Top 3 Tactics:</b><br>{tactics_str}",
        align="left",
        font=dict(size=12),
        width=250,  # Set a fixed width to allow wrapping
    ),
    go.layout.Annotation(
        x=1.05,
        y=0.25,
        xref="paper",
        yref="paper",
        showarrow=False,
        text=f"<b>Mitigation Suggestions:</b><br>{mitigations_str}",  # Suggestions in vertical row
        align="left",
        font=dict(size=12),
        width=250,  # Set a fixed width to allow wrapping
    )
]

# Update figure layout to add annotations
fig.update_layout(
    annotations=annotations,
    margin=dict(l=0, r=400, t=50, b=0),  # Adjust right margin for space
)

# Show the figure
fig.show()
