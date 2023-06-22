# Legaxonomy by Disco Inferno - SMU LIT Hackathon 2023

## Problem Statement - Generative AI in the legal research process
Generative AI in the legal research process
Organisations are faced with the dilemma of having powerful technologies available to them, such as GPT4, while also knowing that the technologies need to be harnessed in such a way that they are reliable in a professional services context.

Please demonstrate how can generative AI be harnessed and combined with a legal taxonomy such as LIST maintained by Stanford Legal Design Lab (or any other taxonomy - Singapore has 2 or 3 legal taxonomies that could be aligned), to help organisations tag their legal texts with the taxonomy, facilitate efficient reliable retrieval of legal texts, and support the summarisation of those texts when requested by users.

## Solution Idea
Legal research has always been a labour-intensive process. Part of it requires them to read through legal texts, label them and then look through them again when retrieving the legal texts. This can hinder progress in cases that could be time-sensitive. Hence, our team has developed a solution to help improve the efficiency of this whole process.

Harnessing the power of the OpenAI API (which powers ChatGPT), we propose creating a Case Management System where the summarisation and tagging of legal texts are automated. This will then allow the easy retrieval of those cases by a legal practitioner through the tags that have been generated, allowing for a more efficient legal research process. This solution taps on AI (i.e. Large Learning Models) through the use of the Open AI Api.

Our application has two use cases:

1. Summarisation, Tagging, Storage
- Firstly, users would be able to upload files into the application. These files would then be processed. This part would include summarising the legal texts, extracting key informations (such as the corem, court and facts of case) and give them tags (which could be done according to the taxonomy of legal issues such as LIST). This helps to cut down the time taken to read through the case, summarise it and label them accordingly.

2. Retrieval
- Secondly, users would be able to retrieve the files in an efficient manner through the tags from the previous step. This is an improvement from the normal way where you have to look through folders (either physically or digitally). Cases are returned based on input parameters set by the user.

For our next steps, our solution can be put onto the market as a low-cost solution for lawyers to reduce their workload, as it is a cost-effective way for lawyers to reduce the amount of mundane work that they are required to do, allowing them to focus on their main job of closing cases rather than administrative tasks. We can further upgrade and finetune the accuracy of our model using input data from users whenever they edit the tags manually.

Proceed to this link to have a feel as to how this solution would work from the user's point of view. [ADD LINK]

## Architecture
Here is a high-level view of how our solution would work. The code provided is how the part boxed in red would work.
![image](https://github.com/Musyaffaq/lit-hackathon-2023-disco-inferno/assets/18120258/113421fc-0d55-4783-9e59-18e6d75212e3)


## Setting Up the Code
1. Download a copy of this repo on your local machine.
2. Inside current folder, do `pip install -r requirements.txt`.
3. Open up `ENVEXAMPLE` and add in your own Open AI secret key. [Here is guide on how to get your own](https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/).
4. Rename the file to `.env`.

## Testing the Code
1. Run `python llm-summary.py` in the current folder.
2. You will be prompted to select a file. You can either choose your own case or use the sample case we have provided titled `sample_case.pdf`, which is the classic Spandeck case!
![image](https://github.com/Musyaffaq/lit-hackathon-2023-disco-inferno/assets/18120258/c1f48aa7-ce4e-4b39-9d42-d7bfd5141d0d)

3. Now open the file called `Database.csv` under the folder `Database`.
4. Wait for a few seconds for the program to run.
5. Once it has run, you will be able to see that the information has been saved!
![image](https://github.com/Musyaffaq/lit-hackathon-2023-disco-inferno/assets/18120258/20485f14-287d-4c72-a8e1-195cd49e3740)

**_NOTE:_** Each time you run the file, you will be charged by Open AI for the usage of their models.
