import os


def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")


files = os.listdir()
files.remove("main.py")

createIfNotExist('Images')
createIfNotExist('Docs')
createIfNotExist('Media')
createIfNotExist('Others')

imgExts = [".png", ".jpg", ".jpeg"]
images = [
    file for file in files if os.path.splitext(file)[1].lower() in imgExts
]

docExts = [".txt", ".pdf", ".zip", ".docx", ".doc"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

mediaExts = [".mp3", ".mp4"]
medias = [
    file for file in files if os.path.splitext(file)[1].lower() in mediaExts
]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in mediaExts) and (ext not in docExts) and (
            ext not in imgExts) and os.path.isfile(file):
        others.append(file)

move("Media", medias)
move("Docs", docs)
move("Images", images)
move("Others", others)