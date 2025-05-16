# Odoo Task Manager Module

A custom Odoo 17.0 module that provides basic task management functionality.  
Designed for local development and learning purposes.

## 📦 Features

- Custom model for managing tasks
- Cron job setup for scheduled operations
- Access control and menu integration
- Custom reports

---

## ⚙️ Project Setup

Tested on Ubuntu 22.04 with Odoo 17 and PostgreSQL.

### 1. Create Odoo System User
```bash
sudo adduser --system --home=/opt/odoo --group odoo
sudo usermod -aG odoo $USER
```

### 2. Install PostgreSQL
```bash
sudo apt install postgresql -y
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

Create PostgreSQL user `odoo`:
```bash
sudo -u postgres createuser --createdb --pwprompt odoo
# password: your-pswd
```

If needed, update the password manually:
```bash
sudo -u postgres psql
ALTER USER odoo WITH PASSWORD 'your-pswd';
```

### 3. Clone Odoo Source
```bash
sudo git clone https://github.com/odoo/odoo --depth 1 --branch 17.0 --single-branch /opt/odoo
```

### 4. Setup Python Virtual Environment
```bash
cd /opt/odoo
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🛠️ Configuration

Create the config file `/opt/odoo/odoo.conf`:

```ini
[options]
addons_path = /opt/odoo/addons,/opt/odoo/custom_addons
db_host = localhost
db_port = 5432
db_user = odoo
db_password = your-pswd
admin_passwd = admin-secret
xmlrpc_port = 8069
```

---

## 🚀 Running Odoo

```bash
cd /opt/odoo
mkdir custom-addons
source venv/bin/activate
./odoo-bin -c odoo.conf
```

Then open in browser:

[http://localhost:8069](http://localhost:8069)

Create a new database and activate your module.

---

## 📁 Module Location

This module resides in:
```
/opt/odoo/custom_addons/task_manager
```

Make sure to include `/opt/odoo/custom_addons` in the `addons_path` in `odoo.conf`.

---

## 🧹 .gitignore (recommended)

If this repo contains only the custom module, include:
```
__pycache__/
*.pyc
*.pyo
*.swp
*.log
.idea/
.vscode/
.DS_Store
```

---

## ✅ Notes

- If PostgreSQL connection fails, make sure Docker or other services are not occupying port 5432.
- Use `sudo ss -ltnp | grep 5432` to debug.

