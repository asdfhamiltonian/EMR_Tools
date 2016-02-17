from tkinter import Tk

pain = """ Check all that describe your pain today:
[ ] Aching	[X] Shooting	[X] Cramping
[ ] Spasming	[X] Dull		[X] Squeezing
[X] Tingling/Pins & Needles	[X] Tiring/Exhausting
[X] Hot/Burning		[ ] Stabbing/Sharp
[ ] Numb	[ ] Throbbing [X] Shock-like
Which word best describes the frequency of your pain?
  ( ) Constant	(X) Intermittent
  """

pains = pain.split("]")
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
for i in range(0, len(pain_descriptors_list) - 1):
    if reported_pains_bool[i]:
        reported_symptoms.append(pain_descriptors_list[i])

outputString = "Patient reports " + frequency + " pain that is " + listSymptoms(reported_symptoms) + " in nature."

print(outputString)

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

    outString = """"""
    outString += """\n Constitutional \n""" + const(constText)
    outString += """\n\n Eyes \n""" + eye(eyesText)
    outString += """\n\n Ears/Nose/Throat/Neck \n""" + ent(entText)
    outString += "\n\n Cardiovascular \n" + cardiovascular(cardioText)
    outString += "\n\n Respiratory \n" + respiratory(respiratoryText)
    outString += "\n\n Gastrointestinal \n" + gastrointestinal(gastrointestinalText)
    outString += "\n\n Musculoskeletal \n" + musculoskeletal(musculoskeletalText)
    outString += "\n\n Genitourinary \n" + genitourinary(genitourinaryText)
    outString += "\n\n Neurological \n" + neurological(neurologicalText)
    outString += "\n\n Psychiatric \n" + psychiatric(psychiatricText)

    copy(outString)
    print(outString)