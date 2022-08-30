import streamlit as st
import streamlit_authenticator as stauth

from database_controllers.user_db_controller import UserDBController
from dashboard_pages.homepage import HomePage
from dashboard_pages.add_new_patient import AddNewPatient

if __name__ == '__main__':
    # Set Page title and layout
    st.set_page_config(page_title="Sai's Child Care Medical Records", layout="wide")

    # To remove empty space on top
    st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True
    )

    user_db_controller = UserDBController()
    credentials = user_db_controller.fetch_users()
    authenticator = stauth.Authenticate(credentials,
                                        cookie_name='sai_clinic_records', 
                                        key="magic",
                                        cookie_expiry_days=7)
    with st.columns(3)[1]:
        user_full_name, authentication_status, user_name = authenticator.login("Signin", "main")

    
    if authentication_status == False:
        with st.columns(3)[1]:
            st.error("username or password is incorrect. Kindly recheck.")
    elif authentication_status == None:
        with st.columns(3)[1]:
            st.warning("Please enter your username and password")
    elif authentication_status == True:
        if 'go_to_homepage' in st.session_state:
            if st.session_state['go_to_homepage'] is True:
                st.session_state['add_patient_button_status'] = False
                st.session_state['go_to_homepage'] = False
        if 'add_patient_button_status' in st.session_state:
            if st.session_state['add_patient_button_status'] is True:
                AddNewPatient(st).add_new_patient_entry()
            else:
                homepage = HomePage(st, authenticator, user_full_name)
                homepage.show_homepage()
        else:     
            homepage = HomePage(st, authenticator, user_full_name)
            homepage.show_homepage()

