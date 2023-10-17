/** @odoo-module */

import { Component, onMounted, useState } from "@odoo/owl";
import { useNavbarStore } from "./navbarStore";
import { useContentStore } from "../root/contentStore";
import { useService } from "@web/core/utils/hooks";

export class SubMenu extends Component {
  setup() {
    this.navStore = useNavbarStore();
    this.contentStore = useContentStore();
    this.action = useService("action");
  }

  doAction(item) {
    console.log("item", item);
    const args = {
      additionalContext: {
        no_breadcrumbs: true,
      },
      clearBreadcrumbs: true,
    };

    if (item.actionName === "" || item.actionName === undefined) {
      console.log("actionName nothing");
    } else {
      this.action.doAction(item.actionName, args);
    }
    this.navStore.changeLevel([...item.level, item.label]);
  }
}

SubMenu.template = "mes-bom-ui.sub-menu";
