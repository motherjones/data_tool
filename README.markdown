#Data Tool Readme

The main purpose of this application is to save and analyse people who receive our newsletters.

##Development TODOs
1. Fix the pygal requirement in requirements/apps.txt so that it doesn't fail on install.
2. See how high the batch size in the query_loader task can be without failing.  Its currently 300 but turning it up to 1000 or more will speed up the upload time.
3. Combine the report and query upload into a single form so that both can loaded in at the same time.
4. Automate the query so that it runs each week automatically so that it takes less time and runs at the same time each week.

##Deployment instructions
From the playbook directory run this command `ansible-playbook mojo_data.yml --tags=django` to update and restart apache and celery and install any python requirements.

If you want to do a fresh setup on a new machine run `ansible-playbook mojo_data.yml` both will prompt for the decryption password(ask Robert or Mikela).

##Weekly Upload
Each week on Monday morning you will need to download two CSV files from Convio.  The report will be emailed to Robert every Monday morning and will need to be uploaded.  The query needs to be manually run at or as close as possible to 10am(PST).

###Running Report
1. Download the CSV file from the email at 10am
2. Go to the anonymizer folder and type: python ./data_anonymizer.py -i input_file -o export_file
3. Go to https://data.motherjones.com/newsletter/subscribers-upload and upload it.

###Running Query
1. In Convio use the "Not Receiving Emails" query by going here: https://secure3.convio.net/mojo/admin/QueryAdmin/391464787?cmd=results
2. Click on Use Query and then Mail Merge
3. Add name and description
4. Click on the Email/Email selection and then Add Selection
5. Click Next Step
6. Click confirm
10. Now your be on a mail merge listing page
11. Yours will say In Progress so keep refreshing till it offer a Blue Floppy
12. Then click and save it
13. Go to the anonymizer folder and type: python ./query_anonymizer.py -i input_file -o export_file
14. Go to https://data.motherjones.com/newsletter/query-upload and upload the anonymized query.

##Server Layout
* Datatool repo is at /opt/data-tool
* Datatool virtualenv is at /opt/data-tool_virtualenv
* Run `source /opt/data-tool_virtualenv/bin/activate` to put yourself in the python environment
* Run `./manage shell` from /opt/data-tool to use the django shell
