
import numpy as np
from Database_Module import DataBaseModule

# Input: ID(from main function perhaps), infoDB(from Database function)
# output: Three predicted parameters, three Alert signals(Type:Boolean

class AI_module:
    def __init__(self, infoDict):
        self.infoDB = infoDict

    def Query_Data_From_Database(self,ID):
        ## connect database, query previous one day data from Database
        # Database = database_dict()
        Blood_oxygen= []
        Diastolic_BP = []
        Pulses= []
        Systolic_BP = []
        
        info = DataBaseModule()
        info.authen('admin','123456')
        info = info.search(ID)
        # Username = input("")
        #get dictionary from database
        for key in self.infoDB:
            if key== ID:
                _Diastolic_BP = info['Diastolic_BP']
                _Systolic_BP = info['Systolic_BP']
                _oxygen = info['blood_oxygen']
                _Pulse = info['heartrate']
                Diastolic_BP.append(int(_Diastolic_BP))
                Systolic_BP.append(int(_Systolic_BP))
                Blood_oxygen.append(int(_oxygen))
                Pulses.append(int(_Pulse))


        return Blood_oxygen, Diastolic_BP, Systolic_BP, Pulses


    def AI_Module(self,Blood_oxygen, Diastolic_BP, Systolic_BP, Pulses):

        ## AI module do the prediection, The AI module uses previous data
        oxygen=np.array(Blood_oxygen)
        Diastolic_BP = np.array(Diastolic_BP)
        Systolic_BP = np.array(Systolic_BP)
        Pulse = np.array(Pulses)
        Diastolic_BP_result = np.mean(Diastolic_BP)
        Systolic_BP_result = np.mean(Systolic_BP)
        Pulse_predict_result = np.mean(Pulse)
        oxygen_predict_result = np.mean(oxygen)

        return oxygen_predict_result, Pulse_predict_result, Diastolic_BP_result, Systolic_BP_result


    def Feedback(self, Diastolic_BP_result, Systolic_BP_result, Blood_oxygen_predict_result, Pulse_predict_result):
        lower_BP= 80
        upper_BP= 120
        lower_BO = 80
        upper_BO = 120
        lower_Pulse = 80
        upper_Pulse = 120
        BP_Alert= False
        BO_Alert = False

        Pulse_Alert =False
        if(Blood_oxygen_predict_result<lower_BO or Blood_oxygen_predict_result>upper_BO):
            BO_Alert =True
        if(Systolic_BP_result<lower_BP or Diastolic_BP_result>upper_BP):
            BP_Alert =True
        if(Pulse_predict_result< lower_Pulse or Pulse_predict_result >upper_Pulse):
            Pulse_Alert =True
        ## feedback the AI prediction restult to the interface
        ## It will turn on the Alert when the statues get worse.
        return (BO_Alert,BP_Alert,Pulse_Alert)


