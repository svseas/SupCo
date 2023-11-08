/** @odoo-module */
import { Component, onMounted, useState } from "@odoo/owl";
import { useNavbarStore } from "./navbarStore";
import { useService } from "@web/core/utils/hooks";

export class NavbarSubItem extends Component {
  setup() {
    this.navStore = useNavbarStore();
    this.action = useService("action");
  }
  openSubMenu(menu) {
    // In legacy this will open sub menu -> now, it will open the new views
    this.navStore.changeSubMenu(menu);
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
      this.navStore.toggleMobile();
    }
    this.navStore.changeLevel([...item.level, item.label]);
  }
}

NavbarSubItem.props = {
  sub: Object,
};

NavbarSubItem.template = "mes-bom-ui.navbar-sub-item";
