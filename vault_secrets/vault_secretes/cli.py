import requests

def get_vault_secret(base_url, token, path):
    
    headers = {
        "X-Vault-Token": token
    }
    response = requests.get(f"{base_url}/v1/{path}", headers=headers)

    if response.status_code == 200:
        return response.json()["data"]
    elif response.status_code == 403:
        print("Access denied. Please check your token permissions.")
    else:
        print(f"Error {response.status_code}: {response.text}")

def get_role_list(token):
   
    headers = {
        "X-Vault-Token": token
    }
    
    vault_url = "http://127.0.0.1:8200/v1/database/roles"
    response =  requests.request("LIST", vault_url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        roles = data.get("data", {}).get("keys", [])
        print("Roles:", roles)
    else:
        print("Error:", response.status_code, response.text)


def main():
    base_url= "http://127.0.0.1:8200" # provide choice while running on server or localy in future
    token= input("Enter the token here: ").strip()
    
    print("Select the secret type to retrieve")
    print("1. Database credentials")
    print("2. Key/Value secret")

    choice = input("Enter choice (1 or 2): ").strip()

    if choice == "1":
        print("List of Roles available")
        get_role_list(token)
        role_path = input("Enter the database role from the list (e.g., my-role): ").strip()
        role_path = (f"database/creds/{role_path}") 
        creds = get_vault_secret(base_url, token, role_path)
        if creds:
            print("Database credentials:")
            print(f"Username: {creds['username']}")
            print(f"Password: {creds['password']}")
    elif choice == "2":
        kv_path = input("Enter the KV secret path (e.g., my-secret): ").strip()
        kv_path = (f"secret/data/{kv_path}")
        kv_data = get_vault_secret(base_url, token, kv_path)
        if kv_data:
            print("KV Secret Data:")
            for key, value in kv_data["data"].items():
                print(f"{key}: {value}")
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()