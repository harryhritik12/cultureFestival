🎉 Cultural Tapestry: An Interactive Indian Festival & Tourism Dashboard

🌟 Project Overview
Cultural Tapestry is an interactive, data-driven dashboard that bridges the gap between India's vibrant cultural festivals and its dynamic tourism landscape. It offers a centralized platform to explore Indian festivals, understand their geographical distribution, and analyze their impact on tourist footfall.

💡 Problem Statement
India is home to an incredibly diverse range of festivals celebrated across regions and cultures. However, comprehensive, organized, and interactive data—covering festival dates, cultural context, geographic spread, and tourism trends—is often fragmented and inaccessible. This makes it challenging for:

Tourists to plan cultural journeys

Researchers to analyze festival-tourism correlation

Local enthusiasts to explore regional celebrations

✨ Our Solution & Key Features
Our dashboard delivers a seamless user experience powered by Snowflake and a modern Python tech stack.

📅 Interactive Festival Calendar
Browse festivals by month with names, dates, and the states/UTs where they are celebrated.

Quickly discover cultural events throughout the year.

📊 Tourist Footfall Analysis
Visualize monthly tourist numbers for 2021 and 2022 using interactive bar charts.

Compare trends year-over-year to identify growth patterns and popular travel seasons.

Key metrics offer a quick overview of growth trends.

📍 Geographical Mapping of Festivals
Interactive map showing locations of major festivals across India.

Helps users visually understand regional distribution and plan visits.

🚀 Tech Stack
Component	Technology Used
Backend (Data)	Snowflake
Frontend	Streamlit
Programming Language	Python
Data Handling	Pandas
Visualization	Plotly Express
Database Connector	snowflake-connector-python
Environment Mgmt	python-dotenv

⚙️ Setup and Installation
1. Clone the Repository
bash
Copy
Edit
git clone <your-repository-url>
cd cultural-tapestry
2. Create and Activate a Virtual Environment (Recommended)
bash
Copy
Edit
python -m venv venv

# On Windows
.\venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Snowflake Setup
a. Environment Variables
Create a .env file in your root directory:

env
Copy
Edit
SNOWFLAKE_USER='your_username'
SNOWFLAKE_PASSWORD='your_password'
SNOWFLAKE_ACCOUNT='your_account_identifier' # e.g., xy12345.us-east-1
SNOWFLAKE_WAREHOUSE='your_warehouse_name'
SNOWFLAKE_DATABASE='your_database_name'
SNOWFLAKE_SCHEMA='your_schema_name'
b. Prepare Data Files
Ensure the following CSV files are available and correctly formatted:

festivals_with_locations.csv → For FESTIVALS_2022

sql
Copy
Edit
ID,DAY,FESTIVAL_DATE,YEAR,FESTIVAL_NAME,STATE_UT,LATITUDE,LONGITUDE
tourism_statistics.csv → For TOURISM_STATISTICS

sql
Copy
Edit
MONTH,VALUE_2021,VALUE_2022,GROWTH_2022_21
major_festivals_map.csv → For MAJOR_FESTIVAL_LOCATIONS

Copy
Edit
STATE_UT,FESTIVAL,LAT,LON
c. Run Snowflake SQL Scripts
Navigate to snowflake_setup/ and execute:

bash
Copy
Edit
snowsql -f snowflake_setup/init_db.sql
Then, execute the data load scripts:

bash
Copy
Edit
snowsql -f snowflake_setup/load_data_festivals.sql
snowsql -f snowflake_setup/load_data_tourism.sql
⚠️ If you're using S3 for staging, edit the scripts with your bucket path and AWS credentials.

5. Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
Your dashboard should now open in your default browser.

📈 Future Enhancements
Predictive Analytics for tourist trends around major festivals

User-Defined Filters by state, festival type, or date range

Detailed Festival Pages with historical and cultural information

State/District-Level Tourist Data for granular insights

Community Contributions to allow user-submitted festival info

Additional Data Sources from tourism and cultural bodies

🤝 Contribution
We welcome contributions!
Feel free to fork, raise issues, or submit pull requests.

📄 License
This project is licensed under the MIT License.

🙏 Acknowledgements
Snowflake for powering our data backend

Streamlit, Pandas, Plotly — the amazing open-source tools that made this project possible
