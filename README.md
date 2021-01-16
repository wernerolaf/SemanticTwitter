# SemanticTwitter

## Setup

- Conda environment
    ```
    conda env update -f environment.yaml
    conda activate semantic-twitter
    ```

- Download the Spacy model
    ```
    python -m spacy download en_core_web_sm
    ```
- App credentials

    Create the ```config.py``` file with your Twitter API keys:

        API_KEY = ...
        API_SECRET = ...
        ACCESS_TOKEN = ...
        ACCESS_TOKEN_SECRET = ...
        BEARER_TOKEN = ...
        
    Your credentials will be automatically imported to ```process_twitter.py``` script which connects to the API.
