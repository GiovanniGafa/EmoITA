This folder contains files developed for the shared task EmotivITA (https://sites.google.com/view/emotivita) at EVALITA 2023 (https://www.evalita.it/campaigns/evalita-2023/).
'Development set.csv' contains 8,000 Italian sentences annotated according to the VAD dimensions, originally released to participants on 7th February 2023. 
'Test set.csv' contains 2,063 Italian sentences withous annotations, originally released to participants on 12th May 2023.
'Test set - Gold labels.csv' contains the 2,063 Italian sentences from 'Test set.csv' along with their annotations, originally released to participants on 15th June 2023
'evaluation.py' contains the script used to evaluate submissions by participant systems for both sub-task A and sub-task B in the EmotivITA shared task. 
'requirements.txt' lists the versions of the Python libraries used in the evaluation.py script. The Python version used for the evaluation script will be 3.9.7.
'Baselines.pdf' contains the baselines for both sub-tasks. The results were obtained using "Development set.csv' to fine-tune to regression a BERT model available on HuggingFace (https://huggingface.co/dbmdz/bert-base-italian-xxl-uncased) for four epochs, with Learning rate=1e-05, Batch size=8, Sequence lenght=512, and then using 'Test set.csv' for testing. We made 4 runs for each script and reported average results as the baselines. 
'EmotivITA Guidelines.pdf' contains the guidelines for the shared task. 
