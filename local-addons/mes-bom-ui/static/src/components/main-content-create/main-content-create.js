/**@odoo-module */
const { Component, onMounted, useState } = owl;
import { registry } from "@web/core/registry";
const actionRegistry = registry.category("actions");
const rpc = require('web.rpc');
import { MesButton } from "../mes-button/mes-button";
import { MesInput } from "../mes-input/mes-input";

export class MainContentCreate extends Component {
  setup() {
    super.setup(...arguments);
  }
  static components = {
    MesInput,
    MesButton,
  }
}
MainContentCreate.template = "mes-bom-ui.main_content_create_template";