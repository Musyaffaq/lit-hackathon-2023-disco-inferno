# Legaxonomy by Disco Inferno - SMU LIT Hackathon 2023

## Problem Statement
Generative AI in the legal research process
Organisations are faced with the dilemma of having powerful technologies available to them, such as GPT4, while also knowing that the technologies need to be harnessed in such a way that they are reliable in a professional services context.

Please demonstrate how can generative AI be harnessed and combined with a legal taxonomy such as LIST maintained by Stanford Legal Design Lab (or any other taxonomy - Singapore has 2 or 3 legal taxonomies that could be aligned), to help organisations tag their legal texts with the taxonomy, facilitate efficient reliable retrieval of legal texts, and support the summarisation of those texts when requested by users.

## Solution Idea
Harnessing the power of the Open AI API (which powers ChatGPT), we propose creating a Case Management System where the summarisation and tagging of legal texts are automated. This will then allow the easy retrieval of those cases by a legal practitioner through the tags that have been generated, allowing for a more efficient legal research process.

Proceed to this link to have a feel as to how this solution would work from the user's point of view. [ADD LINK]

## Architecture
Here is a high-level view of how our solution would work. The code provided is how the part boxed in red would work.
![image](https://github.com/Musyaffaq/lit-hackathon-2023-disco-inferno/assets/18120258/113421fc-0d55-4783-9e59-18e6d75212e3)


## Testing the Code
1. Download a copy of this repo on your local machine.
2. Inside current folder, do `pip install -r requirements.txt`.
3. Open up `ENVEXAMPLE` and add in your own Open AI secret key. [Here is guide on how to get your own](https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/).
4. Rename the file to `.env`.
5. To test the summarisation and tagging, run `python llm-summary.py` in the current folder. Currently it is using the sample legal case provided in `sample_case.txt`.

**_NOTE:_** Each time you run the file, you will be charged by Open AI for the usage of their models.
