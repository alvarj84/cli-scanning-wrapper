import json
import argparse
import subprocess
import os

def load_config(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

def build_command(config, cmd_name, image_name):
    cmd = [cmd_name]
    for flag, value in config.items():
        if isinstance(value, bool) and value:
            cmd.append(f'--{flag}')
        elif isinstance(value, list):
            for val in value:
                cmd.append(f'--{flag}')
                cmd.append(str(val))
        else:
            cmd.append(f'--{flag}')
            cmd.append(str(value))
    cmd.append(image_name)
    return cmd

def run_command(cmd, secure_api_token_file):
    env = os.environ.copy()
    with open(secure_api_token_file, 'r') as file:
        env['SECURE_API_TOKEN'] = value = file.read().strip()
    process = subprocess.Popen(cmd, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return process.returncode, stdout.decode('utf-8'), stderr.decode('utf-8')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Wrapper for a command-line tool')
    parser.add_argument('json_config', help='JSON file containing flags and parameters for the command-line tool')
    parser.add_argument('command_name', help='Name of the command-line tool to wrap')
    parser.add_argument('secure_api_token_file', help='Sysdig SECURE API TOKEN file')
    parser.add_argument('image_name', help='Image Name')
    args = parser.parse_args()

    config = load_config(args.json_config)
    command = build_command(config, args.command_name, args.image_name)

    returncode, stdout, stderr = run_command(command, args.secure_api_token_file)

    print(f"Return code: {returncode}\n")
    print("Output:")
    print(stdout)

    if stderr:
        print("Error:")
        print(stderr)
