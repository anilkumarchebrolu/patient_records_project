import pandas as pd

class AddNewPatient:
    def __init__(self, streamlit) -> None:
        self.st = streamlit

    def add_new_patient_entry(self):
        go_to_homepage = self.st.button("Go To HomePage")
        if go_to_homepage:
            self.st.session_state["go_to_homepage"] = True
            self.st.experimental_rerun()
        self.st.header("PATIENT ENTRY")
        with self.st.form("patient_entry"):
            patient_name = self.st.text_input("PATIENT NAME")
            dob = self.st.date_input("DATE OF BIRTH")
            sex = self.st.selectbox("SEX", options=['MALE', 'FEMALE', 'NOT WILLING TO SPECIFY'])

            age = self.st.number_input("AGE", step=1)
            weight = self.st.number_input("WEIGHT (kg)")
            height = self.st.number_input("HEIGHT (cm)")
            head_circumference = self.st.number_input("HEAD CIRCUMFERENCE (cm)")
            immunisation_status = self.st.text_input("IMMUNISATION STATUS")
            present_diagnosis = self.st.text_area("PRESENT DIAGNOSIS")
            treatment_given = self.st.text_area("TREATMENT GIVEN")
            review = self.st.text_area("REVIEW")
            vaccination_due = self.st.date_input("VACCINATION DUE")
            uploaded_files = self.st.file_uploader("UPLOAD PATIENT RECORDS", accept_multiple_files=True)

            submitted = self.st.form_submit_button("Submit")
            if submitted:
                record = {
                    'patient_name' : patient_name,
                    'dob' : dob,
                    'sex' : sex,
                    'age' : age,
                    'weight' : weight,
                    'height' : height,
                    'head_circumference' : head_circumference,
                    'immunisation_status' : immunisation_status,
                    'present_diagnosis' : present_diagnosis,
                    'treatment_given' : treatment_given,
                    'review' : review,
                    'vaccination_due' : vaccination_due,
                    'uploaded_files' : ",".join([uploaded_file.name for uploaded_file in uploaded_files])
                }
                df = pd.DataFrame(record.items())
                self.st.table(df)

                for uploaded_file in uploaded_files:
                    bytes_data = uploaded_file.read()
                    self.st.image(bytes_data)

            



            # bill_number = self.st.number_input("BILL NUMBER", step=1)
            # bill_date = self.st.date_input("BILL DATE")
            # bill_amount = self.st.number_input("BILL AMOUNT")
            # quantity = self.st.text_input("QUANTITY")
            # name_of_the_party = self.st.text_input("NAME OF THE PARTY")
            # place = self.st.text_input("PLACE")
            # submitted = self.st.form_submit_button("Submit")
            # if submitted:
            #     new_row = {'bill_number': bill_number,
            #                 'bill_date': bill_date,
            #                 'bill_amount': bill_amount,
            #                 'quantity': quantity,
            #                 'name_of_the_party': name_of_the_party,
            #                 'place': place,
            #                 'bank_name': '',
            #                 'cheque_or_dd_number': '',
            #                 'cheque_date': '',
            #                 'cheque_amount': '',
            #                 'less': '',
            #                 'interest': ''}
            #     index_list = df[df['bill_number'] == bill_number].index.to_list()
            #     if len(index_list) == 0:
            #         internal_df = pd.DataFrame([new_row],columns=df.columns)
            #         df2 = pd.concat([internal_df, df.loc[:]]).reset_index(drop=True)
            #         df2.drop(df2.columns[df2.columns.str.contains('unnamed', case = False)], axis = 1, inplace = True)
            #         df2.to_csv(csv_path)
                    
            #         self.st.info(f"Bill Number -> {bill_number} added")
            #         self.st.dataframe(pd.DataFrame([new_row]))
            #     else:
            #         self.st.error(""" Bill Number already exists. Please use different bill number.
            #                     ex:if billnumber is '2304' use it as '2304_1' """)