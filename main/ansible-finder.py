import sys
import os


def list_yaml_files(repository):
    for root, dirs, files in os.walk(repository):
        for file in files:
            if file.endswith(".yml"):
                print(os.path.join("repository", file))


if __name__ == "__main__":
    repo = sys.argv[1]
    list_yaml_files(repo)
