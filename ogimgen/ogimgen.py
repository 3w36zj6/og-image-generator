import sys
import os
import yaml

def get_markdown_yaml_metadata(markdown_path: str) -> str:
    yaml_metadata: str = ""
    is_reading_yaml_metadata: bool = False
    with open(markdown_path, "r") as f:
        for line in f:
            if line == "---\n":
                if not is_reading_yaml_metadata:
                    is_reading_yaml_metadata = True
                    continue
                else:
                    return yaml_metadata

            if is_reading_yaml_metadata:
                yaml_metadata += line

    return yaml_metadata

def generate():
    yaml_metadata = get_markdown_yaml_metadata(os.path.join(os.getcwd(), sys.argv[1]))

    data = yaml.load(yaml_metadata, Loader=yaml.SafeLoader)
    print(data)


if __name__ == "__main__":
    generate()
