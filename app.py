from flask import Flask, render_template, request
import pandas as pd
from sqlalchemy import create_engine
import numpy as np 

app = Flask(__name__)

# Function to generate synthetic data
def generate_data(num_records):
    np.random.seed(0)
    data = {
        "Labor_Hours": np.random.randint(1, 12, num_records),
        "Machine_Downtime": np.random.uniform(0, 4, num_records),
        "Material_Quality": np.random.uniform(0.7, 1, num_records),
        "Maintenance_Frequency": np.random.randint(1, 5, num_records),
        "Energy_Costs": np.random.uniform(100, 500, num_records),
        "Production_Volume": np.random.randint(50, 200, num_records),
        "Error_Rate": np.random.uniform(0, 0.1, num_records),
    }
    df = pd.DataFrame(data)
    df["Productivity"] = (df["Production_Volume"] * df["Material_Quality"] - df["Error_Rate"] * df["Labor_Hours"]).clip(lower=0)
    df["Cost"] = df["Labor_Hours"] * 20 + df["Energy_Costs"] + df["Machine_Downtime"] * 50 + df["Maintenance_Frequency"] * 100
    df["Profit"] = (df["Productivity"] * 50) - df["Cost"]
    return df

# Function to connect to a database and save data
def connect_and_save(df, db_type, db_name, table_name="industrial_metrics", user=None, password=None, host=None, port=None):
    try:
        if db_type == "sqlite":
            engine = create_engine(f"sqlite:///{db_name}")
        elif db_type == "mysql":
            engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}")
        elif db_type == "postgresql":
            engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db_name}")
        else:
            return "Database type not supported."
        
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        return f"Data successfully saved to the '{table_name}' table in '{db_name}' database."
    
    except Exception as e:
        return f"An error occurred: {e}"

# Route to display the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Route to process the form submission
@app.route('/submit', methods=['POST'])
def submit():
    num_records = int(request.form['num_records'])
    db_type = request.form['db_type']
    db_name = request.form['db_name']
    
    user = password = host = port = None
    if db_type in ["mysql", "postgresql"]:
        user = request.form['user']
        password = request.form['password']
        host = request.form['host']
        port = request.form['port']
    
    df = generate_data(num_records)
    result = connect_and_save(df, db_type, db_name, user=user, password=password, host=host, port=port)
    return result

if __name__ == "__main__":
    app.run(debug=True)
