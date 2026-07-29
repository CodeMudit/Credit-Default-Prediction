import streamlit as st
import requests


# Page Configuration

st.set_page_config(
    page_title="Credit Default Prediction",
    page_icon="💰",
    layout="centered"
)

# title

st.title("💰 Credit Default Prediction")
st.write("Enter the Customer's Financial Details to predict "
         "whether the customer is likely to default.")

st.divider()

# User Inputs 


with st.form("credit_form"):

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input(
            "Age of the Customer: ",
            min_value = 18,
            max_value = 100,
            value = 35
            )

        revolving = st.number_input(
            "Revolving Utilization of Unsecured Lines",
            min_value = 0.0,
            value = 0.25
            )

        late30 = st.number_input(
            "Number of Times 30-59 Days Past Due",
            min_value=0,
            value=0
            )

        debt = st.number_input(
            "Debt Ratio",
            min_value = 0.0,
            value = 0.45
            )

        income = st.number_input(
            "Monthly Income",
            min_value = 0.0,
            value = 5000.0
            )

    with col2:
        credit = st.number_input(
            "Open Credit Lines and Loans",
            min_value = 0,
            value = 0
            )

        late90 = st.number_input(
             "Number of Times 90 Days Late",
            min_value = 0,
            value = 0
            )

        real_estate = st.number_input(
            "Number of Real Estate Loans",
            min_value = 0,
            value = 1
            )

        late60 = st.number_input(
            "Number of Times 60-89 Days Past Due",
            min_value = 0,
            value = 0
            )

        dependents = st.number_input(
            "Number of Dependents",
            min_value = 0,
            value = 2
            )

    submitted = st.form_submit_button("Predict Credit Risk")

st.divider()

# Form Submission Button

if submitted:

    data = {
        "RevolvingUtilizationOfUnsecuredLines": revolving,
        "age": age,
        "NumberOfTime30_59DaysPastDueNotWorse": late30,
        "DebtRatio": debt,
        "MonthlyIncome": income,
        "NumberOfOpenCreditLinesAndLoans": credit,
        "NumberOfTimes90DaysLate": late90,
        "NumberRealEstateLoansOrLines": real_estate,
        "NumberOfTime60_89DaysPastDueNotWorse": late60,
        "NumberOfDependents": dependents
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict/",
        json = data

    )

    with st.container():

        if response.status_code == 200:
            result = response.json()

            st.header("Prediction Results")
        
            st.success(result["risk"])
            st.subheader(f"This person will have {result["prediction"]}")
            st.subheader("Probability of Default")
            st.progress(result["probability"], text=f"{result["probability"]*100:.2f}%")
            st.write(f"{result["probability"]*100:.2f}%")
            st.subheader("Confidence")
            st.write(result["confidence"])
            st.subheader("Model: XGBoost")

        
        else :
            st.error("Prediction Failed")
            st.write(response.text)

with st.sidebar:

    st.title("About")

    st.write("This application predicts whether an individual is likely"
    " to default on a loan using an XGBoost Machine Learning Model")

    st.divider()

    st.subheader("Model")

    st.write("""
**Algorithm**: XGBoost

**Task**: Binary Classification

**Dataset**: Give Me Some Credit (Kaggle)
""")

    st.divider()

    st.subheader("Tech Stack")
    st.write("""
- Python
- FastAPI
- Streamlit
- XGBoost
- Scikit-Learn""")

    st.write("""
**Developer**: Mudit Sapra
""")

    st.divider()

    st.markdown(
        """"
        <div style='text-align:center; color:gray; font-size:15px;'>
        
        Credit Default Prediction System
        
        Developed by <b>Mudit Sapra<b>

        Developed using <b>Streamlit<b>, <b>FastAPI<b> and <b>XGBoost<b>

        <div>
        
        """,
        unsafe_allow_html=True
    )


st.info("""
### How to Interpret the Results

🟢 **Low Risk:** Customer is unlikely to default.

🟡 **Medium Risk:** Customer has moderate credit risk.

🔴 **High Risk:** Customer is likely to default.
""")
    

    