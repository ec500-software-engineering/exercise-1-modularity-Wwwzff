from AI_module import AI_module
from analyzer import Analyzer
from Database_Module import DataBaseModule
from input_api import input_api, filt
from time import ctime
from OutputAlert_module import *


txtFile = "./example.txt"

authenDB = {'admin':"123456"}
infoDB = {}

# admin login
DB = DataBaseModule()
username = 'admin'
password = '123456'
DB.authen(username, password)


with open(txtFile) as f:
    #read inputstream by line
    infoLine = f.readline().split(" ")
    inputs = input_api(infoLine[0], infoLine[1], infoLine[2], infoLine[3], infoLine[4], infoLine[5], infoLine[6], infoLine[7], ctime())
    inputs.implement_filter()

    #pass info to DB module
    userID,allInfo = inputs.return_request(2)
    DB.insert(userID,allInfo)
    
    #pass info to analyzer
    toAnalyser = inputs.return_request(1)
    Systolic_BP = int(toAnalyser['Systolic_BP'])
    Diastolic_BP = int(toAnalyser['Diastolic_BP'])
    heartrate = int(toAnalyser['heartrate'])
    Heart_O2_Level = int(toAnalyser['blood_oxygen'])
    Body_temp = int(toAnalyser['temperature'])

    #Analysing
    analyse = Analyzer(Systolic_BP,Diastolic_BP,heartrate,Heart_O2_Level,Body_temp)
    signal_loss = analyse.Signal_Loss(heartrate,Body_temp)
    Shock_Alert = analyse.Shock_Alert(heartrate,Body_temp)
    Oxygen_Supply = analyse.Oxygen_Supply(Heart_O2_Level)
    Fever = analyse.Fever(Body_temp)
    Hypotension = analyse.Hypotension(Systolic_BP,Diastolic_BP)
    Hypertension = analyse.Hypertension(Systolic_BP,Diastolic_BP)

    #pass signals to output
    output = receive_basic_iuput_data(signal_loss, Shock_Alert, Oxygen_Supply, Fever, Hypotension, Hypertension)
    print(output)






# Machine Learning Part
MLpart = AI_module(infoDB)
Blood_oxygen, Blood_pressure, Pulses = MLpart.Query_Data_From_Database('50000')
pressure_predict_result, oxygen_predict_result, Pulse_predict_result = MLpart.AI_Module(Blood_oxygen, Blood_pressure, Pulses)
feedback = MLpart.Feedback(pressure_predict_result, oxygen_predict_result, Pulse_predict_result)

print(feedback)