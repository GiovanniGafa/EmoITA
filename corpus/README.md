'EmoITA.csv' is an UTF-8, comma-separated csv file containing 10,063 Italian sentences annotated according to the Valence-Arousal-Dominance psychological model. 

In order to produce it, 16 students from the Master’s Degree in Foreign Languages at the University of Catania were asked to translate to Italian the EmoBank corpus (https://github.com/JULIELab/EmoBank/tree/master). All of them were Italian native speakers and were specializing in English. The same group of subjects also labeled each Italian sentence according to the emotion evoked in an average reader. We took care never to ask a participant to annotate a sentence he had translated. 

Overall, we obtained 7 different annotations for each sentence. The 'EmoITA.csv' file contains the average annotations for each sentence and emotion dimension.

The csv file as the form: id, text, V, A, D, where:
- 'id' is the original id found in the EmoBank corpus (https://github.com/JULIELab/EmoBank/blob/master/corpus/emobank.csv)
- 'text' is the Italian translation of the corresponding English sentence in the EmoBank corpus
- 'V' is the average Valence score annotated for the sentence
- 'A' is the average Arousal score annotated for the sentence
- 'D' is the average Dominance score annotated for the sentence
