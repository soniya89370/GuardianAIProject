import streamlit as st
import pandas as pd
import os
from datetime import datetime


# -------------------------
# Safe Imports
# -------------------------

from database import add_user


try:
    from voice_listener import listen_secret_code
except Exception as e:
    print("Voice module unavailable:", e)

    def listen_secret_code():
        return False



try:
    from camera_live import start_camera
except Exception as e:
    print("Camera module unavailable:", e)

    def start_camera():
        st.warning("Camera feature unavailable on server")



try:
    from sms_sender import send_sms
except Exception as e:
    print("SMS module unavailable:", e)

    def send_sms():
        st.warning("SMS service unavailable")



# -------------------------
# Page Config
# -------------------------

st.set_page_config(
    page_title="GuardianAI",
    page_icon="🛡️",
    layout="wide"
)



# -------------------------
# CSS
# -------------------------

st.markdown(
"""
<style>

.main-title {
font-size:50px;
font-weight:800;
color:#0b3d91;
}

.sub-title {
font-size:22px;
color:#555;
}

.card {
background:white;
padding:25px;
border-radius:20px;
text-align:center;
box-shadow:0px 8px 25px rgba(0,0,0,0.08);
height:170px;
}

.card h2 {
font-size:45px;
}

.card h3 {
color:#0b3d91;
}

.status {
background:#d4edda;
color:#155724;
padding:15px;
border-radius:15px;
font-size:20px;
text-align:center;
}

.emergency {
background:#ffe5e5;
color:#b30000;
padding:15px;
border-radius:15px;
}

</style>
""",
unsafe_allow_html=True
)



# -------------------------
# Data Folder
# -------------------------

if not os.path.exists("data"):
    os.makedirs("data")



# -------------------------
# Header
# -------------------------

st.markdown(
"""
<div class="main-title">
🛡️ GuardianAI
</div>

<div class="sub-title">
Smart Women Safety System
</div>

<br>

<div class="status">
🟢 SYSTEM ONLINE | AI Protection Active
</div>

<br>
""",
unsafe_allow_html=True
)


st.write(
"""
### 🤖 AI Powered Safety Platform

Real-time threat detection, emergency response and intelligent protection system.
"""
)



# -------------------------
# Sidebar
# -------------------------

st.sidebar.markdown(
"""
# 🛡️ GuardianAI

### AI Safety System
"""
)


menu = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "👤 Register",
        "🚨 Emergency SOS",
        "📷 AI Surveillance",
        "🎤 Voice Protection",
        "📜 Security Reports",
        "ℹ️ About"
    ]
)



# -------------------------
# Dashboard
# -------------------------

if menu == "🏠 Dashboard":

    st.header("🤖 GuardianAI Command Center")

    c1,c2,c3,c4 = st.columns(4)

    cards = [
        ("📷","AI Camera","Live Threat Detection"),
        ("🚨","SOS","Emergency Response"),
        ("🎤","Voice AI","Secret Code Detection"),
        ("📜","Reports","Incident History")
    ]


    for col,card in zip(
        [c1,c2,c3,c4],
        cards
    ):
        with col:
            st.markdown(
            f"""
            <div class="card">

            <h2>{card[0]}</h2>

            <h3>{card[1]}</h3>

            <p>{card[2]}</p>

            </div>
            """,
            unsafe_allow_html=True
            )


    st.info(
    """
    🧠 AI Engine:
    YOLO Object Detection + Voice Security + Emergency Monitoring
    """
    )



# -------------------------
# Register
# -------------------------

elif menu == "👤 Register":

    st.header("👤 User Profile Registration")


    name = st.text_input("Full Name")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email")
    address = st.text_area("Address")

    guardian_name = st.text_input(
        "Emergency Contact Name"
    )

    guardian_phone = st.text_input(
        "Emergency Contact Number"
    )


    if st.button("✅ Save Profile"):

        add_user(
            name,
            phone,
            email,
            address,
            guardian_name,
            guardian_phone
        )

        st.success(
            "Profile Saved Successfully"
        )



# -------------------------
# SOS
# -------------------------

elif menu == "🚨 Emergency SOS":

    st.header("🚨 Emergency Control Center")


    st.markdown(
    """
    <div class="emergency">
    ⚠️ Use this button only during emergency.
    </div>
    """,
    unsafe_allow_html=True
    )


    if st.button("🚨 ACTIVATE SOS"):


        now=datetime.now()


        new_data=pd.DataFrame({

            "Date":[
                now.strftime("%d-%m-%Y")
            ],

            "Time":[
                now.strftime("%H:%M:%S")
            ],

            "Status":[
                "SOS Activated"
            ]

        })


        file="data/history.csv"


        if os.path.exists(file):

            old=pd.read_csv(file)

            new_data=pd.concat(
                [old,new_data],
                ignore_index=True
            )


        new_data.to_csv(
            file,
            index=False
        )


        send_sms()

        st.success(
            "Emergency Alert Recorded"
        )



