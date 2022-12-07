import essentia
import essentia.standard as es
from pathlib import Path
import time
import glob

songs = glob.glob('/path/to/files/**.wav')

for song in songs:
  song_name = Path(song).stem
  features, features_frames = es.MusicExtractor(lowlevelStats=['mean', 'stdev'],rhythmStats=['mean', 'stdev'],tonalStats=['mean', 'stdev'])(song)
  results_file = "/content/drive/MyDrive" + '/%s_results.json' % song_name
  es.YamlOutput(filename=results_file, format="json")(features)
  
