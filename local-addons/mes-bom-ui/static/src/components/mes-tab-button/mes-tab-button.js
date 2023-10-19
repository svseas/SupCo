/**@odoo-module */
const { Component, onMounted, useState } = owl;
import { registry } from "@web/core/registry";
const actionRegistry = registry.category("actions");
const rpc = require('web.rpc');
export class MesTabButton extends Component {
  static props = {
    slots: {},
    status: { type: Boolean, optional: true },
  }
  status = {
    true: 'mes__tab--btn--selected--true',
    false: 'mes__tab--btn--selected--false',
  }
  setup() {
    super.setup(...arguments);
  }
  cal(status) {
    if (status) {
      return this.status.true
    }
    if (!status) {
      return this.status.false
    }
    return ''
  }
}
MesTabButton.template = "mes-bom-ui.mes_tab_button_template";