/** @odoo-module */
import { Component, onMounted, useState } from "@odoo/owl";
import { useNavbarStore } from "./navbarStore";

export class NavbarSubItem extends Component {
  setup() {
    this.navStore = useNavbarStore();
  }
  openSubMenu(menu) {
    console.log(menu);
    this.navStore.changeSubMenu(menu);
  }
}

NavbarSubItem.props = {
  sub: Object,
};

NavbarSubItem.template = "mes-bom-ui.navbar-sub-item";
