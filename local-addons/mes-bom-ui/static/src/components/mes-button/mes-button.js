/**@odoo-module */
const { Component, onMounted, useState } = owl;
import { registry } from "@web/core/registry";
const actionRegistry = registry.category("actions");
const rpc = require('web.rpc');
export class MesButton extends Component {
  static props = {
    color: { type: String, optional: true },
    slots: {},
    status: { type: String, optional: true },
  }
  colors = {
    primary: 'mes__btn--primary',
    outline: 'mes__btn--outline',
    ghost: 'mes__btn--ghost',
    active: 'mes__btn--active',
    deactive: 'mes__btn--deactive',
  }
  setup() {
    super.setup(...arguments);
  }
  cal(status) {
    if (status === 'deactive') {
      return this.colors.deactive
    }
    if (status === 'active') {
      return this.colors.active
    }
    return ''
  }
}
MesButton.template = "mes-bom-ui.mes_button_template";