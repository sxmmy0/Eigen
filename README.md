<h1> Eigen Coding Assignment </h1>

<h2> Assignment Brief </h2>

At Sirion Eigen, the compant spend a lot of time getting useful information out of documents. Usually a word or two, perhaps a sentence or paragraph. For this assignment, I aim you to show how I would do something similar!

### Task Outcomes
In this task there were several outcomes:
- extract_words.py -> Common words like 'the', 'and', 'is' etc were removed. The frequency of the words in each document were then accounted for.
- extract_sentences.py -> Sentences in each document are ranked by a scoring system of most important sentence.
- TD_IDF.py -> creating file...tbc

### Installation Instructions
### Step 1. Clone My Repository:
` git clone (https://github.com/sxmmy0/Eigen.git) `

### Step 2. Ensure you directory path is configured:
- In the python script (cmd + f) or (ctrl + f) to find the directory script and replace with your directory path.
  
` directory = "/<your-directory-path>/"  # Replace with your directory path `

### Step 3. Ensure nltk and pandas is installed:
` pip install nltk pandas `

### Step 4. Run python file your IDE which creates a csv file
`python extract_words` 

### Troubleshooting:
• One issue was an nltk iss where the out was not recognising 
`import nltk nltk.download('stopwords') `
### Troubleshooting Fix:
• I fixed this by adding this script:
```
import ssl
import nltk

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

Download the required NLTK resources: 
nltk.download('punkt')
nltk.download('stopwords')
```
This helps to install all the necesssary nltk files and override the ssl error
