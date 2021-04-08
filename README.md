# REST_API

REST API that returns the current time in JSON format when a get request is made to the /currenttime endpoint

Run Program

1. Download Anaconda from https://www.anaconda.com/products/individual
2. Download Visual Studio Code from https://code.visualstudio.com/download
3. Navigate to VS Code in Anaconda Navigator
![image](https://user-images.githubusercontent.com/60635932/113963950-8ab91100-97f8-11eb-82b2-2682352aec6c.png)
4. Install necessary Python packages in VS Code
5. Click on File -> Open Folder -> REST_API to open project
6. Click on Terminal-> New Terminal in Top Menu
7. Run command -> pip install fastapi
8. Run command -> pip install hypercorn
9. Run command -> hypercorn main:app --reload
10. Click on url of local server
![image](https://user-images.githubusercontent.com/60635932/113964286-32364380-97f9-11eb-874c-99eb7a7f286a.png)
11. Modify url by adding '/docs' to the end

![image](https://user-images.githubusercontent.com/60635932/113964386-67db2c80-97f9-11eb-83a7-bcd978498310.png)
12. Click on Get->Try it out-> Execute
13. Output is in JSON format under responses
![image](https://user-images.githubusercontent.com/60635932/113964520-a670e700-97f9-11eb-883d-9d1a0ee61f7c.png)

