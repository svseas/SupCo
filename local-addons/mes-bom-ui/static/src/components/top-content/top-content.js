/**@odoo-module */
const { Component, onMounted, useState } = owl;
import { registry } from "@web/core/registry";
const rpc = require("web.rpc");
import { MesButton } from "../mes-button/mes-button";
import { useNavbarStore } from "../navbar/navbarStore";
import { useService } from "@web/core/utils/hooks";
export class TopContent extends Component {
  setup() {
    super.setup(...arguments);
    this.navStore = useNavbarStore();
    this.action = useService("action");
  }
  static components = {
    MesButton,
  };
  doAction(item) {
    if (item.levelAction === "" || item.levelAction === undefined) {
    } else {
      this.action.doAction(item.levelAction);
    }
  }
  expandedMainmenu() {
    this.navStore.toggleMainMenu()
  }
  expandedSubmenu() {
    const menu = this.navStore.subMenu;
    this.navStore.changeSubMenu(menu);
  }
}
TopContent.template = "mes-bom-ui.top_content_template";
