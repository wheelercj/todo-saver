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
import os
import sys

import jsonpickle
from dotenv import load_dotenv
from todoist_api_python.api import TodoistAPI


def main():
    load_dotenv()

    backup_dir: str = os.environ["backup_dir"]
    if not backup_dir:
        print("Error: could not find env var `backup_dir`")
        sys.exit(1)
    if not os.path.exists(backup_dir):
        print(f"Error: backup directory `{backup_dir}` does not exist")
        sys.exit(1)
    api_token: str = os.environ["todoist_api_token"]
    if not api_token:
        print("Error: could not find env var `todoist_api_token`")
        sys.exit(1)

    api = TodoistAPI(api_token)
    tasks: list = api.get_tasks()
    print(f"Found {len(tasks)} tasks")

    tasks_json: str = jsonpickle.encode(tasks)
    now: str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name: str = f"{now}_todoist_backup.json"
    file_path: str = os.path.join(backup_dir, file_name).replace("\\", "/")
    with open(file_path, "x", encoding="utf8") as f:
        f.write(tasks_json)
    print(f"Backup saved to {file_path}")


if __name__ == "__main__":
    main()
