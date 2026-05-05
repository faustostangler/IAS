import os
import subprocess
import json
from collections import defaultdict

def run_git(args):
    try:
        return subprocess.check_output(['git'] + args, stderr=subprocess.DEVNULL).decode('utf-8', errors='replace').strip()
    except Exception as e:
        return ""

def main():
    if not os.path.exists('.git'):
        print(json.dumps({"error": "No .git directory found. Skipping Git archaeology."}))
        return

    data = {
        "total_commits": 0,
        "contributors": [],
        "first_commit_date": "",
        "last_commit_date": "",
        "pivotal_commits": [],
        "volatility": defaultdict(int)
    }

    # Contributors
    contribs = run_git(['shortlog', '-sne', 'HEAD']).split('\n')
    for c in contribs:
        if c.strip():
            parts = c.strip().split('\t')
            if len(parts) == 2:
                data["contributors"].append({"commits": int(parts[0].strip()), "name": parts[1].strip()})

    # Dates
    dates = run_git(['log', '--format=%cI']).split('\n')
    if dates and dates[0]:
        data["total_commits"] = len(dates)
        data["last_commit_date"] = dates[0]
        data["first_commit_date"] = dates[-1]

    # Pivotal commits (last 500 commits to limit execution time)
    log_lines = run_git(['log', '-n', '500', '--format=%H|%an|%ad|%s', '--date=short', '--name-only']).split('\n')
    
    current_commit = {}
    for line in log_lines:
        if '|' in line and len(line.split('|')) >= 4:
            if current_commit and current_commit.get('files_changed', 0) >= 10:
                data["pivotal_commits"].append(current_commit)
            parts = line.split('|', 3)
            current_commit = {
                "hash": parts[0],
                "author": parts[1],
                "date": parts[2],
                "message": parts[3],
                "files_changed": 0
            }
        elif line.strip() and current_commit:
            current_commit['files_changed'] += 1
            dirname = os.path.dirname(line.strip())
            if dirname and not dirname.startswith('.'):
                data["volatility"][dirname] += 1
                
    if current_commit and current_commit.get('files_changed', 0) >= 10:
        data["pivotal_commits"].append(current_commit)

    # Sort volatility
    sorted_vol = sorted(data["volatility"].items(), key=lambda x: x[1], reverse=True)[:20]
    data["volatility"] = {k: v for k, v in sorted_vol}
    
    os.makedirs('_reversa_sdd/.reversa_historian_data', exist_ok=True)
    with open('_reversa_sdd/.reversa_historian_data/git_data.json', 'w') as f:
        json.dump(data, f, indent=2)
        
    print("Git data successfully extracted to _reversa_sdd/.reversa_historian_data/git_data.json")

if __name__ == '__main__':
    main()
