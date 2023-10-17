/** @odoo-module */

import { Component, onMounted, useState } from "@odoo/owl";
import { useNavbarStore } from "./navbarStore";
import { NavbarSubItem } from "./navbar-sub-item";

export class NavbarItem extends Component {
  setup() {
    this.navStore = useNavbarStore();
    this.isNestedExpand = useState({ value: false });
  }

  toggleNested() {
    this.isNestedExpand.value = !this.isNestedExpand.value;
  }

  expandFromMini() {
    this.navStore.toggleMainMenu();
    this.isNestedExpand.value = true;
  }
}

NavbarItem.components = { NavbarSubItem };
NavbarItem.props = {
  item: Object,
};

NavbarItem.template = "mes-bom-ui.navbar-item";
