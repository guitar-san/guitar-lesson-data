# Guitar Lesson Dataset

This is dataset regarding one-on-one classical guitar lessons, categorized by the pieces of music (LS1 to 7) for which two or more lessons were conducted. There are a total of 24 data entries.

* inaSpeechSegmenter: Audio segments detected using [inaSpeechSegmenter](https://github.com/ina-foss/inaSpeechSegmenter)). It comprises four elements: music, speech, noise, and noEnergy.

* resource_dataset: This dataset contains speech data extracted using [whisper](https://openai.com/research/whisper). It includes 'T-Speech' for teacher utterances and 'S-Speech' for student utterances. Additionally, the 'music' category indicates performance duration as detected by inaSpeechSegmenter. It's important to note that specific content details of the utterances are omitted to preserve privacy.

* network: Data for analyzing bi-grams and co-occurrence networks. You can implement this in a Jupyter Notebook.
