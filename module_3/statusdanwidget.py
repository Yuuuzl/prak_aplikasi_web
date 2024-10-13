import streamlit as st
import time

# #PROGRESS BAR
# # Menyiapkan tempat untuk teks dan progress bar
# latest_iteration1 = st.empty()
# bar1 = st.progress(0)

# latest_iteration2 = st.empty()
# bar2 = st.progress(0)

# latest_iteration3 = st.empty()
# bar3 = st.progress(0)

# # Loop untuk tiga progress bar dengan kecepatan berbeda
# for i in range(100):
#     # Progress bar pertama (paling cepat)
#     latest_iteration1.text(f"Iteration {i+1}")
#     bar1.progress(i + 1)

#     # Progress bar kedua (sedang)
#     if i % 2 == 0:  # hanya update setiap 2 iterasi
#         latest_iteration2.text(f"Iteration {i//2+1}")
#         bar2.progress((i//2) + 1)

#     # Progress bar ketiga (paling lambat)
#     if i % 4 == 0:  # hanya update setiap 4 iterasi
#         latest_iteration3.text(f"Iteration {i//4+1}")
#         bar3.progress((i//4) + 1)

#     time.sleep(0.1)
    

    
# "...and now we're done!"


# #SPINNER

# with st.spinner("Waiting..."):
#     time.sleep(5)
#     st.success("Finished!")
    
# #BALLOONS

# with st.spinner("Waiting..."):
#     time.sleep(5)
#     st.balloons()
    
# # SNOWFLAKES

# with st.spinner("Waiting..."):
#     time.sleep(5)
#     st.snow()
    
#ERROR BOX
st.error("This is an error")

#WARNING BOX
st.warning("This is a warning")
    
    