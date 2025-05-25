import pandas as pd

# Load your raw CSV
df = pd.read_csv("festivals.csv")

# Clean column names
df.columns = [col.strip().replace(" ", "_") for col in df.columns]

# Enclose all string values in double quotes and escape any internal quotes
def escape_quotes(value):
    if pd.isnull(value):
        return ""
    value = str(value)
    value = value.replace('"', '""')  # Escape double quotes
    return f'"{value}"'               # Enclose in double quotes

# Apply to object (string) columns
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].apply(escape_quotes)

# Save cleaned and escaped CSV
df.to_csv("festivals_2022_snowflake_ready.csv", index=False, quoting=3)  # quoting=3 => QUOTE_NONE (quotes handled manually)

print("✅ Data cleaned and ready for Snowflake upload.")
