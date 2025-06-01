# Copyright 2024 Chris Wheeler

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import datetime
from typing import Iterator
import argparse
import os
import sys

import jsonpickle # pip install jsonpickle
from dotenv import load_dotenv # pip install python-dotenv
from todoist_api_python.api import TodoistAPI # pip install todoist-api-python
from todoist_api_python.models import Task # pip install todoist-api-python


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dest")
    args = parser.parse_args()

    loaded_dotenv: bool = False

    backup_dir: str
    if args.dest:
        backup_dir = args.dest
    else:
        load_dotenv()
        loaded_dotenv = True
        backup_dir = os.environ["backup_dir"]
    if not backup_dir:
        print("Error: backup directory not chosen")
        sys.exit(1)
    if not os.path.exists(backup_dir):
        print(f"Error: backup directory `{backup_dir}` does not exist")
        sys.exit(1)

    api_token: str
    if os.path.exists("/home/chris/.config/todo-saver/todoist-token"):
        with open("/home/chris/.config/todo-saver/todoist-token") as file:
            api_token = file.readline().strip()
    else:
        if not loaded_dotenv:
            load_dotenv()
        api_token = os.environ["todoist_api_token"]
        if not api_token:
            print("Error: could not find env var `todoist_api_token`")
            sys.exit(1)

    api = TodoistAPI(api_token)
    tasks_iter: Iterator[list[Task]] = api.get_tasks()

    tasks: list[Task] = []
    for tasks_page in tasks_iter:  # each iteration fetches a page of tasks
        tasks.extend(tasks_page)
    print(f"Found {len(tasks)} tasks")

    tasks_json = jsonpickle.encode(tasks)
    assert isinstance(tasks_json, str)

    now: str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name: str = f"{now}_todoist_backup_v2.json"
    file_path: str = os.path.join(backup_dir, file_name).replace("\\", "/")
    with open(file_path, "x", encoding="utf8") as f:
        f.write(tasks_json)
    print(f"Backup saved to {file_path}")


if __name__ == "__main__":
    main()
