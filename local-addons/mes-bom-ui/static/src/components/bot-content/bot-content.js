/**@odoo-module */
const { Component, onMounted, useState } = owl;
import { registry } from "@web/core/registry";
const actionRegistry = registry.category("actions");
const rpc = require('web.rpc');
export class BotContent extends Component {
  setup() {
    super.setup(...arguments);
  }
}
BotContent.template = "mes-bom-ui.bot_content_template";