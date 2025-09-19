import streamlit as st
import numpy as np
import pandas as pd
import altair as alt


st.header('st.write')

# Example 1
st.write('# Example 1：Text with Markdown')

st.write('Hello, *World!* :sunglasses:')

# Example 2
st.write('## Example 2：Numbers')

st.write(1234)

# Example 3
st.write('### Example 3：DataFrame')

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

st.write(df)

# Example 4
st.write('#### Example 4：DataFrame with text')

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5
st.subheader('Example 5：Chart')

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

chart = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(chart)
