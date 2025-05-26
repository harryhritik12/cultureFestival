import os
import streamlit as st
import plotly.express as px
import snowflake.connector
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# Improved connection handling with error checking
def get_snowflake_conn():
    try:
        conn = snowflake.connector.connect(
            user=os.getenv("SNOWFLAKE_USER"),
            password=os.getenv("SNOWFLAKE_PASSWORD"),
            account=os.getenv("SNOWFLAKE_ACCOUNT"),
            warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
            database=os.getenv("SNOWFLAKE_DATABASE"),
            schema=os.getenv("SNOWFLAKE_SCHEMA")
        )
        return conn
    except Exception as e:
        st.error(f"Connection error: {str(e)}")
        return None

def get_festivals_by_month(month):
    conn = get_snowflake_conn()
    if conn is None:
        return pd.DataFrame()
    
    try:
        cur = conn.cursor()
        month_num = datetime.strptime(month, "%B").month
        
        query = f"""
            SELECT * FROM festivals_2022
            WHERE EXTRACT(MONTH FROM Date) = {month_num}
            ORDER BY Date
        """
        cur.execute(query)
        df = cur.fetch_pandas_all()
        
        if not df.empty:
            df.columns = ['Id', 'Day', 'Date', 'Year', 'Festival_Name']
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.strftime('%Y-%m-%d')
        else:
            st.warning(f"No festivals found for {month}")
            
        return df
    except Exception as e:
        st.error(f"Query error: {str(e)}")
        return pd.DataFrame()
    finally:
        if 'cur' in locals(): cur.close()
        if conn: conn.close()

def get_tourist_data():
    conn = get_snowflake_conn()
    if conn is None:
        return pd.DataFrame()
    
    try:
        cur = conn.cursor()
        query = """
    SELECT 
        MONTH,
        VALUE_2021, 
        VALUE_2022,
        GROWTH_2022_21 AS GROWTH
    FROM RAW_FESTIVAL_DATA
    WHERE MONTH != 'Total (Jan-Dec)'
    ORDER BY CASE MONTH
        WHEN 'January' THEN 1
        WHEN 'February' THEN 2
        WHEN 'March' THEN 3
        WHEN 'April' THEN 4
        WHEN 'May' THEN 5
        WHEN 'June' THEN 6
        WHEN 'July' THEN 7
        WHEN 'August' THEN 8
        WHEN 'September' THEN 9
        WHEN 'October' THEN 10
        WHEN 'November' THEN 11
        WHEN 'December' THEN 12
        ELSE 13
    END
"""

        cur.execute(query)
        df = cur.fetch_pandas_all()
        
        if not df.empty:
            df.columns = ['Month', 'Value_2021', 'Value_2022', 'Growth']
        else:
            st.warning("No tourist data found")
            
        return df
    except Exception as e:
        st.error(f"Query error: {str(e)}")
        return pd.DataFrame()
    finally:
        if 'cur' in locals(): cur.close()
        if conn: conn.close()

# Streamlit UI
st.set_page_config(layout="wide", page_title="Cultural Festival Dashboard")

# Title and description
st.title("🎉 Cultural Festival Calendar & Insights")
st.markdown("""
Explore festival data and tourism trends across different months in India.
Perfect for travel planning and cultural research!
""")

# Split layout into columns
col1, col2 = st.columns([1, 2])

with col1:
    # Month selection
    month = st.selectbox("Choose a month", [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ], key='month_select')

    # Festivals display
    st.subheader(f"Festivals in {month}")
    festival_df = get_festivals_by_month(month)
    
    if not festival_df.empty:
        st.dataframe(festival_df, use_container_width=True)
    else:
        st.info("No festival data available for the selected month")

with col2:
    # Tourist Stats
    st.subheader("📊 Tourist Footfall Comparison")
    tourist_df = get_tourist_data()
    
    if not tourist_df.empty:
        monthly_tourist = tourist_df[tourist_df['Month'].str.lower() == month.lower()]
        
        if not monthly_tourist.empty:
            st.metric(label=f"Tourist Growth in {month}", 
                     value=f"{monthly_tourist['Growth'].values[0]}%",
                     delta=f"From {monthly_tourist['Value_2021'].values[0]:,} to {monthly_tourist['Value_2022'].values[0]:,}")
        
        fig = px.bar(tourist_df, 
                    x="Month", 
                    y=["Value_2021", "Value_2022"], 
                    barmode="group",
                    labels={"value": "Tourist Count", "variable": "Year"},
                    color_discrete_sequence=["#FFA07A", "#20B2AA"])
        
        fig.update_layout(showlegend=True, 
                        plot_bgcolor='rgba(0,0,0,0)',
                        yaxis_title="Number of Tourists")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No tourist data available")

# Map visualization
if not festival_df.empty:
    st.subheader("📍 Famous Festivals by State & UT")

    

# Convert to DataFrame



