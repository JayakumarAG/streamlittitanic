import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
st.header("Titanic")
st.subheader("Passenger Details")
titanic =pd.read_csv('/Users/Jayakumar/Downloads/titanicship.csv')
st.text("Total Passengers")
titanic.size
titanic.head()
titanic.columns
Survived = titanic.groupby('Survived')
Survived.size()

Survived_alive=Survived.get_group(1)
Survived_alive
import pandas as pd
import numpy as np
import seaborn as sns
sns.displot(titanic['Survived'])
sns.jointplot(x='Survived',y='Age',data=titanic,kind='scatter')