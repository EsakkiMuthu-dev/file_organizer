
import os
import shutil
# directories that we want to create
DIRECTORIES = {
	"PROGRAMMING STUFFS": [".html5", ".html", ".htm", ".xhtml",".txt", ".in", ".out",
    ".php",".py",".xml",".json"],
	"IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
			".heif", ".psd"],
	"VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
			".qt", ".mpg", ".mpeg",'.mkv', ".3gp"],
	"DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
				".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
				".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
				".pptx",".pdf",".sh",".odp",".ps"],
	"SOFTWARES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
				".dmg", ".rar", ".xar", ".zip",".tgz",".xz",".exe",".deb",".run",".vsix",".AppImage"],
	"AUDIO": [ ".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
			".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma",],
    "SUBTITLES":[".srt",".nfo"]


}



def file_organizer(pat):
    files = os.listdir(pat) #all the files in the directory
    print("files that are locatedin this directory are:"+ str(files))
    for file in files:
        filename,file_format = os.path.splitext(file) #getting extension of an file
        for key in DIRECTORIES.keys():
            for format in DIRECTORIES.get(key):
                if format == file_format:
                    source = pat+'/'+ file
                    print('\n our source path is :'+ str(source))
                    destination = pat+'/'+key
                    path = os.path.join(pat,destination)
                    print(path)
                    print('\n our destination path is :'+ str(destination))
                    try:
                        if os.path.exists(destination):
                            shutil.move(source,destination)
                        else:
                            os.makedirs(destination)
                            shutil.move(source,destination)
                    except:
                        print('Ooops.. file already exists... ')
                  

                        
                    
                    
                            
                   



if __name__ == '__main__':
    pat = input('enter the path to scan:')
    file_organizer(pat)

    '''
                        os.makedirs(destination)
                        shutil.move(source,destination)
                    except FileExistsError:
                        
                    '''