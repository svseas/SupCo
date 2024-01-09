/** @odoo-module */

import { useState, reactive } from "@odoo/owl";
import { subDefault } from "./submenu-data-default";

export const navStore = reactive({
  isMainMenuExpanded: true,
  isSubMenuExpanded: false,
  isMobileExpanded: false,
  subMenu: subDefault,
  level: [
    {
      levelName: "Công tác báo chí",
      levelAction: "",
    },

    {
      levelName: "Giấy Giới Thiệu",
      levelAction: "supco.action_supreme_court_letters",
    },
  ],
  toggleMainMenu() {
    this.isMainMenuExpanded = !this.isMainMenuExpanded;
  },
  notExpandMainMenu() {
    this.isMainMenuExpanded = false;
  },
  toggleMobile() {
    this.isMobileExpanded = !this.isMobileExpanded;
  },
  toggleSubMenu() {
    this.isSubMenuExpanded = !this.isSubMenuExpanded;
  },
  changeSubMenu(menu) {
    this.isSubMenuExpanded = true;
    this.subMenu = menu;
  },
  changeLevel(level) {
    this.level = level;
  },
});

function useNavbarStore() {
  return useState(navStore);
}

export { useNavbarStore };
