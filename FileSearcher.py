from ffmpegManager import *

def FileInfo(Find, file, output_path, CuttingStart, CuttingToEnd, CuttingEnd):
    if Find == False:
        if output_path == None:
            Outfile = os.path.split(file)[0] + '\\Cut_' + os.path.split(file)[1]
            Cutting(file, Outfile, CuttingStart, CuttingToEnd, CuttingEnd)
        else:
            Outfile = output_path + '\\Cut_' + os.path.split(file)[1]
            Cutting(file, Outfile, CuttingStart, CuttingToEnd, CuttingEnd)
    else:
        if '"' == file[0]:
            file = file[1:-1]
        for root, dirs, files in os.walk(file):
            for f in files:
                FilePath = os.path.join(root, f)
                FileInfo = os.path.split(FilePath)
                if 'mp4' == FileInfo[1][-3:]:
                    if output_path == None:
                        Outfile = FileInfo[0] + '\\Cut_' + FileInfo[1]
                        Cutting('"' + FilePath + '"', '"' + Outfile + '"', CuttingStart, CuttingToEnd, CuttingEnd)
                    else:
                        Outfile = output_path + '\\Cut_' + FileInfo[1]
                        Cutting('"' + FilePath + '"', '"' + Outfile + '"', CuttingStart, CuttingToEnd, CuttingEnd)
