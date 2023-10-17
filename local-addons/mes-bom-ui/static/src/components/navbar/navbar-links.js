/** @odoo-module */
import { Component, reactive, useState } from "@odoo/owl";
import { useNavbarStore } from "./navbarStore";
import { NavbarItem } from "./navbar-item";
import { navData } from "./navbar-data";

export class NavbarLinks extends Component {
  setup() {
    this.items = navData.navItems;
    this.navStore = useNavbarStore();
  }
}

NavbarLinks.components = { NavbarItem };
NavbarLinks.template = "mes-bom-ui.navbar-links";
