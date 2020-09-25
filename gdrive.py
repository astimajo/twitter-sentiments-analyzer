from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

def drive_save_public(filename):
    #Authentication and web server setup with the client_secrets.json file
    g_login = GoogleAuth()
    g_login.LocalWebserverAuth()
    drive = GoogleDrive(g_login)

    #Uploader script V1: To Root directory
    '''
    with open("musk.csv", "r") as file:
        file_drive = drive.CreateFile({'title':os.path.basename(file.name), 'parents': [{'id': folder['Public']}]})  
        file_drive.SetContentString(file.read()) 
        file_drive.Upload()
    '''
    #Uploader script V2: With Subfolder selection

    folderName = 'Public'  # Please set the folder name.

    folders = drive.ListFile(
        {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
    for folder in folders:
        if folder['title'] == folderName:
            file2 = drive.CreateFile({'parents': [{'id': folder['id']}]})
            file2.SetContentFile(filename)
            file2.Upload()

        return