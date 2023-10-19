/** @odoo-module */
import { Component, onMounted } from "@odoo/owl";
import { useNavbarStore } from "./navbarStore";
import { NavbarTabSystem } from "./navbar-tab-system";
import { NavbarLinks } from "./navbar-links";
import { SubMenu } from "./sub-menu";
import { useService } from "@web/core/utils/hooks";

export class Navbar extends Component {
  setup() {
    this.navStore = useNavbarStore();
    this.userService = useService("user");
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
    const userId = this.userService.userId;
    if (userId === 2 || userId === 1) {
      const header = document.querySelector("header");
      header.classList.toggle("d-none");
    }
  }
}

Navbar.template = "mes-bom-ui.navbar";