# -------------------------
# Camera
# -------------------------

elif menu=="📷 AI Surveillance":

    st.header(
        "📷 AI Surveillance System"
    )


    if st.button(
        "▶ Start AI Monitoring"
    ):

        start_camera()



# -------------------------
# Voice
# -------------------------

elif menu=="🎤 Voice Protection":

    st.header(
        "🎤 Secret Voice Security"
    )


    if st.button(
        "🎙 Start Listening"
    ):


        with st.spinner(
            "AI Listening..."
        ):

            result=listen_secret_code()


        if result:

            send_sms()

            st.success(
                "🚨 Secret Code Detected"
            )

        else:

            st.error(
                "No Secret Code Found"
            )



# -------------------------
# Reports
# -------------------------

elif menu=="📜 Security Reports":

    st.header(
        "📜 AI Security Reports"
    )


    file="data/history.csv"


    if os.path.exists(file):

        df=pd.read_csv(file)

        st.metric(
            "Total Incidents",
            len(df)
        )


        st.dataframe(
            df,
            use_container_width=True
        )


    else:

        st.info(
            "No incidents available"
        )



# -------------------------
# About
# -------------------------

elif menu=="ℹ️ About":

    st.header(
        "ℹ️ About GuardianAI"
    )


    st.write(
    """
## 🛡️ GuardianAI

AI based Smart Women Safety System.

Technologies:

🤖 YOLO AI  
📷 OpenCV  
🐍 Python  
🎤 Voice Recognition  
🗄️ Database System  

Mission:

Provide intelligent safety assistance using Artificial Intelligence.
"""
    )




# import streamlit as st
# import pandas as pd
# import os
# from datetime import datetime

# from database import add_user
# from voice_listener import listen_secret_code
# from camera_live import start_camera
# from sms_sender import send_sms


# # -------------------------
# # Page Config
# # -------------------------

# st.set_page_config(
#     page_title="GuardianAI",
#     page_icon="🛡️",
#     layout="wide"
# )


# # -------------------------
# # Premium UI CSS
# # -------------------------

# st.markdown("""
# <style>

# body {
#     background-color:#f4f7fb;
# }


# .main-title {
#     font-size:50px;
#     font-weight:800;
#     color:#0b3d91;
# }


# .sub-title {
#     font-size:22px;
#     color:#555;
# }


# .card {

#     background: rgba(255,255,255,0.9);
#     padding:25px;
#     border-radius:20px;
#     text-align:center;
#     box-shadow:0px 8px 25px rgba(0,0,0,0.08);
#     height:170px;

# }


# .card:hover {

#     transform:scale(1.03);

# }


# .card h2 {

#     font-size:45px;

# }


# .card h3 {

#     color:#0b3d91;

# }


# .status {

#     background:#d4edda;
#     color:#155724;
#     padding:15px;
#     border-radius:15px;
#     font-size:20px;
#     text-align:center;

# }


# .emergency {

#     background:#ffe5e5;
#     color:#b30000;
#     padding:15px;
#     border-radius:15px;

# }


# </style>

# """, unsafe_allow_html=True)



# # -------------------------
# # Data Folder
# # -------------------------

# if not os.path.exists("data"):
#     os.makedirs("data")



# # -------------------------
# # Header
# # -------------------------


# st.markdown(
# """
# <div class="main-title">
# 🛡️ GuardianAI
# </div>

# <div class="sub-title">
# Smart Women Safety System
# </div>

# <br>

# <div class="status">
# 🟢 SYSTEM ONLINE | AI Protection Active
# </div>

# <br>

# """,
# unsafe_allow_html=True
# )



# st.write(
# """
# ### 🤖 AI Powered Safety Platform

# Real-time threat detection, emergency response and intelligent protection system.
# """
# )# -------------------------
# # Sidebar
# # -------------------------

# st.sidebar.markdown(
# """
# # 🛡️ GuardianAI

# ### AI Safety System

# """
# )

# menu = st.sidebar.radio(
#     "Navigation",
#     [
#         "🏠 Dashboard",
#         "👤 Register",
#         "🚨 Emergency SOS",
#         "📷 AI Surveillance",
#         "🎤 Voice Protection",
#         "📜 Security Reports",
#         "ℹ️ About"
#     ]
# )


# # -------------------------
# # Dashboard
# # -------------------------

# if menu == "🏠 Dashboard":

