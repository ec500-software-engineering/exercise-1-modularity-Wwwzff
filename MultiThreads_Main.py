import threading
from AI_module import AI_module
from analyzer import Analyzer
from Database_Module import DataBaseModule
from input_api import input_api, filt
from time import ctime
from OutputAlert_module import *
import time

#source of input signals
txtFile = "./example.txt"

# admin login
DB = DataBaseModule()
username = 'admin'
password = '123456'
DB.authen(username, password)

class MultiThreads:
    def __init__(self):
        #self.printed = False
        self.output = {}
        self.inputbuffer = []

    def inputpart(self):
        print('[InputModule]start working')
        with open(txtFile) as f:
            #read inputstream by line
            for line in f.readlines():
                infoLine = line.strip().split(" ")
                inputs = input_api(infoLine[0], infoLine[1], infoLine[2], \
                    infoLine[3], infoLine[4], infoLine[5], infoLine[6], infoLine[7], ctime())
                inputs.implement_filter()
                #pass info to DB module
                userID,allInfo = inputs.return_request(2)
                DB.insert(userID,allInfo)
                self.inputbuffer.append(inputs.return_request(1))
                time.sleep(1)

    def process(self):
        print('[ProcessingModule]start working')
        if len(self.inputbuffer)!= 0:
            for toAnalyser in self.inputbuffer:
                #pass info to analyzer
                Systolic_BP = int(toAnalyser['Systolic_BP'])
                Diastolic_BP = int(toAnalyser['Diastolic_BP'])
                heartrate = int(toAnalyser['heartrate'])
                Heart_O2_Level = int(toAnalyser['blood_oxygen'])
                Body_temp = int(toAnalyser['temperature'])

                #Analysing
                analyse = Analyzer(Systolic_BP, Diastolic_BP, heartrate, Heart_O2_Level, Body_temp)
                signal_loss = analyse.Signal_Loss(heartrate, Body_temp)
                Shock_Alert = analyse.Shock_Alert(heartrate, Body_temp)
                Oxygen_Supply = analyse.Oxygen_Supply(Heart_O2_Level)
                Fever = analyse.Fever(Body_temp)
                Hypotension = analyse.Hypotension(Systolic_BP, Diastolic_BP)
                Hypertension = analyse.Hypertension(Systolic_BP, Diastolic_BP)

                #pass alert signals to output
                self.output[ctime()] = receive_basic_iuput_data(signal_loss, Shock_Alert, \
                    Oxygen_Supply, Fever, Hypotension, Hypertension)
                #self.printed = False
            self.inputbuffer = []
            time.sleep(1)

    def output_module(self):
        print('[OutputModule]start working')
        while True:
            if len(self.output) != 0:
                print(self.output)
                #self.printed = True
                self.output = {}
                time.sleep(1)



task = MultiThreads()

threads = []
thread1 = threading.Thread(target=task.inputpart())
threads.append(thread1)
thread2 = threading.Thread(target=task.process())
threads.append(thread2)
thread3 = threading.Thread(target=task.output_module())
threads.append(thread3)

for part in threads:
    part.start()






'''
# Machine Learning Part
MLpart = AI_module(DB.infoDB)
Blood_oxygen, Diastolic_BP, Systolic_BP, Pulses = MLpart.Query_Data_From_Database('50000')
oxygen_predict_result, Pulse_predict_result, Diastolic_BP_result, Systolic_BP_result = MLpart.AI_Module(Blood_oxygen, Diastolic_BP, Systolic_BP, Pulses)
feedback = MLpart.Feedback(Diastolic_BP_result, Systolic_BP_result, oxygen_predict_result, Pulse_predict_result)

#feedback for prediction
#BO_Alert,BP_Alert,Pulse_Alert
#Boolean type
print(feedback)
'''