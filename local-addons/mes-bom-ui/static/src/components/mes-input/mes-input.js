/**@odoo-module */
const { Component, onMounted, useState } = owl;
import { registry } from "@web/core/registry";
const actionRegistry = registry.category("actions");
const rpc = require('web.rpc');
export class MesInput extends Component {
  setup() {
    super.setup(...arguments);
  }
  static props = {
    slots: {},
    status: { type: String, optional: true },
    placeholder: { type: String, optional: true },
    value: { type: [String, Number], optional: true },
  }
  styles = {
    completed: 'mes__input--completed',
    invalid: 'mes__input--invalid',
  }
  cal(status) {
    if (status === 'invalid') {
      return this.styles.invalid
    }
    if (status === 'completed') {
      return this.styles.completed
    }
    return ''
  }
}
MesInput.template = "mes-bom-ui.mes_input_template";