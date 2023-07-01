from pathlib import Path
import pandas as pd

df = pd.read_csv('states.csv')

sql_folder = Path.cwd() / 'sql'

unique_states = df['NOM_ENT'].unique()
states = { x + 1 : unique_states[x] for x in range(0, len(unique_states)) }

for id, state in states.items():
    with open(sql_folder / 'states.sql', 'a') as file:
        file.write(f"INSERT INTO states(id, name) VALUES('{id}', '{state}');\n")
        
        cities = df[df['NOM_ENT'] == state]['NOM_MUN'].unique()

        with open(sql_folder / 'cities.sql', 'a') as file:
            
            for city in cities:
                file.write(f"INSERT INTO cities(name, state_id) VALUES('{city}', '{id}');\n")


