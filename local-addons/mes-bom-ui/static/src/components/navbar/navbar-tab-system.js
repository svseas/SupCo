/** @odoo-module */
import { Component, useState } from "@odoo/owl";
import { navData } from "./navbar-data";
import { useNavbarStore } from "./navbarStore";

export class NavbarTabSystem extends Component {
  setup() {
    this.data = navData.tabSystem;
    this.navStore = useNavbarStore();
  }
}

NavbarTabSystem.template = "mes-bom-ui.navbar-tab-system";
