# Guitar Lesson Data

This is data regarding one-on-one classical guitar lessons, categorized by the pieces of music (LS1 to 7) for which two or more lessons were conducted. There are a total of 24 data entries.

* resource_data: This is the original data that combines speech information obtained by whisper with the 'music' identified by inaSpeechSegmenter.

* inaSpeechSegmenter: Speech segments detected using inaSpeechSegmenter. It comprises four elements: music, speech, noise, and noEnergy.

* time_series: Python code for visualizing the time-series changes in performance ('music') and speech (teacher and student) for each lesson. You can try two patterns: the instructional topic label (_itl) and the instructional content label (_icl).

* network: Data for analyzing bi-grams and co-occurrence networks. You can implement this in a Jupyter Notebook.
