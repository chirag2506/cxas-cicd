import os, json
from pathlib import Path

config = os.environ.get("CONFIG_VALUE", "{}")
target_dir = os.environ.get("TARGET_DIR", "")
try:
    config_json: dict = json.loads(config)
    if target_dir != "":
        # env.json
        print("Updating environment.json")
        if config_json.get("environment", None) is not None and isinstance(config_json["environment"], dict):
            with open(f"{target_dir}/environment.json", "w") as f:
                f.write(json.dumps(config_json["environment"]))
        print("Updated environment.json")

        # var updates
        print("Updating variables")
        if config_json.get("variables", None) is not None and isinstance(config_json["variables"], dict):
            app_file = Path(f"{target_dir}/app.json")
            if app_file.is_file():
                with open(str(app_file), "r") as f:
                    cnt = json.loads(f.read())
                    variables_to_be_updated = list(config_json["variables"].keys())
                    for declaration in cnt.get("variableDeclarations", []):
                        name = declaration.get("name")
                        if name in variables_to_be_updated:
                            print(f"updating {name}")
                            schema = declaration.get("schema", {})
                            schema["default"] = config_json["variables"][name]
                            declaration["schema"] = schema
                    with open(str(app_file), "w") as f:
                        f.write(json.dumps(cnt))
                    
        print("Updated variables")

except Exception as e:
    print("Error in updating: {}".format(e))
