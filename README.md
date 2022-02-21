# Problem Understanding
An external system / supplier sends patients' data to EMIS's platform using the FHIR standard. 
This project aims to formulate data that is in structured and workable format and to further design business intelligence dashboards.

# Approach to Solution
Though there were many resources but the solution targets at the augmentation and preprocessing of patients data. This was done by loading each json file from the system and was search for Patient's resourceType. 
### The output was saved in 2 formats:

1. Excel file
2. Mongo DB 

## Programming Languages 
	> Python 
## Data Storage Layer 
	> XLSX
	> Mongo DB
## Challenges

### Project Challenge
> There were many attributes to be considered, therefore to fulfil the bare minimum requirements some of them were chosen, so that remaining can be inculcated at a later stage.

### Personal Challenge
> Due to work commitments and overtime in current organisation the project could not be started until the weekend and majorly carried till sunday night and final bits were pushed post office timings on Monday(D-day).

## Future Scope: 
1. The pipeline to seek specific resource/attributes request from user.
2. Flask server work is still in progress, may update by midnight of Monday.
3. Queuing can be taken care by establishing flask server but in case, large amount of data/files/requests need to be processed, celery could be used.

## Github Repository:
https://github.com/nipsachdeva/emis.git

File_Path: Code/docker_environment

Manual_script_execution: python main.py

## How to Run:

In the Terminal run: 

### Docker run emis_v1