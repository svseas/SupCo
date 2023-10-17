/** @odoo-module */

import { Component } from "@odoo/owl";

export class PropsExample extends Component {
  setup() {
    this.name = this.props.name;
  }

  static props = {
    name: { type: String, optional: true },
  };
}

PropsExample.template = "mes-bom-ui.props-example";
