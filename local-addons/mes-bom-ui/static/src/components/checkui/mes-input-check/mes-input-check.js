/**@odoo-module */
const { Component, onMounted, useState } = owl;
import { registry } from "@web/core/registry";
const actionRegistry = registry.category("actions");
const rpc = require('web.rpc');
import { MesInput } from "../../mes-input/mes-input";
export class MesInputCheck extends Component {
  setup() {
    super.setup(...arguments);
  }
  static components = { MesInput }
  statusArr = ['normal', 'invalid', 'completed']

}
MesInputCheck.template = "mes-bom-ui.mes_input_check_template";