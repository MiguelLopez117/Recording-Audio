# import required libraries 
from pydub import AudioSegment  
from pydub.playback import play 
  
# importing audio file 
a = AudioSegment.from_file("delme_rec_unlimited_9bk9jtc8.wav")  
  
# Split stereo to mono  
b = a.split_to_mono()  
print(b)  
print(b[0].channels ) 
print(b[1].channels )
  
  
b[0].export(out_f="mono1.wav",format="wav")
b[1].export(out_f="mono2.wav",format="wav")