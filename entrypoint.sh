#!/bin/bash

# Update supco module
odoo -u supco --stop-after-init
echo "Module updated"

# Start Odoo normally
/entrypoint.sh odoo
