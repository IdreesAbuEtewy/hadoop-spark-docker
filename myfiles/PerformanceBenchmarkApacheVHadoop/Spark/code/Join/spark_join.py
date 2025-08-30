from pyspark.sql import SparkSession
import time

# Create a Spark session
spark = SparkSession.builder.appName("JoinExample").getOrCreate()

# Specify the path to your text file
file_path = 'dataset1.txt'

# Initialize an empty list to store the data
data1 = []

# Read the file and process each line
with open(file_path, 'r') as file:
    for line in file:
        # Split each line by tab to separate columns
        columns = line.strip().split('\t')
        
        # Convert the first column to an integer and leave the second column as a string
        record = (int(columns[0]), columns[1])
        
        # Append the record to the data list
        data1.append(record)

# Read the text file
with open("dataset1.5.txt", "r") as file:
    lines = file.readlines()

# Process each line and create the desired format for data2
data2 = []

for line in lines:
    # Split the line into individual components
    components = line.strip().split("\t")

    # Ensure that the components list has at least 12 elements
    while len(components) < 12:
        components.append(None)

    # Convert appropriate elements to their respective data types
    code2 = int(components[0])
    col2 = int(components[1])
    name = components[2]
    address1 = components[3]
    address2 = components[4]
    city = components[5]
    state = components[6]
    zip_code = components[7]
    phone = components[8]
    first_name = components[9]
    last_name = components[10]
    code1 = int(components[11])

    # Append the tuple to data2
    data2.append((code2, col2, name, address1, address2, city, state, zip_code, phone, first_name, last_name, code1))



columns1 = ['code1', 'col1']
columns2 = ['code2', 'col2', 'name', 'address1', 'address2', 'city', 'state', 'zip', 'phone', 'first_name', 'last_name', 'code1']

df1 = spark.createDataFrame(data1, columns1)
df2 = spark.createDataFrame(data2, columns2)

# Step 3: Perform Inner Join
inner_join_df = df1.join(df2, df1['code1'] == df2['code1'], 'inner')

# Step 4: Show Inner Join Result
print("Inner Join Result:")
inner_join_df.show(truncate=False)

# Step 5: Perform Outer Join
outer_join_df = df1.join(df2, df1['code1'] == df2['code1'], 'outer')

# Step 6: Show Outer Join Result
print("Outer Join Result:")
outer_join_df.show(truncate=False)


# Step 7: Stop SparkSession
time.sleep(30)
spark.stop()