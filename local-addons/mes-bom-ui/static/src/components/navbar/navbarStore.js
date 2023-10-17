/** @odoo-module */

import { useState, reactive } from "@odoo/owl";

export const navStore = reactive({
  isMainMenuExpanded: false,
  isSubMenuExpanded: false,
  subMenu: {},
  level: ["Công tác báo chí", "Giấy Giới Thiệu", "Giấy Giới Thiệu"],
  toggleMainMenu() {
    this.isMainMenuExpanded = !this.isMainMenuExpanded;
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
