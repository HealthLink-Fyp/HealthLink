prompt_template = """
Based on the conversation transcript, generate clinical notes in the following format (JSON), use the provided examples as a reference to structure the output. The output should include the following sections:

1. key_points (List of key points): Concise list of keywords of various medical conditions, events, or treatments, providing specific details such as frequency, duration, dosage, timing, and relevant context.

Example:
[Sudden severe chest pain (lasted 30 mins),
Back pain (every morning and worsens with sitting),
Migraines (Twice weekly and stress triggers),
Father's heart attack (55 age),
Diagnosed with diabetes (5 years ago),
Blood pressure (Lisinopril 10 mg daily),
Laparoscopic colectomy (scheduled next month),
Elevated LDL (160 mg/dL) and normal CBC,
Processed foods (High intake),
Smoking (1 pack/day for 20 years)]


2. likely_diagnoses (List of diagnosis and %probability): Probabilistic assessments of potential diagnoses based on the context provided in the transcript, assigning likelihoods to each possible condition.

Example:
[["Pneumonia", "60%"],
["Hypertensive crisis", "30%"],
["Migraine with aura", "10%"],
["Occipital neuralgia", "5%"]]


3. followup_questions (list of questions): Structured inquiries used by healthcare providers to gather specific details and pertinent information from patients during consultations, aimed at understanding their medical history, symptoms, and potential risk factors. These questions should be tailored to the context of the transcript not generic.



Here is the Transcript of conversation, just give me output in JSON format, nothing else:
{anonymized_text}
"""


prompt_template_dashboard = """
Based on the medical records of the patient, Generate medical notes (JSON OBJECT) in the following format. You can suggest the possible symptoms and their severity levels, as well as the potential diseases based on the patient's conditions and their risk percentages. Assume percentages for severity levels and risk percentages for potential diseases, if not provided in the medical records.

1. Body parts with symptoms and their severity levels, alongside corresponding symptoms.
2. Patient's conditions and their risk percentages for potential diseases.

Example JSON Format:
```json
{{
  "symptoms": [
    {{
      "body_part": "Head",
      "symptoms": [
        {{"symptom": "Headache", "severity": "30%"}},
        {{"symptom": "Dizziness", "severity": "20%"}}
      ]
    }},
    {{
      "body_part": "Hand",
      "symptoms": [
        {{"symptom": "Fracture", "severity": "40%"}},
        {{"symptom": "Swelling", "severity": "10%"}}
      ]
    }}
  ],
  "conditions": [
    {{"condition": "Caries", "riskPercentage": "5%"}},
    {{"condition": "Hematoma", "riskPercentage": "20%"}},
    {{"condition": "Acne", "riskPercentage": "30%"}},
    {{"condition": "Fracture", "riskPercentage": "40%"}},
    {{"condition": "Cold", "riskPercentage": "50%"}}
  ]
}}

```


Please provide the response in the exact JSON format as specified above. No additional sentences or responses are needed.
Here is the Medical records of the patient:

{anonymized_text}

"""
