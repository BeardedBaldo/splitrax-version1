import os
#from scipy.io.wavfile import write


def GetFileType(file):
	return type(file)

# def savefile(file):
# 	Dir = os.getwd()
# 	write(f"{os.path.join(Dir, file)}.mp3")
# 	#write(f"{os.path.join(FolderPath, StemList[i])}.wav", Track.rate, Stems[i])
