"""Script for validation of manifest files."""

import json
from pathlib import Path

import jsonschema
import yaml
import rich

MANIFEST_SCHEMA = "manifest-schema.json"
MANIFESTS_DIR = "../manifests"


def validate_all(manifestsdir):
    """Validate all manifests in manifestsdir."""
    for p in Path(manifestsdir).iterdir():
        if p.suffix == ".yaml":
            validate(p.name)
    pass


def validate(manifest_name):
    """Validate a yaml manifest against the json schema."""
    manifestfile = Path(MANIFESTS_DIR) / manifest_name
    json_data = load_manifest(manifestfile)
    if not json_data:
        print_error(f"'{manifest_name}' did not validate.")
        return

    with open(MANIFEST_SCHEMA) as f:
        schema = json.load(f)

    try:
        jsonschema.validate(instance=json_data, schema=schema)
        print_success(f"'{manifest_name}' validated!")
    
    except jsonschema.SchemaError as e:
        print_error("There is an error with the schema!")
        print_error(e)
        
    except jsonschema.ValidationError as e:
        msg = [f"'{manifest_name}' did not validate:"]
        msg.append(e.message)
        if len(e.path):
            msg.append(f"Error occurred at property: {'/'.join(str(i) for i in e.path)}")
        print_error("\n".join(msg))


def load_manifest(yaml_file):
    """Read YAML file and handle errors."""
    try:
        with open(yaml_file) as f:
            return yaml.load(f, Loader=yaml.FullLoader)
            
    except yaml.parser.ParserError as e:
        print_error("Could not parse manifests file:\n" + str(e))
    except yaml.scanner.ScannerError as e:
        print_error("An error occurred while reading the manifest file:\n" + str(e))
    except FileNotFoundError:
        print_error(f"Could not find the plugin manifest")

    return {}


def print_error(msg):
    """Print error messages to the console."""
    rich.print(f"\n[red]{msg}[/red]")

def print_success(msg):
    """Print success messages to the console."""
    rich.print(f"\n[green]{msg}[/green]")

if __name__ == "__main__":
    validate_all(MANIFESTS_DIR)
