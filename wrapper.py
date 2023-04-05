import json
import argparse
import subprocess

def load_config(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

def build_command(config, cmd_name):
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
    return cmd

def run_command(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return process.returncode, stdout.decode('utf-8'), stderr.decode('utf-8')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Wrapper for a command-line tool')
    parser.add_argument('json_config', help='JSON file containing flags and parameters for the command-line tool')
    parser.add_argument('command_name', help='Name of the command-line tool to wrap')
    args = parser.parse_args()

    config = load_config(args.json_config)
    command = build_command(config, args.command_name)

    returncode, stdout, stderr = run_command(command)

    print(f"Return code: {returncode}\n")
    print("Output:")
    print(stdout)

    if stderr:
        print("Error:")
        print(stderr)
