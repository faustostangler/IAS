import os
import json

def main():
    if not os.path.exists('_reversa_sdd'):
        print(json.dumps({"error": "_reversa_sdd folder not found. Cannot consolidate."}))
        return
        
    inventory = {
        "total_files": 0,
        "total_size_bytes": 0,
        "confidence_markers": {
            "🟢": 0,
            "🟡": 0,
            "🔴": 0
        },
        "files": []
    }
    
    for root, _, files in os.walk('_reversa_sdd'):
        # Ignore historian data folder
        if '.reversa_historian_data' in root:
            continue
            
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                size = os.path.getsize(path)
                inventory["total_files"] += 1
                inventory["total_size_bytes"] += size
                
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        inventory["confidence_markers"]["🟢"] += content.count("🟢")
                        inventory["confidence_markers"]["🟡"] += content.count("🟡")
                        inventory["confidence_markers"]["🔴"] += content.count("🔴")
                except:
                    pass
                    
                inventory["files"].append({
                    "path": os.path.relpath(path, '_reversa_sdd'),
                    "size": size
                })
                
    os.makedirs('_reversa_sdd/.reversa_historian_data', exist_ok=True)
    with open('_reversa_sdd/.reversa_historian_data/artifact_inventory.json', 'w') as f:
        json.dump(inventory, f, indent=2)
        
    print("Artifact inventory successfully created at _reversa_sdd/.reversa_historian_data/artifact_inventory.json")

if __name__ == '__main__':
    main()
