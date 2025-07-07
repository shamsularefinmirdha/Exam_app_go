import streamlit as st

# ------------- Set page config -------------
st.set_page_config(
    page_title="Exam Operations Entry",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ------------- Custom CSS -------------
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        height: 3em;
        width: 100%;
        font-size: 16px;
    }
    .stTextInput input, .stDateInput input, .stTextArea textarea {
        border-radius: 6px;
    }
    .st-bj {
        font-size: 18px;
    }
    .st-dp {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# ------------- Sidebar Navigation -------------
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Microsoft_logo.svg/2560px-Microsoft_logo.svg.png", width=150)
    st.title("📋 Exam Operations")
    st.info("Please login and submit daily exam operations schedule. Only authorized staff may access this app.")

# ------------- Login Page -------------
def login():
    st.title("🔒 Staff Login")
    st.write("Enter your credentials to access the system.")
    username = st.text_input("Username", placeholder="Enter username")
    password = st.text_input("Password", type="password", placeholder="Enter password")
    if st.button("Login"):
        if username == "admin" and password == "password123":
            st.session_state["logged_in"] = True
            st.session_state["page"] = "form"
            st.experimental_rerun()
        else:
            st.error("❌ Invalid username or password.")

# ------------- Form Page -------------
def form_page():
    st.title("📝 Daily Exam Operations Entry Form")
    st.write("Please fill out all fields below carefully:")

    # Group inputs inside a container for better visuals
    with st.container():
        date = st.date_input("📅 Date")
        day = st.text_input("📆 Day", placeholder="e.g., Monday")
        weekend = st.radio("🌤️ Weekend", ["No", "Yes"])

        st.markdown("---")
        st.subheader("🗂️ Operational Tasks")
        cmr_am_release = st.text_input("CMR team AM CM release reporting at 6.30 am")
        ielts_team_member = st.text_input("IELTS/School/EP CM collection & transfer at Transit Room")
        td_am_release = st.text_input("TD team AM CM release reporting at 6.30 am")
        td_pm_receive = st.text_input("TD team AM CM Receive reporting at 2.00 pm")
        td_bag_staff = st.text_input("TD Staff for bag receive & next day pack")
        ielts_osm_scanning = st.text_input("IELTS OSM scanning/Shredding/ATRF/TRF Print")
        ielts_cm_sorting = st.text_input("IELTS CM sorting for next day")
        school_ep_cm_sorting = st.text_input("School/EP CM sorting for next day")
        back_office_staff = st.text_input("Back office support staff for venue sorting")
        school_ep_script_group1 = st.text_input("School/EP script despatch (Group 1)")
        school_ep_script_group2 = st.text_input("School/EP script despatch (Group 2)")
        ielts_qp_sorting = st.text_input("IELTS QP sorting & seals check A/Initial sorting")
        ielts_score_1st_entry = st.text_input("IELTS score 1st entry + amendments + Recording/Pic upload")
        ielts_score_2nd_entry = st.text_input("IELTS score 2nd entry + jagged run/upload/IOC Power BI check")
        ielts_result_status = st.text_input("IELTS result status check & publish")
        remark = st.text_area("Additional Remarks", placeholder="Optional notes")

    if st.button("✅ Submit Entry"):
        st.session_state["submitted_data"] = {
            "Date": str(date),
            "Day": day,
            "Weekend": weekend,
            "CMR AM Release": cmr_am_release,
            "IELTS Team Member": ielts_team_member,
            "TD AM Release": td_am_release,
            "TD PM Receive": td_pm_receive,
            "TD Bag Staff": td_bag_staff,
            "IELTS OSM Scanning": ielts_osm_scanning,
            "IELTS CM Sorting": ielts_cm_sorting,
            "School/EP CM Sorting": school_ep_cm_sorting,
            "Back Office Staff": back_office_staff,
            "School/EP Script Group 1": school_ep_script_group1,
            "School/EP Script Group 2": school_ep_script_group2,
            "IELTS QP Sorting": ielts_qp_sorting,
            "IELTS Score 1st Entry": ielts_score_1st_entry,
            "IELTS Score 2nd Entry": ielts_score_2nd_entry,
            "IELTS Result Status": ielts_result_status,
            "Remark": remark
        }
        st.session_state["page"] = "summary"
        st.experimental_rerun()

# ------------- Summary Page -------------
def summary_page():
    st.title("✅ Submission Summary")
    st.success("Your data has been recorded successfully! 🎉")
    submitted_data = st.session_state.get("submitted_data", {})
    st.write("### 📊 Here is your submitted information:")
    st.json(submitted_data)
    if st.button("🔄 Submit Another Entry"):
        st.session_state["page"] = "form"
        st.experimental_rerun()

# ------------- Navigation Controller -------------
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "page" not in st.session_state:
    st.session_state["page"] = "login"

if st.session_state["logged_in"]:
    if st.session_state["page"] == "form":
        form_page()
    elif st.session_state["page"] == "summary":
        summary_page()
else:
    login()
