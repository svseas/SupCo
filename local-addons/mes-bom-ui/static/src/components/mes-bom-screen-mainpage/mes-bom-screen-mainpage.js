/**@odoo-module */
const { Component, onMounted, useState } = owl;
import { registry } from "@web/core/registry";
const actionRegistry = registry.category("actions");
const rpc = require("web.rpc");
import { MesButton } from "../mes-button/mes-button";
import { MesInput } from "../mes-input/mes-input";
import { MesGetData } from "../mes-get-data/mes-get-data";
import { OrmExample } from "../orm-example/orm-example";
import { MesBomAddPage } from "../mes-bom-screen-addpage/mes-bom-screen-addpage";

export class MesBomMainPage extends Component {
  setup() {
    super.setup(...arguments);
    onMounted(() => {});
  }
  static components = {
    MesInput,
    MesButton,
    MesGetData,
  };

  newPage() {
    console.log(globalThis.contentStore);
    this.contentStore = globalThis.contentStore;
    this.contentStore.changeContent(MesBomAddPage);
  }
}
MesBomMainPage.template = "mes-bom-ui.mes_bom_screen_mainpage_template";