#     st.header("🤖 GuardianAI Command Center")


#     col1,col2,col3,col4 = st.columns(4)


#     with col1:
#         st.markdown(
#         """
#         <div class="card">
#         <h2>📷</h2>
#         <h3>AI Camera</h3>
#         <p>Live Threat Detection</p>
#         </div>
#         """,
#         unsafe_allow_html=True
#         )


#     with col2:
#         st.markdown(
#         """
#         <div class="card">
#         <h2>🚨</h2>
#         <h3>SOS</h3>
#         <p>Emergency Response</p>
#         </div>
#         """,
#         unsafe_allow_html=True
#         )


#     with col3:
#         st.markdown(
#         """
#         <div class="card">
#         <h2>🎤</h2>
#         <h3>Voice AI</h3>
#         <p>Secret Code Detection</p>
#         </div>
#         """,
#         unsafe_allow_html=True
#         )


#     with col4:
#         st.markdown(
#         """
#         <div class="card">
#         <h2>📜</h2>
#         <h3>Reports</h3>
#         <p>Incident History</p>
#         </div>
#         """,
#         unsafe_allow_html=True
#         )


#     st.markdown("---")


#     st.info(
#         """
#         🧠 AI Engine:
#         YOLO Object Detection + Voice Security + Emergency Monitoring
#         """
#     )



# # -------------------------
# # Register
# # -------------------------

# elif menu == "👤 Register":

#     st.header("👤 User Profile Registration")


#     name = st.text_input("Full Name")
#     phone = st.text_input("Phone Number")
#     email = st.text_input("Email")
#     address = st.text_area("Address")

#     guardian_name = st.text_input(
#         "Emergency Contact Name"
#     )

#     guardian_phone = st.text_input(
#         "Emergency Contact Number"
#     )


#     if st.button("✅ Save Profile"):

#         add_user(
#             name,
#             phone,
#             email,
#             address,
#             guardian_name,
#             guardian_phone
#         )

#         st.success(
#             "Profile Saved Successfully"
#         )



# # -------------------------
# # SOS
# # -------------------------

# elif menu == "🚨 Emergency SOS":

#     st.header("🚨 Emergency Control Center")

#     st.markdown(
#     """
#     <div class="emergency">
#     ⚠️ Use this button only during emergency.
#     </div>
#     """,
#     unsafe_allow_html=True
#     )

#     if st.button("🚨 ACTIVATE SOS"):

#         now = datetime.now()

#         data = pd.DataFrame({
#             "Date": [now.strftime("%d-%m-%Y")],
#             "Time": [now.strftime("%H:%M:%S")],
#             "Status": ["SOS Activated"]
#         })

#         file = "data/history.csv"

#         if os.path.exists(file):
#             old = pd.read_csv(file)
#             data = pd.concat([old, data], ignore_index=True)

#         data.to_csv(file, index=False)

#         send_sms()

#         st.success("Emergency Alert Recorded")



# # -------------------------
# # Camera
# # -------------------------

# elif menu == "📷 AI Surveillance":

#     st.header("📷 AI Surveillance System")


#     st.info(
#     """
#     YOLO AI is ready for real-time threat detection.
#     """
#     )


#     if st.button(
#         "▶ Start AI Monitoring"
#     ):

#         start_camera()



# ## -------------------------
# # Voice
# # -------------------------

# elif menu == "🎤 Voice Protection":

#     st.header("🎤 Secret Voice Security")

#     if st.button("🎙 Start Listening"):

#         with st.spinner("AI Listening..."):
#             result = listen_secret_code()

#         if result:
#             send_sms()
#             st.success("🚨 Secret Code Detected")

#         else:
#             st.error("No Secret Code Found")



# # -------------------------
# # History
# # -------------------------

# elif menu == "📜 Security Reports":

#     st.header("📜 AI Security Reports")


#     file="data/history.csv"


#     if os.path.exists(file):

#         df=pd.read_csv(file)

#         st.metric(
#             "Total Incidents",
#             len(df)
#         )


#         st.dataframe(
#             df,
#             use_container_width=True
#         )

#     else:

#         st.info(
#             "No incidents available"
#         )



# # -------------------------
# # About
# # -------------------------

# elif menu == "ℹ️ About":

#     st.header("ℹ️ About GuardianAI")


#     st.write(
#     """
#     ## 🛡️ GuardianAI

#     AI based Smart Women Safety System.

#     Technologies:

#     🤖 YOLO AI  
#     📷 OpenCV  
#     🐍 Python  
#     🎤 Voice Recognition  
#     🗄️ Database System  


#     Mission:

#     Provide intelligent safety assistance using Artificial Intelligence.
#     """
#     )
    