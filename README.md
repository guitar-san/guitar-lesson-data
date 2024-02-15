# Guitar Lesson Dataset

This is dataset regarding one-on-one classical guitar lessons, categorized by the pieces of music (LS1 to 7) for which two or more lessons were conducted. There are a total of 24 data entries.

* resource_dataset: This dataset contains speech data obtained by whisper. It includes 'T-Speech' for teacher speech and 'S-Speech' for student speech. Additionally, the 'music' category indicates performance duration as detected by the inaSpeechSegmenter.

* inaSpeechSegmenter: Speech segments detected using inaSpeechSegmenter. It comprises four elements: music, speech, noise, and noEnergy.

* network: Data for analyzing bi-grams and co-occurrence networks. You can implement this in a Jupyter Notebook.
