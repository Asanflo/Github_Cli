def format_event(event):
    """
    Transforme un événement GitHub en message lisible.
    """
    event_type = event['type']
    repo_name = event['repo']['name']

    if event_type == 'PushEvent':
        commits = len(event['payload'].get('commits', []))
        return f"Pushed {commits} commit{'s' if commits > 1 else ''} to {repo_name}"

    elif event_type == 'IssuesEvent':
        action = event['payload'].get('action', 'did something')
        return f"{action.capitalize()} a new issue in {repo_name}"

    elif event_type == 'IssueCommentEvent':
        return f"Commented on an issue in {repo_name}"

    elif event_type == 'PullRequestEvent':
        action = event['payload'].get('action', 'did something')
        return f"{action.capitalize()} a pull request in {repo_name}"

    elif event_type == 'WatchEvent':
        return f"Starred {repo_name}"

    elif event_type == 'ForkEvent':
        return f"Forked {repo_name}"

    elif event_type == 'CreateEvent':
        ref_type = event['payload'].get('ref_type', 'something')
        return f"Created {ref_type} in {repo_name}"

    else:
        return f"{event_type} on {repo_name}"
