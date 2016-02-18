from tkinter import Tk

def listSymptoms(symptoms):
    symptomString = ""
    if len(symptoms) == 1:
        symptomString = symptoms[0]
    else:
        last = symptoms.pop()
        symptomString = ", ".join(symptoms)
        symptomString += " and " + last
    return symptomString

def copy(inputString):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(inputString)
    r.destroy()

def intake(inputText):
    pains = inputText.split("]")
    frequencies = pains.pop()
    frequencies = frequencies.split(")")
    frequencies.pop() # The last string does not have any checkbox data

    # print(pains)
    # print(frequencies)

    pain_descriptors_list = ["aching", "shooting", "cramping", "spasming",
                             "dull", "squeezing", "tingling/pins & needles",
                             "tiring/exhausting", "hot/burning", "stabbing/sharp",
                             "numb", "throbbing", "shock-like"]
    reported_pains_bool = []
    for pain in pains:
        if pain[-1] == "X":
            reported_pains_bool.append(True)
        else:
            reported_pains_bool.append(False)
    # print(reported_pains_bool)

    # extracting pain frequency
    frequency = ""
    if frequencies[0][-1] == "X":
        frequency = "constant"
    elif frequencies[1][-1] == "X":
        frequency = "intermittent"

    def listSymptoms(symptoms):
        symptomString = ""
        if len(symptoms) == 1:
            symptomString = symptoms[0]
        else:
            last = symptoms.pop()
            symptomString = ", ".join(symptoms)
            symptomString += " and " + last
        return symptomString

    reported_symptoms = []
    for i in range(0, len(pain_descriptors_list)):
        if reported_pains_bool[i]:
            reported_symptoms.append(pain_descriptors_list[i])

    outputString = "Pain quality described as " + frequency + ", " + listSymptoms(reported_symptoms) + ". "
    copy(outputString)
    return outputString

const_list = ["chills", "difficulty sleeping", "easy bruising",
              "excessive sweating", "excessive thirst",
              "fatigue", "fevers", "insomnia", "low sex drive",
              "night sweats", "tremors", "unexplained weight gain",
              "unexplained weight loss"]

eye_list = ["recent visual changes"]

ent_list = ["dental problems", "earaches", "hearing problems", "nosebleeds",
             "recurring sore throats", "ringing in the ears", "sinus problems"]

cardiovascular_list = ["bleeding disorder", "chest pain", "hearing problems", "noseblees",
                        "high blood pressure", "irregular heart beat", "lightheadedness",
                        "swelling in the feet", "shortness of breath during sleep"]

respiratory_list = ["cough", "wheezing", "pulmonary embolism",
                    "shortness of breath on exertion/effort"]

gastrointestinal_list = ["abdomnial cramps", "acid reflux", "constipation",
                         "dark and tarry stools", "diarrhea", "hernia", "vomiting",
                         "coffee ground appearance in vomit"]

musculoskeletal_list = ["back pain", "joint pain", "joint stiffness", "joint swelling",
                        "muscle spasms", "neck pain"]

genitourinary_list = ["blood in urine", "flank pain", "painful urination",
                      "decreased urine flow/frequency/volume"]

neurological_list = ["dizziness", "headaches", "numbness/tingling", "carpal tunnel syndrome",
                     "tremors", "seizures", "instability when walking"]

psychiatric_list = ["depressed mood", "feeling anxious", "stress problems", "suicidal thoughts",
                    "suicidal planning"]

def listSymptoms(symptoms):
    symptomString = ""
    if len(symptoms) == 1:
        symptomString = symptoms[0]
    elif len(symptoms) == 0:
        symptomString = "no symptoms"
    else:
        last = symptoms.pop()
        symptomString = ", ".join(symptoms)
        symptomString += " and " + last
    return symptomString

def ros_item(inputText, ros_list):
    ros = inputText.split("]")
    ros.pop() # The last string does not have any checkbox data

    reported_findings_bool = []
    for finding in ros:
        if finding[-1] == "X":
            reported_findings_bool.append(True)
        else:
            reported_findings_bool.append(False)

    reported_findings = []
    for i in range(0, len(ros_list)):
        if reported_findings_bool[i]:
            reported_findings.append(ros_list[i])

    if len(reported_findings) == 0:
        outputString = "Denies relevant symptoms. "
    else:
        outputString = "Complaints of " + listSymptoms(reported_findings) + ". "

    return outputString

