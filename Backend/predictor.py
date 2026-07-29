import joblib
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv("data/cs-training.csv")
df["MonthlyIncome"].fillna(df["MonthlyIncome"].median(), inplace=True)
df["NumberOfDependents"].fillna(df["NumberOfDependents"].median(), inplace=True)
df = df.drop("Unnamed: 0", axis=1)

X_train, X_test, y_train, y_test = train_test_split(df.drop("SeriousDlqin2yrs", axis=1), df["SeriousDlqin2yrs"], test_size=0.2, random_state=42)


model = joblib.load("models/credit_default.pkl")
scaler = joblib.load("models/scaler(1).pkl")

y_preds = model.predict(X_test)

def predict_credit(features):

    features = scaler.transform(features) 

    prediction = model.predict(features)[0]

    probability = model.predict_proba(features)[0][1]

    percentage = probability * 100

    percentage = round(percentage, 2)

    accuracy = accuracy_score(y_test, y_preds)
    accuracy = f"{round(accuracy*100, 2)}%"
    risk = ""

    if percentage >= 0  and percentage < 35:
        risk = "🟢 Low Risk"

    elif percentage >= 35 and percentage < 70:
        risk = "🟡 Medium Risk"

    else :
        risk = "🔴 High Risk"
    
    

    return prediction, probability, risk, accuracy
