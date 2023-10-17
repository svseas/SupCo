/**@odoo-module */
const { Component, onMounted, useState } = owl;
import { registry } from "@web/core/registry";
const rpc = require("web.rpc");
import { MesButton } from "../mes-button/mes-button";
import { useNavbarStore } from "../navbar/navbarStore";
export class TopContent extends Component {
  setup() {
    super.setup(...arguments);
    this.navStore = useNavbarStore();
  }
  static components = {
    MesButton,
  };
}
TopContent.template = "mes-bom-ui.top_content_template";
