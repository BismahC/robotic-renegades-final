#importing general objects
import pandas as pd
import plotly.express as px
import numpy as np
import streamlit as st

country_cont = pd.read_csv('clean_data.csv')
better_data = pd.read_csv('clean_data.csv')
location = pd.read_csv('location.csv')
pie_data = pd.read_csv('pie_data.csv')

#Meet the team
#short bio on each person
st.header("This is our :violet[_wonderful_] team!")
st.markdown("Hellooo, i'm :blue[Advik]! I'm from the city of Mumbai, India and am studying in grade 11. I also a huge tech fan!! Apart from the little programming I've done in HTML/CSS, JavaScript / React.js, and Java, I was yet to explore python (specifically in relation to data science) and what better way to learn it than at AI camp! (even if that means I've to stay up till 1:30am!!)")
st.markdown("Hey i'm :green[Devesh] and i'm from New York(the city of :orange[_dreams_]) and currently in grade 10. I have always loved computer science and developing things with code cause it's so cool!")
st.markdown("Hello i'm :violet[Bismah] and I have always been interested in data science. I am a grade 11 student from Ontario, Canada. I enjoy coding and have coded with HTML, CSS, Java, C#, and C++ but I never tried Python which made this project a great learning experience!")
st.markdown("We all :red[love] data science because who doesn't!")
st.header(":orange[What Factors Affect the Social Progress Index?]")
st.subheader("Well what is the :blue[_Social Progress Index_]?")
st.markdown("The :red[_Social Progress Index_](SPI) measures how countries are progressing and working to accommodate the social and environmental needs of their people. The SPI measures the wellbeing of societies by observing and recording social and environmental factors instead of the common approach of viewing societies from an economic perspective. These factors range from the accommodations toward physical wellness such as healthcare, shelter, and sanitation to the accommodations toward social wellness such as equality, inclusion, and personal safety.  One part of social progress is a society’s ability to establish building blocks that allow individuals and communities to enhance the quality of their lives as well as reach their full potential. Understanding social progress in different parts of the world allows us to visualize the importance of social and physical maintenance and how components of society are interdependent. It essentially brings insight to what is working and what is not in different nations which we can use as a means of feedback to society to further social improvement. Healthy and well educated individuals are far more able to contribute to the wellbeing and advancements of society so it’s important to use this data to understand how we can further this outcome.")

#show off clean_data here
st.header('The Data')
st.dataframe(country_cont.head())


st.markdown("""---""")

st.header("Social Progress Around the World") 
st.plotly_chart(px.scatter_geo(location, locations="code_3", color="spi_score", hover_name="country", size="spi_score", size_max=10, projection="natural earth"))


#Advik
st.header(":violet[_Which continents do the Top 30 countries in the Social Progress Index belong to?_]")
st.plotly_chart(px.pie(pie_data, names='continent', title='Representation of Continents in the TOP 30 of the SPI Rankings'))
st.markdown("The main goal behind using a pie chart is to see what percentage of the top 30 countries in the Social Progress Index belong to which continents. So as the results show, Europe has the highest number of countries representing it in the Top 30, comprising of 71% of the whole, which is significantly greater than any of the others! The next most represented continent is Asia, contributing 12.9% to the whole. The Americas and Oceania are the next best continents tied at 6.45% each, and last but not the least, Africa, which has a 3.23% representation in the top 30.")

st.markdown("""---""")

#Bismah
st.header("To what extent does :red[_inclusiveness_] contribute to the overall :blue[_wellbeing_] of society and the _individuals in it_?")
st.subheader("What is inclusivity?")
st.markdown("Inclusion is when a country does not have barriers, social or physical, that excludes members of society such as prejudice or discrimination. It’s when societies empower and promote the different groups of their diverse community instead of trying to separate them. Social and physical inclusion is valuing people’s needs and allowing them to live with dignity, engage within the community, and contribute to their society. It plays an important role in social progress overall and is interdependent with other factors of society to contribute to its overall well being.")
st.plotly_chart(px.scatter(country_cont, 'inclusiveness', 'opportunity', color = 'continent', size = 'access_adv_edu', hover_name = "country", title = "Inclusiveness & Opportunities"))
st.markdown("This scatter plot displays how the rate of inclusiveness is related with both the rate of opportunity and access to advanced education throughout the continents. Overall, it was found that higher levels of inclusivity related to higher levels of opportunity. This could be because higher inclusivity means lower levels of discrimination in the processes revolving around opportunities. While more access to advanced education correlates with higher levels of opportunity since there are more qualified individuals, a fair portion of countries have higher levels of access to advanced education but lower levels of inclusivity. This could be due to the fact that even though higher levels of education can be financially or physically accessible, that does not mean they are necessarily inclusive in their acceptance process. This in turn gives that country lower rates of opportunity. The scatter plot overall shows how inclusiveness is an important factor to the wellbeing of society in terms of education and the driving factors of our economy which is why it should be deemed as a priority in the progression of nations.")
st.plotly_chart(px.histogram(country_cont, x="inclusiveness", y="personal_safety", histfunc="avg", title = "Inclusiveness & Safety"))
st.markdown("This histogram displays how the rate of inclusiveness is more related to personal safety than the average person would think. The graph displays how nations with generally higher levels of inclusiveness also fall under high levels of personal safety while those with less inclusiveness generally have less rates of personal safety. This is because personal safety does not only involve physical safety but also psychological safety.  Inclusion is necessary to establish mutual learning which in turn allows individuals to socially progress themselves and further the progression of their community. It also relates to the previous graph regarding discriminatory factors blocking opportunities because the environment which a person is in needs to make them feel as though they are accepted and that they belong. The chart essentially determines how inclusiveness also contributes to the wellbeing of individuals.")

st.markdown("""---""")

#Devesh
st.header("How does :green[freedom] and the :blue[wellbeing] of the people contribute to the SPI score of a nation?")
st.plotly_chart(px.scatter(better_data, x = "personal_freedom_choice", y = "wellbeing", color= "continent", size = 'spi_score', hover_name = 'spi_rank', title="Freedom of Choise & Wellbeing"))
st.markdown("The relationship between freedom of choice and wellbeing illustrates how individuals are happier when they have greater freedom. Factors that affect people's welfare include freedom, more rights, access to knowledge, safety, and many more factors. ")
st.plotly_chart(px.scatter(better_data, x = "personal_freedom_choice", y = "spi_score", color= "continent", size = 'spi_score', hover_name = 'spi_rank', title="Freedom of Choice & Overall SPI Score"))
st.markdown("Personal safety and well-being in general are crucial for society's growth and advancement in the SPI rankings, as well as for the welfare of the nation's citizens. All of this data is summed up by wellbeing, which is related to freedom, rights, safety, and SPI score. Both graphs exhibit a very similar linear, upward trend, which may indicate that a nation is doing better when its citizens are happier, safer, and more secure. People would be more supportive of their government or nation because they feel safer and have greater freedom, which would boost the SPI rating. However, nations begin to fall in the SPI rankings when their citizens have lower wellbeing scores.")

st.markdown("""---""")


#Always good to section out your code for readability.
st.header('Conclusions')
st.markdown("The End!")
st.markdown('- **Data Science is Fun!**')
st.markdown('- **Inclusiveness not only furthers the social progression of individuals and their societies, but it also sustains the wellbeing of people.**')
st.markdown('- **The SPI rank for a nation rises as a result of the increase in well-being brought on by greater freedom, safety, education, and opportunity for all.**')
