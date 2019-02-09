
def receive_basic_iuput_data(Singal_Loss, Shock_Alert, Oxygen_Supply, Fever, Hypotension, Hypertension):
 ##Recevie data from input module, then analyze it using some judge functions to generate boolean result
 ##Boolean Parameters
 ##If paramter returns True, means it should be alerted, then add it to the array
    BasicResult = []
    if(Singal_Loss == True):
        BasicResult.append(Singal_Loss)
    if(Shock_Alert == True):
        BasicResult.append(Shock_Alert) 
    if(Oxygen_Supply == True):
        BasicResult.append(Oxygen_Supply)
    if(Fever == True):
        return BasicResult.append(Fever) 
    if(Hypotension == True):
        BasicResult.append(Hypotension)
    if(Hypertension == True):
        BasicResult.append(Hypertension) 

    return BasicResult

'''
def send_basic_input_data(BasicResult, BasicData):
 ## Receive the result and show it on terminal or web page
    sentData = analyze(BasicResult)
    return sentData, BasicData
'''
def receive_AI_iuput_data(Singal_Loss, Shock_Alert, Oxygen_Supply, Fever, Hypotension, Hypertension):
 ## Recevie AI data from input module, then analyze it using some judge functions to generate boolean result
 ## Paramter is boolean
 ## If paramter is True, means it should be alerted, then add it to the array
    AIResult = []
    if(Singal_Loss == True):
        AIResult.append(Singal_Loss) 
    if(Shock_Alert == True):
        AIResult.append(Shock_Alert) 
    if(Oxygen_Supply == True):
        AIResult.append(Oxygen_Supply)
    if(Fever == True):
        return AIResult.append(Fever) 
    if(Hypotension == True):
        AIResult.append(Hypotension)
    if(Hypertension == True):
        AIResult.append(Hypertension) 
    return AIResult

'''
def send_AI_input_data(AIResult):
 ## Receive the result and show it on terminal or web page
    #sentData = analyze(AIResult)
    return sentData
'''