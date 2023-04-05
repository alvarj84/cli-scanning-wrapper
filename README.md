# Sysdig CLI Scanner Tool Wrapper

This Python script serves as a wrapper for the sysdig-cli-scanner tool. It takes a JSON file containing flags and parameters for the tool and runs the tool using the provided flags and parameters. Additionally, it reads a secure API token from a file and passes it as an environment variable to the subprocess.

## Requirements

- Python 3.6 or higher
- Sysdig CLI scanner: https://docs.sysdig.com/en/docs/sysdig-secure/vulnerabilities/pipeline/

## Usage

1. Prepare a JSON configuration file with the flags and parameters for the command-line tool. For example:

```
{
    "apiurl": "us2.app.sysdig.com",
    "dbpath": "./sysdig-cli-scanner/cache/db",
    "cachepath": "./sysdig-cli-scanner/cache/scanner-cache/",
    "policy": "sysdig-best-practice"
}
```

Make sure to have the secure API token file ready.

## Run the script:

```
python wrapper.py json_config sysdig-cli-scanner secure_api_token_file image_name:tag
```

Arguments:

- `json_config`: Path to the JSON file containing flags and parameters for the command-line tool.
- `sysdig-cli-scanner`: Name of the command-line tool to wrap.
- `secure_api_token_file`: Path to the file containing the secure API token.
- `image_name`: Image name to be appended to the command.

The script will execute `sysdig-cli-scanner` with the flags and parameters specified in config.json, and the environment variable `SECURE_API_TOKEN` will be set to the value read from `secure_api_token_file`. The image name my_image:latest will be appended to the command.The output and any errors will be displayed in the terminal.

## Contributors:
- Jorge Alvarado (jorge.alvarado@sysdig.com)