def const(inputText):
    return ros_item(inputText, const_list)

def eye(inputText):
    return ros_item(inputText, eye_list)

def ent(inputText):
    return ros_item(inputText, ent_list)

def cardiovascular(inputText):
    return ros_item(inputText, cardiovascular_list)

def respiratory(inputText):
    return ros_item(inputText, respiratory_list)

def gastrointestinal(inputText):
    return ros_item(inputText, gastrointestinal_list)

def musculoskeletal(inputText):
    return ros_item(inputText, musculoskeletal_list)

def genitourinary(inputText):
    return ros_item(inputText, genitourinary_list)

def neurological(inputText):
    return ros_item(inputText, neurological_list)

def psychiatric(inputText):
    return ros_item(inputText, psychiatric_list)

def allROS(inputText):
    remainder = inputText.split("Eyes:")
    constText = remainder[0]
    remainder = remainder[1].split("Ears/Nose/Throat/Neck:")
    eyesText = remainder[0]
    remainder = remainder[1].split("Cardiovascular:")
    entText = remainder[0]
    remainder = remainder[1].split("Respiratory:")
    cardioText = remainder[0]
    remainder = remainder[1].split("Gastrointestinal:")
    respiratoryText = remainder[0]
    remainder = remainder[1].split("Musculoskeletal:")
    gastrointestinalText = remainder[0]
    remainder = remainder[1].split("Genitourinary/Nephrology:")
    musculoskeletalText = remainder[0]
    remainder = remainder[1].split("Neurological:")
    genitourinaryText = remainder[0]
    remainder = remainder[1].split("Psychiatric:")
    neurologicalText = remainder[0]
    psychiatricText = remainder[1]

    def lister(things_list):
        if len(things_list) == 0:
            return ""
        elif len(things_list) == 1:
            return things_list[0]
        else:
            last = things_list.pop()
            outString = ", ".join(things_list)
            outString += " and " + last
            return outString

    outString = """"""
    negatives_list = []
    if const(constText) != "Denies relevant symptoms. ":
        outString += """Constitutional \n""" + const(constText)
    else:
        negatives_list.append("Constitutional")

    if eye(eyesText) != "Denies relevant symptoms. ":
        outString += """\n\nEyes \n""" + eye(eyesText)
    else:
        negatives_list.append("Eyes")

    if ent(entText) != "Denies relevant symptoms. ":
        outString += """\n\nEars/Nose/Throat/Neck \n""" + ent(entText)
    else:
        negatives_list.append("ENT")

    if cardiovascular(cardioText) != "Denies relevant symptoms. ":
        outString += "\n\nCardiovascular \n" + cardiovascular(cardioText)
    else:
        negatives_list.append("Cardio")

    if respiratory(respiratoryText) != "Denies relevant symptoms. ":
        outString += "\n\nRespiratory \n" + respiratory(respiratoryText)
    else:
        negatives_list.append("Respiratory")

    if gastrointestinal(gastrointestinalText) != "Denies relevant symptoms. ":
        outString += "\n\nGastrointestinal \n" + gastrointestinal(gastrointestinalText)
    else:
        negatives_list.append("GI")

    if musculoskeletal(musculoskeletalText) != "Denies relevant symptoms. ":
        outString += "\n\nMusculoskeletal \n" + musculoskeletal(musculoskeletalText)
    else:
        negatives_list.append("Musculoskeletal")

    if genitourinary(genitourinaryText) != "Denies relevant symptoms. ":    
        outString += "\n\nGenitourinary \n" + genitourinary(genitourinaryText)
    else:
        negatives_list.append("GU")

    if neurological(neurologicalText) != "Denies relevant symptoms. ":
        outString += "\n\nNeurological \n" + neurological(neurologicalText)
    else:
        negatives_list.append("Neuro")

    if psychiatric(psychiatricText) != "Denies relevant symptoms. ":
        outString += "\n\nPsychiatric \n" + psychiatric(psychiatricText)
        print(psychiatricText)
    else:
        negatives_list.append("Psych")

    if len(negatives_list) >= 1:
        outString += "\n\nThe review of systems is negative for "
        outString += lister(negatives_list)
        outString += "."
    
    copy(outString)
    print(outString)