festivals = {
    "Andhra Pradesh": {"festival": "Ugadi", "lat": 15.9129, "lon": 79.7400},
    "Arunachal Pradesh": {"festival": "Losar", "lat": 28.2180, "lon": 94.7278},
    "Assam": {"festival": "Bihu", "lat": 26.2006, "lon": 92.9376},
    "Bihar": {"festival": "Chhath Puja", "lat": 25.0961, "lon": 85.3131},
    "Chhattisgarh": {"festival": "Bastar Dussehra", "lat": 21.2787, "lon": 81.8661},
    "Goa": {"festival": "Carnival", "lat": 15.2993, "lon": 74.1240},
    "Gujarat": {"festival": "Navratri", "lat": 22.2587, "lon": 71.1924},
    "Haryana": {"festival": "Teej", "lat": 29.0588, "lon": 76.0856},
    "Himachal Pradesh": {"festival": "Kullu Dussehra", "lat": 31.1048, "lon": 77.1734},
    "Jharkhand": {"festival": "Sarhul", "lat": 23.6102, "lon": 85.2799},
    "Karnataka": {"festival": "Mysuru Dasara", "lat": 12.2958, "lon": 76.6394},
    "Kerala": {"festival": "Onam", "lat": 10.8505, "lon": 76.2711},
    "Madhya Pradesh": {"festival": "Lokrang", "lat": 22.9734, "lon": 78.6569},
    "Maharashtra": {"festival": "Ganesh Chaturthi", "lat": 19.7515, "lon": 75.7139},
    "Manipur": {"festival": "Yaoshang", "lat": 24.6637, "lon": 93.9063},
    "Meghalaya": {"festival": "Wangala", "lat": 25.4670, "lon": 91.3662},
    "Mizoram": {"festival": "Chapchar Kut", "lat": 23.1645, "lon": 92.9376},
    "Nagaland": {"festival": "Hornbill", "lat": 26.1584, "lon": 94.5624},
    "Odisha": {"festival": "Rath Yatra", "lat": 20.9517, "lon": 85.0985},
    "Punjab": {"festival": "Baisakhi", "lat": 31.1471, "lon": 75.3412},
    "Rajasthan": {"festival": "Gangaur", "lat": 27.0238, "lon": 74.2179},
    "Sikkim": {"festival": "Pang Lhabsol", "lat": 27.5330, "lon": 88.5122},
    "Tamil Nadu": {"festival": "Pongal", "lat": 11.1271, "lon": 78.6569},
    "Telangana": {"festival": "Bathukamma", "lat": 18.1124, "lon": 79.0193},
    "Tripura": {"festival": "Kharchi Puja", "lat": 23.9408, "lon": 91.9882},
    "Uttar Pradesh": {"festival": "Kumbh Mela", "lat": 26.8467, "lon": 80.9462},
    "Uttarakhand": {"festival": "Ganga Dussehra", "lat": 30.0668, "lon": 79.0193},
    "West Bengal": {"festival": "Durga Puja", "lat": 22.9868, "lon": 87.8550},
    "Delhi": {"festival": "Diwali", "lat": 28.7041, "lon": 77.1025},
    "Jammu and Kashmir": {"festival": "Hemis", "lat": 33.7782, "lon": 76.5762},
    "Ladakh": {"festival": "Losar", "lat": 34.1526, "lon": 77.5770},
    "Puducherry": {"festival": "Masi Magam", "lat": 11.9416, "lon": 79.8083},
    "Chandigarh": {"festival": "Baisakhi", "lat": 30.7333, "lon": 76.7794},
    "Dadra and Nagar Haveli and Daman and Diu": {"festival": "Nariyal Poornima", "lat": 20.3974, "lon": 72.8328},
    "Lakshadweep": {"festival": "Eid", "lat": 10.5667, "lon": 72.6417},
    "Andaman and Nicobar Islands": {"festival": "Island Tourism Festival", "lat": 11.7401, "lon": 92.6586}
}

map_df = pd.DataFrame([
    {"State/UT": state, "Festival": data["festival"], "lat": data["lat"], "lon": data["lon"]}
    for state, data in festivals.items()
])

# Display the map
st.map(map_df, zoom=4)

# Display festival details
with st.expander("📜 One Famous mainFestival Details by State/UT"):
    cols = st.columns(3)
    for idx, row in map_df.iterrows():
        with cols[idx % 3]:
            st.metric(label=row["State/UT"], value=row["Festival"])


# About section
with st.expander("About this Project"):
    st.markdown("""
    **Key Features:**
    - Real-time Snowflake data integration
    - Interactive visualizations
    - Mobile-responsive design
    
    **Data Sources:**
    - Festival dates from Government of India
    - Tourism statistics from Ministry of Tourism
    """)

# Download buttons
if not festival_df.empty:
    st.sidebar.download_button(
        label="Download Festival Data",
        data=festival_df.to_csv(index=False).encode('utf-8'),
        file_name=f'festivals_{month}.csv',
        mime='text/csv'
    )
