import streamlit as st
import json
from api_wrapper import api_client
import pandas as pd
import numpy as np 
import altair as alt
import matplotlib.pyplot as plt
import plotly.express as px



st.title("Education Loan Dashboard")

st.subheader("Institution wise number of students availing education loan - 2012-2013")

# https://data.telangana.gov.in/api/1/datastore/query/ae305fca-068b-4e61-b7f8-d9bf651e1b69/8
# api_c = api_client.ApiClient()
# data = api_c.get_data("ae305fca-068b-4e61-b7f8-d9bf651e1b69/52");

# print(data)
#data framing and clean up.
# res = pd.DataFrame(data['results'])
# res['load'] = res['load'].astype(float)
# res.rename(columns = {'circle':'District','subdivision':'Mandal'}, inplace = True)


data = pd.read_csv("https://data.gov.in/files/ogdpv2dms/s3fs-public/Report-118-20042015014232457PM-2012-2013.csv",encoding= 'unicode_escape')
total = data[-1:]
data = data[:-1]

# st.area_chart(res)
# res.to_csv("test.csv")

column_names = ['Caste-Category - Total - Male', 'Caste-Category - Total - Female',
       'Caste-Category - SC - Male', 'Caste-Category - SC - Female',
       'Caste-Category - ST - Male', 'Caste-Category - ST - Female',
       'Caste-Category - OBC - Male', 'Caste-Category - OBC - Female',
       'Out Of Total - PWD - Male', 'Out Of Total - PWD - Female',
       'Out Of Total - Muslim - Male', 'Out Of Total - Muslim - Female',
       'Out Of Total - Other Minority Communities - Male',
       'Out Of Total - Other Minority Communities - Female']


# selected_column = st.selectbox("Select a column", column_names)	
selected_column = st.multiselect("Select columns", column_names)

chart_type = st.selectbox("Select Chart Type", ["bar", "pie"])


# st.write(selected_column)
def get_total_based_on_column(column_name, total = total):
    return {col: total[col].values[0] for col in column_name}

output = get_total_based_on_column(selected_column,total)


# st.write(output)



# df = pd.DataFrame.from_dict(output, orient='index', columns=['Value'])
# df['Value'] = df['Value'].astype(int)  # Convert value to integer


# fig, ax = plt.subplots()
# ax.pie(output.values(), labels=output.keys(), autopct='%1.1f%%', startangle=90)
# ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# # Display the pie chart using Streamlit
# st.pyplot(fig)

df = pd.DataFrame.from_dict(output, orient='index', columns=['Value'])
df.reset_index(inplace=True)
df.columns = ['Category', 'Value']


if chart_type == "pie":


	# Create an interactive pie chart using Plotly Express
	fig = px.pie(df, values='Value', names='Category', title='Pie Chart Example')

	# Display the pie chart using Streamlit
	st.plotly_chart(fig, use_container_width=True)
else:


	# _________________________________________
	fig = px.bar(df, x='Category', y='Value', title='Bar Plot Example')

	# Display the bar plot using Streamlit
	st.plotly_chart(fig, use_container_width=True)






insights = [
    "Gender Distribution",
    "Caste Category Distribution",
    "Minority Community Representation",
    "Disability Representation"
]

selected_insight = st.selectbox("Select an Insight", insights)	




# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])

# st.area_chart(chart_data)