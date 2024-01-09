/**@odoo-module */
const { Component, onMounted, useState } = owl;
import { registry } from "@web/core/registry";
const actionRegistry = registry.category("actions");
const rpc = require("web.rpc");
import { ColorTemplate } from "./color/colorTemplate";
import { MesButtonGallery } from "./mes-button-gallery/mes-button-gallery";
import { MesInputCheck } from "./mes-input-check/mes-input-check";
import { TestNavbar } from "./test-navbar/test-navbar";
import { PropsExample } from "../props-example/props-example";
import { OrmExample } from "../orm-example/orm-example";
import { MainContentCreate } from "../main-content-create/main-content-create";

export class CheckUi extends Component {
  static components = {
    ColorTemplate,
    MesButtonGallery,
    MesInputCheck,
    TestNavbar,
    PropsExample,
    OrmExample,
    MainContentCreate,
  };
}
CheckUi.template = "mes-bom-ui.CheckUi";
actionRegistry.add("mes-bom-ui.action_checkui_js", CheckUi);
