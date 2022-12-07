# PyMusicData
This is a quick and easy way to get essentia musicextractor data for your songs.  

Connect your drive, link the songs, analyse! 
(There is time to analyse, Thom!)

Files are downloaded to json.  

This is easy and quick!  

Take the json and process in the comfort of your own code editor.

The main reason I put this together was linked to the difficulties in getting Essentia installed on MacOS.

https://colab.research.google.com/github/rayking99/PyMusicData/blob/main/PyMusicData.ipynb

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rayking99/PyMusicData/blob/main/PyMusicData.ipynb)

OUTPUTS (from: https://essentia.upf.edu/streaming_extractor_music.html)

loudness_ebu128
average_loudness
dynamic_complexity
silence_rate_20dB, silence_rate_30dB, silence_rate_60dB
spectral_rms
spectral_flux
spectral_centroid, spectral_kurtosis, pectral_spread, spectral_skewness
spectral_rolloff
spectral_decrease
hfc
spectral_strongpeak
zerocrossingrate zero-crossing rate.
spectral_energy
spectral_energyband_low, spectral_energyband_middle_low, spectral_energyband_middle_high, spectral_energyband_high
barkbands
melbands
melbands128
erbbands
mfcc
gfcc
barkbands_crest, barkbands_flatness_db
barkbands_kurtosis, barkbands_skewness, barkbands_spread
melbands_crest, melbands_flatness_db
melbands_kurtosis, melbands_skewness, melbands_spread
erbbands_crest, erbbands_flatness_db
erbbands_kurtosis, erbbands_skewness, erbbands_spread
dissonance
spectral_entropy
pitch_salience
spectral_complexity
spectral_contrast_coeffs, spectral_contrast_valleys
beats_position
beats_count
bpm
bpm_histogram
bpm_histogram_first_peak_bpm, bpm_histogram_first_peak_spread, bpm_histogram_first_peak_weight, bpm_histogram_second_peak_bpm, bpm_histogram_second_peak_spread, bpm_histogram_second_peak_weight
beats_loudness, beats_loudness_band_ratio
onset_rate
danceability
tuning_frequency
hpcp, thpcp
hpcp_entropy
hpcp_crest
key_temperley, key_krumhansl, key_edma
chords_strength, chords_histogram, chords_changes_rate, chords_number_rate, chords_key, chords_scale
tuning_diatonic_strength
tuning_equal_tempered_deviation, tuning_nontempered_energy_ratio

