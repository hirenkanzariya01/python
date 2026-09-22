# #  ? square , cube  , trable  , total sum from 1 to n,
# print(f'Square of the {n} :- ', n*n)
# print(f'cube of the {n} :- ', n*n*n)

# print('=========== CUBE ===========')
# for i in range(1, n + 1):
#     print(i, "x", i, "x", i, "=", i**3)

# print('=========== Square ===========')
# for i in range(1, n + 1):
#     print(i, "x", i, "=", i*i)

# print('=========== Table ===========')
# for i in range(1, 11):
#     print(n, "x", i, "=", n*i)


import streamlit as st

st.header("Math Calculator")
n = st.text_input("Enter Number")
if st.button("Get Caluclation"):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### Square")
        for i in range(1, int(n) + 1):
            st.markdown(int(n) * i)
    with col2:
        st.markdown("### CUBE")
        for i in range(1, int(n) + 1):
            st.markdown(f" {i} x {i} x {i} = {i**3}")
    with col3:
        st.markdown("### Table")
        for i in range(1, 11):
            st.markdown(f"{n} x {i} = {int(n)*i}")
            
