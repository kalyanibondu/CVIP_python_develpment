import pyaudio
import wave
audio_file=pyaudio.PyAudio()

stream_line=audio_file.open(format=pyaudio.paInt16,channels=1,rate=4400,input=True,frames_per_buffer=1024)
frames=[]
try:
    while True:
        data=stream_line.read(1026)
        frames.append(data)
except KeyboardInterrupt:
    pass

stream_line.stop_stream()
stream_line.close()
audio_file.terminate()

sound_file=wave.open("myreacording.wav","wb")
sound_file.setnchannels(1)
sound_file.setsampwidth(audio_file.get_sample_size(pyaudio.paInt16))
sound_file.setframerate(44100)
sound_file.writeframes(b''.join(frames))
sound_file.close()