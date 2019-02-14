
def receive_basic_iuput_data(Singal_Loss, Shock_Alert, Oxygen_Supply, Fever, Hypotension, Hypertension):
 ##Recevie data from input module, then analyze it using some judge functions to generate boolean result
 ##Boolean Parameters
 ##If paramter returns True, means it should be alerted, then add it to the array
    BasicResult = {}
    if Singal_Loss:
        BasicResult["Singal_Loss"] = True
    if Shock_Alert:
        BasicResult['Shock_Alert'] = True
    if Oxygen_Supply:
        BasicResult['Oxygen_Supply'] = True
    if Fever:
        BasicResult['Fever'] = True 
    if Hypotension:
        BasicResult['Hypotension'] = True
    if Hypertension:
        BasicResult['Hypertension'] = True  

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
    if Singal_Loss:
        AIResult.append(Singal_Loss) 
    if Shock_Alert:
        AIResult.append(Shock_Alert) 
    if Oxygen_Supply:
        AIResult.append(Oxygen_Supply)
    if Fever:
        AIResult.append(Fever) 
    if Hypotension:
        AIResult.append(Hypotension)
    if Hypertension:
        AIResult.append(Hypertension) 
    return AIResult

'''
def send_AI_input_data(AIResult):
 ## Receive the result and show it on terminal or web page
    #sentData = analyze(AIResult)
    return sentData
'''