# SemanticTwitter

## Setup

- Download the [geckodriver](https://github.com/mozilla/geckodriver/releases)

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

        # Twitter app keys
        API_KEY = ...
        API_SECRET = ...
        ACCESS_TOKEN = ...
        ACCESS_TOKEN_SECRET = ...
        BEARER_TOKEN = ...

        # Twitter account credentials
        ACCOUNT = ...
        PASSWD = ...

    Your credentials will be automatically imported to ```process_twitter.py``` script which connects to the API.

## Webpage modification

Modify Twitter by calling the script:

    % PATH=$PATH:<geckodriver containing directory> python modify_webpage.py
