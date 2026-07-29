from fastapi import FastAPI, APIRouter
from Backend.schemas import CreditRequest, PredictionResponse
from Backend.predictor import predict_credit

router = APIRouter(
    prefix = "/predict",
    tags = ["Prediction"]
)

@router.post("/", response_model=PredictionResponse)
async def predict(request: CreditRequest):

    features = [[
        request.RevolvingUtilizationOfUnsecuredLines,
        request.age,
        request.NumberOfTime30_59DaysPastDueNotWorse,
        request.DebtRatio,
        request.MonthlyIncome,
        request.NumberOfOpenCreditLinesAndLoans,
        request.NumberOfTimes90DaysLate,
        request.NumberRealEstateLoansOrLines,
        request.NumberOfTime60_89DaysPastDueNotWorse,
        request.NumberOfDependents
    ]]

    prediction, probability, risk, accuracy = predict_credit(features)

    if prediction == 1:
        result = "Default"

    else:
        result = "No Default"

    return PredictionResponse(
        prediction=result,
        probability=round(probability,4),
        risk=risk,
        confidence=accuracy
    )