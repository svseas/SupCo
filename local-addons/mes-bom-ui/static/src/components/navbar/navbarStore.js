/** @odoo-module */

import { useState, reactive } from "@odoo/owl";

export const navStore = reactive({
  isMainMenuExpanded: true,
  isSubMenuExpanded: false,
  subMenu: {},
  level: [
    {
      levelName: "Công tác báo chí",
      levelAction: "",
    },
    {
      levelName: "Giấy Giới Thiệu",
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
