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
    this.action = useService("action");
    this.userName = this.userService.name;
    this.shortName = this.userName
      .split(" ")
      .map((name) => name[0].toUpperCase())
      .join("");
  }

  static components = {
    NavbarTabSystem,
    NavbarLinks,
    SubMenu,
  };

  changeState() {
    this.navStore.toggleMainMenu();
  }

  changeStateMobile() {
    this.navStore.toggleMobile();
  }

  toggleHeader() {
    const userId = this.userService.userId;
    console.log("userId", this.userService);
    if (userId === 2 || userId === 1) {
      const header = document.querySelector("header");
      header.classList.toggle("d-none");
      header.style.zIndex = 99999;
    } else {
      this.action.doAction("supco.action_supreme_court_letters", {
        additionalContext: {
          no_breadcrumbs: true,
        },
        clearBreadcrumbs: true,
      });
    }
  }
}

Navbar.template = "mes-bom-ui.navbar";
