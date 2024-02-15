# Guitar Lesson Dataset

This is dataset regarding one-on-one classical guitar lessons, categorized by the pieces of music (LS1 to 7) for which two or more lessons were conducted. There are a total of 24 data entries.

* resource_dataset: This dataset contains speech data extracted using [whisper](https://openai.com/research/whisper). It includes 'T-Speech' for teacher speech and 'S-Speech' for student speech. Additionally, the 'music' category indicates performance duration as detected by inaSpeechSegmenter.

* inaSpeechSegmenter: Audio segments detected using [inaSpeechSegmenter](https://github.com/ina-foss/inaSpeechSegmenter)). It comprises four elements: music, speech, noise, and noEnergy.

* network: Data for analyzing bi-grams and co-occurrence networks. You can implement this in a Jupyter Notebook.
