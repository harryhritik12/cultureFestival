Cultural Tapestry: An Interactive Indian Festival & Tourism Dashboard
🌟 Project Overview
Cultural Tapestry is an interactive, data-driven dashboard designed to bridge the gap between India's rich cultural festivals and its dynamic tourism landscape. This project aims to provide a centralized and intuitive platform for anyone interested in exploring Indian festivals, understanding their geographical distribution, and analyzing their associated impact on tourist footfall.

💡 Problem Statement
India is a land of incredible cultural diversity, with countless festivals celebrated throughout the year. However, comprehensive information on these festivals—their precise dates, cultural significance, specific locations, and their correlation with tourism trends—is often fragmented and not easily accessible in an interactive format. This makes it challenging for tourists, researchers, and even local enthusiasts to plan cultural journeys or gain quick insights into regional celebrations and peak travel periods.

✨ Our Solution & Key Features
Our dashboard tackles this problem by offering a seamless experience powered by Snowflake as the robust data backend.

📅 Interactive Festival Calendar:
Browse festivals month-wise, displaying their names, dates, and the states/UTs where they are predominantly celebrated.
Provides a quick and easy way to discover cultural events throughout the year.
📊 Tourist Footfall Analysis:
Visualize monthly tourist numbers for 2021 and 2022 using interactive bar charts.
Compare year-over-year trends and identify growth patterns, highlighting popular travel seasons.
Includes a prominent metric for quick insights into monthly tourist growth.
📍 Geographical Mapping of Festivals:
An interactive map pinpoints the locations of major festivals across different Indian states and Union Territories.
Helps users visually understand the geographical spread of cultural celebrations and plan regional explorations.
🚀 How We Built It: Tech Stack
Our solution leverages a modern, scalable architecture, with Snowflake at its core.

Data Warehouse: Snowflake
Used for storing all raw and processed data, including festival details, tourism statistics, and geographical coordinates.
Ensures high performance, scalability, and secure data management.
Web Application Framework: Streamlit (Python)
Provides a rapid way to build interactive and responsive web applications.
Enables intuitive UI components like st.selectbox, st.dataframe, st.metric, and st.map.
Programming Language: Python
Data Manipulation: Pandas
Used for efficient data handling and preparation within the Streamlit application.
Visualization: Plotly Express
Generates interactive and visually appealing charts for tourist footfall analysis.
Database Connector: snowflake-connector-python
Facilitates seamless and secure connectivity between the Streamlit app and Snowflake.
Environment Management: python-dotenv
Used for securely managing Snowflake credentials and other environment variables.
⚙️ Setup and Installation
Follow these steps to get the project running locally:

1. Clone the Repository
Bash

git clone <your-repository-url>
cd cultural-tapestry
2. Create and Activate a Virtual Environment (Recommended)
Bash

python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
3. Install Dependencies
Bash

pip install -r requirements.txt
4. Snowflake Setup
Before running the application, you need to set up your Snowflake environment and load the data.

a.  Environment Variables:
Create a .env file in the root directory of your project with your Snowflake connection details:

```env
SNOWFLAKE_USER='your_username'
SNOWFLAKE_PASSWORD='your_password'
SNOWFLAKE_ACCOUNT='your_account_identifier' # e.g., xy12345.us-east-1
SNOWFLAKE_WAREHOUSE='your_warehouse_name'
SNOWFLAKE_DATABASE='your_database_name'
SNOWFLAKE_SCHEMA='your_schema_name'
```
b.  Prepare Data Files:
You'll need CSV files for your data. Ensure they are correctly formatted:
* festivals_with_locations.csv: For FESTIVALS_2022 table.
(Example columns: ID,DAY,FESTIVAL_DATE,YEAR,FESTIVAL_NAME,STATE_UT,LATITUDE,LONGITUDE)
* tourism_statistics.csv: For TOURISM_STATISTICS table.
(Example columns: MONTH,VALUE_2021,VALUE_2022,GROWTH_2022_21)
* major_festivals_map.csv: For MAJOR_FESTIVAL_LOCATIONS table.
(Example columns: STATE_UT,FESTIVAL,LAT,LON)

c.  Run Snowflake SQL Scripts:
Navigate to the snowflake_setup/ directory and execute the SQL scripts in order using SnowSQL or your preferred Snowflake client.

* `init_db.sql`: Creates the database, schema, and tables.
* `load_data_festivals.sql`: Loads data into `FESTIVALS_2022` and `MAJOR_FESTIVAL_LOCATIONS`.
* `load_data_tourism.sql`: Loads data into `TOURISM_STATISTICS`.

Example for `init_db.sql` using SnowSQL:
```bash
snowsql -f snowflake_setup/init_db.sql
```
*(Remember to replace `YOUR_WAREHOUSE_NAME`, `your-s3-bucket/path/`, and AWS credentials in the `load_data_*.sql` files if you are using S3 stages for loading, or adjust for local staging.)*
5. Run the Streamlit Application
Bash

streamlit run app.py
This command will open the dashboard in your default web browser.

📈 Future Enhancements
Predictive Analytics: Implement forecasting models for future tourist footfall, especially around major festivals.
User-Defined Filters: Allow users to filter festivals by state, type, or specific date ranges.
Detailed Festival Pages: Add more in-depth information about individual festivals, including historical context and associated events.
State-Specific Tourist Data: If available, integrate more granular tourist data at the state or district level for a richer analysis.
Community Contributions: Explore ways for users to submit or verify festival information.
More Data Sources: Integrate data from additional tourism bodies or cultural archives.
🤝 Contribution
Feel free to fork this repository, open issues, or submit pull requests.

📄 License
This project is open-source and available under the MIT License.

🙏 Acknowledgements
Snowflake for providing a powerful data platform for this hackathon.
Streamlit, Pandas, Plotly for amazing open-source libraries that made development a breeze.
