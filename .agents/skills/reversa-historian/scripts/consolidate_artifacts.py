import os
import json

def main():
    if not os.path.exists('sdd'):
        print(json.dumps({"error": "sdd folder not found. Cannot consolidate."}))
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
    
    for root, _, files in os.walk('sdd'):
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
                    "path": os.path.relpath(path, 'sdd'),
                    "size": size
                })
                
    os.makedirs('sdd/.reversa_historian_data', exist_ok=True)
    with open('sdd/.reversa_historian_data/artifact_inventory.json', 'w') as f:
        json.dump(inventory, f, indent=2)
        
    print("Artifact inventory successfully created at sdd/.reversa_historian_data/artifact_inventory.json")

if __name__ == '__main__':
    main()
