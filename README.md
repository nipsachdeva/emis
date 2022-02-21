# Problem Understanding
An external system / supplier is sending patient data of patients to EMIS's platform using the FHIR standard. To make it easier for the team to uderstand data and to design business intelligence dashboards the data needs to be processed in workable format.

# Approach to Problem statement
Though there were many resources but the solution targets at the augmentation and preprocessing of patients data. This was done by loading each json file from the system and was serach for Patient's resourceType. 
### The output was saved in 2 formats:

1. Excel file
2. Mongo DB 

## Challenges

Due to work commitments at workplace, the project was started on Friday and majorly carried till sunday night and final bits were pushed post office on monday(D day).

## Future Scope: 
1. The pipeline to seek specific resource/attributes request from user
2. Flask server work is still in progress, may update by midnight of Monday.
3. Queuing can be taken care by flask but in case at a time large amount of data/files/requests needs to be process,celery could be used.

## Github Repository:
https://github.com/nipsachdeva/emis.git

File_Path: Code/docker_environment

Manual_script_execution: python main.py

## How to Run:

In the Terminal run : 

### Docker run emis_v1