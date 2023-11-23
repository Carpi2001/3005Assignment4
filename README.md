Prerequisites:

Latest Version of Python and Pip
pgAdmin4 and PostgreSQL 16 server already congifured past the initial set up

Steps:

1. Open pgAdmin4, right click your server of choice, and select Create > Database
2. Give your Database a name of your choice. For this example, I will name it Assignment4.
3. Select the proper owner, usually that is the postgres user that should be there by default.
4. Hit the save button in the window.
5. In the sidebar, right-click the new database and then press Query Tools
6. Near the top, hit the file button, it should open your file viewer. 
7. Navigate to where the assignment files are downloaded and select the ddl.sql files. 
8. You should see text appear in the box. In the top bar hit the run button. The console output below should say "Query returned successfully in X msec."
9. Press the file button again and find the dml.sql file now.
10. Once the text shows up in the box below, hit the run button again. You should get the same message as before. 
11. Now you can minimize pgAdmin4. Next open cmd prompt if you are on windows or the prefered console application for your operating system.
12. Run the command "pip install psycopg2" and let that install.
13. Once it is install, use your command interface to navigate to the folder where the a4.py file is located.
14. Run the script by typing "python a4.py"
15. If for some reason the application doesn't run or gives an error, try "python3 a4.py", sometimes the python command uses an older version of python and python 3 has a seperate command, depening on how it was installed on your system.
16. Just follow the on screen prompts now to test the program. 
17. For the initial connection when the program starts, the host is the address to your server, this will likely be localhost for you. Database is the name of the database from step 2, username is the user you chose for the database, password is the users password****

https://www.youtube.com/watch?v=3QNJAt8vmnc
