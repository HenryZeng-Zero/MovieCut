import subprocess
import json
import os

CuttingStart = 18.3
CuttingToEnd = 7
CuttingEnd = None

def GetInfo(ffprobe, File):
    args = [ffprobe, '-print_format', 'json', '-show_streams', File]
    Program = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = Program.communicate()
    return json.loads(out.decode('utf-8'))['streams']


def Cut(ffmpeg, Start, Keep, File_In, File_Out):
    args = ffmpeg + ' -i ' + File_In + ' -ss ' + str(Start) + ' -to ' + str(Keep) + ' -codec copy ' + File_Out
    Program = subprocess.Popen(args)
    Program.communicate()


def Cutting(file, outfile):
    ffprobe_ = os.getcwd() + '\\ffprobe.exe'
    ffmpeg_ = os.getcwd() + '\\ffmpeg.exe'
    VideoInfo = GetInfo(ffprobe_, file)[0]
    Length = float(VideoInfo['duration'])
    Start = CuttingStart
    if CuttingEnd == None:
        Cut(ffmpeg_, Start, Length - CuttingToEnd, file, outfile)
    else:
        Cut(ffmpeg_, Start, CuttingEnd, file, outfile)
