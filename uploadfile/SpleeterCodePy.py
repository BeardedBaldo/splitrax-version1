from spleeter.separator import Separator

Track = "/Volumes/Data/Adithya/ML_for_Audio_processing/Spleeter_vs_Demucs/Boulevard/Boulevard.mp3"
OutputDest = "/Volumes/Data/Adithya/ML_for_Audio_processing/Spleeter_vs_Demucs/Boulevard/"
NStems = 4
OPType = "mp3"


def SpleeterRun(Track, OutputDest, OPType, NStems):
	try:
		separator = Separator("spleeter:{}".format(NStems))
		separator.separate_to_file(Track, OutputDest, codec = OPType)
	except Exception as e:
		print(e)


if __name__ == "__main__":
	SpleeterRun(Track, OutputDest, OPType, NStems)
