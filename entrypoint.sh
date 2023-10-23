#!/bin/bash

# Update supco module
odoo -u supco --stop-after-init

# Start Odoo normally
/entrypoint.sh odoo
