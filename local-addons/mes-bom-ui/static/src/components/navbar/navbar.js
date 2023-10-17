/** @odoo-module */
import { Component, onMounted } from "@odoo/owl";
import { useNavbarStore } from "./navbarStore";
import { NavbarTabSystem } from "./navbar-tab-system";
import { NavbarLinks } from "./navbar-links";
import { SubMenu } from "./sub-menu";

export class Navbar extends Component {
  setup() {
    this.navStore = useNavbarStore();
  }

  static components = {
    NavbarTabSystem,
    NavbarLinks,
    SubMenu,
  };

  changeState() {
    this.navStore.toggleMainMenu();
  }

  toggleHeader() {
    const header = document.querySelector("header");
    header.classList.toggle("d-none");
  }
}

Navbar.template = "mes-bom-ui.navbar";
