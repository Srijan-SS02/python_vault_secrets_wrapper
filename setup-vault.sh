#!/bin/sh

export VAULT_ADDR='http://127.0.0.1:8200'

# Wait for Vault to be ready
until vault status > /dev/null 2>&1; do
    echo "Waiting for Vault to be initialized..."
    sleep 2
done
echo "Vault is ready."

# Enable the database secrets engine
if vault secrets enable database; then
    echo "Database secrets engine enabled."
else
    echo "Error: Failed to enable the database secrets engine." >&2
    exit 1
fi

# Configure the PostgreSQL connection
if vault write -tls-skip-verify database/config/postgresql \
    plugin_name=postgresql-database-plugin \
    allowed_roles="postgres-role" \
    connection_url="postgresql://{{username}}:{{password}}@db:5432/postgres?sslmode=disable" \
    username="admin" \
    password="admin"; then
    echo "PostgreSQL connection configured successfully."
else
    echo "Error: Failed to configure the PostgreSQL connection." >&2
    exit 1
fi

# Create the PostgreSQL role
if vault write database/roles/postgres-role \
    db_name=postgresql \
    creation_statements="CREATE ROLE \"{{name}}\" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}'; \
                         GRANT SELECT ON ALL TABLES IN SCHEMA public TO \"{{name}}\";" \
    default_ttl="1h" \
    max_ttl="24h"; then
    echo "PostgreSQL role created successfully."
else
    echo "Error: Failed to create PostgreSQL role." >&2
    exit 1
fi

echo "Vault setup completed successfully."
