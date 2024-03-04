# todo-saver

Back up your Todoist tasks to a JSON file that they can be restored from.

This tool uses the [Todoist API](https://developer.todoist.com) but does not back up projects, sections, labels, or comments. Be careful of [the API's request limits](https://developer.todoist.com/rest/v2/#request-limits).

## setup

1. clone the repo
2. `pip install -r requirements.txt`
3. create a `.env` file with variables `backup_dir` and `todoist_api_token`
4. `py main.py`
