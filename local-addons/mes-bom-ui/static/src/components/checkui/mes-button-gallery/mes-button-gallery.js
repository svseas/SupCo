/**@odoo-module */
const { Component, onMounted, useState } = owl;
import { registry } from "@web/core/registry";
const actionRegistry = registry.category("actions");
const rpc = require('web.rpc');
import { MesButton } from "../../mes-button/mes-button";
import { MesTabButton } from "../../mes-tab-button/mes-tab-button";
export class MesButtonGallery extends Component {
  setup() {
    super.setup(...arguments);
  }
  static components = {
    MesButton,
    MesTabButton,
  }
  statusArr = ['normal', 'active', 'deactive']
  buttonType = ['primary', 'outline', 'ghost']
  tabStatus = [true, false]

}
MesButtonGallery.template = "mes-bom-ui.mes_button_gallery_template";