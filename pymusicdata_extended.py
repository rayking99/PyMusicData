import essentia
import essentia.standard as es
from pathlib import Path
import time
import glob
import pandas as pd 
import json
import glob
from natsort import natsorted,index_natsorted,order_by_index


songs = glob.glob('/content/drive/MyDrive/**.wav')

for song in songs:
  song_name = Path(song).stem
  features, features_frames = es.MusicExtractor(lowlevelStats=['mean', 'stdev'],rhythmStats=['mean', 'stdev'],tonalStats=['mean', 'stdev'])(song)
  results_file = "/content/drive/MyDrive" + '/%s_results.json' % song_name
  es.YamlOutput(filename=results_file, format="json")(features)

json_files = glob.glob('path/to/jsonfiles/**.json')


all_dynamic_complexity = []
all_integrated = []
all_spectral_energy = []
all_spectral_entropy = []
all_spectral_spread = []
all_danceability = []
all_mean = []
all_bpm = []
all_chords_key = []
all_chords_scale = []
all_title = []
all_artist = []

for file in json_files:
    file = open(file).read()
    data = json.loads(file)
    dynamic_complexity = data['lowlevel']['dynamic_complexity']
    all_dynamic_complexity.append(dynamic_complexity)
    integrated = data['lowlevel']['loudness_ebu128']['integrated']
    all_integrated.append(integrated)
    spectral_energy = data['lowlevel']['spectral_energy']['mean']
    all_spectral_energy.append(spectral_energy)
    spectral_entropy = data['lowlevel']['spectral_entropy']['mean']
    all_spectral_entropy.append(spectral_entropy)
    spectral_spread = data['lowlevel']['spectral_spread']['mean']
    all_spectral_spread.append(spectral_spread)
    danceability = data['rhythm']['danceability']
    all_danceability.append(danceability)
    mean = data['rhythm']['beats_loudness']['mean']
    all_mean.append(mean)
    bpm = data['rhythm']['bpm']
    all_bpm.append(bpm)
    chords_key = data['tonal']['chords_key']
    all_chords_key.append(chords_key)
    chords_scale = data['tonal']['chords_scale']
    all_chords_scale.append(chords_scale)
    title = data['metadata']['tags']['title'][0]
    all_title.append(title)
    artist = data['metadata']['tags']['artist'][0]
    all_artist.append(artist)

df = pd.DataFrame()

df['artist'] = all_artist
df['title'] = all_title
df['loudness'] = all_integrated
df['danceability'] = all_danceability
df['beats_loudness'] = all_mean
df['dynamic_complexity'] = all_dynamic_complexity
df['spectral_energy'] = all_spectral_energy
df['spectral_entropy'] = all_spectral_entropy
df['spectral_spread'] = all_spectral_spread
df['bpm'] = all_bpm
df['chords_key'] = all_chords_key
df['chords_scale'] = all_chords_scale


df = df.reindex(index=order_by_index(df.index,index_natsorted(df['title'])))
df = df.reset_index().drop(columns=['index'])
df.to_csv('path/to/output.csv')