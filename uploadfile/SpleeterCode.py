import os 

Track = "/Volumes/Data/Adithya/ML_for_Audio_processing/Spleeter_vs_Demucs/Neon/Neon.mp3"
OutputDest = "/Volumes/Data/Adithya/ML_for_Audio_processing/Spleeter_vs_Demucs/Neon"
OPType = "mp3"
NStems = "2stems"

# "ffmpeg -i {tr} -f segment -segment_time 2 -c copy {trname}%03d.mp3"


def SpleeterRun(TrackPath, OutputPath, OutputType, NStems):
	try:# Command = "spleeter separate -i {tp} -o {op} -c {ot} -p spleeter:{ns}".format(tp = TrackPath, op = OutputPath, ot = OutputType, ns = NStems)
		Command = "spleeter aslkdf alsd m"
	# print(Command)
		os.system(Command)
	except Exception as e:
		print(e)




if __name__ == "__main__":
	SpleeterRun(Track, OutputDest, OPType, NStems)

