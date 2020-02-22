from ffmpegManager import *

output_path = None


def FileInfo(Walk, file):
    global output_path
    if Walk == False:
        if output_path == None:
            Outfile = os.path.split(file)[0] + '\\Cut_' + os.path.split(file)[1]
            Cutting(file, Outfile)
        else:
            Outfile = output_path + '\\Cut_' + os.path.split(file)[1]
            Cutting(file, Outfile)
    else:
        for root, dirs, files in os.walk(file):
            for f in files:
                FilePath = os.path.join(root, f)
                FileInfo = os.path.split(FilePath)
                if 'mp4' == FileInfo[1][-3:]:
                    Outfile = FileInfo[0] + '\\Cut_' + FileInfo[1]
                    Cutting(FilePath, Outfile)
