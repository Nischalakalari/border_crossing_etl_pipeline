# border_crossing_etl_pipeline
An ETL pipeline project using Python, PostgreSQL, and Pandas with data visualization.
This project implements an ETL (Extract, Transform, Load) pipeline for the Border Crossing Entry Data using Python, PostgreSQL, and data visualization libraries. It involves extracting data from a CSV file, transforming it through cleaning and formatting, loading it into a PostgreSQL database, and generating visualizations.

#etl_pipeline
│
├── Border_Crossing_Entry_Data.csv   # Raw dataset
├── project.py                       # ETL pipeline code
├── visualization.py                 # Data visualization code
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation

#Tools and Technologies Used
Python: For data processing and database operations.
PostgreSQL: For storing and querying processed data.
pgAdmin: To manage PostgreSQL and execute SQL queries.
Pandas: For data manipulation.
Psycopg2: PostgreSQL adapter for Python.
Seaborn/Matplotlib: For data visualization.

#ETL Pipeline Steps
Extract: Reads CSV data using Pandas.
Transform: Cleans data, removes duplicates, fills missing values, and formats dates.
Load: Connects to PostgreSQL, creates a table, and inserts data.

#Data Visualization
Retrieves data from PostgreSQL with SQL queries.
Uses Pandas and Seaborn to visualize top ports by total crossings.


