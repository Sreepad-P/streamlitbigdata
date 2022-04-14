import streamlit as st

st.title("Business Metadata")

st.header("What is business metadata?")

st.markdown("Business metadata provides the meaning of data, by defining terms in everyday language without regard to technical implementation. It is concerned with the organizational aspect of the available data sources, helping to structure and classify the information. Business metadata defines everyday business terms, such as table and column definitions, business rules, data sharing rules and data quality rules.")

st.header("Check the box below to view the business terms")

bus = st.checkbox('View Business terms')

if bus:
     st.write('Business terms:')