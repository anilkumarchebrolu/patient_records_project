from operator import add
from turtle import onclick
from dashboard_pages.add_new_patient import AddNewPatient

class HomePage:
    def __init__(self, streamlit, authenticator, user_full_name) -> None:
        self.st = streamlit
        self.authenticator = authenticator
        self.user_full_name = user_full_name

    def show_homepage(self):
        
        self.st.markdown(f"<h2 style='text-align: left; background-color: lightblue; font-size: 35px; border: 2px lightblue; border-radius: 9px; text-indent: 10px; vertical-align: text-top;'> Sai's Child Care Medical Records </h2>", unsafe_allow_html=True)
        self.st.markdown(f"<p style='text-align:right; font-size:20px;'> signed in as <strong>{self.user_full_name}</strong></p>", unsafe_allow_html=True)
        with self.st.columns(12)[-1]:
            self.authenticator.logout('Sign out')
        
        self.st.markdown('----------------------------------------------------------------------------')
        self.st.markdown(f"<h3 style='text-align: left;'> ADD OR VIEW PATIENT </h3>", unsafe_allow_html=True)
        self.st.markdown(f"<p style='text-align: center; text-indent: -25px;'> CLICK TO ADD NEW PATIENT </p>", unsafe_allow_html=True)
        with self.st.columns(7)[3]:
            self.st.write()
            add_patient_button = self.st.button("ADD NEW PATIENT")
            # if "add_patient_button_status" in self.st.session_state:
            if add_patient_button:
                self.st.session_state["add_patient_button_status"] = True
                self.st.experimental_rerun()
        
        self.st.markdown(f"<h5 style='text-align: center; text-indent: -35px;'> OR </h5>", unsafe_allow_html=True)

        with self.st.columns(3)[1]:
            self.st.write("FIND EXISTING PATIENT RECORD")
            with self.st.form("search_by_patient_id"):
                patient_id = self.st.number_input("PATIENT ID", step=1)
                submitted = self.st.form_submit_button("Search By Patient ID")
                if submitted:
                    self.st.write(f"patient id is {patient_id}")
        with self.st.columns(3)[1]:
            self.st.markdown('----------------------------------------------------------------------------')
        self.st.markdown(f"<h3 style='text-align: left;'> FIND PATIENT ID </h3>", unsafe_allow_html=True)

        find_by_phone_num, find_by_name = self.st.columns(2)
        
        with find_by_phone_num:
            self.st.write("FIND PATIENT ID BY PHONE NUMBER")
            with self.st.form("search_by_phone_num"):
                phone_num = self.st.number_input("PHONE NUMBER", step=1)
                submitted = self.st.form_submit_button("Search By Phone Number")
                if submitted:
                    self.st.write(f"Phone Number is {phone_num}")

        with find_by_name:
            self.st.write("FIND PATIENT ID BY PATIENT NAME")
            with self.st.form("search_by_patient_name"):
                name = self.st.text_input("PATIENT NAME")
                submitted = self.st.form_submit_button("Search By Patient Name")
                if submitted:
                    self.st.write(f"Patient Name is {name}")
        
        
        