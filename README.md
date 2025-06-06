# todo-saver

> [!NOTE]
> This repository is deprecated in favor of https://github.com/wheelercj/todo which now has an `export` command.

Back up your Todoist tasks to a JSON file. (I haven't written any code for restoring the tasks! I haven't needed it so far.)

This tool uses the [Todoist SDK](https://doist.github.io/todoist-api-python/) but does not back up projects, sections, labels, or comments. Be careful of [the API's request limits](https://developer.todoist.com/rest/v2/#request-limits).

## setup

1. Clone the repo
2. Create a `.env` file with variables `backup_dir` and `todoist_api_token`
3. `uv run main.py`
